---
title: 경력자 이력서 정리 플랫폼 - 종합 비즈니스 분석 리포트
report-date: 2025-01-26
type: Comprehensive Business Analysis
overall-score: 6.5
business-idea-score: 6.3
feasibility-score: 6.8
recommendation: GO (조건부 - PoC + 인터뷰 검증 후)
confidence: Medium-High (70%)
tags: [comprehensive-analysis, resume, career-tech, saas, korean-market, go-decision]
---

# 종합 비즈니스 분석 리포트: 경력자 이력서 정리 플랫폼

**Date:** 2025-01-26
**Analyst:** business-orchestrator (Multi-Agent System)
**Status:** ✅ **GO (조건부)**
**Confidence Level:** Medium-High (70%)

---

## 🎯 Executive Summary

**One-line pitch:** Slack/Jira에서 자동으로 업무 성과를 추출하고, 채용공고 맞춤형 이력서를 AI로 생성하며, 크라우드소싱 면접 질문으로 이직 준비를 돕는 경력자 전용 플랫폼

**Final Assessment:**

이 아이디어는 **조건부 GO**입니다. 기술적으로 실현 가능하고(7.5/10), 재정 리스크가 매우 낮으며(8.0/10), 시장도 검증되었습니다(6.5/10). 하지만 **Slack API 연동의 기술적 타당성**과 **고객의 실제 니즈**를 먼저 검증해야 합니다.

**핵심 강점:**
1. **차별점 명확**: Poromy는 수동 입력, 이 서비스는 Slack/Jira 자동 추출
2. **낮은 진입 장벽**: 초기 비용 ₩15K, 월 운영 ₩10K-₩30K, 무료 티어 활용
3. **검증된 시장**: Rezi $2.4M ARR, StandOut CV £40K MRR → 수익 가능성 입증

**핵심 리스크:**
1. **Slack API 복잡도**: 데이터 추출 가능성 검증 필수 (PoC 1주)
2. **Churn 높을 것**: 이직은 주기적 니즈 → "이직 패키지" 모델로 완화
3. **시간 부족 가능성**: 사이드로 주 10-15시간 확보 어려울 수 있음

**Recommendation:** **PoC (1주) + 고객 인터뷰 (10명, 2주) 완료 후 최종 GO 판단**
- PoC 성공 + 인터뷰 긍정적 → Full MVP 개발 (2-3개월)
- PoC 실패 or 인터뷰 부정적 → 피벗 or 다른 아이디어

---

## 📊 Agent Analysis Summary

### 1. Business Idea Evaluation: 50/80 (6.25/10)

**Grade:** 중간 잠재력 (ITERATE 권장)

**8-Dimension Scores:**

| Dimension | Score | Weight | Weighted | Key Insight |
|-----------|-------|--------|----------|-------------|
| Problem Intensity | 7/10 | 20% | 1.4 | 실제 pain point, 시간 절약 가치 높음 |
| Market Size | 6/10 | 15% | 0.9 | 국내 5-10만명, SAM 1-2만명 |
| Competition | 5/10 | 15% | 0.75 | Poromy 존재, 중간 경쟁 강도 |
| Monetization | 6/10 | 15% | 0.9 | 구독제 Churn 리스크 → 이직 패키지로 완화 |
| Differentiation | 7/10 | 10% | 0.7 | Slack/Jira 자동 연동이 핵심 차별점 |
| Time to Market | 5/10 | 10% | 0.5 | 2-3개월 MVP, Slack API 학습 필요 |
| Solo/Team Fit | 6/10 | 10% | 0.6 | 초기 1인 가능, 성장 시 운영 부담 |
| Skills Match | 8/10 | 5% | 0.4 | 풀스택 능력 보유 ✅ |
| **TOTAL** | **50/80** | **100%** | **6.15/10** | |

**Key Strengths:**
- ✅ **Problem Intensity (7/10)**: 경력자들의 실제 pain point (이력서 정리 귀찮음)
- ✅ **Differentiation (7/10)**: Slack/Jira 자동 연동 독특
- ✅ **Skills Match (8/10)**: 풀스택 개발 능력 보유

**Key Concerns:**
- ⚠️ **Time to Market (5/10)**: Slack/Jira API 학습 복잡
- ⚠️ **Competition (5/10)**: Poromy 존재, ChatGPT 보편화
- ⚠️ **Market Size (6/10)**: 국내 시장 한정 (TAM 작음)

**Recommended Iterations:**
1. **MVP 범위 축소**: 면접 질문 제외, Slack만 지원 (Jira Phase 2)
2. **수익 모델 변경**: 월 구독 → 이직 패키지 (₩99,000/3개월)
3. **차별화 메시지 강화**: "AI 이력서" → "Slack에서 자동 정리"

**After Iterations:** 50/80 → **54/80 (6.75/10)** → 조건부 GO

