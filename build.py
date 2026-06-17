# -*- coding: utf-8 -*-
"""
수원 출장마사지 · 홈타이 지역 SEO 사이트 정적 생성기
- 메인 1 + 행정구 4 + 대표 행정동 29 + 역세권 14 + 생활권 10 + 기타 5 = 63 페이지
- 메타 디스크립션은 모두 80자 이내
- Schema: WebPage / BreadcrumbList / Organization (LocalBusiness 미사용)
"""
import os
import html
import datetime

# ---------------------------------------------------------------------------
# 사이트 전역 설정 (도메인은 실제 값으로 교체하세요)
# ---------------------------------------------------------------------------
SITE_NAME = "바로 GO"
PHONE = "0508-202-4719"
PHONE_TEL = "0508-202-4719"
SITE_URL = "https://suwon-chuljangmassage.kr"   # 실제 도메인으로 교체
OG_IMAGE = SITE_URL + "/assets/og-image.svg"
TODAY = datetime.date.today().isoformat()

OUT = os.path.dirname(os.path.abspath(__file__))

# 80자 이내 검증용
def chk(desc):
    assert len(desc) <= 80, f"[80자 초과 {len(desc)}] {desc}"
    return desc

# ---------------------------------------------------------------------------
# 데이터 정의
# ---------------------------------------------------------------------------
# 각 항목: slug(상대경로), title, h1, desc(<=80), keyword, ctx(본문 소재 리스트), links(내부링크 키)
DISTRICTS = {
    "jangan": dict(
        slug="suwon/jangan-gu-chuljangmassage",
        name="장안구",
        title="장안구 출장마사지｜성균관대역·화서역·정자동 홈타이 안내",
        h1="장안구 출장마사지 · 홈타이 생활권 안내",
        desc="장안구 출장마사지·홈타이 예약 전 성균관대역, 화서역 주변을 확인하세요.",
        keyword="장안구 출장마사지",
        ctx=["성균관대역", "화서역", "정자동", "조원동", "파장동", "송죽동", "북수원 생활권"],
        intro="장안구는 성균관대역, 화서역, 정자동, 조원동, 파장동을 중심으로 한 북수원 생활권입니다. "
              "정자시장과 수원종합운동장, 장안구청 인근이 주요 거점이며, 파장동과 연무동 일부는 차량 이동 기준이 달라질 수 있습니다.",
    ),
    "gwonseon": dict(
        slug="suwon/gwonseon-gu-chuljangmassage",
        name="권선구",
        title="권선구 출장마사지｜권선동·호매실·고색 생활권 안내",
        h1="권선구 출장마사지 · 홈타이 생활권 안내",
        desc="권선구 출장마사지·홈타이 이용 전 권선동, 호매실, 고색 기준을 확인하세요.",
        keyword="권선구 출장마사지",
        ctx=["세류역", "권선동", "호매실동", "고색역", "오목천역", "서수원 생활권"],
        intro="권선구는 수원역 남부, 세류역, 고색역, 오목천역과 권선동·호매실동 생활권이 함께 있는 서수원·남수원 지역입니다. "
              "호매실동과 금곡동은 서수원 주거지와 광역교통 이슈를 함께 고려하는 것이 좋습니다.",
    ),
    "paldal": dict(
        slug="suwon/paldal-gu-chuljangmassage",
        name="팔달구",
        title="팔달구 출장마사지｜수원역·인계동·행궁동 홈타이 안내",
        h1="팔달구 출장마사지 · 홈타이 생활권 안내",
        desc="팔달구 출장마사지·홈타이 예약 전 수원역, 인계동, 행궁동을 확인하세요.",
        keyword="팔달구 출장마사지",
        ctx=["수원역", "매교역", "인계동", "행궁동", "화서동", "수원화성"],
        intro="팔달구는 수원역, 매교역, 인계동, 행궁동, 화서동, 수원화성 생활권이 중심입니다. "
              "수원역 로데오거리와 나혜석거리, 화성행궁 등 유동 인구가 많은 거점이 모여 있습니다.",
    ),
    "yeongtong": dict(
        slug="suwon/yeongtong-gu-chuljangmassage",
        name="영통구",
        title="영통구 출장마사지｜광교·영통·망포 생활권 안내",
        h1="영통구 출장마사지 · 홈타이 생활권 안내",
        desc="영통구 출장마사지·홈타이 이용 전 광교, 영통, 망포 생활권을 확인하세요.",
        keyword="영통구 출장마사지",
        ctx=["광교동", "영통동", "망포동", "매탄동", "원천동", "광교호수공원"],
        intro="영통구는 광교, 영통, 망포, 매탄, 원천 생활권을 중심으로 검색 수요가 생기는 지역입니다. "
              "광교중앙역·광교역, 영통역·청명역, 망포역과 삼성전자 수원사업장 인근이 주요 거점입니다.",
    ),
}

