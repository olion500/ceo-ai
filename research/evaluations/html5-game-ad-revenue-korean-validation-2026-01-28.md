---
title: "한국 문화 HTML5 게임 + 광고 수익 - Idea Validation"
date: 2026-01-28
type: Idea Validation
mode: Comprehensive
composite-score: 4.9
verdict: PIVOT
confidence: High
market-opportunity: 5.1
execution-feasibility: 8.4
strategic-position: 3.6
risk-profile: 4.3
intellectual-honesty: 2.8
investment-worthiness: 6.1
tags: [validation, html5-game, ad-revenue, korean-culture, quiz-game]
---

# Idea Validation: 한국 문화 HTML5 게임 + 광고 수익

## Executive Summary

**One-line pitch:** 초성 퀴즈, 한국사 퀴즈 등 한국 문화 기반 무료 HTML5 웹 게임을 만들어 AdSense 광고로 수익화.
**Composite Score:** 4.9/10 (Raw: 5.4 → Override 적용)
**Verdict:** PIVOT
**Confidence:** High

실행 용이성(8.4)과 확장성(8/10)은 우수하지만, 지적 정직성(2.8), 전략적 포지션(3.6), 리스크 프로파일(4.3) 모두 심각한 수준이다. 핵심 문제는 세 가지: (1) 한국 웹게임 AdSense RPM이 예상(₩5,000)보다 훨씬 낮을 가능성(₩1,000-2,000), (2) 마케팅 비용 ₩0으로 월 500,000 플레이 달성이라는 비현실적 성장 가정, (3) 진입장벽 제로로 방어 불가능한 제품. 광고 수익 모델이 아닌 교육/B2B 피벗 또는 UGC 플랫폼화를 권장한다.

---

## Scoring Matrix

| # | Framework | Score | Weight | Weighted | Status |
|---|-----------|-------|--------|----------|--------|
| 1 | Market Opportunity | 5.1/10 | 20% | 1.02 | Weak |
| 2 | Execution Feasibility | 8.4/10 | 20% | 1.68 | Strong |
| 3 | Strategic Position | 3.6/10 | 15% | 0.54 | Critical |
| 4 | Risk Profile | 4.3/10 | 15% | 0.65 | Weak |
| 5 | Intellectual Honesty | 2.8/10 | 10% | 0.28 | Critical |
| 6 | Investment Worthiness | 6.1/10 | 20% | 1.22 | OK |
| | **RAW COMPOSITE** | | **100%** | **5.4** | |
| | **FINAL (Override)** | | | **4.9** | **PIVOT** |

**Override 적용:**
- Intellectual Honesty 2.8 < 3.0 → Composite cap 5.9
- 2개 프레임워크 < 4.0 (Strategic 3.6, Honesty 2.8) → Composite cap **4.9**
- 최종 적용: 가장 엄격한 cap **4.9**

---

## Framework 1: Startup Validator — Market Opportunity (5.1/10)

### Sub-Scores

| Dimension | Score |
|-----------|-------|
| Demand Signal | 6/10 |
| Market Size | 6/10 |
| Pricing Power | 3/10 |
| Timing | 5/10 |

### Key Findings

- **수요 존재하나 특정 제품 수요 미검증**: "무료 게임" 월 50,000+ 검색은 있으나, "초성 퀴즈"나 "한국사 퀴즈 게임" 자체의 검색량은 미확인. 캐주얼 게임 다운로드 1.77억 건(2024)으로 전반적 수요는 있으나 웹 퀴즈 게임에 대한 유료/광고 수요는 별도 검증 필요.
- **한국 RPM 구조적 한계**: 한국 평균 CPC $0.25 (미국 $0.61의 41%), 게임/엔터테인먼트 분야 CPC $0.20 미만. 예상 RPM ₩5,000은 낙관적이며 현실적으로 ₩1,500-3,500 수준.
- **Online Solitaire 참고 사례의 한계**: $10K/월은 영어권 글로벌 트래픽 + Freestar 전문 광고 네트워크 활용 결과. 한국어 전용 + AdSense만으로는 동일 결과 재현 불가.
- **초성퀴즈 온라인 실패 사례**: 1인 개발자가 만든 초성퀴즈 온라인이 유저 부족으로 2020년 서비스 종료.