[상세 리포트: resume-platform-evaluation-2025-01-26.md](../evaluations/resume-platform-evaluation-2025-01-26.md)

---

### 2. Success Pattern Analysis

**Analyzed:** 4 successful resume/career platforms (StandOut CV, Grammarly, Huntr, Wanted/Rocketpunch)

**5 Key Success Patterns Identified:**

#### Pattern 1: Freemium은 필수 (StandOut CV, Grammarly)
- **무료**: 핵심 가치 제공 (이력서 작성) → 바이럴 성장
- **유료**: 고급 기능 (무제한 생성, Slack 연동)
- **전환율**: Grammarly 40%, StandOut CV 0.1% (하지만 수익성)
- **적용**: 무료 1개, 유료 무제한 + Slack 연동

#### Pattern 2: SEO/콘텐츠가 최고의 성장 채널
- **StandOut CV**: SEO 100%, £40K MRR, 1,000+ 콘텐츠
- **Grammarly**: SEO 40%, 블로그 월 20M 방문자
- **복리 효과**: 콘텐츠 늘수록 트래픽 지수 성장
- **적용**: 주 1-2개 블로그 (병행), 6개월 후 주 3-5개로 증가

#### Pattern 3: 플랫폼 통합 = 마찰 제거 = 성장 가속
- **Grammarly**: Chrome, MS Office, Google Docs 통합
- **사용 빈도 ↑** → Stickiness ↑
- **적용**: Phase 2-3에서 Slack Bot, Chrome Extension

#### Pattern 4: Niche Targeting > Broad Market
- **Wanted/Rocketpunch**: IT/스타트업 특화 → 시장 장악 → 확장
- **마케팅 메시지 명확**, 커뮤니티 효과
- **적용**: 경력 개발자 (3년차+) only → PM/디자이너 확장은 Phase 3

#### Pattern 5: B2B Partnerships = 안정적 수익
- **Huntr**: 100+ 학교/부트캠프 파트너십
- **Grammarly**: 대학 → 기업 확장
- **적용**: PMF 후 (6-12개월) 부트캠프 파트너십 시작

**Pattern Combination for Your Idea:**
- ✅ **Phase 1 (MVP):** Freemium + Niche Targeting
- ✅ **Phase 2 (Growth):** SEO 본격화 + Slack Integration
- ✅ **Phase 3 (Scale):** Partnerships + Platform Integration

**Anti-Patterns to Avoid:**
- ❌ "Everyone" Targeting (범용 접근)
- ❌ Paid Ads Only (광고 의존)
- ❌ 완벽한 제품 기다리기 (출시 지연)
- ❌ 무료 기능 부실 (바이럴 X)
- ❌ B2C만 집착 (Churn 높음)

[상세 리포트: resume-career-platforms-success-patterns-2025-01-26.md](../stories/resume-career-platforms-success-patterns-2025-01-26.md)

---

### 3. Feasibility Assessment: 6.8/10

**Grade:** 실현 가능 (with effort, manageable risks)

**Breakdown:**

| Factor | Score | Weight | Weighted | Assessment |
|--------|-------|--------|----------|------------|
| Technical | 7.5/10 | 30% | 2.25 | 풀스택 능력, Slack API 학습 가능 (2-3주) |
| Market | 6.5/10 | 30% | 1.95 | 시장 존재 (Rezi $2.4M ARR), 경쟁 중간 |
| Financial | 8.0/10 | 20% | 1.60 | 초기 ₩15K, 월 ₩10K-₩30K, 16개월 런웨이 |
| Time | 6.0/10 | 20% | 1.20 | 사이드로 2-3개월 MVP, 타이트하지만 가능 |
| **TOTAL** | | **100%** | **7.0/10** | |

#### Technical Feasibility: 7.5/10 ✅

**Skills Match:**
- 풀스택 개발: 9/10 (React, Next.js, Node.js)
- Slack API: 0/10 → 7/10 (학습 2-3주)
- AI/LLM: 7/10 (OpenAI API 경험)

**Complexity:**
- Low Risk: 4/8 components (Frontend, Backend, DB, AI)
- Medium Risk: 2/8 components (Auth, Payment)
- High Risk: 2/8 components (Slack, Jira)
- **Mitigation**: MVP에서 Jira 제외 → Slack만 집중

**Tech Stack:**
- Frontend: Next.js 14 + React + Tailwind
- Backend: Next.js API Routes (or Node.js)
- Database: Supabase (500MB 무료)
- Auth: Clerk (10K MAU 무료)
- AI: OpenAI API (₩20K-₩50K/월)
- Hosting: Vercel (100GB 무료)

#### Financial Feasibility: 8.0/10 ✅

**Costs:**
- **Initial:** ₩15,000 (도메인)
- **Monthly:** ₩10K-₩30K (초기) → ₩142K-₩192K (성장기)
- **예산:** ₩500,000 사용 가능 → 16개월 런웨이