# 대표 행정동: (key) -> dict(district, slug, name, title, desc_tail, ctx)
DONGS = [
    # 장안구
    ("jangan", "pajang-dong", "파장동", "파장동 출장마사지｜북수원 차량 이동 생활권 안내",
     "파장동, 북수원 차량 이동 기준을", ["북수원", "파장동", "차량 이동", "추가 이동비"]),
    ("jangan", "yulcheon-dong", "율천동", "율천동 출장마사지｜성균관대역·율전동 홈타이 안내",
     "성균관대역, 율전동 생활권을", ["성균관대역", "율전동", "성균관대 자연과학캠퍼스"]),
    ("jangan", "jeongja-dong", "정자동", "정자동 출장마사지｜정자시장·북수원 생활권 안내",
     "정자시장, 북수원 생활권을", ["정자시장", "수원종합운동장 인접", "화서역", "성균관대역 접근성"]),
    ("jangan", "yeonghwa-dong", "영화동", "영화동 출장마사지｜장안문·영화동 주거권 안내",
     "장안문, 영화동 주거권을", ["장안문", "영화동 주거권", "북수원"]),
    ("jangan", "songjuk-dong", "송죽동", "송죽동 출장마사지｜송죽동·종합운동장 인접권 안내",
     "송죽동, 수원종합운동장 인접권을", ["송죽동", "수원종합운동장 인접"]),
    ("jangan", "jowon-dong", "조원동", "조원동 출장마사지｜장안구청·수원종합운동장 안내",
     "장안구청, 수원종합운동장 생활권을", ["장안구청", "수원종합운동장", "조원시장"]),
    ("jangan", "yeonmu-dong", "연무동", "연무동 출장마사지｜연무동·광교산 인접 생활권 안내",
     "연무동, 광교산 인접 생활권을", ["연무동", "광교산 인접", "차량 이동"]),
    # 권선구
    ("gwonseon", "seryu-dong", "세류동", "세류동 출장마사지｜세류역·남수원 생활권 안내",
     "세류역, 남수원 생활권을", ["세류역", "남수원", "수원공군기지 인접"]),
    ("gwonseon", "pyeong-dong", "평동", "평동 출장마사지｜수원역 서부·평동 생활권 안내",
     "수원역 서부, 평동 생활권을", ["수원역 서부", "평동", "탑동"]),
    ("gwonseon", "seodun-dong", "서둔동", "서둔동 출장마사지｜서둔동·탑동 생활권 안내",
     "서둔동, 탑동 생활권을", ["서둔동", "탑동", "농촌진흥청 부지 인근"]),
    ("gwonseon", "guun-dong", "구운동", "구운동 출장마사지｜구운동·서수원 생활권 안내",
     "구운동, 서수원 생활권을", ["구운동", "서수원", "서호공원 인근"]),
    ("gwonseon", "geumgok-dong", "금곡동", "금곡동 출장마사지｜호매실지구 인접 생활권 안내",
     "호매실지구 인접, 금곡동 생활권을", ["금곡동", "호매실지구 인접", "서수원 주거지", "광역교통"]),
    ("gwonseon", "homaesil-dong", "호매실동", "호매실동 출장마사지｜호매실지구 홈타이 안내",
     "호매실지구 생활권을", ["호매실동", "호매실지구", "서수원 주거지", "신분당선 연장"]),
    ("gwonseon", "gwonseon-dong", "권선동", "권선동 출장마사지｜수원시청역·권선시장 안내",
     "수원시청역, 권선시장 생활권을", ["수원시청역", "권선시장", "매탄권선역 인접"]),
    ("gwonseon", "gokseon-dong", "곡선동", "곡선동 출장마사지｜곡반정동·권선 인접권 안내",
     "곡반정동, 권선 인접권을", ["곡반정동", "권선 인접권"]),
    ("gwonseon", "ipbuk-dong", "입북동", "입북동 출장마사지｜입북동·당수 생활권 안내",
     "입북동, 당수 생활권을", ["입북동", "당수지구", "서수원 외곽", "차량 이동"]),
    # 팔달구
    ("paldal", "haenggung-dong", "행궁동", "행궁동 출장마사지｜수원화성·행궁동 생활권 안내",
     "수원화성, 행궁동 생활권을", ["수원화성", "화성행궁", "장안문", "팔달문"]),
    ("paldal", "maegyo-dong", "매교동", "매교동 출장마사지｜매교역·팔달구 생활권 안내",
     "매교역, 팔달구 생활권을", ["매교역", "팔달구 중심", "인계동 인접"]),
    ("paldal", "maesan-dong", "매산동", "매산동 출장마사지｜수원역·로데오거리 안내",
     "수원역, 로데오거리 생활권을", ["수원역", "로데오거리", "AK플라자", "환승센터"]),
    ("paldal", "godeung-dong", "고등동", "고등동 출장마사지｜고등지구·수원역 인접권 안내",
     "고등지구, 수원역 인접권을", ["고등지구", "수원역 인접", "팔달구 서부"]),
    ("paldal", "hwaseo-dong", "화서동", "화서동 출장마사지｜화서역·스타필드 인근 안내",
     "화서역, 스타필드 인근 생활권을", ["화서역", "스타필드 수원", "정자동 인접"]),
    ("paldal", "ji-dong", "지동", "지동 출장마사지｜지동시장·팔달문 생활권 안내",
     "지동시장, 팔달문 생활권을", ["지동시장", "팔달문", "수원화성 인접"]),
    ("paldal", "uman-dong", "우만동", "우만동 출장마사지｜아주대·월드컵경기장 인근 안내",
     "아주대, 월드컵경기장 인근을", ["아주대", "수원월드컵경기장", "우만시장"]),
    ("paldal", "ingye-dong", "인계동", "인계동 출장마사지｜나혜석거리·수원시청역 안내",
     "나혜석거리, 수원시청역 생활권을", ["나혜석거리", "수원시청역", "권선동 인접"]),
    # 영통구
    ("yeongtong", "maetan-dong", "매탄동", "매탄동 출장마사지｜매탄권선역·삼성전자 인근 안내",
     "매탄권선역, 삼성전자 인근을", ["매탄권선역", "삼성전자 수원사업장", "권선동 인접"]),
    ("yeongtong", "woncheon-dong", "원천동", "원천동 출장마사지｜아주대·광교호수공원 인접권 안내",
     "아주대, 광교호수공원 인접권을", ["아주대", "광교호수공원", "원천저수지"]),
    ("yeongtong", "gwanggyo-dong", "광교동", "광교동 출장마사지｜광교중앙역·광교신도시 안내",
     "광교중앙역, 광교신도시 생활권을", ["광교중앙역", "광교신도시", "광교호수공원", "경기대 인근"]),
    ("yeongtong", "yeongtong-dong", "영통동", "영통동 출장마사지｜영통역·청명역 중심상권 안내",
     "영통역, 청명역 중심상권을", ["영통역", "청명역", "영통 중심상권"]),
    ("yeongtong", "mangpo-dong", "망포동", "망포동 출장마사지｜망포역·영통 남부 생활권 안내",
     "망포역, 영통 남부 생활권을", ["망포역", "영통 남부", "동탄 인접", "기흥 인접"]),
]