### Evidence

- 한국 캐주얼 게임 2024년 1.77억 다운로드, 향후 5년간 38% 증가 전망 ([센서타워](https://sensortower.com/ko/blog/state-of-gaming-in-korea-2025-report-KR))
- 한국 CPC 평균 $0.25, 게임 카테고리 $0.20 미만 ([heendoll](https://heendoll.com/blog/adsense-cpc-by-country/))
- 2025년 AdSense RPM 하락 추세: $2.80-6.50 수준 ([WebmasterWorld](https://www.webmasterworld.com/google_adsense/5123987.htm))
- Online Solitaire: Freestar 전문 네트워크 전환 후 수익 2000%+ 증가 ([Freestar](https://freestar.com/case-studies/online-solitaire/))

---

## Framework 2: Execution Auditor — Feasibility (8.4/10)

### Sub-Scores

| Dimension | Score |
|-----------|-------|
| Skills Match | 9/10 |
| Cost & Runway | 10/10 |
| Timeline Realism | 8/10 |
| Technical Complexity | 8/10 |
| Dependency Risk | 6/10 |

### Key Findings

- **거의 완벽한 스킬 매치**: JS/HTML5 개발 스킬 보유, Phaser.js 학습 0.5-1주. 부족한 것은 AdSense 연동과 카카오톡 SDK 정도 (각각 수일 학습).
- **제로 비용**: Vercel/Netlify 무료 호스팅, 도메인 선택사항. 금전적 리스크 완전 제로.
- **2-3주 MVP 현실적**: 사용자 추정 1주는 낙관적이나, 2x 보정 적용해도 2-3주면 충분. AdSense 승인 대기(1-14일)가 변수.
- **AdSense 승인이 핵심 의존성**: 수익 모델 전체가 AdSense에 의존. 대안으로 카카오 애드핏, 텐핑 존재.

### Cost Projection

- Initial: ₩0-15,000 | Monthly: ₩0/mo
- Break-even: 즉시 (비용 없음)

### Timeline Estimate

- MVP: 2-3주 | First Revenue: 1-2개월 (AdSense 승인 + 트래픽 확보)

---

## Framework 3: Strategic Advisor — Position (3.6/10)

### Sub-Scores

| Dimension | Score |
|-----------|-------|
| Competitive Moat | 2/10 |
| Differentiation | 5/10 |
| Mental Model Fit | 4/10 |
| Long-term Position | 3.5/10 |

### Strategic Positioning

- Primary moat: **None** (Brand이 유일한 가능성이나 캐주얼 게임 브랜드 충성도 매우 낮음)
- Differentiation: **Niche-first** (한국 문화 특화 — 명확하나 쉽게 복제 가능)
- Strategic pattern: **Red Ocean** (초성 퀴즈, 한국사 퀴즈 사이트/앱 이미 다수 존재)

### Key Insights

- **Network effect, data moat, switching cost 모두 부재**: 싱글플레이어 퀴즈는 유저가 많아도 게임 품질 향상 없음. 계정 불필요, 설치 불필요로 전환비용 제로.
- **"한국 문화 특화"는 로컬라이제이션이지 차별화가 아님**: 기존 초성 퀴즈/한국사 퀴즈 제품과 근본적 경험 차이 없음.
- **피벗 권장**: UGC 플랫폼화(유저가 퀴즈 제작/공유) 또는 B2B(교육기관 라이선싱)로 방어 가능한 해자 추가 필요.
- **3년 전망**: 해자 없이는 트래픽이 점진적 하락, 신규 게임 출시마다 일시적 반등 패턴 반복 후 정체.

---

## Framework 4: Risk Analyst — Risk Profile (4.3/10)

### Sub-Scores

| Dimension | Score |
|-----------|-------|
| Failure Scenarios | 3/10 |
| Dependencies | 5/10 |
| External Threats | 5/10 |
| Blind Spots | 4/10 |

### Top Kill Risks

1. **[CRITICAL] 트래픽-수익 데스밸리**: 월 100,000 플레이 달성까지 6-12개월 소요, 그 기간 수익 월 ₩5-15만. 실제 RPM이 ₩1,000-2,000이면 목표 트래픽 달성 후에도 월 ₩10-20만에 불과. → Mitigation: MVP 1주 출시 후 실제 RPM 조기 확보. ₩2,000 미만이면 수익 모델 피벗.
2. **[HIGH] 콘텐츠 트레드밀 번아웃**: 퀴즈 게임은 끊임없이 새 문제 요구. 1인 개발자가 개발+콘텐츠+마케팅+유지보수 모두 감당하면 3-6개월 내 번아웃. → Mitigation: AI(GPT) 문제 자동 생성 + 수동 검증. UGC 시스템 도입.
3. **[MODERATE] 플랫폼 의존성**: AdSense 계정 정지, 카카오 API 제한, Google SEO 알고리즘 변경 중 하나만 발생해도 수익 50-100% 급감. → Mitigation: 카카오 애드핏 보조 운영, 이메일/푸시로 직접 트래픽 채널 확보.

### Fatal Risk Present?

**No (단, 조건부)** — 단독 fatal risk는 없으나, 트래픽-수익 데스밸리가 준치명적. 반드시 부업으로 시작해야 하며, 2주 내 실제 RPM 데이터 확보 필수.

---

## Framework 5: Devil's Advocate — Honesty (2.8/10)

### Sub-Scores

| Dimension | Score |
|-----------|-------|
| Assumption Audit | 2/10 |
| Bias Detection | 3/10 |
| Counter-Arguments | 3/10 |

### Unvalidated Assumptions

1. **RPM ₩5,000**: 한국 캐주얼 웹 퀴즈 게임의 실제 RPM 데이터 없음. 짧은 세션(1-3분)으로 광고 노출 제한. 실제 ₩500-1,500일 수 있어 수익이 3-10배 하향.
2. **"무료 게임" 검색 = 초성 퀴즈 수요**: 키워드 불일치. "무료 게임" 검색자가 원하는 것은 액션/RPG/카드게임이지 퀴즈가 아님.
3. **Year 1에 500,000 플레이/월**: 마케팅 비용 ₩0으로 50배 성장 근거 전무.
4. **1주일 제작, 개발비 ₩0**: 게임 디자인, UX, 사운드, QA, 광고 SDK 통합 등 무시. 실제 1-3개월.
5. **카카오톡 바이럴**: 공유 버튼 ≠ 바이럴. K-factor > 1.0 달성 제품은 극히 드묾.
6. **Online Solitaire 비교**: 영어권 글로벌 시장, 보편적 인지 게임, 세션 15-30분 vs 한국어 니치, 세션 1-3분 — 비교 부적절.

### Biases Detected

- **Survivorship bias**: Online Solitaire 단일 성공 사례 일반화. 동일 모델 실패 수천 건 무시.
- **Confirmation bias**: "무료 게임" 검색량만 인용, 초성 퀴즈 실제 검색량 미확인.
- **Dunning-Kruger**: 게임 개발 = 코드 작성이라는 과소평가. 실제 게임 개발에서 코드는 30-40%.
- **Anchoring**: RPM ₩5,000 단일 수치 고정, 범위 분석(best/base/worst) 부재.
- **Optimism bias**: 모든 변수(트래픽, RPM, 성장률, 개발 기간)가 최선 시나리오.

### Kill Criteria

- [ ] 출시 후 3개월간 월간 플레이 수 1,000회 미만
- [ ] 실측 RPM ₩1,500 미만
- [ ] 카카오톡 공유율 전체 유저의 2% 미만
- [ ] 개발 기간 1개월 초과
- [ ] "초성 퀴즈 게임", "한국사 퀴즈 게임" 키워드 합산 월 검색량 5,000 미만

---

## Framework 6: Investor Lens — Investment (6.1/10)

### Sub-Scores

| Dimension | Score |
|-----------|-------|
| Unit Economics | 7/10 |
| ROI Potential | 7/10 |
| Scalability | 8/10 |
| Revenue Quality | 3/10 |

### Key Numbers

- LTV:CAC: 현금 기준 ∞:1 / 시간 포함 ~1:1
- Target MRR (12mo): ₩2,000,000-7,500,000 (≈$1,500-5,500)
- Gross margin: 95%+
- Payback period: 즉시 (제로 자본)
- 유저당 LTV: ~₩500 (광고 + IAP 포함)

### Key Insight

비대칭적 리스크-리워드(현금 리스크 제로, upside 열림)는 매력적이나, Revenue Quality(3/10)가 치명적. 광고 RPM은 Google이 결정하고, 트래픽은 SEO 알고리즘에 의존. "부업 사이드프로젝트"로는 적합하나 "본업 비즈니스"로는 수익 예측 불가능.

---

## Synthesis

### Cross-Framework Consensus

**Strengths confirmed by multiple frameworks:**
- **실행 용이성 극대화** — Execution Auditor(8.4) + Investor Lens(Scalability 8/10). 제로 비용, 2-3주 MVP, 95%+ 마진, 개발 스킬 완벽 매치.
- **비대칭적 리스크-리워드** — Investor Lens(ROI 7/10) + Execution Auditor(Cost 10/10). 현금 리스크 제로, 실패해도 금전적 손실 없음.

**Weaknesses confirmed by multiple frameworks:**
- **RPM/수익 예측 비현실적** — Market Opportunity(Pricing 3/10) + Devil's Advocate(Assumptions 2/10) + Risk Analyst(Failure 3/10). ₩5,000 RPM은 낙관적, 실제 ₩1,000-2,000 가능. 수익 예측 3-10배 과대.
- **방어 불가능한 제품** — Strategic Advisor(Moat 2/10) + Devil's Advocate(Counter-Arguments 3/10). 진입장벽 제로, 복제 쉬움, network effect 없음, switching cost 제로.
- **트래픽 확보 난이도 과소평가** — Devil's Advocate(전체 2.8/10) + Risk Analyst(Blind Spots 4/10). 마케팅 ₩0으로 50배 성장은 비현실적. SEO 6-12개월, 바이럴은 "전략"이 아닌 "희망".

### Framework Conflicts

| Point | Execution Says | Market/Strategy Says | Resolution |
|-------|---------------|---------------------|-----------|
| 전체 가치 | 8.4 — 쉽게 만들 수 있다 | 2.8-5.1 — 만들어도 성과 불확실 | **"만들 수 있는가"와 "돈이 되는가"는 별개.** 제로 비용이라 시도 자체는 무해하나, 시간 투자 대비 수익이 매우 낮을 가능성. |
| Online Solitaire 참고 | Investor: 모델 검증됨 | Devil's Advocate: 비교 부적절 | **Solitaire는 영어권/글로벌/긴세션/전문광고네트워크.** 한국어/니치/짧은세션/AdSense와는 완전히 다른 조건. |

### Emergent Insights

- **퀴즈 세션 길이 = 수익 구조적 한계**: Solitaire 세션 15-30분 vs 퀴즈 1-3분. 동일 트래픽 대비 광고 노출 기회 3-6배 차이. 이는 RPM에 직접 영향.
- **"쉽게 만들 수 있다 = 누구나 만들 수 있다" 역설**: 이전 아이디어(프롬프트 판매)와 동일 패턴. Execution 높을수록 경쟁자 진입도 쉬움.
- **한국 문화 퀴즈의 진짜 가치는 "교육"에 있다**: 광고 수익 모델보다 교육 기관/기업 대상 B2B 라이선싱이나 학습 플랫폼 통합이 더 높은 가치 창출 가능.

---

## Decision

### Verdict: PIVOT

**Score:** 4.9/10 (Raw 5.4, Override 적용) | **Confidence:** High

### Rationale

이 아이디어는 실행 가능성(8.4)에서 높은 점수를 받았으나, 2개 프레임워크가 4.0 미만(Strategic 3.6, Honesty 2.8)이어서 composite가 4.9로 cap되었다.

핵심 문제는 **광고 수익 모델의 구조적 한계**이다. 한국 웹게임 CPC $0.20 미만, 퀴즈 세션 1-3분(Solitaire 대비 1/5-1/10), AdSense RPM 하락 추세가 겹치면서, 예상 수익 ₩7,500,000/월(Year 1)은 극도로 비현실적이다. 현실적 Year 1 수익은 ₩100,000-300,000/월 수준이며, 이는 투입 시간 대비 최저시급 이하.

그러나 "한국 문화 퀴즈"라는 콘텐츠 자체의 가치는 인정된다. 광고 수익이 아닌 다른 수익 모델로 피벗하면 동일 역량으로 더 방어 가능한 비즈니스 구축이 가능하다.

### Strengths to Leverage

1. **제로 비용 + 빠른 MVP**: ₩0으로 2-3주 내 시장 테스트 가능
2. **한국 문화 콘텐츠 고유성**: 초성, 한국사, 지명은 한국어 전용 콘텐츠로 글로벌 경쟁 무관
3. **교육적 가치**: "재미 + 학습" 포지셔닝으로 학부모/교사/학생 타겟 확장 가능

### Issues to Address

1. **수익 모델 재설계**: AdSense 광고 → 교육/B2B/프리미엄 구독으로 전환
2. **방어 가능성 추가**: UGC(유저 퀴즈 제작), 커뮤니티, 랭킹 시스템으로 switching cost 생성
3. **수익 예측 현실화**: RPM ₩1,500-2,000 기준으로 재산출, ₩0 마케팅 가정 폐기

---

## Action Plan

### PIVOT Options

**Pivot 1: 교육용 퀴즈 플랫폼 (Revenue Model + Customer Pivot) — 권장**

한국 문화 퀴즈를 교육 도구로 리포지셔닝. B2C + B2B 이중 수익 구조.

- B2C: 학생 대상 프리미엄 구독 (₩2,900/월 — 광고 제거 + 전체 퀴즈 + 학습 통계)
- B2B: 교육 기관/학원 라이선스 (₩50,000-200,000/월)
- 채널: 클래스101, 학부모 커뮤니티, 교사 커뮤니티
- 방어 가능성: 교육 과정 통합, 학습 데이터 축적, 기관 계약

**Pivot 2: UGC 퀴즈 플랫폼 (Solution Pivot)**

유저가 직접 퀴즈를 만들고 공유하는 플랫폼. Kahoot! 한국 문화 버전.

- 수익: 프리미엄 기능 (커스텀 퀴즈, 그룹 대결, 통계) ₩4,900/월
- 방어 가능성: UGC 콘텐츠 축적 = 네트워크 효과, 콘텐츠 해자
- 리스크: 1인 개발자로서 플랫폼 구축은 기술적 부담 큼

**Pivot 3: 바이럴 웹 게임 + 스폰서 광고 (Channel Pivot)**

AdSense 대신 교육 업체(메가스터디, EBS 등) 직접 스폰서 광고 영업.

- 수익: 스폰서 배너 ₩500,000-2,000,000/월 (트래픽 10만+ 달성 시)
- 방어 가능성: 직접 광고주 관계 = AdSense 의존도 제거
- 리스크: 영업 역량 필요, 트래픽 선확보 필수

### Validation Sprint (Before Pivot, 2주)

- [ ] **Test 1**: 네이버 키워드 도구로 "초성 퀴즈", "한국사 퀴즈 게임" 실제 검색량 확인
- [ ] **Test 2**: 기존 한국 퀴즈 앱(Google Play)의 다운로드 수, 리뷰 수, 수익 추정 조사
- [ ] **Test 3**: MVP 1개(초성 퀴즈) 빠르게 제작 후 실제 AdSense RPM 측정 (2주)
- [ ] **Test 4**: 클래스101/학부모 커뮤니티에서 "교육용 퀴즈 게임" 수요 확인

---

## Kill Criteria

If ANY of these prove true, re-evaluate immediately:

- [ ] 실측 AdSense RPM ₩1,500 미만 (광고 수익 모델 성립 불가)
- [ ] "초성 퀴즈" + "한국사 퀴즈 게임" 합산 네이버 검색량 월 5,000 미만
- [ ] 출시 후 3개월간 월간 플레이 수 1,000회 미만
- [ ] 카카오톡 공유율 전체 유저의 2% 미만 (바이럴 전략 실패)
- [ ] 개발 기간 1개월 초과 (기회비용 재평가 필요)

---

*Validated by idea-validator skill (Comprehensive mode, 6 frameworks)*
*Date: 2026-01-28*
