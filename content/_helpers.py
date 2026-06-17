# 지역(동)·역 페이지 공용 빌더 — 모든 하위 페이지가 동일한 구조/요금/CTA를 공유한다.
from .pricing import PRICING

CTA = """
<section class="cta">
<h2>예약문의</h2>
<p>방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:0508-202-4719">0508-202-4719</a>
</section>
"""


def dong_page(gu_slug, gu_name, dong_slug, dong_name, desc, sections):
    """대표 행정동 페이지 dict. sections 는 <section><h2>…</h2>…</section> 반복 HTML."""
    return {
        "path": f"suwon/{gu_slug}/{dong_slug}/",
        "title": f"{dong_name} 출장마사지·홈타이 | 수원 방문 관리 예약 안내",
        "desc": desc,
        "h1": f"{dong_name} 방문 관리 안내",
        "body": sections + PRICING + CTA,
        "breadcrumb": [("지역별 안내", "/suwon/"), (gu_name, f"/suwon/{gu_slug}/"), (dong_name, None)],
    }


def station_page(station_slug, station_name, desc, sections):
    """지하철역·철도역 페이지 dict."""
    return {
        "path": f"suwon/stations/{station_slug}/",
        "title": f"{station_name} 출장마사지·홈타이 | 수원 역세권 방문 관리 안내",
        "desc": desc,
        "h1": f"{station_name} 인근 방문 관리 안내",
        "body": sections + PRICING + CTA,
        "breadcrumb": [("지하철역별 안내", "/suwon/stations/"), (station_name, None)],
    }