# 역세권: (slug, name, title, desc_tail, ctx, future)
STATIONS = [
    ("suwon-station", "수원역", "수원역 출장마사지｜매산동·수원역 로데오거리 홈타이 안내",
     "매산동, 수원역 로데오거리 기준을", ["매산동", "로데오거리", "AK플라자", "환승센터"],
     "수원역은 1호선·수인분당선·KTX가 함께 지나가며 GTX-C 노선이 논의되는 거점입니다. 노선별로 페이지를 나누지 않고 본문에서 환승 특징만 보조로 안내합니다."),
    ("hwaseo-station", "화서역", "화서역 출장마사지｜화서동·정자동 인접 생활권 안내",
     "화서동, 정자동 인접 생활권을", ["화서동", "정자동 인접", "스타필드 수원"],
     "화서역은 장안구·팔달구 인접 생활권으로 스타필드 수원이 가깝습니다. 신분당선 연장 이슈는 본문 보조 설명으로만 다룹니다."),
    ("sungkyunkwan-univ-station", "성균관대역", "성균관대역 출장마사지｜율천동·정자동 생활권 안내",
     "율천동, 정자동 생활권을", ["율천동", "정자동", "성균관대 자연과학캠퍼스"],
     "성균관대역은 율천동·정자동 생활권을 담당하는 역세권입니다."),
    ("seryu-station", "세류역", "세류역 출장마사지｜세류동·권선 남부 생활권 안내",
     "세류동, 권선 남부 생활권을", ["세류동", "권선 남부", "수원공군기지 인접"],
     "세류역은 세류동과 권선구 남부 생활권을 담당합니다."),
    ("maegyo-station", "매교역", "매교역 출장마사지｜매교동·팔달구 생활권 안내",
     "매교동, 팔달구 생활권을", ["매교동", "팔달구", "인계동 인접"],
     "매교역은 팔달구 매교동·인계동 인접 생활권을 담당합니다."),
    ("suwon-cityhall-station", "수원시청역", "수원시청역 출장마사지｜인계동·권선동 중심 안내",
     "인계동, 권선동 중심 생활권을", ["인계동", "권선동", "나혜석거리"],
     "수원시청역은 인계동·권선동 생활권의 중심입니다."),
    ("maetangwonseon-station", "매탄권선역", "매탄권선역 출장마사지｜매탄동·권선동 인접권 안내",
     "매탄동, 권선동 인접권을", ["매탄동", "권선동 인접", "삼성전자 인근"],
     "매탄권선역은 매탄동·권선동 인접 생활권을 담당합니다."),
    ("mangpo-station", "망포역", "망포역 출장마사지｜망포동·영통 남부 홈타이 안내",
     "망포동, 영통 남부 생활권을", ["망포동", "영통 남부", "동탄 인접"],
     "망포역은 망포동·영통 남부 생활권을 담당하며 동탄인덕원선 이슈는 본문 보조 설명으로 다룹니다."),
    ("yeongtong-station", "영통역", "영통역 출장마사지｜영통 중심상권 방문 안내",
     "영통 중심상권 주변을", ["영통 중심상권", "청명역 인접"],
     "영통역은 영통 중심상권을 담당하는 역세권입니다."),
    ("cheongmyeong-station", "청명역", "청명역 출장마사지｜영통동·청명 생활권 안내",
     "영통동, 청명 생활권을", ["영통동", "청명 생활권"],
     "청명역은 영통동·청명 생활권을 담당합니다."),
    ("gwanggyo-jungang-station", "광교중앙역", "광교중앙역 출장마사지｜광교신도시 중심 생활권 안내",
     "광교신도시 중심 생활권을", ["광교신도시", "광교호수공원", "신분당선"],
     "광교중앙역은 광교신도시 중심 생활권을 담당하는 역세권입니다."),
    ("gwanggyo-station", "광교역", "광교역 출장마사지｜광교산·경기대 인근 안내",
     "광교산, 경기대 인근을", ["광교산", "경기대 인근", "광교 상류"],
     "광교역은 광교산·경기대 인근 생활권을 담당합니다."),
    ("gosaek-station", "고색역", "고색역 출장마사지｜서수원·고색 생활권 안내",
     "서수원, 고색 생활권을", ["서수원", "고색동", "권선 서부"],
     "고색역은 서수원·고색 생활권을 담당합니다."),
    ("omokcheon-station", "omokcheon", "오목천역 출장마사지｜권선 서부 생활권 안내",
     "권선 서부, 오목천동 생활권을", ["오목천동", "권선 서부"],
     "오목천역은 오목천동·권선 서부 생활권을 담당합니다."),
]
# 오목천역 name 보정
STATIONS[-1] = ("omokcheon-station", "오목천역", STATIONS[-1][2], STATIONS[-1][3], STATIONS[-1][4], STATIONS[-1][5])

