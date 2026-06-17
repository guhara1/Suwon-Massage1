# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "경기도 수원시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 수원시"
  }},
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "₩90,000 - ₩180,000"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "수원시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 장안구, 권선구, 팔달구, 영통구와 대표 행정동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "수원역이나 광교중앙역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "매탄1동, 영통2동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "매탄1~4동은 매탄동, 영통1~3동은 영통동처럼 숫자 행정동은 대표 동 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "테마별 관리는 어디에서 확인하나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 수원시 전지역</p>
    <h1>수원 출장마사지·홈타이<br>예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>4개</strong><span>행정구</span></li>
      <li><strong>29개</strong><span>대표 동 안내</span></li>
      <li><strong>14개</strong><span>역세권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>수원 출장마사지·홈타이 서비스 안내</h2>
<p>수원시에서 방문 마사지와 홈타이 예약을 찾는 분들을 위해 가능 지역, 예약 절차, 코스 선택 기준, 이용 전 확인사항을 한곳에 정리했습니다. 이 페이지는 수원시 전체 구조를 설명하는 허브 역할을 하며, 더 자세한 내용은 행정구별·지하철역별·테마별 안내 페이지에서 확인하실 수 있습니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 처음 이용하시는 분도 어렵지 않게 예약할 수 있도록 각 단계를 명확하게 안내해 드립니다.</p>
</section>

<section id="hometai">
<h2>수원 홈타이 안내</h2>
<p>수원 홈타이는 자택, 오피스텔, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 같은 방문 관리라도 부드러운 이완이 필요한 날과 뭉친 근육을 풀어야 하는 날이 다르므로, 컨디션에 맞춰 코스와 테마를 고르시면 됩니다. 홈타이와 출장마사지는 같은 방문 관리 안에서 함께 안내되며, 구체적인 구성은 <a href="/courses/">코스안내</a>와 <a href="/themes/">테마별 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="coverage">
<h2>수원시 전지역 방문 가능 안내</h2>
<p>수원시 지역 안내는 장안구, 권선구, 팔달구, 영통구 네 개 행정구를 중심으로 구성되어 있습니다. 정자1동부터 정자3동, 매탄1동부터 매탄4동, 영통1동부터 영통3동처럼 숫자로 나뉜 행정동은 별도 페이지를 만들지 않고 각 대표 동 페이지에서 통합하여 안내합니다. 같은 생활권을 잘게 쪼개 비슷한 내용을 반복하는 것보다, 대표 동 단위로 묶어 생활권 특징과 방문 조건을 한 번에 설명하는 편이 이용자에게도 정확하기 때문입니다.</p>
</section>

