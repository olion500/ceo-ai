---
title: "프라이버시 중심 Chrome Extension (로컬 저장) - Idea Validation"
date: 2026-01-29
type: Idea Validation
mode: Comprehensive
composite-score: 4.9
verdict: PIVOT
confidence: High
market-opportunity: 4.6
execution-feasibility: 7.6
strategic-position: 3.9
risk-profile: 3.8
intellectual-honesty: 3.4
investment-worthiness: 6.3
tags: [validation, privacy-chrome-extension, chrome-extension, privacy, one-time-purchase]
---

# Idea Validation: 프라이버시 중심 Chrome Extension (로컬 저장)

## Executive Summary

**One-line pitch:** YouTube/Instagram/Naver 시청·활동 기록을 100% 로컬에 저장하는 Chrome Extension으로, 서버 전송 없이 프라이버시를 보장한다.
**Composite Score:** 4.9/10
**Verdict:** PIVOT
**Confidence:** High

실행 가능성(7.6)과 투자 효율성(6.3)은 양호하지만, 시장 기회(4.6), 전략적 포지션(3.9), 리스크 프로파일(3.8), 지적 정직성(3.4) 등 4개 프레임워크에서 심각한 약점이 확인되었다. 핵심 문제는 (1) 무료 대안이 이미 다수 존재하여 유료 전환이 어렵고, (2) "추적 차단" USP가 Manifest V3 기술적 제약으로 구현이 제한되며, (3) Chrome Web Store라는 단일 배포 채널에 대한 절대적 의존성이다. 3개 프레임워크가 4.0 미만이므로 Composite는 4.9로 Cap되었고, 현재 형태로는 PIVOT이 필요하다.

---

## Scoring Matrix

| # | Framework | Score | Weight | Weighted | Status |
|---|-----------|-------|--------|----------|--------|
| 1 | Market Opportunity | 4.6/10 | 20% | 0.91 | Weak |
| 2 | Execution Feasibility | 7.6/10 | 20% | 1.52 | Strong |
| 3 | Strategic Position | 3.9/10 | 15% | 0.59 | Critical |
| 4 | Risk Profile | 3.8/10 | 15% | 0.57 | Critical |
| 5 | Intellectual Honesty | 3.4/10 | 10% | 0.34 | Critical |
| 6 | Investment Worthiness | 6.3/10 | 20% | 1.25 | OK |
| | **COMPOSITE** | | **100%** | **5.18 → 4.9 (capped)** | **PIVOT** |

**Override 적용:** 3개 프레임워크 < 4.0 (Strategic 3.9, Risk 3.8, Honesty 3.4) → Composite capped at 4.9. Fatal risk (플랫폼 정책 위반) 식별 → capped at 5.4 (4.9가 더 낮으므로 4.9 적용).

---

## Framework 1: Startup Validator — Market Opportunity (4.6/10)

### Sub-Scores
| Dimension | Score |
|-----------|-------|
| Demand Signal | 4/10 |
| Market Size | 4/10 |
| Pricing Power | 3/10 |
| Timing | 8/10 |

### Key Findings
- **무료 대안 이미 존재:** "Local YouTube Video History Tracker"가 Chrome Web Store에서 무료로 제공 중이며, 동일한 기능(IndexedDB 로컬 저장, 추적 없음)을 제공한다. Instagram 아카이버도 무료 확장 프로그램 다수 존재.
- **유료 전환 장벽 극도로 높음:** Chrome Extension 사용자는 무료를 기본 기대하며, 유료 확장 프로그램 비율은 전체의 1-3%에 불과하다. 70%의 Chrome Extension이 100명 미만의 사용자를 보유.
- **타이밍은 우수:** 한국 PIPA 개정(2025), 카카오페이/알리페이 사건(83억원 과징금), SK텔레콤 데이터 유출, MyData 확대 등 프라이버시 인식이 역대 최고 수준.
- **Naver 특화가 유일한 차별점:** Naver 검색기록 로컬 백업을 제공하는 기존 확장 프로그램이 없으나, 수요 검증은 미완.