# 생활권: (slug, name, title, desc_tail, ctx)
AREAS = [
    ("ingye-nahyeseok", "인계동 나혜석거리", "인계동 나혜석거리 출장마사지｜수원시청역 중심 상권 안내",
     "수원시청역 중심 상권을", ["나혜석거리", "수원시청역", "인계동 중심상권"]),
    ("suwon-rodeo", "수원역 로데오거리", "수원역 로데오거리 출장마사지｜매산동 중심 생활권 안내",
     "매산동 중심 생활권을", ["수원역 로데오거리", "매산동", "AK플라자"]),
    ("gwanggyo-newtown", "광교신도시", "광교신도시 출장마사지｜광교중앙역·호수공원 안내",
     "광교중앙역, 호수공원 생활권을", ["광교신도시", "광교중앙역", "광교호수공원"]),
    ("yeongtong-center", "영통 중심상권", "영통 중심상권 출장마사지｜영통역·청명역 생활권 안내",
     "영통역, 청명역 생활권을", ["영통 중심상권", "영통역", "청명역"]),
    ("mangpo-area", "망포역 생활권", "망포역 생활권 출장마사지｜망포동·영통 남부 안내",
     "망포동, 영통 남부 생활권을", ["망포역", "망포동", "영통 남부"]),
    ("hwaseo-starfield", "화서역 스타필드 인근", "화서역 스타필드 인근 출장마사지｜화서동·정자동 안내",
     "화서동, 정자동 생활권을", ["화서역", "스타필드 수원", "정자동"]),
    ("sungkyunkwan-area", "성균관대역 생활권", "성균관대역 생활권 출장마사지｜율천동·천천동 안내",
     "율천동, 천천동 생활권을", ["성균관대역", "율천동", "천천동"]),
    ("homaesil-district", "호매실지구", "호매실지구 출장마사지｜금곡동·호매실동 안내",
     "금곡동, 호매실동 생활권을", ["호매실지구", "금곡동", "호매실동"]),
    ("gwonseon-area", "권선동 생활권", "권선동 생활권 출장마사지｜수원시청역·권선시장 안내",
     "수원시청역, 권선시장 생활권을", ["권선동", "수원시청역", "권선시장"]),
    ("suwon-cityhall-area", "수원시청 인근", "수원시청 인근 출장마사지｜인계동·권선동 방문 기준 안내",
     "인계동, 권선동 방문 기준을", ["수원시청", "인계동", "권선동"]),
]

# 기타 페이지
MISC = [
    ("reservation", "예약 안내", "예약 안내｜수원 출장마사지 · 홈타이 예약 방법",
     "수원 출장마사지·홈타이 예약 방법과 가능 시간, 결제·취소 기준을 안내합니다."),
    ("before-use", "이용 전 확인사항", "이용 전 확인사항｜수원 출장마사지 · 홈타이",
     "수원 출장마사지·홈타이 이용 전 방문 지역, 이동비, 취소 기준을 확인하세요."),
    ("hometai-guide", "홈타이 이용 가이드", "홈타이 이용 가이드｜수원 출장마사지 · 홈타이",
     "수원 홈타이 이용 가이드. 방문형 관리 서비스 절차와 준비 사항을 안내합니다."),
    ("privacy", "개인정보 처리방침", "개인정보 처리방침｜수원 출장마사지 · 홈타이",
     "수원 출장마사지·홈타이 사이트의 개인정보 수집·이용·보관 기준을 안내합니다."),
    ("support", "고객센터", "고객센터｜수원 출장마사지 · 홈타이 문의 안내",
     "수원 출장마사지·홈타이 예약 문의와 고객센터 연락 방법을 안내합니다."),
]

# 검증
for d in DISTRICTS.values():
    chk(d["desc"])
for m in MISC:
    chk(m[3])

# ---------------------------------------------------------------------------
# 경로/URL 유틸
# ---------------------------------------------------------------------------
def dong_slug(d):
    district, slug = d[0], d[1]
    return f"suwon/{district}/{slug}-chuljangmassage"

def station_slug(s):
    return f"suwon/{s[0]}-chuljangmassage"

def area_slug(a):
    return f"suwon/area/{a[0]}-chuljangmassage"

MAIN_SLUG = "suwon-chuljangmassage"

def url_of(slug):
    return f"{SITE_URL}/{slug}/"

# ---------------------------------------------------------------------------
# HTML 템플릿
# ---------------------------------------------------------------------------
def jsonld(slug, title, desc, breadcrumbs):
    page_url = url_of(slug)
    items = []
    for i, (name, b_slug) in enumerate(breadcrumbs, start=1):
        item_url = SITE_URL + "/" if b_slug == "" else url_of(b_slug)
        items.append({
            "@type": "ListItem", "position": i,
            "name": name, "item": item_url
        })
    import json
    data = [
        {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": title,
            "description": desc,
            "url": page_url,
            "inLanguage": "ko",
            "primaryImageOfPage": {"@type": "ImageObject", "url": OG_IMAGE},
            "isPartOf": {"@type": "WebSite", "name": f"{SITE_NAME} 수원 출장마사지", "url": SITE_URL + "/"},
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": items,
        },
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": SITE_NAME,
            "url": SITE_URL + "/",
            "logo": OG_IMAGE,
            "image": OG_IMAGE,
            "telephone": PHONE,
            "areaServed": "수원시",
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": PHONE,
                "contactType": "reservations",
                "areaServed": "KR",
                "availableLanguage": "Korean",
            },
        },
    ]
    return json.dumps(data, ensure_ascii=False, indent=2)


def render(slug, title, desc, h1, breadcrumbs, body_html, related):
    """related: list of (label, slug)"""
    page_url = url_of(slug)
    bc_html = []
    for i, (name, b_slug) in enumerate(breadcrumbs):
        if i < len(breadcrumbs) - 1:
            href = SITE_URL + "/" if b_slug == "" else f"/{b_slug}/"
            bc_html.append(f'<a href="{href}">{html.escape(name)}</a>')
        else:
            bc_html.append(f'<span aria-current="page">{html.escape(name)}</span>')
    bc = '<nav class="breadcrumb" aria-label="breadcrumb">' + ' <span class="sep">›</span> '.join(bc_html) + '</nav>'

    related_html = ""
    if related:
        lis = "\n".join(f'        <li><a href="/{rs}/">{html.escape(rl)}</a></li>' for rl, rs in related)
        related_html = f"""
    <section class="related">
      <h2>관련 지역 바로가기</h2>
      <ul class="link-grid">
{lis}
      </ul>
    </section>"""

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{page_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME} 수원 출장마사지">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{page_url}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:locale" content="ko_KR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">
{jsonld(slug, title, desc, breadcrumbs)}
</script>
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/">{SITE_NAME} <span>수원 출장마사지</span></a>
    <a class="cta-phone" href="tel:{PHONE_TEL}">전화예약 {PHONE}</a>
  </div>
