# 지역(동)·역 페이지 공용 빌더 — 모든 하위 페이지가 동일한 구조/요금/CTA를 공유한다.
from .pricing import PRICING

CTA = """
<section class="cta">
<h2>예약문의</h2>
<p>방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:0508-202-4719">0508-202-4719</a>
</section>
"""


def related_links(items, title="함께 찾아보는 안내", lead=None):
    """롱테일 주제 내부링크 섹션. items = [(앵커 텍스트, href), ...]."""
    lead_html = f"<p>{lead}</p>" if lead else ""
    lis = "".join(
        f'<li><a href="{href}">{text}</a></li>' for text, href in items
    )
    return (
        f'<section class="related-links" aria-label="{title}">'
        f"<h2>{title}</h2>{lead_html}"
        f'<ul class="related-grid">{lis}</ul></section>'
    )


# 지역(동)·역 페이지 공통 롱테일 내부링크 — 모든 하위 페이지에 자동 삽입한다.
_DONG_RELATED = related_links(
    [
        ("수원 출장마사지 코스·요금 한눈에 보기", "/courses/#price"),
        ("처음 이용한다면 준비물·절차 가이드", "/guide/#first"),
        ("스웨디시와 타이마사지 차이 비교", "/magazine/swedish-vs-thai/"),
        ("운동 후 회복 마사지 받는 타이밍", "/magazine/post-workout-timing/"),
        ("심야 24시간 방문 마사지 이용 안내", "/themes/24hours/"),
        ("수면 가능 새벽 홈타이 안내", "/themes/overnight/"),
        ("커플 동시 진행 마사지 코스", "/themes/couple/"),
        ("예약 방법·변경·취소 기준 안내", "/reservation/"),
        ("실제 이용자 후기 모아 보기", "/reviews/"),
    ],
    title="이 지역에서 함께 많이 찾는 주제",
    lead="원하시는 주제를 눌러 더 자세한 안내를 확인하세요. 어느 지역이든 동일한 기준으로 예약하실 수 있습니다.",
)


def dong_page(gu_slug, gu_name, dong_slug, dong_name, desc, sections):
    """대표 행정동 페이지 dict. sections 는 <section><h2>…</h2>…</section> 반복 HTML."""
    return {
        "path": f"suwon/{gu_slug}/{dong_slug}/",
        "title": f"{dong_name} 출장마사지·홈타이 | 수원 방문 관리 예약 안내",
        "desc": desc,
        "h1": f"{dong_name} 방문 관리 안내",
        "body": sections + _DONG_RELATED + PRICING + CTA,
        "breadcrumb": [("지역별 안내", "/suwon/"), (gu_name, f"/suwon/{gu_slug}/"), (dong_name, None)],
    }


def station_page(station_slug, station_name, desc, sections):
    """지하철역·철도역 페이지 dict."""
    return {
        "path": f"suwon/stations/{station_slug}/",
        "title": f"{station_name} 출장마사지·홈타이 | 수원 역세권 방문 관리 안내",
        "desc": desc,
        "h1": f"{station_name} 인근 방문 관리 안내",
        "body": sections + _DONG_RELATED + PRICING + CTA,
        "breadcrumb": [("지하철역별 안내", "/suwon/stations/"), (station_name, None)],
    }
