# 바로 GO — 수원 출장마사지·홈타이 안내 사이트

경기도 수원시 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

> 노원 블랙 마사지 사이트 엔진(PLAYBOOK.md 참고)을 수원으로 이식했습니다.
> 다크 럭스 디자인 · 상단/하위 메뉴 · 좌측 목차 · 글자수 기반 색인 게이팅을 그대로 사용합니다.

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·목차·글자수 검사·sitemap 생성)
content/
  site.py           # 상호(바로 GO)·전화·BASE_URL·상단/하위 메뉴(NAV)
  _helpers.py       # 동/역 페이지 공용 빌더(요금표·CTA 포함)
  main.py           # 메인 (히어로 + HealthAndBeautyBusiness/FAQPage JSON-LD)
  areas.py          # 지역: 수원 허브 + 행정구 허브 4(장안·권선·팔달·영통)
  dongs_*.py        # 대표 행정동 29 (구별 모듈)
  stations.py       # 지하철역: 허브 + 14개 역
  themes.py         # 테마: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
  magazine.py       # 매거진 허브 + 아티클
  about.py          # 운영자 소개 (E-E-A-T)
assets/             # 다크 럭스 CSS, 모바일 내비 JS, 파비콘/OG
tools/audit.py      # 배포 전 감사(중복·깨진 링크·JSON-LD·유사도)
```

## 빌드

```bash
python3 build.py        # 페이지별 글자수 리포트 + sitemap/robots 생성
python3 tools/audit.py  # 배포 전 감사
```

## 메뉴 구조 (상단 + 하위)

```
홈 · 수원 출장마사지(/massage/) · 지역별 안내(/suwon/) · 지하철역별 안내(/suwon/stations/)
테마별 안내 · 코스안내 · 예약안내 · 이용가이드 · 매거진 · 후기 · 고객센터
지역별 안내 ▸ 수원시 전체 / 장안구 / 권선구 / 팔달구 / 영통구 → 각 구에서 대표 동 펼침
```

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 지역은 대표 동 단위만 — 숫자 행정동(정자1~3동, 매탄1~4동 등) 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역(수원역)도 URL 하나, 출구별 페이지 없음
- **지역+역+테마 조합 페이지 없음**(도어웨이 방지) — 테마는 독립 페이지로만 운영
- 페이지별 고유 본문 작성 (지역명만 바꾼 복붙 없음)

## 남은 작업 (다음 단계)

현재 색인 게이팅에 따라 일부 페이지가 2,000자에 약간 못 미쳐 `noindex` 상태입니다.
색인시키려면 본문을 2,000자 이상으로 보강하면 됩니다.

- 지역 허브(/suwon/), 행정구 허브 4곳, 역세권 허브(/suwon/stations/)
- 역세권 상세 14개 페이지

## 색인 가속 (네이버·구글·빙)

빌드 시 자동 생성: `sitemap.xml`(lastmod 포함), `rss.xml`(매거진 피드),
`robots.txt`(주요 봇 명시 + sitemap), IndexNow 키 파일 `e93b2eb05cecdff4896a9ef76434b898.txt`.

### IndexNow — 빙·네이버·얀덱스 즉시 통보 (추천)

키 파일이 배포돼 있으면(빌드가 루트에 생성) 아래 한 줄로 전체 또는 개별 URL을 통보합니다.

```bash
python tools/indexnow.py                  # sitemap의 모든 URL 일괄 통보
python tools/indexnow.py https://suwon-massage1.netlify.app/magazine/new-post/   # 새 글 1건
```

> 글을 올리거나 페이지를 고칠 때마다 해당 URL만 통보하면 즉시 색인 요청이 전달됩니다.
> 빙과 네이버(Yeti)가 IndexNow에 참여합니다. **키 파일이 먼저 배포된 뒤** 실행하세요.

### 구글 Indexing API — 구글 즉시 통보 (구글은 IndexNow 미참여)

```bash
# 사전: Indexing API 사용설정 + 서비스계정 JSON + Search Console 소유자 등록 + pip install google-auth requests
GOOGLE_APPLICATION_CREDENTIALS=/path/sa.json python tools/google_index.py
```

> 구글 Indexing API는 공식적으로 JobPosting·BroadcastEvent용입니다. 일반 페이지는
> Search Console 사이트맵 제출 + URL 검사가 가장 확실합니다.

### sitemap ping은?

구글(2023.6)·빙의 `ping?sitemap=` 엔드포인트는 **폐지**되었습니다. 현재 권장 경로는
①IndexNow(빙·네이버) + ②Search Console/서치어드바이저 사이트맵 제출 + ③구글 Indexing API 입니다.

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console / 네이버 서치어드바이저에 `sitemap.xml` 제출