</header>
<main class="wrap">
  {bc}
  <article>
    <h1>{html.escape(h1)}</h1>
{body_html}
{related_html}
    <section class="cta-box">
      <h2>예약 문의</h2>
      <p>방문 가능 지역과 예약 가능 시간을 먼저 확인한 뒤 전화로 문의해 주세요.</p>
      <p class="phone-big"><a href="tel:{PHONE_TEL}">{SITE_NAME} 전화예약 {PHONE}</a></p>
    </section>
  </article>
</main>
<footer class="site-footer">
  <div class="wrap">
    <p class="biz">상호: {SITE_NAME} · 전화예약: {PHONE}</p>
    <nav class="foot-nav">
      <a href="/suwon-chuljangmassage/">메인</a>
      <a href="/reservation/">예약 안내</a>
      <a href="/before-use/">이용 전 확인사항</a>
      <a href="/hometai-guide/">홈타이 가이드</a>
      <a href="/privacy/">개인정보 처리방침</a>
      <a href="/support/">고객센터</a>
    </nav>
    <p class="notice">본 사이트는 수원시 방문형 마사지·홈타이 지역 정보 안내 사이트입니다. 불법·선정적 서비스를 제공하거나 알선하지 않습니다.</p>
  </div>
</footer>
</body>
</html>
"""


def write(slug, content):
    path = os.path.join(OUT, slug, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# 본문 생성 (지역별 고유 문단)
# ---------------------------------------------------------------------------
def trust_block(area_name):
    return f"""    <section>
      <h2>{html.escape(area_name)} 예약 전 확인사항</h2>
      <ul class="check">
        <li>방문 가능 지역과 예약 가능 시간을 먼저 확인합니다.</li>
        <li>거리에 따라 추가 이동비가 발생할 수 있습니다.</li>
        <li>결제 방식, 취소 기준, 서비스 범위를 사전에 안내받으세요.</li>
        <li>개인정보는 예약 목적 범위에서만 이용·보관됩니다.</li>
      </ul>
    </section>"""


def keyword_join(ctx):
    return ", ".join(ctx)


def all_links():
    """label->slug 매핑 (관련 링크용)"""
    m = {}
    for k, d in DISTRICTS.items():
        m[f"{d['name']} 출장마사지"] = d["slug"]
    for d in DONGS:
        m[f"{d[2]} 출장마사지"] = dong_slug(d)
    for s in STATIONS:
        m[f"{s[1]} 출장마사지"] = station_slug(s)
    for a in AREAS:
        m[f"{a[1]} 출장마사지"] = area_slug(a)
    return m

LINKS = all_links()

def L(label):
    """label로 (표시명, slug) 반환"""
    return (label, LINKS[label])


# ---------------------------------------------------------------------------
# 1) 메인 페이지
# ---------------------------------------------------------------------------
def build_main():
    slug = MAIN_SLUG
    title = "수원 출장마사지｜수원시 홈타이 지역별 예약 안내"
    desc = chk("수원 출장마사지·홈타이 예약 전 4개 구, 역세권, 이용 기준을 정리했습니다.")
    h1 = "수원 출장마사지 · 수원시 홈타이 지역별 예약 안내"

    def gu_links():
        return "\n".join(
            f'        <li><a href="/{d["slug"]}/">{d["name"]} 출장마사지</a></li>'
            for d in DISTRICTS.values())

    def station_links():
        rows = "\n".join(
            f'        <li><a href="/{station_slug(s)}/">{s[1]} 출장마사지</a></li>'
            for s in STATIONS)
        return rows

    def area_links():
        return "\n".join(
            f'        <li><a href="/{area_slug(a)}/">{a[1]} 출장마사지</a></li>'
            for a in AREAS)

    def dong_links():
        out = []
        for key, d in DISTRICTS.items():
            out.append(f'      <h3>{d["name"]}</h3>\n      <ul class="link-grid">')
            for dn in DONGS:
                if dn[0] == key:
                    out.append(f'        <li><a href="/{dong_slug(dn)}/">{dn[2]} 출장마사지</a></li>')
            out.append('      </ul>')
        return "\n".join(out)

    body = f"""    <section>
      <h2>수원시에서 출장마사지를 찾는 이유</h2>
      <p>수원 출장마사지를 찾는 분들은 대부분 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다.
      수원시는 장안구, 권선구, 팔달구, 영통구로 나뉘고 각 구의 생활권 성격이 다릅니다. 이 사이트는 4개 구,
      대표 행정동, 역세권, 생활권을 기준으로 본인 위치에 맞는 정보를 빠르게 찾도록 정리한 지역 안내 사이트입니다.</p>
      <p>수원 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다.
      예약 전 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제·취소 기준을 확인하는 것이 좋습니다.</p>
    </section>

    <section>
      <h2>장안구·권선구·팔달구·영통구 생활권 차이</h2>
      <p>장안구는 성균관대역·화서역·정자동·조원동·파장동 중심의 북수원 생활권, 권선구는 세류동·권선동·호매실동·고색동·오목천동의 서수원·남수원 생활권입니다.
      팔달구는 수원역·매교역·인계동·행궁동·수원화성 생활권, 영통구는 광교·영통·망포·매탄·원천 생활권을 중심으로 검색 수요가 생깁니다.</p>
      <ul class="link-grid">
{gu_links()}
      </ul>
    </section>

    <section>
      <h2>대표 행정동별 방문 가능 지역 안내</h2>
      <p>번호가 붙은 행정동은 개별 페이지로 만들지 않고 대표 동으로 통합했습니다.
      정자1~3동은 정자동, 세류1~3동은 세류동, 매탄1~4동은 매탄동, 영통1~3동은 영통동으로 묶어 중복 콘텐츠를 피했습니다.</p>
{dong_links()}
    </section>

    <section>
      <h2>수원역·광교중앙역·영통역·망포역 역세권 안내</h2>
      <p>같은 역을 노선별로 나누면 중복 콘텐츠 위험이 생기므로, 수원역은 1호선·수인분당선·KTX가 있어도 한 개 페이지로 운영하고 본문에서 환승 특징을 설명합니다.</p>
      <ul class="link-grid">
{station_links()}
      </ul>
    </section>

    <section>
      <h2>인계동·광교·영통·호매실 생활권 구성 방식</h2>
      <ul class="link-grid">
{area_links()}
      </ul>
    </section>

    <section>
      <h2>수원 홈타이 예약 전 확인사항</h2>
      <ul class="check">
        <li>방문 가능 지역과 예약 가능 시간을 먼저 확인합니다.</li>
        <li>광교·영통·망포 생활권과 호매실·고색·오목천, 북수원 생활권은 이동 동선이 다릅니다.</li>
        <li>금곡동·호매실동·오목천동·파장동·연무동 일부는 차량 이동 기준과 추가 이동비가 달라질 수 있습니다.</li>
        <li>결제 방식, 취소 기준, 개인정보 처리 기준을 사전에 확인하세요.</li>
      </ul>
    </section>

    <section>
      <h2>수원 출장마사지 사이트 이용 가이드</h2>
      <p>메인페이지는 수원시 전체 안내, 행정구 페이지는 4개 구 생활권, 대표 행정동 페이지는 지역 검색,
      역세권 페이지는 실제 검색 수요가 있는 역 키워드를 담당합니다. 자세한 절차는
      <a href="/reservation/">예약 안내</a>와 <a href="/hometai-guide/">홈타이 이용 가이드</a>를 참고하세요.</p>
    </section>"""

    breadcrumbs = [("홈", ""), ("수원 출장마사지", "")]
    # 메인은 breadcrumb 마지막이 자기 자신
    breadcrumbs = [("홈", ""), ("수원 출장마사지", slug)]
    content = render(slug, title, desc, h1, breadcrumbs, body, related=[])
    write(slug, content)


# ---------------------------------------------------------------------------
# 2) 행정구 페이지
# ---------------------------------------------------------------------------
def build_districts():
    for key, d in DISTRICTS.items():
        slug = d["slug"]
        # 관련: 해당 구의 대표 동 + 주요 역
        dongs_here = [dn for dn in DONGS if dn[0] == key]
        related = [(f"{dn[2]} 출장마사지", dong_slug(dn)) for dn in dongs_here]
        body = f"""    <section>
      <h2>{d['name']} 생활권 한눈에 보기</h2>
      <p>{d['intro']}</p>
      <p>주요 거점: {keyword_join(d['ctx'])}. {d['name']} 출장마사지와 홈타이는 거점별로 이동 동선과 예약 가능 시간이 다를 수 있어,
      방문 전 본인 위치와 가까운 대표 동·역세권 페이지를 함께 확인하는 것이 좋습니다.</p>
    </section>

    <section>
      <h2>{d['name']} 대표 행정동 안내</h2>
      <p>{d['name']}의 번호 행정동은 대표 동으로 통합해 안내합니다. 아래에서 가까운 지역을 선택하세요.</p>
    </section>