**Break-even:**
- Target: ₩5M MRR (지속 가능)
- 필요 고객: 152명 (이직 패키지 ₩99K/3개월)
- 달성 시점: Month 6-9 (realistic)

**무료 티어 전략:**
- Months 1-3: ₩10K-₩30K (OpenAI만)
- Months 4-6: ₩56K-₩76K (Vercel 업그레이드)
- Months 7-12: ₩142K-₩192K (Supabase, Clerk 업그레이드)

#### Time Feasibility: 6.0/10 ⚠️

**Timeline:**
- Week 1-2: PoC + 고객 인터뷰 (20-30시간)
- Week 3-6: MVP Core (40-60시간)
- Week 7-10: MVP 완성 & 베타 (40-60시간)
- Week 11-12: Public Launch (20-30시간)
- **Total:** 120-180 시간 (2.5-3개월, 주 10-15시간)

**Risk:**
- ⚠️ Slack API 학습 예상보다 길 수 있음 (4-5주)
- ⚠️ 사이드 프로젝트 번아웃 (주 10-15시간 유지 어려움)
- ⚠️ Day job 바빠지면 중단 가능성

**Mitigation:**
- ✅ PoC 먼저 (1주) → 기술 검증
- ✅ MVP 범위 최소화 (Jira, 면접 질문 제외)
- ✅ 공개 빌딩 (accountability)

#### Market Feasibility: 6.5/10 ✅

**Competitors:**
- Rezi: $2.4M ARR, 4M users (글로벌, 한국 약함)
- StandOut CV: £40K MRR, 23K paid (영어권)
- Poromy: 데이터 없음 (한국, 수동 입력)

**Market Size:**
- TAM: 한국 IT 경력자 50만명
- SAM: 연간 이직자 5-10만명
- SOM (Year 1): 500-1,000명 유료 전환

**Differentiation:**
- 자동 데이터 수집 (Poromy 대비)
- 한국 특화 (Rezi 대비)

**Revenue Projections:**
| Metric | Month 1 | Month 6 | Month 12 |
|--------|---------|---------|----------|
| MRR | ₩0.2M-₩0.5M | ₩9M-₩18M | ₩25M-₩42M |
| 유료 고객 | 5-12 | 150-300 | 360-600 |

[상세 리포트: resume-platform-feasibility-2025-01-26.md](../evaluations/resume-platform-feasibility-2025-01-26.md)

---

## 🎯 Integrated Insights

### What All Agents Agree On

✅ **Consensus Points:**

1. **Freemium 모델 필수**
   - business-idea-evaluator: 진입 장벽 낮춤
   - success-formula-analyzer: Grammarly/StandOut CV 모두 사용
   - feasibility-checker: 바이럴 성장에 유리

2. **Slack 자동 연동이 핵심 차별점**
   - business-idea-evaluator: Differentiation 7/10
   - success-formula-analyzer: Poromy 대비 유일한 강점
   - feasibility-checker: 기술적 타당성 검증 필요 (PoC)

3. **경력 개발자 니치 타겟팅**
   - business-idea-evaluator: "모든 직군"은 실패 요인
   - success-formula-analyzer: Wanted/Rocketpunch 성공 사례
   - feasibility-checker: 마케팅 효율성 ↑

4. **SEO가 장기 성장 채널**
   - business-idea-evaluator: Time to Market 개선 필요
   - success-formula-analyzer: StandOut CV £40K MRR (SEO 100%)
   - feasibility-checker: 초기 병행, 6개월 후 본격화

### Where Agents Diverge

⚠️ **Divergence 1: 면접 질문 기능**
- **business-idea-evaluator**: MVP에 포함 (통합 플랫폼 강점)
- **success-formula-analyzer**: 성공 사례 없음, Cold Start 문제
- **feasibility-checker**: MVP에서 제외 권장 (복잡도 ↑, 시간 ↑)
- **Resolution:** ✅ **MVP에서 제외, Phase 3로 연기**

⚠️ **Divergence 2: 수익 모델**
- **business-idea-evaluator**: 월 구독 ₩19,900/월 (Monetization 6/10)
- **success-formula-analyzer**: 성공 사례들은 월 구독 ($29/월)
- **feasibility-checker**: 이직 패키지 ₩99,000/3개월 (Churn 관리)
- **Resolution:** ✅ **이직 패키지 모델 채택** (Churn 리스크 낮춤)

⚠️ **Divergence 3: Jira 연동 시점**
- **business-idea-evaluator**: MVP에 포함 (차별점 강화)
- **success-formula-analyzer**: 성공 패턴에서 발견 안 됨
- **feasibility-checker**: MVP에서 제외 권장 (학습 시간 ↓)
- **Resolution:** ✅ **MVP에서 제외, Phase 2로 연기**

### Surprising Discoveries

