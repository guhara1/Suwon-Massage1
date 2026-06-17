#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — Bing·Naver·Yandex·Seznam 동시.

단일 엔드포인트(api.indexnow.org)에 통보하면 IndexNow 참여 검색엔진에 함께 전달된다.
네이버(Yeti)와 빙이 IndexNow에 참여하므로, 글을 올리거나 페이지를 고칠 때마다
이 스크립트를 실행하면 즉시 색인 요청이 전달된다.

사용법:
  python tools/indexnow.py                 # sitemap.xml 의 모든 URL 통보
  python tools/indexnow.py <url> [<url> …]  # 지정한 URL만 통보 (새 글 1건 등)

키 파일: 사이트 루트에 {INDEXNOW_KEY}.txt 가 배포되어 있어야 한다(build.py 가 생성).
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE).split("/")[0]
ENDPOINT = "https://api.indexnow.org/indexnow"


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>([^<]+)</loc>", f.read())


def submit(urls):
    urls = [u for u in urls if u.startswith(BASE)]
    if not urls:
        sys.exit("통보할 URL이 없습니다. (도메인 불일치 또는 빈 목록)")
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    print(f"IndexNow → {ENDPOINT}")
    print(f"  host={HOST}  keyLocation={BASE}/{INDEXNOW_KEY}.txt  urls={len(urls)}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            code = resp.status
            body = resp.read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        code = e.code
        body = e.read().decode("utf-8", "ignore")
    # 200=수신, 202=수락(검증 대기). 그 외는 키/도메인 문제일 수 있음.
    print(f"  HTTP {code} {body.strip()[:200]}")
    if code in (200, 202):
        print("  ✅ 통보 완료 (Bing·Naver·Yandex·Seznam 로 전달됨)")
    else:
        print("  ⚠ 실패 — 키 파일 배포 여부와 도메인을 확인하세요.")
        sys.exit(1)


if __name__ == "__main__":
    targets = sys.argv[1:] if len(sys.argv) > 1 else sitemap_urls()
    submit(targets)