{trust_block(d['name'])}"""
        breadcrumbs = [("홈", ""), ("수원 출장마사지", MAIN_SLUG), (f"{d['name']} 출장마사지", slug)]
        content = render(slug, d["title"], d["desc"], d["h1"], breadcrumbs, body, related)
        write(slug, content)


# ---------------------------------------------------------------------------
# 3) 대표 행정동 페이지
# ---------------------------------------------------------------------------
def build_dongs():
    for dn in DONGS:
        district, sslug, name, title, desc_tail, ctx = dn
        slug = dong_slug(dn)
        desc = chk(f"{name} 출장마사지·홈타이 이용 전 {desc_tail} 확인하세요.")
        h1 = f"{name} 출장마사지 · 홈타이 안내"
        gu = DISTRICTS[district]
        # 관련: 같은 구 다른 동 일부 + 구 페이지
        siblings = [x for x in DONGS if x[0] == district and x[1] != sslug][:5]
        related = [(f"{gu['name']} 출장마사지", gu["slug"])]
        related += [(f"{x[2]} 출장마사지", dong_slug(x)) for x in siblings]
        body = f"""    <section>
      <h2>{name} 방문 가능 지역</h2>
      <p>{name} 출장마사지와 홈타이는 {gu['name']} 생활권에 속하며, 주요 거점은 {keyword_join(ctx)}입니다.
      {name}은(는) 인근 생활권과 이동 동선이 이어지므로, 방문 전 정확한 위치와 예약 가능 시간을 함께 확인하는 것이 좋습니다.</p>
      <p>홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다.
      {name} 일대는 거리와 시간대에 따라 추가 이동비가 달라질 수 있습니다.</p>
    </section>

{trust_block(name)}"""
        breadcrumbs = [
            ("홈", ""),
            ("수원 출장마사지", MAIN_SLUG),
            (f"{gu['name']} 출장마사지", gu["slug"]),
            (f"{name} 출장마사지", slug),
        ]
        content = render(slug, title, desc, h1, breadcrumbs, body, related)
        write(slug, content)


# ---------------------------------------------------------------------------
# 4) 역세권 페이지
# ---------------------------------------------------------------------------
def build_stations():
    for s in STATIONS:
        sslug, name, title, desc_tail, ctx, future = s
        slug = station_slug(s)
        desc = chk(f"{name} 출장마사지·홈타이 예약 전 {desc_tail} 확인하세요.")
        h1 = f"{name} 출장마사지 · 홈타이 안내"
        # 관련: 주변 역 일부
        others = [x for x in STATIONS if x[0] != sslug][:6]
        related = [(f"{x[1]} 출장마사지", station_slug(x)) for x in others]
        body = f"""    <section>
      <h2>{name} 주변 생활권</h2>
      <p>{name} 출장마사지와 홈타이를 찾을 때는 역 주변 생활권을 함께 확인하면 검색 의도가 분명해집니다.
      {name}의 주요 생활권은 {keyword_join(ctx)}입니다. {future}</p>
    </section>