💡 **Insight 1: Poromy 데이터 없음 = 기회**
- Poromy가 웹에서 데이터가 거의 없음
- → 아직 작은 플레이어 or 마케팅 약함
- → 경쟁 위협 낮을 수 있음

💡 **Insight 2: 한국 시장 willingness to pay 높음**
- 이력서 작성 대행: ₩50K-₩300K
- 커리어 코칭: ₩500K-₩2M
- → 경력자는 이력서에 돈 쓸 의향 있음

💡 **Insight 3: Slack API 복잡도 예상보다 높음**
- "Deep and wide, possibly intimidating"
- 커스터마이징, 복잡한 룰, rich content
- → PoC 필수, 실패 가능성 고려

---

## 🧮 Final Score Calculation

```
Final Score = (Idea: 50/80 × 0.4) + (Pattern Match: 7/10 × 0.3) + (Feasibility: 6.8/10 × 0.3)
            = (6.25 × 0.4) + (7 × 0.3) + (6.8 × 0.3)
            = 2.5 + 2.1 + 2.04
            = 6.64/10
```

**Interpretation:** 강력한 잠재력 (Good potential, some risks to address)

**Rounded Final Score: 6.5/10**

---

## 🔴 Risk Assessment

### Critical Risks (Must Address Before Proceeding)

**1. Slack API 기술적 타당성 불명확 🔴**
- **Probability:** Medium (40%)
- **Impact:** Critical (프로젝트 실패)
- **Mitigation:**
  - ✅ **1주 PoC 필수**: 본인 Slack에서 데이터 추출 테스트
  - ✅ **Success Criteria**: 의미 있는 업무 성과 (프로젝트, 완료, 배포 등) 추출 가능
  - ✅ **Failure Plan**: 자동화 포기 → Poromy처럼 수동 입력 모델로 피벗
- **Timeline:** Week 1 (즉시)
- **Budget:** ₩0

**2. 고객 니즈 검증 미흡 🔴**
- **Probability:** Medium (30%)
- **Impact:** High (PMF 실패)
- **Mitigation:**
  - ✅ **10명 인터뷰 필수**: 이직 준비 경력자
  - ✅ **Success Criteria**: 5명 이상 "쓰고 싶다", 가격 의향 ₩50K+
  - ✅ **Failure Plan**: 니즈 재정의 or 다른 아이디어 탐색
- **Timeline:** Week 2-3 (PoC 후)
- **Budget:** ₩0 (시간만 투자)

### High Risks (Address in First 3 Months)

**3. 월 구독 모델 Churn 🟡**
- **Probability:** High (70%)
- **Impact:** High (MRR 불안정)
- **Mitigation:**
  - ✅ **이직 패키지 모델**: ₩99,000/3개월 (월 환산 ₩33K)
  - ✅ **연간 구독 옵션**: ₩199,000/년 (할인)
  - ✅ **B2B 파트너십** (6개월 후): 부트캠프, 헤드헌팅 회사
- **Timeline:** MVP 설계 단계 (즉시)
- **Budget:** ₩0

**4. 경쟁사 증가 가능성 🟡**
- **Probability:** Medium (50%)
- **Impact:** Medium (시장 점유율 하락)
- **Mitigation:**
  - ✅ **빠른 출시**: 2-3개월 내 MVP
  - ✅ **차별화 강화**: Slack 자동 연동 강조
  - ✅ **SEO 조기 시작**: 6개월 후 유기적 트래픽 확보
- **Timeline:** 지속적
- **Budget:** ₩0 (시간 투자)

### Medium Risks (Monitor and Manage)

**5. 사이드 프로젝트 지속 어려움 🟢**
- **Probability:** Medium (40%)
- **Impact:** Medium (출시 지연)
- **Mitigation:**
  - ✅ **주간 10-15시간 확보**: Day job과 균형
  - ✅ **공개 빌딩**: Twitter, 블로그 (accountability)
  - ✅ **작은 마일스톤**: 주간 목표 설정
- **Timeline:** 지속적
- **Budget:** ₩0

**6. Slack/Jira 사용 패턴 다양성 🟢**
- **Probability:** High (80%)
- **Impact:** Medium (디버깅 요청 많음)
- **Mitigation:**
  - ✅ **초기에는 특정 패턴만 지원**: 점진적 확대
  - ✅ **셀프서비스 위주**: 문서화 강화
  - ✅ **Phase 2에서 확장**: 다양한 회사 패턴 대응
- **Timeline:** MVP 후 (3개월+)
- **Budget:** ₩0

### Low Risks (Accept and Track)

**7. 국내 시장 규모 한계 🟢**
- **Probability:** High (90%)
- **Impact:** Low (Year 1-2는 국내만으로 충분)
- **Mitigation:**
  - ✅ **국내 PMF 먼저**: Year 1-2
  - ✅ **해외 확장 고려**: PMF 후 (일본, 동남아)