### Evidence
- [Local YouTube Video History Tracker](https://chromewebstore.google.com/detail/local-youtube-video-histo/pebiokefjgdbfnkolmblaaladkmpilba) — 무료, 동일 기능
- [Chrome Extension Statistics](https://www.debugbear.com/blog/counting-chrome-extensions) — 70% Extension < 100 users
- [한국 PIPA 개정](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2025/south-korea) — 프라이버시 규제 강화

---

## Framework 2: Execution Auditor — Feasibility (7.6/10)

### Sub-Scores
| Dimension | Score |
|-----------|-------|
| Skills Match | 8/10 |
| Cost & Runway | 9/10 |
| Timeline Realism | 7/10 |
| Technical Complexity | 7/10 |
| Dependency Risk | 5/10 |

### Key Findings
- **기술적으로 충분히 구현 가능:** Chrome Extension 개발 능력 보유, Manifest V3/LocalStorage/IndexedDB는 표준 패턴.
- **비용 거의 제로:** 서버 불필요, Chrome Web Store 등록비 $5만 필요. 95% 이상의 매출총이익률.
- **2주 MVP는 단일 플랫폼에 대해 현실적:** YouTube 단독 확장 프로그램은 1개월 내 가능하나, 3개 플랫폼 동시 개발은 3-4개월 필요.
- **Instagram DOM 파싱이 가장 큰 기술적 리스크:** Meta의 공격적 안티스크래핑 조치로 인해 안정적 DOM 파싱이 극히 어렵다.

### Cost Projection
- Initial: $5 | Monthly: $0-50/mo

### Timeline Estimate
- MVP (YouTube 단독): ~1개월 | First Revenue: 1.5-2개월

---

## Framework 3: Strategic Advisor — Position (3.9/10)

### Sub-Scores
| Dimension | Score |
|-----------|-------|
| Competitive Moat | 2/10 |
| Differentiation | 6/10 |
| Mental Model Fit | 4/10 |
| Long-term Position | 3.5/10 |

### Strategic Positioning
- Primary moat: **없음** (구조적으로 moat 구축 불가)
- Differentiation: **Niche-first** (한국 프라이버시 사용자) + **Radically Simpler** (서버 제거)
- Strategic pattern: Blue Ocean 시도이나 "바다"가 너무 작음

### Key Insights
- **"100% 로컬"이라는 설계 철학이 모든 moat 구축 메커니즘을 구조적으로 차단한다.** 네트워크 효과 없음, 데이터 moat 없음, 전환 비용 없음, 규모의 경제 없음.
- **오픈소스 + 유료는 자기모순적:** 코드가 공개되면 포크가 즉시 가능하며, 프라이버시 의식이 높은 사용자일수록 직접 빌드할 가능성이 높다.
- **차별화 메시지는 명확:** "당신의 데이터는 당신의 컴퓨터에만 있습니다"는 강력한 한 줄 메시지이나, 이것만으로는 유료 제품을 지탱할 수 없다.

---

## Framework 4: Risk Analyst — Risk Profile (3.8/10)

### Sub-Scores
| Dimension | Score |
|-----------|-------|
| Failure Scenarios | 3/10 |
| Dependencies | 3/10 |
| External Threats | 4/10 |
| Blind Spots | 6/10 |

### Top Kill Risks
1. **[FATAL] Chrome Web Store 정책/플랫폼 ToS 위반 삭제:** "추적 차단" 기능이 Google 정책과 직접 충돌. Instagram 아카이브는 Meta ToS 위반 가능성 매우 높음. Manifest V3에서 webRequestBlocking 제거로 핵심 기능 구현 자체가 제한됨.
   - Mitigation: "추적 차단" 대신 "로컬 백업/내보내기"로 리프레이밍. 공식 API 활용.
2. **[HIGH] 유료 전환 실패:** Chrome Web Store 유료 판매 중단(2020년), 무료 대안 다수, Google Takeout 존재, 프라이버시 사용자의 역설적 불신.
   - Mitigation: Freemium 모델 전환, 외부 결제(Gumroad) 활용.
3. **[MEDIUM] 3개 플랫폼 DOM 유지보수 지옥:** YouTube/Instagram/Naver 모두 정기적 프론트엔드 업데이트. 1인이 3개 플랫폼 동시 유지보수는 지속 불가.
   - Mitigation: YouTube 단일 플랫폼 집중, 공식 API 활용으로 DOM 의존성 최소화.

### Fatal Risk Present?
**Yes** — Manifest V3에서 webRequestBlocking 제거로 "Google 추적 차단" 구현이 근본적으로 제한되며, Chrome Web Store 정책과 직접 충돌하는 기능을 핵심 USP로 내세우고 있다. 유일한 배포 채널(Chrome Web Store)에서 삭제될 경우 사업 자체가 소멸한다.

---

## Framework 5: Devil's Advocate — Honesty (3.4/10)

### Sub-Scores
| Dimension | Score |
|-----------|-------|
| Assumption Audit | 3/10 |
| Bias Detection | 3/10 |
| Counter-Arguments | 4/10 |

### Unvalidated Assumptions
1. **"사용자가 로컬 히스토리 저장에 돈을 낼 것":** 어떤 사용자 인터뷰, 설문, 대기자 명단 데이터도 없음. 프라이버시 패러독스(말은 중요하다고 하지만 행동은 하지 않음)가 이 가정을 직접적으로 위협.
2. **"Show HN + Reddit r/privacy로 Month 1에 ₩990,000 달성":** r/privacy 사용자는 상업적 포스팅에 적대적. HN 프론트 페이지 확률 ~5%, 전환율 < 1%. 근거 없는 수치.
3. **"100% 로컬이 의미 있는 차별점":** 대부분의 Chrome Extension은 이미 로컬에서 실행됨. "서버 전송 제로"는 기능이 아니라 기본 아키텍처.
4. **"이 아이디어는 시도된 적 없다":** Chrome Web Store에 유사 무료 확장 프로그램 다수 존재.
5. **"One-time purchase 모델이 지속 가능하다":** 반복 매출 없이 매월 신규 고객 확보 필요. ₩9,900에서 지속 가능한 사업은 대량 판매 없이 불가.

### Biases Detected
- **확증 편향:** "프라이버시가 중요하므로 프라이버시 도구에 돈을 낸다"는 전제만 검토
- **낙관 편향:** Month 1 ₩990,000은 상위 5% Chrome Extension 수준 — 근거 없는 수치
- **생존자 편향:** Signal/Brave 성공만 보고 수천 개의 실패한 프라이버시 도구 무시
- **편승 효과:** "프라이버시" 트렌드에 편승했으나 구체적 사용 사례의 수요 분석 부재

### Kill Criteria
- [ ] Show HN + Reddit 등 5개 채널 홍보 후 2주 내 무료 베타 가입자 50명 미만
- [ ] 베타 사용자 중 "반드시 구매하겠다" 응답 10% 미만
- [ ] Chrome Web Store 출시 후 30일 내 유료 구매 10건 미만
- [ ] "프라이버시"나 "로컬"이라는 단어 없이 사용자 문제를 설명할 수 없는 경우
- [ ] 타겟 사용자 인터뷰에서 이미 무료 대안을 사용 중이며 전환 의사 없음 확인

---

## Framework 6: Investor Lens — Investment (6.3/10)

### Sub-Scores
| Dimension | Score |
|-----------|-------|
| Unit Economics | 7/10 |
| ROI Potential | 8/10 |
| Scalability | 7/10 |
| Revenue Quality | 2/10 |

### Key Numbers
- LTV:CAC: 3-5:1 (오가닉 중심 시나리오)
- Target Monthly Revenue (12mo): ~₩720,000/월 (base case)
- Gross margin: 95%
- Payback period: 즉시 (one-time purchase)
- Break-even: ~485건 판매 (시간 가치 포함 총 투자 $3,405 회수)
- 12개월 Base Case: ~$8,650

### Key Insight
단위 경제(95% 마진), ROI(141% base case), 확장성(서버 비용 제로)은 우수하나, **Revenue Quality가 2/10으로 치명적 약점.** One-time purchase는 반복 매출 없이 매월 제로에서 시작하며, 단일 채널(Chrome Web Store) 의존으로 수익 예측 불가. 구독 모델 전환 없이는 "사이드 프로젝트 수준 용돈"에 머물 가능성 높다.

---

## Synthesis

### Cross-Framework Consensus

**강점 (다수 프레임워크 확인):**
- **실행 비용이 극히 낮다** — Execution(9/10 Cost), Investor(95% 마진, $5 초기 투자)
- **기술적으로 구현 가능하다** — Execution(8/10 Skills), Investor(8/10 ROI)
- **프라이버시 타이밍이 우수하다** — Market(8/10 Timing), Strategic(Niche-first differentiation)

**약점 (다수 프레임워크 확인):**
- **유료 전환이 극히 어렵다** — Market(3/10 Pricing Power), Honesty(unvalidated assumption), Investor(2/10 Revenue Quality), Risk(유료 전환 실패 kill risk)
- **방어 가능한 경쟁 우위가 없다** — Strategic(2/10 Moat), Honesty(포크 가능), Risk(무료 오픈소스 경쟁)
- **플랫폼 의존 리스크가 치명적이다** — Risk(FATAL, Chrome Web Store 삭제), Strategic(Google 위에서 anti-Google 제품), Execution(5/10 Dependency)

### Framework Conflicts
- **Execution vs Market:** 실행은 쉽지만(7.6) 시장이 원하지 않는다(4.6). "만들 수 있다"와 "팔 수 있다"는 별개 문제.
- **Investor (ROI) vs Investor (Revenue Quality):** ROI 자체는 8/10이지만 Revenue Quality는 2/10. 적은 투자로 높은 수익률이 가능하나, 수익의 질이 극히 낮아 지속 가능한 사업이 아닌 일회성 프로젝트에 가깝다.

### Emergent Insights
- **"프라이버시 도구의 역설"이 핵심 장벽:** 프라이버시를 중시하는 사용자일수록 (1) 알 수 없는 확장 프로그램 설치를 경계하고, (2) 오픈소스 코드를 직접 빌드하며, (3) Google 플랫폼(Chrome) 자체를 기피한다. 타겟 고객의 특성이 제품의 비즈니스 모델과 구조적으로 충돌한다.
- **"로컬 저장"은 기능이지 제품이 아니다:** 사용자는 아키텍처가 아니라 결과(outcome)에 돈을 낸다. "내가 지난주에 뭘 봤는지 찾을 수 있다"는 Chrome 기본 히스토리가 이미 해결하는 문제다.

---

## Decision

### Verdict: PIVOT

**Score:** 4.9/10 | **Confidence:** High

현재 형태의 "프라이버시 중심 로컬 저장 Chrome Extension"은 실행 가능성과 비용 효율성은 우수하지만, 시장 수요, 경쟁 우위, 리스크 프로파일에서 근본적인 문제를 가지고 있다.

핵심 문제는 세 가지다. 첫째, 무료 대안이 이미 존재하며 사용자가 이 카테고리에 돈을 낼 의사가 검증되지 않았다. 둘째, "추적 차단"이라는 핵심 USP가 Manifest V3 기술적 제약과 Chrome Web Store 정책에 의해 구현이 제한된다. 셋째, 100% 로컬·오픈소스라는 설계 철학이 모든 경쟁 우위 구축 메커니즘을 구조적으로 차단한다.

그러나 긍정적 요소도 명확하다: $5의 초기 투자, 95% 마진, 프라이버시 트렌드 타이밍, 기술적 실행 가능성. 이 요소들을 살리면서 근본적 약점을 해결하는 피벗이 필요하다.

### Strengths to Leverage
1. 극히 낮은 실행 비용 ($5 초기 투자, 서버 불필요, 95% 마진)
2. 프라이버시 타이밍이 우수 (한국 PIPA 강화, 대형 유출 사건, MyData 확대)
3. Chrome Extension 기술 스킬 보유, 2주 내 MVP 가능

### Issues to Address
1. 유료 전환 근거 부재 — 무료 대안과의 차별화 불충분
2. 플랫폼 정책 충돌 — "추적 차단" USP와 Chrome Web Store 정책 모순
3. 반복 매출 모델 없음 — One-time purchase로는 지속 불가
4. 경쟁 우위 구축 불가 — 100% 로컬 + 오픈소스 = 포크 가능, moat 없음

---

## Action Plan

### PIVOT Options

**Pivot 1: "프라이버시 분석 대시보드"로 전환 (Recommended)**
- "추적 차단" 대신 "당신의 데이터가 어디로 가는지 분석/시각화"
- 사용자에게 인사이트 제공 (어떤 사이트가 가장 많은 트래커를 사용하는지, 주간 프라이버시 점수 등)
- Freemium 구독 모델: 기본 무료 + 상세 분석 월 ₩2,900
- Chrome Web Store 정책과 충돌하지 않음 (데이터 수집이 아닌 분석)

**Pivot 2: "한국 플랫폼 데이터 내보내기 도구"로 집중**
- 프라이버시보다 "데이터 소유권/포터빌리티"에 초점
- 네이버, 카카오, 쿠팡 등 한국 서비스의 개인 데이터를 구조화된 형태로 내보내기
- MyData 제도와 연계한 포지셔닝
- B2B 가능성: 기업의 데이터 포터빌리티 컴플라이언스 도구

**Pivot 3: 포트폴리오 프로젝트로 전환**
- 유료 판매 포기, 무료 오픈소스 프로젝트로 전환
- YouTube History Keeper 하나만 집중
- 개발자 브랜딩/포트폴리오 구축 목적
- GitHub 스타 축적 → 다른 유료 프로젝트의 신뢰도 확보

---

## Kill Criteria

If ANY of these prove true, re-evaluate immediately:
- [ ] 5개 채널 홍보 후 2주 내 무료 베타 가입자 50명 미만
- [ ] 사용자 20명 인터뷰에서 "반드시 구매" 응답 10% 미만
- [ ] Chrome Web Store 출시 30일 내 유료 구매 10건 미만
- [ ] Chrome Web Store 리뷰에서 정책 위반으로 거부
- [ ] 타겟 사용자가 이미 무료 대안 사용 중이며 전환 의사 없음 확인

---

*Validated by idea-validator skill (Comprehensive mode, 6 frameworks)*
*Date: 2026-01-29*
