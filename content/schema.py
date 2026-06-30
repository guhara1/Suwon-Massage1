# 전 페이지 공통 구조화 데이터(Schema.org JSON-LD) + 후기/평점 UI 생성기.
#
# build.py 가 모든 페이지에 대해 page_schema(page) 를 호출해 head 에 주입한다.
#   - LocalBusiness(HealthAndBeautyBusiness): 사업장·평점(aggregateRating)·후기(review)·코스(offer)
#   - BreadcrumbList: 페이지 breadcrumb 기반
#   - FAQPage: 본문 .faq-item 자동 추출
#   - WebSite: 사이트 전체 식별
# 후기 카드/평점 요약 HTML 은 화면 노출 콘텐츠로, Review 스키마와 1:1로 대응시킨다.
import json
import re

from .site import (
    BASE_URL, BRAND, PHONE, REGION, REGION_FULL,
    GEO, POSTAL_CODE, RATING_VALUE, REVIEW_COUNT, BEST_RATING, REVIEWS,
)

BASE = BASE_URL.rstrip("/")


def _ld(obj) -> str:
    """dict → <script type="application/ld+json"> 블록. 한글 보존(ensure_ascii=False)."""
    body = json.dumps(obj, ensure_ascii=False, indent=2)
    return f'<script type="application/ld+json">\n{body}\n</script>\n'


# ---------------------------------------------------------------------------
# 사업장 + 평점 + 후기 + 코스 (전 페이지 공통)
# ---------------------------------------------------------------------------
_OFFERS = [
    ("60분 코스", "90000", "기본 컨디션·릴랙스 케어"),
    ("90분 코스", "150000", "아로마 포함 추천 구성"),
    ("120분 코스", "180000", "전신 집중 프리미엄 케어"),
]


def _reviews_ld():
    out = []
    for r in REVIEWS:
        out.append({
            "@type": "Review",
            "author": {"@type": "Person", "name": r["author"]},
            "datePublished": r["date"],
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": str(r["rating"]),
                "bestRating": BEST_RATING,
                "worstRating": "1",
            },
            "reviewBody": r["body"],
        })
    return out


def business_jsonld() -> str:
    obj = {
        "@context": "https://schema.org",
        "@type": "HealthAndBeautyBusiness",
        "@id": f"{BASE}/#business",
        "name": BRAND,
        "telephone": PHONE,
        "url": f"{BASE}/",
        "image": f"{BASE}/assets/og-image.png",
        "logo": f"{BASE}/assets/icon-512.png",
        "description": f"{REGION_FULL} 전지역 방문 출장마사지·홈타이 예약 안내",
        "priceRange": "₩90,000 - ₩180,000",
        "currenciesAccepted": "KRW",
        "openingHours": "Mo-Su 00:00-24:00",
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday",
                          "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59",
        }],
        "address": {
            "@type": "PostalAddress",
            "addressCountry": "KR",
            "addressRegion": "경기도",
            "addressLocality": "수원시",
            "postalCode": POSTAL_CODE,
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": GEO["lat"],
            "longitude": GEO["lng"],
        },
        "areaServed": {"@type": "AdministrativeArea", "name": REGION_FULL},
        "hasMap": "https://map.naver.com/p/search/수원%20출장마사지",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": RATING_VALUE,
            "reviewCount": REVIEW_COUNT,
            "bestRating": BEST_RATING,
            "worstRating": "1",
        },
        "review": _reviews_ld(),
        "makesOffer": [
            {
                "@type": "Offer",
                "name": name,
                "price": price,
                "priceCurrency": "KRW",
                "description": desc,
            }
            for name, price, desc in _OFFERS
        ],
    }
    return _ld(obj)


def website_jsonld() -> str:
    return _ld({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{BASE}/#website",
        "url": f"{BASE}/",
        "name": BRAND,
        "inLanguage": "ko-KR",
        "publisher": {"@id": f"{BASE}/#business"},
    })