- **Timeline:** Year 2+
- **Budget:** 나중에 결정

---

## 💎 Opportunity Map

### Immediate Opportunities (0-3 Months)

**1. 무료 베타로 빠른 검증**
- **Effort:** Low (Week 7-10)
- **Impact:** Early feedback, PMF validation
- **Actions:**
  - [ ] 베타 사용자 50명 모집 (블라인드, 오픈챗)
  - [ ] 무료로 Slack 연동 + 이력서 생성 제공
  - [ ] 피드백 수집 & Iteration

**2. 개발자 커뮤니티 타겟 마케팅**
- **Effort:** Low (런칭 시)
- **Impact:** 니치 타겟에 빠른 도달
- **Actions:**
  - [ ] 블라인드 "이직" 토픽에 포스팅
  - [ ] 오픈챗 개발자 방에서 공유
  - [ ] LinkedIn 개발자 그룹 타겟

**3. SEO 조기 시작**
- **Effort:** Medium (주 1-2시간)
- **Impact:** 장기 유기적 트래픽
- **Actions:**
  - [ ] "개발자 이력서 작성법" 시리즈 (10개)
  - [ ] "경력 전환 이력서" 가이드
  - [ ] "네이버/카카오 이직" 케이스 스터디

### Medium-term Opportunities (3-12 Months)

**4. Linkable Asset (데이터 리포트)**
- **Effort:** Medium (6개월 후, 40시간)
- **Impact:** 50-100 백링크, 브랜드 인지도
- **Actions:**
  - [ ] "2025 한국 개발자 이직 통계" 설문 (100-200명)
  - [ ] 리포트 발행 (PDF + 블로그)
  - [ ] 언론 배포 (ZDNet, GeekNews 등)

**5. 부트캠프 파트너십**
- **Effort:** Low-Medium (6-12개월 후)
- **Impact:** 월 50-100명 유입, 안정적 MRR
- **Actions:**
  - [ ] 코드스테이츠, 패스트캠퍼스 등 컨택
  - [ ] 졸업생 무료 or 학교 소액 (Win-Win)
  - [ ] 파일럿 1-2곳 진행

**6. Slack Bot 출시 (Phase 2)**
- **Effort:** Medium (3-6개월 후, 40시간)
- **Impact:** 마찰 감소, 사용 빈도 ↑
- **Actions:**
  - [ ] `/resume` 명령어로 자동 요약
  - [ ] 채널에서 바로 이력서 생성
  - [ ] Slack App Directory 등록

### Long-term Strategic Plays (12+ Months)

**7. B2B SaaS 모델 (헤드헌팅 회사)**
- **Effort:** High (Year 2)
- **Impact:** 대규모 MRR, 안정적 수익
- **Actions:**
  - [ ] 헤드헌터용 대시보드 개발
  - [ ] 여러 후보자 관리 기능
  - [ ] Enterprise 가격 (₩500K-₩1M/월)

**8. Chrome Extension (LinkedIn 통합)**
- **Effort:** Medium (Year 2)
- **Impact:** 글로벌 확장 가능
- **Actions:**
  - [ ] LinkedIn 공고 보면서 바로 이력서 생성
  - [ ] Grammarly처럼 브라우저 통합
  - [ ] Chrome Web Store 등록

---

## ✅ Recommendation: GO (조건부)

### Decision: GO (조건부 - PoC + 인터뷰 검증 후)

### Why Proceed

**1. 기술적으로 실현 가능 (7.5/10)**
- 풀스택 개발 능력 보유 (React, Next.js, Node.js)
- Slack API는 새롭지만 학습 가능 (2-3주)
- 무료 티어로 초기 비용 최소화 (₩10K-₩30K/월)

**2. 시장 검증됨 (6.5/10)**
- Rezi: $2.4M ARR, 4M users → 글로벌 시장 존재
- StandOut CV: £40K MRR → 소규모도 수익 가능
- 한국 willingness to pay 높음 (이력서 대행 ₩50K-₩300K)

**3. 차별점 명확 (7/10)**
- Poromy: 수동 입력 vs 이 서비스: 자동 추출
- Rezi: 글로벌 vs 이 서비스: 한국 특화
- ChatGPT: 기억 의존 vs 이 서비스: 실제 데이터

**4. 재정 리스크 매우 낮음 (8.0/10)**
- 초기 ₩15K, 월 ₩10K-₩30K
- 예산 ₩500K = 16개월 런웨이
- Break-even 현실적 (152-215명, Month 6-9)

**5. 성공 패턴 적용 가능**
- Freemium 모델 (Grammarly, StandOut CV)
- SEO 중심 성장 (StandOut CV £40K MRR)
- 니치 타겟팅 (Wanted/Rocketpunch)

### Critical Success Factors

**1. PoC 성공 (1주 내)**
- Slack 데이터에서 의미 있는 업무 성과 추출 가능
- 실패 시 → 자동화 포기, 수동 입력 모델로 피벗

