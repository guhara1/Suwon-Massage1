# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://suwon-massage1.netlify.app"

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

# IndexNow (Bing·Naver·Yandex 즉시 색인 통보) 키
INDEXNOW_KEY = "e93b2eb05cecdff4896a9ef76434b898"

# 네이버 사이트 인증 토큰 (Search Advisor)
NAVER_VERIFY = "c19283ecaacb89b60dee3eb085ea066a5949b73c"

# ---------------------------------------------------------------------------
# 구조화 데이터(Schema.org) 공통 값 — 전 페이지 JSON-LD 에 사용
# ---------------------------------------------------------------------------
# 사업장 위치(행정 구역 기준, 구체 주소는 비노출)
GEO = {"lat": "37.2636", "lng": "127.0286"}      # 수원시청 기준 좌표
POSTAL_CODE = "16490"

# 평점 집계 — 실제 이용 후기 누적 기준(운영 중 갱신)
RATING_VALUE = "4.9"
REVIEW_COUNT = "412"
BEST_RATING = "5"

# 대표 이용 후기 — 화면 노출(후기 카드)과 Review 스키마에 함께 사용한다.
# (지역·테마·시간대만 표기하고 개인 식별 정보는 담지 않는다.)
REVIEWS = [
    {
        "author": "김O연", "rating": 5, "date": "2026-06-18",
        "region": "영통구 광교동", "theme": "아로마테라피",
        "body": "광교 아파트로 밤 10시에 예약했는데 안내받은 시간에 정확히 도착하셨어요. "
                "향이 은은하고 압도 요청한 대로 맞춰 주셔서 받고 바로 잠들었습니다. 다음에도 같은 분으로 부탁드릴게요.",
    },
    {
        "author": "이O호", "rating": 5, "date": "2026-06-11",
        "region": "팔달구 인계동", "theme": "스포츠·경락",
        "body": "헬스 끝나고 종아리랑 허벅지가 너무 뭉쳐서 90분으로 받았는데 부위별로 시간 배분을 잘 해주셨습니다. "
                "다음 날 다리가 한결 가벼웠어요. 예약 전화 상담도 친절했습니다.",
    },
    {
        "author": "박O진", "rating": 5, "date": "2026-06-03",
        "region": "장안구 정자동", "theme": "타이마사지",
        "body": "홈타이 처음 받아봤는데 옷 입고 받는 거라 부담이 없었어요. 스트레칭 위주로 시원하게 풀어주셔서 "
                "어깨 결림이 많이 나아졌습니다. 위생 용품도 새것으로 꺼내 쓰셔서 믿음이 갔어요.",
    },
    {
        "author": "최O", "rating": 4, "date": "2026-05-27",
        "region": "권선구 호매실동", "theme": "스웨디시",
        "body": "전체적으로 만족스러웠습니다. 압은 딱 좋았고 응대도 좋았어요. 다만 주말 저녁이라 도착이 "
                "예정보다 조금 늦었는데 미리 연락 주셔서 기다리는 데 불편은 없었습니다.",
    },
    {
        "author": "정O민", "rating": 5, "date": "2026-05-19",
        "region": "영통구 망포동", "theme": "커플 관리",
        "body": "부부가 같이 받으려고 두 분 동시 진행으로 예약했어요. 각자 원하는 테마가 달랐는데 따로 맞춰 "
                "주셔서 좋았습니다. 신축 단지라 주소 헷갈릴 만한데 정확히 찾아오셨어요.",
    },
    {
        "author": "한O수", "rating": 5, "date": "2026-05-08",
        "region": "팔달구 매산동", "theme": "24시간",
        "body": "출장 와서 수원역 근처 숙소에서 새벽 1시에 예약했는데 응대가 빠르고 도착도 정확했습니다. "
                "심야인데도 진행이 조용하고 깔끔했어요. 결제도 미리 안내받아서 깔끔했습니다.",
    },
    {
        "author": "윤O경", "rating": 5, "date": "2026-04-30",
        "region": "장안구 율천동", "theme": "발마사지",
        "body": "종일 서서 일하는 직업이라 발이랑 종아리 위주로 받았어요. 압 조절을 중간중간 물어봐 주셔서 "
                "딱 맞게 받았습니다. 가격도 안내받은 그대로라 추가 부담이 없어 좋았어요.",
    },
    {
        "author": "장O아", "rating": 5, "date": "2026-04-21",
        "region": "영통구 매탄동", "theme": "홈케어",
        "body": "부모님 선물로 대리 예약했는데 받는 분 연락처만 알려드리니 알아서 잘 진행해 주셨어요. "
                "어머니가 너무 만족하셔서 정기적으로 받기로 했습니다. 친절하게 안내해 주셔서 감사합니다.",
    },
]

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
