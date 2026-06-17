# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://suwon-massage1.pages.dev"

BRAND = "바로 GO"
BRAND_MARK = "수"                       # 브랜드 심볼(헤더 원형 마크)
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 지역 정체성 (build.py 헤더/푸터에서 사용)
REGION = "수원"                          # 키워드 접두 (수원 출장마사지)
REGION_FULL = "경기도 수원시"
TAGLINE = "수원시 전지역 방문 관리"
FOOTER_DESC = ("수원시 전지역 방문 출장마사지·홈타이 안내 사이트입니다. "
               "모든 서비스는 안내된 관리 범위와 위생·안전 기준 안에서만 제공됩니다.")
FOOTER_REGION = "경기도 수원시 전지역"

# 주요 허브 경로
MASSAGE_HUB = "/massage/"
AREA_HUB = "/suwon/"
STATIONS_HUB = "/suwon/stations/"

# 행정구 정의 (slug, 한글명)
GU = [
    ("jangan-gu", "장안구"),
    ("gwonseon-gu", "권선구"),
    ("paldal-gu", "팔달구"),
    ("yeongtong-gu", "영통구"),
]

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("수원 출장마사지", "/massage/", [
        ("출장마사지 안내", "/massage/#service"),
        ("홈타이 안내", "/massage/#hometai"),
        ("전지역 방문 안내", "/massage/#coverage"),
        ("지하철역 인근 안내", "/massage/#stations"),
        ("예약 가능 시간", "/massage/#hours"),
        ("코스 선택 안내", "/massage/#course"),
        ("이용 전 확인사항", "/massage/#check"),
        ("위생·안전 안내", "/massage/#safety"),
        ("자주 묻는 질문", "/massage/#faq"),
    ]),
    ("지역별 안내", "/suwon/", [
        ("수원시 전체", "/suwon/"),
        ("장안구", "/suwon/jangan-gu/"),
        ("권선구", "/suwon/gwonseon-gu/"),
        ("팔달구", "/suwon/paldal-gu/"),
        ("영통구", "/suwon/yeongtong-gu/"),
    ]),
    ("지하철역별 안내", "/suwon/stations/", [
        ("역 전체", "/suwon/stations/"),
        ("수원역", "/suwon/stations/suwon-station/"),
        ("화서역", "/suwon/stations/hwaseo-station/"),
        ("성균관대역", "/suwon/stations/sungkyunkwan-univ-station/"),
        ("세류역", "/suwon/stations/seryu-station/"),
        ("매교역", "/suwon/stations/maegyo-station/"),
        ("수원시청역", "/suwon/stations/suwon-cityhall-station/"),
        ("매탄권선역", "/suwon/stations/maetangwonseon-station/"),
        ("망포역", "/suwon/stations/mangpo-station/"),
        ("영통역", "/suwon/stations/yeongtong-station/"),
        ("청명역", "/suwon/stations/cheongmyeong-station/"),
        ("광교중앙역", "/suwon/stations/gwanggyo-jungang-station/"),
        ("광교역", "/suwon/stations/gwanggyo-station/"),
        ("고색역", "/suwon/stations/gosaek-station/"),
        ("오목천역", "/suwon/stations/omokcheon-station/"),
    ]),
    ("테마별 안내", "/themes/", [
        ("전체 테마", "/themes/"),
        ("스웨디시", "/themes/swedish/"),
        ("로미로미", "/themes/lomilomi/"),
        ("타이마사지", "/themes/thai/"),
        ("중국마사지", "/themes/chinese/"),
        ("아로마테라피", "/themes/aroma/"),
        ("홈케어", "/themes/homecare/"),
        ("호텔식마사지", "/themes/hotel-style/"),
        ("발마사지", "/themes/foot/"),
        ("스포츠·경락", "/themes/sports/"),
        ("스킨케어", "/themes/skincare/"),
        ("왁싱", "/themes/waxing/"),
        ("커플 관리", "/themes/couple/"),
        ("24시간", "/themes/24hours/"),
        ("수면 가능", "/themes/overnight/"),
    ]),
    ("코스안내", "/courses/", [
        ("전체 코스", "/courses/"),
        ("피로 회복 관리", "/courses/#recovery"),
        ("아로마 관리", "/courses/#aroma"),
        ("스포츠 관리", "/courses/#sports"),
        ("홈타이 코스", "/courses/#hometai"),
        ("커플·가족 방문 관리", "/courses/#couple"),
        ("기업·단체 방문 관리", "/courses/#group"),
        ("가격 안내", "/courses/#price"),
        ("코스 선택 가이드", "/courses/#guide"),
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용가이드", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 전 준비사항", "/guide/#prepare"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("금지행위 안내", "/guide/#prohibited"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("매거진", "/magazine/", [
        ("전체 글", "/magazine/"),
        ("마사지 비교 가이드", "/magazine/swedish-vs-thai/"),
        ("처음 이용 가이드", "/magazine/first-time-guide/"),
        ("수면과 마사지", "/magazine/sleep-and-massage/"),
        ("운동 후 회복", "/magazine/post-workout-timing/"),
        ("어깨·목 결림 관리", "/magazine/neck-shoulder-care/"),
        ("부모님 선물 가이드", "/magazine/parents-gift/"),
    ]),
    ("후기", "/reviews/", [
        ("전체 후기", "/reviews/"),
        ("지역별 후기", "/reviews/#area"),
        ("역세권 후기", "/reviews/#station"),
        ("후기 작성 안내", "/reviews/#write"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