**2. 고객 니즈 검증 (2-3주 내)**
- 10명 인터뷰, 5명 이상 긍정 반응
- 가격 의향 ₩50K-₩100K 확인

**3. MVP 범위 집중 (2-3개월)**
- Slack 연동 + AI 이력서 생성만
- Jira, 면접 질문은 Phase 2-3

**4. 주 10-15시간 시간 확보**
- 사이드 프로젝트 지속 가능 일정
- Day job과 균형

**5. 빠른 출시 & Iteration**
- 2-3개월 내 MVP 런칭
- 베타 피드백 즉각 반영

### Action Plan

#### Phase 0: Pre-Development (Week 1-3)

**Objectives:**
- Slack API 기술 검증 (PoC)
- 고객 니즈 검증 (인터뷰 10명)
- MVP 범위 최종 확정

**Tasks:**
- [ ] **Week 1: Slack API PoC**
  - Slack 앱 생성, OAuth 연동
  - 본인 Slack 워크스페이스 데이터 추출
  - 업무 성과 파싱 가능한지 검증
  - Success: 의미 있는 정보 추출 → 고객 인터뷰 진행
  - Failure: 자동화 포기 → 수동 입력 모델 피벗

- [ ] **Week 2-3: 고객 인터뷰 10명**
  - 타겟: 이직 준비 경력 개발자 (블라인드, 오픈챗)
  - 질문: 이력서 작성 pain point, 자동화 니즈, 가격 의향
  - Success: 5명 이상 긍정, ₩50K+ 의향 → MVP 개발
  - Failure: 니즈 부족 → 다른 아이디어 탐색

**Success Metrics:**
- PoC: Slack 데이터 추출 성공
- 인터뷰: 5명 이상 "쓰고 싶다" (60-70%)
- 가격: 평균 willingness to pay ₩50K+

**Budget:** ₩0
**Time Required:** 20-30시간

**Decision Point (Week 3):**
- ✅ PoC Success + 인터뷰 긍정적 → MVP 개발 시작
- ❌ PoC Failure or 인터뷰 부정적 → 피벗 or 중단

---

#### Phase 1: MVP Development (Week 4-12, 2-3개월)

**Objectives:**
- Slack 연동 + AI 이력서 생성 기능 완성
- 베타 사용자 50명 확보
- 초기 피드백 수집 & Iteration

**Milestones:**

**Week 4-6: MVP Core (40-60시간)**
- Next.js 프로젝트 셋업
- Clerk Auth 통합 (10K MAU 무료)
- Supabase DB 스키마 설계
- Slack OAuth 2.0 연동
- Slack 데이터 추출 & 파싱
- OpenAI API 이력서 생성
- 기본 UI/UX

**Week 7-10: MVP 완성 (40-60시간)**
- 채용공고 맞춤 기능
- 이력서 템플릿 3종 (개발자/PM/디자이너)
- 수동 결제 (은행 송금, Stripe는 Phase 2)
- 베타 사용자 50명 모집
- 피드백 수집 & 버그 수정
- 랜딩 페이지 + SEO 최적화

**Week 11-12: Public Launch (20-30시간)**
- Product Hunt 준비 & 런칭
- Hacker News Show HN
- 블로그 포스트 3개 (SEO)
- 커뮤니티 마케팅 (블라인드, 오픈챗)
- 런칭 & 초기 고객 서포트

**Success Metrics:**
- 베타 사용자: 50명
- 유료 전환: 5-10명 (10-20%)
- NPS: >30
- 피드백: 핵심 기능 동작 확인

**Budget:** ₩10K-₩30K/월 (OpenAI API)
**Time Required:** 100-150시간 (주 10-15시간 × 10주)

**Decision Point (Week 12):**
- ✅ 베타 사용자 >30명, 유료 >3명 → Phase 2 진행
- ⚠️ 베타 사용자 <30명 → 마케팅 재검토
- ❌ 유료 전환 0명 → 가격/가치 재설계

---

#### Phase 2: Growth & Iteration (Month 4-6)

**Objectives:**
- Public Launch로 100-300명 가입자
- 유료 전환 10-20% 달성 (10-60명)
- MRR ₩1M-₩3M 달성
- SEO 본격화

**Key Focus Areas:**

**1. Customer Acquisition**
- Goal: 300-1,000 가입자 by Month 6
- Channels: Product Hunt, Hacker News, SEO, 커뮤니티
- Budget: ₩100K (Product Hunt 프로모션, 페이스북 광고)

**2. Product Development**
- Jira 연동 추가 (Phase 2-1)
- 면접 질문 커뮤니티 (Phase 2-2, optional)
- Stripe 결제 통합
- 사용자 피드백 반영 (주간 iteration)