{trust_block(name)}"""
        breadcrumbs = [
            ("홈", ""),
            ("수원 출장마사지", MAIN_SLUG),
            (f"{name} 출장마사지", slug),
        ]
        content = render(slug, title, desc, h1, breadcrumbs, body, related)
        write(slug, content)


# ---------------------------------------------------------------------------
# 5) 생활권 페이지
# ---------------------------------------------------------------------------
def build_areas():
    for a in AREAS:
        sslug, name, title, desc_tail, ctx = a
        slug = area_slug(a)
        desc = chk(f"{name} 출장마사지·홈타이 이용 전 {desc_tail} 확인하세요.")
        h1 = f"{name} 출장마사지 · 홈타이 안내"
        others = [x for x in AREAS if x[0] != sslug][:5]
        related = [(f"{x[1]} 출장마사지", area_slug(x)) for x in others]
        body = f"""    <section>
      <h2>{name} 생활권 안내</h2>
      <p>{name} 출장마사지와 홈타이는 {keyword_join(ctx)} 생활권을 중심으로 방문 수요가 생깁니다.
      생활권 페이지는 실제 검색 의도에 가깝게 거점을 묶어 안내하며, 같은 본문에서 지역명만 바꾸지 않고 거점별 특징을 설명합니다.</p>
    </section>

{trust_block(name)}"""
        breadcrumbs = [
            ("홈", ""),
            ("수원 출장마사지", MAIN_SLUG),
            (f"{name} 출장마사지", slug),
        ]
        content = render(slug, title, desc, h1, breadcrumbs, body, related)
        write(slug, content)


# ---------------------------------------------------------------------------
# 6) 기타 페이지
# ---------------------------------------------------------------------------
MISC_BODY = {
    "reservation": """    <section>
      <h2>예약 절차</h2>
      <ol class="steps">
        <li>방문 희망 지역(구·동·역세권)과 시간을 확인합니다.</li>
        <li>전화로 방문 가능 여부와 예약 가능 시간을 문의합니다.</li>
        <li>추가 이동비, 결제 방식, 서비스 범위를 안내받습니다.</li>
        <li>예약 확정 후 방문 시간을 조율합니다.</li>
      </ol>
    </section>
    <section>
      <h2>예약 시 확인할 항목</h2>
      <ul class="check">
        <li>방문 가능 지역과 예약 가능 시간</li>
        <li>거리별 추가 이동비 발생 여부</li>
        <li>결제 방식과 취소 기준</li>
      </ul>
    </section>""",
    "before-use": """    <section>
      <h2>이용 전 확인사항</h2>
      <ul class="check">
        <li>방문 가능 지역: 장안구·권선구·팔달구·영통구 생활권별로 이동 동선이 다릅니다.</li>
        <li>추가 이동비: 금곡동·호매실동·오목천동·파장동·연무동 일부는 기준이 달라질 수 있습니다.</li>
        <li>예약 가능 시간과 취소 기준을 사전에 확인하세요.</li>
        <li>과장·허위 후기나 선정적 표현이 포함된 안내는 신뢰하지 마세요.</li>
      </ul>
    </section>""",
    "hometai-guide": """    <section>
      <h2>홈타이 이용 가이드</h2>
      <p>수원 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다.
      예약 전 방문 지역과 시간을 확인하고, 준비 사항과 서비스 범위를 안내받는 것이 좋습니다.</p>
      <ul class="check">
        <li>방문 공간과 주차·출입 방법을 미리 확인합니다.</li>
        <li>예약 가능 시간과 소요 시간을 확인합니다.</li>
        <li>결제 방식과 취소 기준을 사전에 안내받습니다.</li>
      </ul>
    </section>""",
    "privacy": """    <section>
      <h2>개인정보 처리방침</h2>
      <p>본 사이트는 예약 문의 처리를 위해 필요한 최소한의 정보만 수집·이용합니다.</p>
      <ul class="check">
        <li>수집 항목: 예약 문의 시 제공하는 연락처 및 방문 지역 정보</li>
        <li>이용 목적: 예약 확인 및 방문 안내</li>
        <li>보관 기간: 목적 달성 후 지체 없이 파기</li>
        <li>제3자 제공: 법령에 근거가 없는 한 제공하지 않습니다.</li>
      </ul>
    </section>""",
    "support": f"""    <section>
      <h2>고객센터</h2>
      <p>예약 문의는 전화로 안내드립니다.</p>
      <p class="phone-big"><a href="tel:{PHONE_TEL}">{SITE_NAME} 전화예약 {PHONE}</a></p>
      <ul class="check">
        <li>상호: {SITE_NAME}</li>
        <li>전화예약: {PHONE}</li>
        <li>서비스 지역: 수원시 장안구·권선구·팔달구·영통구</li>
      </ul>
    </section>""",
}

def build_misc():
    for sslug, name, title, desc in MISC:
        slug = sslug
        h1 = name
        body = MISC_BODY[sslug]
        breadcrumbs = [("홈", ""), ("수원 출장마사지", MAIN_SLUG), (name, slug)]
        content = render(slug, title, chk(desc), h1, breadcrumbs, body, related=[])
        write(slug, content)


# ---------------------------------------------------------------------------
# 루트 index.html → 메인으로 연결 (canonical은 메인 슬러그)
# ---------------------------------------------------------------------------
def build_root_redirect():
    target = f"/{MAIN_SLUG}/"
    content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>수원 출장마사지｜수원시 홈타이 지역별 예약 안내</title>
<meta name="description" content="수원 출장마사지·홈타이 예약 전 4개 구, 역세권, 이용 기준을 정리했습니다.">
<link rel="canonical" href="{url_of(MAIN_SLUG)}">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<main class="wrap">
<p>수원 출장마사지 안내 페이지로 이동합니다. 이동되지 않으면 <a href="{target}">여기를 클릭</a>하세요.</p>
</main>
</body>
</html>
"""
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# sitemap.xml / robots.txt
# ---------------------------------------------------------------------------
def all_slugs():
    slugs = [MAIN_SLUG]
    slugs += [d["slug"] for d in DISTRICTS.values()]
    slugs += [dong_slug(d) for d in DONGS]
    slugs += [station_slug(s) for s in STATIONS]
    slugs += [area_slug(a) for a in AREAS]
    slugs += [m[0] for m in MISC]
    return slugs

