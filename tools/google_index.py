#!/usr/bin/env python3
"""구글 Indexing API 색인 통보 (구글은 IndexNow 미참여).

구글에 URL 업데이트/삭제를 즉시 알린다. IndexNow 와 별도로 동작한다.

사전 준비(1회):
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Google Search Console 에서 해당 사이트 속성에 그 서비스 계정 이메일을
     '소유자(Owner)' 로 추가
  4) pip install google-auth requests

사용법:
  GOOGLE_APPLICATION_CREDENTIALS=/path/sa.json python tools/google_index.py
      → sitemap.xml 의 모든 URL 통보 (URL_UPDATED)
  ... python tools/google_index.py <url> [<url> …]
      → 지정한 URL만 통보
  ... python tools/google_index.py --delete <url>
      → URL_DELETED

참고: 구글 Indexing API 는 공식적으로 JobPosting·BroadcastEvent 구조화 데이터
페이지를 위한 것입니다. 일반 페이지에도 호출은 되지만 색인을 보장하지는 않습니다.
가장 확실한 일반 색인 경로는 Search Console 의 sitemap 제출 + URL 검사입니다.
"""
import os
import re
import sys
import json
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content.site import BASE_URL  # noqa: E402

BASE = BASE_URL.rstrip("/")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def get_token():
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("환경변수 GOOGLE_APPLICATION_CREDENTIALS 에 서비스 계정 JSON 경로를 지정하세요.")
    try:
        from google.oauth2 import service_account
        import google.auth.transport.requests as greq
    except ImportError:
        sys.exit("pip install google-auth requests 를 먼저 실행하세요.")
    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    creds.refresh(greq.Request())
    return creds.token


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>([^<]+)</loc>", f.read())


def notify(token, url, kind):
    body = json.dumps({"url": url, "type": kind}).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=body, method="POST",
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return f"{e.code} {e.read().decode('utf-8','ignore')[:160]}"


if __name__ == "__main__":
    args = sys.argv[1:]
    kind = "URL_UPDATED"
    if args and args[0] == "--delete":
        kind = "URL_DELETED"
        args = args[1:]
    targets = [u for u in (args or sitemap_urls()) if u.startswith(BASE)]
    if not targets:
        sys.exit("통보할 URL이 없습니다.")
    token = get_token()
    ok = 0
    for u in targets:
        res = notify(token, u, kind)
        flag = "✅" if res == 200 else "⚠"
        print(f"  {flag} {kind} {u} -> {res}")
        if res == 200:
            ok += 1
    print(f"\n구글 Indexing API: {ok}/{len(targets)} 성공")
    if ok < len(targets):
        print("일부 실패 — 서비스 계정이 Search Console 소유자로 등록됐는지 확인하세요.")