**3. Content Marketing (SEO)**
- 주 3-5개 블로그 포스트
- "개발자 이력서" 키워드 타겟
- Linkable Asset 1개 ("2025 개발자 이직 통계")

**Success Metrics:**
- 가입자: 300-1,000명
- 유료 전환: 10-20% (30-200명)
- MRR: ₩1M-₩6M
- Churn: <30%
- 유기적 트래픽: 월 500+ (SEO 시작 효과)

**Budget:** ₩200K-₩300K/월 (운영 ₩56K-₩76K + 마케팅 ₩100K)
**Time Required:** 주 15-20시간 (성장 단계)

---

#### Phase 3: Scale (Month 7-12)

**Objectives:**
- MRR ₩10M-₩30M 달성
- 유료 고객 150-600명
- B2B 파트너십 시작
- 플랫폼 통합 (Slack Bot, Chrome Extension)

**Key Focus Areas:**

**1. Customer Acquisition**
- Goal: 1,500-5,000 가입자 by Month 12
- Channels: SEO (주력), 파트너십, 커뮤니티
- SEO 복리 효과: 월 1,000-3,000 유기적 트래픽

**2. Product Development**
- Slack Bot 출시 (마찰 감소)
- Chrome Extension (LinkedIn 통합)
- 면접 질문 커뮤니티 (if validated)

**3. Partnerships**
- 부트캠프 2-3곳 파트너십
- 헤드헌팅 회사 B2B 파일럿

**Success Metrics:**
- 가입자: 3,000-5,000명
- 유료 전환: 10-12% (300-600명)
- MRR: ₩25M-₩42M
- Churn: <25%
- NPS: >40

**Budget:** ₩300K-₩500K/월
**Time Required:** 풀타임 고려 (MRR >₩15M 시)

---

## 📈 Decision Points & Kill Criteria

### Month 1 Decision Point (PoC + 인터뷰 완료)

**Evaluate:**
- PoC 성공 여부
- 고객 관심도 (10명 중 5명 이상)
- 가격 의향 (₩50K+)

**Continue if:**
- ✅ Slack 데이터 추출 성공
- ✅ 5명 이상 "쓰고 싶다"
- ✅ 가격 의향 ₩50K 이상

**Pivot if:**
- ❌ PoC 실패 (자동화 불가능)
- ❌ 고객 관심 낮음 (<5명)
- ❌ 가격 저항 높음 (<₩30K)

### Month 3 Decision Point (MVP 완료)

**Evaluate:**
- 베타 사용자 수
- 유료 전환율
- 피드백 품질

**Continue if:**
- ✅ 베타 사용자 >30명
- ✅ 유료 전환 >3명 (10%+)
- ✅ 긍정적 피드백 다수

**Pivot if:**
- ❌ 베타 사용자 <20명
- ❌ 유료 전환 0명
- ❌ 부정적 피드백 다수

### Month 6 Decision Point (Public Launch 후)

**Evaluate:**
- MRR 성장 추이
- Churn 율
- 시장 반응

**Continue if:**
- ✅ MRR >₩2M
- ✅ 월 성장률 >10%
- ✅ Churn <30%

**Abandon if:**
- ❌ MRR <₩1M (flat)
- ❌ Churn >50%
- ❌ 시장 반응 부정적

### Month 12 Decision Point (Year 1 완료)

**Evaluate:**
- MRR 규모
- 지속 가능성
- 기회 비용

**Continue if:**
- ✅ MRR >₩10M (지속 가능)
- ✅ 성장 추세 유지
- ✅ 풀타임 전환 고려 가능

**Pivot/Exit if:**
- ❌ MRR <₩5M (사이드로만 유지)
- ❌ 성장 정체
- ❌ 더 좋은 기회 발견

---

## 📊 Success Metrics Dashboard

### Lagging Indicators (Measure Success)

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| **MRR** | ₩0.2M-₩0.5M | ₩1M-₩2M | ₩5M-₩10M | ₩15M-₩30M |
| **Paying Customers** | 5-12 | 15-40 | 80-200 | 200-500 |
| **Churn** | - | 35% | 30% | 25% |
| **ARPU** | ₩40K | ₩50K | ₩60K | ₩70K |
| **NPS** | - | >30 | >35 | >40 |

### Leading Indicators (Predict Success)

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| **Total Users** | 100-250 | 300-500 | 1,000-2,000 | 3,000-5,000 |
| **Weekly Active Users** | 50-100 | 150-250 | 500-1,000 | 1,500-2,500 |
| **Free→Paid Conversion** | 5% | 8% | 10% | 12% |
| **Retention (D7)** | - | 40% | 50% | 60% |
| **Organic Traffic** | 100-200 | 300-500 | 1,000-2,000 | 3,000-5,000 |

### Tracking Tools
- **Revenue**: 초기 수동 (은행 송금) → Stripe (Phase 2)
- **Users**: Google Analytics + Mixpanel
- **Retention**: Mixpanel Cohort Analysis
- **Feedback**: Typeform + 수동 인터뷰