<section id="areas">
<h2>행정구별 안내</h2>
<p>지역별 안내는 수원시 네 개 행정구 기준으로 구성됩니다. 각 구 페이지에서는 소속 대표 동, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간을 구마다 고유한 내용으로 설명합니다. 아래에서 거주하시거나 머무시는 구를 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/suwon/jangan-gu/">장안구</a></li>
<li><a href="/suwon/gwonseon-gu/">권선구</a></li>
<li><a href="/suwon/paldal-gu/">팔달구</a></li>
<li><a href="/suwon/yeongtong-gu/">영통구</a></li>
</ul>
<p>수원시 전체 구조가 궁금하시면 <a href="/suwon/">지역별 안내</a>에서 네 개 구와 대표 동을 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>지하철역 인근 안내</h2>
<p>지하철역별 안내는 수원시를 지나는 1호선, 수인분당선, 신분당선 주요 역세권을 기준으로 구성합니다. 각 역 페이지에서는 인근 생활권, 주변 대표 동, 예약 가능 시간, 방문 전 준비사항을 설명하며, 출구별 페이지나 역과 테마를 조합한 페이지는 만들지 않습니다. 수원역처럼 노선이 여러 개인 환승역도 페이지는 하나로 운영합니다.</p>
<ul class="card-grid">
<li><a href="/suwon/stations/suwon-station/">수원역</a></li>
<li><a href="/suwon/stations/hwaseo-station/">화서역</a></li>
<li><a href="/suwon/stations/sungkyunkwan-univ-station/">성균관대역</a></li>
<li><a href="/suwon/stations/seryu-station/">세류역</a></li>
<li><a href="/suwon/stations/maegyo-station/">매교역</a></li>
<li><a href="/suwon/stations/suwon-cityhall-station/">수원시청역</a></li>
<li><a href="/suwon/stations/maetangwonseon-station/">매탄권선역</a></li>
<li><a href="/suwon/stations/mangpo-station/">망포역</a></li>
<li><a href="/suwon/stations/yeongtong-station/">영통역</a></li>
<li><a href="/suwon/stations/cheongmyeong-station/">청명역</a></li>
<li><a href="/suwon/stations/gwanggyo-jungang-station/">광교중앙역</a></li>
<li><a href="/suwon/stations/gwanggyo-station/">광교역</a></li>
<li><a href="/suwon/stations/gosaek-station/">고색역</a></li>
<li><a href="/suwon/stations/omokcheon-station/">오목천역</a></li>
</ul>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>테마별 안내에서는 관리 유형별 특징, 추천 대상, 예약 전 확인사항을 설명합니다. 테마는 각각 독립 페이지로 운영하며, 지역 페이지와 역 페이지에서는 관련 테마로 연결만 해 드립니다. 특정 역과 테마를 조합한 페이지는 운영하지 않으니, 원하시는 관리 유형을 먼저 고른 뒤 예약 시 위치를 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/themes/swedish/">스웨디시</a></li>
<li><a href="/themes/lomilomi/">로미로미</a></li>
<li><a href="/themes/thai/">타이마사지</a></li>
<li><a href="/themes/chinese/">중국마사지</a></li>
<li><a href="/themes/aroma/">아로마테라피</a></li>
<li><a href="/themes/homecare/">홈케어</a></li>
<li><a href="/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/themes/foot/">발마사지</a></li>
<li><a href="/themes/sports/">스포츠·경락</a></li>
<li><a href="/themes/skincare/">스킨케어</a></li>
<li><a href="/themes/waxing/">왁싱</a></li>
<li><a href="/themes/couple/">커플 관리</a></li>
<li><a href="/themes/24hours/">24시간</a></li>
<li><a href="/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="course">
<h2>코스 선택 안내</h2>
<p>코스는 이용 목적과 그날의 컨디션에 따라 선택하시는 것이 좋습니다. 누적된 피로를 풀고 싶은 분, 편안한 휴식이 필요한 분, 운동 후 근육 이완이 필요한 분, 숙소로 방문을 원하시는 분, 커플이 함께 받고 싶은 분 등 상황에 맞는 선택 기준을 <a href="/courses/">코스안내</a> 페이지에서 자세히 다룹니다. 고민되시면 예약 전화에서 상태를 말씀해 주세요. 함께 정해 드립니다.</p>
</section>

<section id="how">
<h2>예약 진행 방식</h2>
<p>예약은 다섯 단계로 진행됩니다. 먼저 희망 지역 또는 역 인근 위치를 확인하고, 희망 시간을 확인한 뒤, 코스와 인원을 정하고, 방문 가능 여부를 안내받은 다음, 예약을 확정합니다. 저녁 시간대나 주말에는 문의가 몰릴 수 있으므로 한두 시간 이상 여유를 두고 예약하시기를 권장합니다. 자세한 절차는 <a href="/reservation/">예약안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="check">
<h2>이용 전 확인사항</h2>
<p>원활한 방문 관리를 위해 정확한 주소, 공동현관 출입 방법, 주차 가능 여부, 조용한 공간 확보 여부를 미리 확인해 주시면 좋습니다. 광교·영통·망포 생활권과 호매실·고색·오목천 생활권, 장안구 북수원 생활권은 이동 동선이 다르고, 금곡동·호매실동·오목천동·파장동·연무동 일부는 차량 이동 기준과 추가 이동비가 달라질 수 있습니다. 준비사항 전체는 <a href="/guide/">이용가이드</a>에 정리되어 있습니다.</p>
</section>

<section id="safety">
<h2>위생 및 안전 안내</h2>
<p>건전하고 안전한 방문 관리를 위해 위생 기준, 예약 정보 확인, 개인정보 보호, 금지행위 안내를 명확히 제공합니다. 이용 전 서비스 범위와 유의사항을 확인해 주시고, 불법적이거나 무리한 요청은 어떤 경우에도 진행하지 않는다는 기준을 분명히 안내드립니다. 예약 정보는 관리 목적 외에 사용하지 않습니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>수원시 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 장안구, 권선구, 팔달구, 영통구와 대표 행정동 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>수원역이나 광교중앙역 근처도 가능한가요?</h3>
<p>주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>매탄1동, 영통2동은 왜 따로 없나요?</h3>
<p>매탄1~4동은 매탄동, 영통1~3동은 영통동처럼 숫자 행정동은 대표 동 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다.</p>
</div>
<div class="faq-item">
<h3>테마별 관리는 어디에서 확인하나요?</h3>
<p>스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>수원시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "수원 출장마사지·홈타이 | 수원시 전지역 방문 마사지 예약 안내",
    "desc": "수원 출장마사지·홈타이 안내 페이지입니다. 장안구, 권선구, 팔달구, 영통구와 수원역·광교중앙역 등 주요 역세권, 테마별 관리, 예약 전 확인사항을 확인해보세요.",
    "h1": "수원 출장마사지·홈타이 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