# ---------------------------------------------------------------------------
# BreadcrumbList — 페이지 breadcrumb 기반
# ---------------------------------------------------------------------------
def breadcrumb_jsonld(crumbs, path) -> str:
    items = [{
        "@type": "ListItem", "position": 1, "name": "홈", "item": f"{BASE}/",
    }]
    pos = 2
    for label, href in (crumbs or []):
        entry = {"@type": "ListItem", "position": pos, "name": label}
        if href:
            entry["item"] = BASE + href
        else:
            entry["item"] = BASE + "/" + path
        items.append(entry)
        pos += 1
    if len(items) < 2:           # 홈만 있으면 생략(메인 페이지)
        return ""
    return _ld({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    })


# ---------------------------------------------------------------------------
# FAQPage — 본문 .faq-item 자동 추출
# ---------------------------------------------------------------------------
_FAQ_RE = re.compile(
    r'<div class="faq-item">\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>',
    re.S,
)


def _strip(t: str) -> str:
    t = re.sub(r"<[^>]+>", "", t)
    return re.sub(r"\s+", " ", t).strip()


def faq_jsonld(body: str) -> str:
    qa = _FAQ_RE.findall(body or "")
    if not qa:
        return ""
    return _ld({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": _strip(q),
                "acceptedAnswer": {"@type": "Answer", "text": _strip(a)},
            }
            for q, a in qa
        ],
    })


# ---------------------------------------------------------------------------
# 페이지별 통합 스키마 — build.py 에서 호출
# ---------------------------------------------------------------------------
def page_schema(page: dict) -> str:
    parts = [business_jsonld()]
    if page.get("path", "") == "":      # 메인에서만 WebSite 선언
        parts.append(website_jsonld())
    bc = breadcrumb_jsonld(page.get("breadcrumb"), page.get("path", ""))
    if bc:
        parts.append(bc)
    faq = faq_jsonld(page.get("body", ""))
    if faq:
        parts.append(faq)
    return "".join(parts)


# ---------------------------------------------------------------------------
# 화면 노출용 후기/평점 UI (Review 스키마와 동일 데이터)
# ---------------------------------------------------------------------------
def _stars(n: int) -> str:
    full = "★" * int(n)
    empty = "☆" * (5 - int(n))
    return (f'<span class="stars" aria-hidden="true">{full}'
            f'<span class="stars-empty">{empty}</span></span>')


def rating_summary_html() -> str:
    """평점 요약 배지 — 평균 별점 + 누적 후기 수."""
    return (
        '<div class="rating-summary">'
        f'<span class="rating-score">{RATING_VALUE}</span>'
        f'{_stars(round(float(RATING_VALUE)))}'
        f'<span class="rating-count">이용 후기 {REVIEW_COUNT}건 기준 평균 평점</span>'
        '</div>'
    )


def review_cards_html(limit=None) -> str:
    """후기 카드 목록 HTML. limit 으로 노출 개수 제한."""
    rows = REVIEWS if limit is None else REVIEWS[:limit]
    cards = []
    for r in rows:
        date_disp = r["date"].replace("-", ". ")
        cards.append(
            '<li class="review-card">'
            '<div class="review-head">'
            f'<span class="review-author">{r["author"]}</span>'
            f'{_stars(r["rating"])}'
            f'<span class="review-rating-num">{r["rating"]}.0</span>'
            '</div>'
            '<div class="review-meta">'
            f'<span class="review-tag">{r["region"]}</span>'
            f'<span class="review-tag">{r["theme"]}</span>'
            f'<time datetime="{r["date"]}">{date_disp}</time>'
            '</div>'
            f'<p class="review-body">{r["body"]}</p>'
            '</li>'
        )
    return (
        f'{rating_summary_html()}'
        f'<ul class="review-list">{"".join(cards)}</ul>'
    )