---

## 🎯 Final Recommendation Summary

### GO (조건부)

**Success Probability: 40-60%**

**Breakdown:**
- 기술 구현 성공: 80-90% ✅
- PMF 달성: 30-50% ⚠️
- 수익 목표 (₩5M MRR): 20-40% ⚠️

**Why 40-60%?**
- ✅ 기술/재정적으로 매우 feasible
- ⚠️ 시장 검증은 불확실 (경쟁, Churn)
- ✅ PoC + 인터뷰로 early validation → 실패 확률 낮춤

**Realistic Outcome (Base Case):**
- Year 1: ₩5M-₩15M MRR (지속 가능한 사이드 프로젝트)
- Year 2: ₩20M-₩40M MRR (풀타임 전환 고려 가능)

**Start With:**
1. ✅ **Week 1: Slack API PoC** (본인 워크스페이스 테스트)
2. ✅ **Week 2-3: 고객 인터뷰 10명** (이직 준비 개발자)
3. ✅ **Week 4+: MVP 개발 시작** (if PoC + 인터뷰 성공)

**Timeline:** 2-3개월 MVP → 6개월 Public Launch → 12개월 ₩10M-₩30M MRR

**Next Immediate Action:** **1주 내 Slack API PoC 시작**

---

## 📚 Appendices

### A. Detailed Agent Reports
- [Business Idea Evaluation](../evaluations/resume-platform-evaluation-2025-01-26.md) - 50/80 (6.25/10)
- [Success Pattern Analysis](../stories/resume-career-platforms-success-patterns-2025-01-26.md) - 5 patterns identified
- [Feasibility Assessment](../evaluations/resume-platform-feasibility-2025-01-26.md) - 6.8/10

### B. Research Sources
- [Rezi Revenue](https://boringcashcow.com/view/resume-builder-achieves-24m-annual-revenue) - $2.4M ARR
- [StandOut CV](https://www.indiehackers.com/post/how-i-grew-my-saas-business-to-40k-mrr-with-seo-3287452853) - £40K MRR (SEO)
- [Grammarly Growth](https://getlatka.com/blog/grammarly-revenue/) - $250M ARR, 30M DAU
- [한국 채용 시장](https://zdnet.co.kr/view/?no=20240718141936) - 사람인 9.22M MAU
- [Slack API Docs](https://api.slack.com/start) - Official documentation
- [Jira Integration Guide](https://developer.atlassian.com/developer-guide/jira-integration-guidelines/)

### C. Financial Projections

**Conservative (70% 신뢰):**
| Month | MRR | 누적 투자 | 누적 수익 | 손익 |
|-------|-----|----------|----------|------|
| 3 | ₩1.5M | ₩100K | ₩4.5M | ₩4.4M |
| 6 | ₩7M | ₩300K | ₩30M | ₩29.7M |
| 12 | ₩15M | ₩500K | ₩120M | ₩119.5M |

**Base Case (50% 신뢰):**
| Month | MRR | 누적 투자 | 누적 수익 | 손익 |
|-------|-----|----------|----------|------|
| 3 | ₩2M | ₩100K | ₩6M | ₩5.9M |
| 6 | ₩10M | ₩300K | ₩42M | ₩41.7M |
| 12 | ₩30M | ₩500K | ₩210M | ₩209.5M |

**Break-even:** Month 1-2 (최소 5-10명 유료 전환)

### D. Technical Architecture

**Tech Stack:**
- Frontend: Next.js 14 + React + Tailwind CSS
- Backend: Next.js API Routes (초기) → Express (Phase 2)
- Database: Supabase (PostgreSQL)
- Auth: Clerk (OAuth 2.0)
- AI: OpenAI API (GPT-4)
- Payment: 수동 (초기) → Stripe (Phase 2)
- Hosting: Vercel
- Monitoring: Sentry (무료 티어)

**Architecture Diagram:**
```
User → Next.js (Vercel)
       ↓
   Clerk Auth → Slack OAuth
       ↓
   Supabase DB ← OpenAI API
       ↓
   Payment (Stripe, Phase 2)
```

---

**Report Completed:** 2025-01-26
**Next Action:** **Slack API PoC (1주)**
**Status:** ✅ **GO (조건부 - PoC 검증 후)**

**Final Message:**
이 아이디어는 기술적으로 실현 가능하고, 시장도 존재하며, 재정 리스크가 낮습니다. 하지만 **Slack API 연동의 기술적 타당성**과 **고객의 실제 니즈**를 먼저 검증해야 합니다. **1주 내 PoC를 시작**하고, **2-3주 내 고객 인터뷰 10명**을 완료하세요. 둘 다 긍정적이면 full MVP 개발을 시작하세요.

**Success Probability: 40-60%** (PoC + 인터뷰 검증 후 70-80%로 상승 가능)
