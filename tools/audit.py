#!/usr/bin/env python3
"""배포 전 감사 — 글자수 범위, 타이틀/디스크립션 중복, 내부링크 무결성,
JSON-LD 파싱, 페이지 간 유사도(8-gram Jaccard)를 한 번에 점검한다.

사용: python3 tools/audit.py   (build.py 와 같은 레포 루트에서)
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content import PAGES  # noqa: E402

MIN_CHARS, MAX_CHARS = 2000, 2600


def body_text(body):
    t = re.sub(r'<section class="pricing">.*?</section>', " ", body, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def shingles(text, n=8):
    text = re.sub(r"\s+", "", text)
    return {text[i:i + n] for i in range(0, max(0, len(text) - n + 1))}


def main():
    problems = []
    titles, descs = {}, {}
    paths = {("" if p["path"] == "" else "/" + p["path"]) for p in PAGES}
    # 루트 호환
    paths.add("/")

    indexable = []  # (path, text)
    for p in PAGES:
        path = p["path"] or "/"
        txt = body_text(p["body"])
        n = len(txt)
        noindex = p.get("noindex", False)

        # 글자수 (noindex/약관 제외)
        if not noindex and n < MIN_CHARS:
            problems.append(f"[글자수 미달 {n}] {path} → noindex 처리됨")
        elif not noindex and n > MAX_CHARS:
            problems.append(f"[글자수 초과 {n}] {path}")

        # 타이틀/디스크립션 길이·중복
        t, d = p["title"], p["desc"]
        if t in titles:
            problems.append(f"[타이틀 중복] {path} == {titles[t]}")
        titles[t] = path
        if d in descs:
            problems.append(f"[디스크립션 중복] {path} == {descs[d]}")
        descs[d] = path
        if not (10 <= len(t) <= 60):
            problems.append(f"[타이틀 길이 {len(t)}] {path}")
        if not (40 <= len(d) <= 160):
            problems.append(f"[디스크립션 길이 {len(d)}] {path}")

        # 내부 링크 무결성 (앵커/외부 제외)
        for href in re.findall(r'href="(/[^"#]*)"', p["body"]):
            if href.startswith("/assets") or href.startswith("/favicon"):
                continue
            if href not in paths:
                problems.append(f"[깨진 내부링크] {path} → {href}")

        # JSON-LD 파싱
        for m in re.finditer(r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
                             p.get("extra_head", ""), re.S):
            try:
                json.loads(m.group(1))
            except Exception as e:
                problems.append(f"[JSON-LD 오류] {path}: {e}")

        if not noindex and n >= MIN_CHARS:
            indexable.append((path, txt))

    # 유사도 (8-gram Jaccard) — 색인 페이지 쌍 중 0.30 이상 경고
    sh = {pp: shingles(tt) for pp, tt in indexable}
    keys = list(sh.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = sh[keys[i]], sh[keys[j]]
            if not a or not b:
                continue
            jac = len(a & b) / len(a | b)
            if jac >= 0.30:
                problems.append(f"[유사도 {jac:.2f}] {keys[i]} ~ {keys[j]}")

    print(f"총 {len(PAGES)} 페이지, 색인 대상 {len(indexable)}개")
    if problems:
        print(f"\n⚠ 문제 {len(problems)}건:")
        for x in problems:
            print("  -", x)
        sys.exit(1)
    print("\n✅ 감사 통과: 중복 0 · 깨진 링크 0 · JSON-LD 정상 · 유사도 < 0.30")


if __name__ == "__main__":
    main()