def build_sitemap():
    urls = []
    for slug in all_slugs():
        priority = "1.0" if slug == MAIN_SLUG else "0.8"
        urls.append(f"""  <url>
    <loc>{url_of(slug)}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n' \
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' \
          + "\n".join(urls) + "\n</urlset>\n"
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)

def build_robots():
    txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(txt)


# ---------------------------------------------------------------------------
# 정적 자산 (CSS, OG 이미지, 파비콘)
# ---------------------------------------------------------------------------
CSS = """:root{--bg:#fff;--ink:#1d2330;--muted:#5b6473;--line:#e6e9ef;--brand:#0f6e5e;--brand-d:#0b5345;--accent:#f4f7f6}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",sans-serif;color:var(--ink);background:var(--bg);line-height:1.7;font-size:16px}
.wrap{max-width:880px;margin:0 auto;padding:0 18px}
a{color:var(--brand-d)}
.site-header{position:sticky;top:0;background:#fff;border-bottom:1px solid var(--line);z-index:10}
.site-header .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:12px;padding-bottom:12px}
.brand{font-weight:800;text-decoration:none;color:var(--ink);font-size:1.05rem}
.brand span{color:var(--brand);font-weight:700}
.cta-phone{background:var(--brand);color:#fff;text-decoration:none;padding:9px 14px;border-radius:999px;font-weight:700;font-size:.92rem;white-space:nowrap}
.breadcrumb{font-size:.85rem;color:var(--muted);margin:18px 0 6px}
.breadcrumb a{color:var(--muted);text-decoration:none}
.breadcrumb .sep{margin:0 4px;color:#b8c0cc}
h1{font-size:1.5rem;line-height:1.35;margin:.4em 0 .6em}
h2{font-size:1.18rem;margin:1.6em 0 .5em;padding-bottom:.3em;border-bottom:1px solid var(--line)}
h3{font-size:1.02rem;margin:1.2em 0 .4em;color:var(--brand-d)}
p{margin:.6em 0;color:#33404f}
ul,ol{padding-left:1.2em}
.check li,.steps li{margin:.35em 0}
.link-grid{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px;margin:.6em 0}
.link-grid li{margin:0}
.link-grid a{display:block;background:var(--accent);border:1px solid var(--line);border-radius:10px;padding:10px 12px;text-decoration:none;color:var(--ink);font-size:.92rem}
.link-grid a:hover{border-color:var(--brand);color:var(--brand-d)}
.related{margin-top:1.4em}
.cta-box{margin:2em 0 1em;background:var(--accent);border:1px solid var(--line);border-radius:14px;padding:18px}
.cta-box h2{border:0;margin-top:0}
.phone-big a{display:inline-block;background:var(--brand);color:#fff;text-decoration:none;font-weight:800;font-size:1.1rem;padding:12px 18px;border-radius:12px;margin-top:6px}
.site-footer{border-top:1px solid var(--line);margin-top:2.5em;padding:22px 0;background:#fafbfc}
.site-footer .biz{font-weight:700;color:var(--ink)}
.foot-nav{display:flex;flex-wrap:wrap;gap:10px 16px;margin:.6em 0}
.foot-nav a{color:var(--muted);text-decoration:none;font-size:.9rem}
.notice{color:var(--muted);font-size:.82rem;margin-top:.6em}
@media(max-width:520px){.cta-phone{font-size:.82rem;padding:8px 11px}.brand{font-size:.95rem}h1{font-size:1.3rem}}
"""

OG_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0f6e5e"/>
      <stop offset="1" stop-color="#0b5345"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#g)"/>
  <text x="600" y="250" font-family="Apple SD Gothic Neo, Malgun Gothic, sans-serif" font-size="92" font-weight="800" fill="#ffffff" text-anchor="middle">수원 출장마사지</text>
  <text x="600" y="345" font-family="Apple SD Gothic Neo, Malgun Gothic, sans-serif" font-size="52" fill="#cdeee6" text-anchor="middle">수원시 홈타이 지역별 예약 안내</text>
  <text x="600" y="470" font-family="Apple SD Gothic Neo, Malgun Gothic, sans-serif" font-size="46" font-weight="700" fill="#ffffff" text-anchor="middle">{SITE_NAME} · 전화예약 {PHONE}</text>
</svg>
"""

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0f6e5e"/><text x="32" y="44" font-size="34" font-weight="800" fill="#fff" text-anchor="middle" font-family="sans-serif">수</text></svg>
"""

def build_assets():
    adir = os.path.join(OUT, "assets")
    os.makedirs(adir, exist_ok=True)
    with open(os.path.join(adir, "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    with open(os.path.join(adir, "og-image.svg"), "w", encoding="utf-8") as f:
        f.write(OG_SVG)
    with open(os.path.join(adir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(FAVICON_SVG)


# ---------------------------------------------------------------------------
def main():
    build_assets()
    build_main()
    build_districts()
    build_dongs()
    build_stations()
    build_areas()
    build_misc()
    build_root_redirect()
    build_sitemap()
    build_robots()
    n = len(all_slugs())
    print(f"생성 완료: {n} 페이지 (메인1+구4+동{len(DONGS)}+역{len(STATIONS)}+생활권{len(AREAS)}+기타{len(MISC)})")

if __name__ == "__main__":
    main()
