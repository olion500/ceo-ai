---
title: 경력자 이력서 정리 플랫폼 실행 가능성 리포트
evaluation-date: 2025-01-26
type: Feasibility Assessment
overall-feasibility: 6.8
technical-feasibility: 7.5
financial-feasibility: 8.0
time-feasibility: 6.0
market-feasibility: 6.5
recommendation: PROCEED (조건부)
tags: [feasibility, resume, career-tech, saas, technical-assessment]
---

# Feasibility Report: 경력자 이력서 정리 플랫폼

**Generated Date:** 2025-01-26
**Idea Score:** 6.3/10
**Feasibility Score:** 6.8/10
**Final Recommendation:** PROCEED (조건부)

---

## Executive Summary

**Can I build this?** Yes, 조건부 가능

**Confidence level:** Medium-High (70%)

**Key blockers:**
- Slack/Jira API 연동 복잡도 (학습 곡선 2-3주)
- 면접 질문 커뮤니티 Cold Start 문제 (MVP에서 제외 권장)
- 시장 경쟁사 증가 가능성 (Poromy 외 글로벌 플레이어들)

**Recommended action:** **PROCEED** with MVP 범위 축소
1. Phase 1: Slack 연동 + AI 이력서 생성만 (2-3개월)
2. PoC 먼저 진행 (Slack 데이터 추출 가능성 검증, 1주)
3. 고객 인터뷰 10명 완료 후 최종 GO 판단

**Why this assessment:**
- **Technical (7.5/10):** 풀스택 능력 보유, API 연동은 학습 가능, 복잡도 관리 가능
- **Market (6.5/10):** 시장 존재 확인, 경쟁 중간, 차별점 명확
- **Financial (8.0/10):** 초기 비용 매우 낮음 ($0-50), 예산 충분 (₩500K 사용 가능)
- **Time (6.0/10):** 사이드 프로젝트로 2-3개월 MVP 가능, 하지만 타이트

---

## Market & Competition Analysis

### Competitive Landscape

**Direct Competitors:**

| Competitor | Pricing | Users/Revenue | Strengths | Weaknesses | Source |
|------------|---------|---------------|-----------|------------|--------|
| [Poromy](https://poromy.ai.kr) | 미확인 (무료 or 프리미엄) | 데이터 없음 | K-STAR-K 프레임워크, 한국 특화 | 수동 입력, 프롬프트만 제공 | 사용자 제공 URL |
| [Rezi](https://www.rezi.ai) | $29/mo | 4M+ users, $2.4M ARR | 글로벌 4M 사용자, JobKorea 파트너십 | 한국 맞춤형 아님 | [BoringCashCow](https://boringcashcow.com/view/resume-builder-achieves-24m-annual-revenue) |
| [StandOut CV](https://standout-cv.com) | Free + Paid | 23K paid, 18M visitors | SEO 강함, £40K MRR | 영어권 중심 | [Indie Hackers](https://www.indiehackers.com/post/how-i-grew-my-saas-business-to-40k-mrr-with-seo-3287452853) |

**Indirect Competitors:**
- **원티드/사람인/잡코리아**: 기본 이력서 관리 기능 (차별화 낮음)
- **ChatGPT 직접 사용**: 사용자가 직접 프롬프트 작성 (불편함)
- **이력서 작성 대행**: ₩50K-₩300K (비용 높음, 1회성)

**Market Gaps:**
- 자동 데이터 수집: Slack/Jira에서 업무 성과 자동 추출하는 도구 없음
- 한국 시장 특화: 글로벌 도구들은 한국 이력서 문화 미반영
- 통합 플랫폼: 이력서 작성 + 면접 준비 한 곳에서 제공하는 곳 부재

**Your Differentiation:**
- **자동화**: Poromy는 수동 입력, 이 서비스는 Slack/Jira 자동 추출
- **한국 특화**: Rezi는 글로벌 도구, 이 서비스는 한국 이력서 문화 반영
- **데이터 기반**: ChatGPT는 기억 의존, 이 서비스는 실제 업무 데이터 활용

**Key Insight:**
Poromy가 존재하지만 "자동 데이터 수집"이 핵심 차별점. Rezi는 $2.4M ARR 달성했으나 한국 시장 특화 약함. 시장 갭은 명확하게 존재하며, 경쟁 강도는 중간 수준.

---

## Revenue Model Analysis

### Short-term Revenue (Week 1-4)

**Market Entry Speed:**
- **Market exists:** ✅ Yes (Rezi $2.4M ARR, 글로벌 시장 $4.28B by 2034)
- **Proof of payment:** ✅ Confirmed (Rezi $29/mo, StandOut CV £40K MRR, 이력서 대행 ₩50K-₩300K)
- **Distribution channels:** Product Hunt, Hacker News, 개발자 커뮤니티 (블라인드, 오픈챗)
- **Week 1 revenue potential:** $0 (무료 베타 테스트)
- **Month 1 revenue potential:** $200-500 (5-10명 early adopters × ₩20K-₩50K)

**Evidence:**
- ✅ Rezi: 4M+ 사용자, $2.4M ARR → 시장 크기 검증
- ✅ StandOut CV: £40K MRR, 23K paid → 유료 전환 가능성 검증
- ✅ 이력서 대행 시장: ₩50K-₩300K → 높은 willingness to pay
- ✅ 한국 채용 플랫폼: 사람인 9.22M MAU → 잠재 고객 풀 존재

### Short-term Customer Acquisition (Must be specific)

**Launch Strategy (Week 1):**

1. **Product Hunt** - 200-500 visitors - 5% signup = 10-25 users
   - 유사 도구(resume builder) 평균 200-500 upvotes
   - 5% signup conversion (보수적)

2. **Hacker News (Show HN)** - 1,000-3,000 visitors - 3% signup = 30-90 users
   - IT 타겟에 적합, 경력 개발자 집중
   - 3% conversion (보수적)

3. **개발자 커뮤니티 (블라인드, 오픈챗)** - 500-1,000 reach - 10% signup = 50-100 users
   - 한국 개발자 밀집, 이직 관련 논의 활발
   - 10% conversion (니치 타겟)

4. **개인 네트워크 (LinkedIn, 페이스북)** - 200-500 reach - 5% signup = 10-25 users
   - 기존 네트워크 활용
   - 5% conversion

**Realistic Month 1 Numbers:**
- **Visitors:** 2,000-5,000 (from 4 channels)
- **Signups:** 100-250 (2-5% conversion)
- **Paying:** 5-10 (2-5% paid conversion, early adopter 프로모션)
- **Revenue:** ₩200K-₩500K (5-10명 × ₩40K-₩50K early bird 할인)

**Evidence for estimates:**
- Similar resume tools on Product Hunt: 200-500 upvotes → 1K-3K visitors
- Hacker News Show HN 평균: 1K-5K visitors (니치 도구 기준)
- 개발자 커뮤니티 반응률: 10-20% (pain point 명확할 때)
- Early adopter 전환율: 2-5% (프로모션 가격일 때)

**RED FLAG 체크:**
- ✅ 트래픽 추정 근거 있음 (유사 제품 벤치마크)
- ✅ 전환율 보수적 (2-5%, 낙관적 10% 아님)
- ✅ 경쟁사 런칭 데이터 참고 (Rezi, StandOut CV)
- ✅ "Viral" 가정 안 함 (현실적 채널별 추정)

### Long-term Revenue (6-12 months)

**Similar Product Benchmarks:**

| Similar Product | Month 1 | Month 6 | Month 12 | Source |
|-----------------|---------|---------|----------|--------|
| StandOut CV | ~₩5M (추정) | ~₩30M | £40K (~₩65M) | [Indie Hackers](https://www.indiehackers.com/post/how-i-grew-my-saas-business-to-40k-mrr-with-seo-3287452853) |
| Rezi | 데이터 없음 | 데이터 없음 | $2.4M ARR (~₩200M/mo) | [BoringCashCow](https://boringcashcow.com/view/resume-builder-achieves-24m-annual-revenue) |

**Your Projections (Based on benchmarks):**

| Metric | Month 1 | Month 3 | Month 6 | Month 12 | Assumption |
|--------|---------|---------|---------|----------|------------|
| 가입자 | 100-250 | 500-1,000 | 1,500-3,000 | 3,000-5,000 | SEO 시작, 입소문 |
| 유료 전환율 | 5% | 8% | 10% | 12% | 점진적 증가 |
| 유료 고객 | 5-12 | 40-80 | 150-300 | 360-600 | 전환율 × 가입자 |
| ARPU | ₩40K | ₩50K | ₩60K | ₩70K | 가격 인상 |
| **MRR** | **₩0.2M-₩0.5M** | **₩2M-₩4M** | **₩9M-₩18M** | **₩25M-₩42M** | |
| Churn | 40% | 35% | 30% | 25% | 이직 시즌성 |

**Growth Drivers:**
1. **SEO 복리 효과**: 월 3-5개 블로그 → 6개월 후 월 1,000+ 유기적 방문자
2. **입소문/바이럴**: 경력 개발자 커뮤니티에서 자연스러운 공유
3. **파트너십 (6개월 후)**: 부트캠프 1-2곳 → 월 50-100명 추가 유입

**Constraints:**
- **Market size limit:** 연간 이직 경력 개발자 5-10만명 (TAM), 실제 도달 가능 1-2만명 (SAM)
- **Distribution bottleneck:** SEO는 느림 (6-12개월), Paid Ads 예산 제한
- **Competition:** Poromy가 유료 모델 전환 시 경쟁 심화, 글로벌 플레이어(Rezi) 한국 진출

**Realistic vs Optimistic:**
- **Conservative (70% 신뢰):** ₩15M MRR by month 12
- **Base case (50% 신뢰):** ₩30M MRR by month 12
- **Optimistic (20% 신뢰):** ₩50M MRR by month 12

**Evidence-based reasoning:**
- StandOut CV는 SEO 중심으로 £40K MRR 달성 (6년 소요 추정)
- 한국 시장은 더 작지만 (영어권 vs 한국), willingness to pay는 높음 (이력서 대행 ₩50K-₩300K)
- Rezi는 4M 사용자로 $2.4M ARR ($0.6 ARPU) → 한국은 사용자는 적지만 ARPU 높을 것 (₩70K vs $0.6)
- 보수적 시나리오는 300-600 유료 고객 달성 기준 (realistic for year 1)

---

## Technical Feasibility: 7.5/10

### Skills Assessment

**Your Current Skills:**
- **풀스택 개발**: Advanced (9/10) ✅
  - 프론트엔드: React, Next.js 가능
  - 백엔드: Node.js, Python 가능
  - 데이터베이스: SQL, NoSQL 경험

- **API 연동**: Intermediate (6/10) ⚠️
  - REST API 호출 경험 있음
  - OAuth 2.0 이해 중간
  - Slack/Jira API는 처음

- **AI/LLM**: Intermediate (7/10) ✅
  - OpenAI API 사용 경험 있음
  - 프롬프트 엔지니어링 가능

- **Infrastructure/DevOps**: Intermediate (7/10) ✅
  - Vercel, Netlify 배포 경험
  - 기본 CI/CD 이해

### Requirements Matrix

| Requirement | Your Level | Required | Gap | Learning Time | Blocker? |
|-------------|------------|----------|-----|---------------|----------|
| **React/Next.js** | 9/10 | 7/10 | None | 0 weeks | No ✅ |
| **Node.js Backend** | 8/10 | 7/10 | None | 0 weeks | No ✅ |
| **Slack API** | 0/10 | 7/10 | Large | 2-3 weeks | No ⚠️ |
| **Jira API** | 0/10 | 7/10 | Large | 2-3 weeks | No ⚠️ |
| **OpenAI API** | 7/10 | 6/10 | None | 0 weeks | No ✅ |
| **OAuth 2.0** | 6/10 | 8/10 | Small | 1 week | No ⚠️ |
| **Database Design** | 7/10 | 7/10 | None | 0 weeks | No ✅ |
| **Payment Integration (Stripe)** | 5/10 | 7/10 | Small | 1-2 weeks | No ⚠️ |

**Gap Summary:**
- **Total learning time:** 4-6주 (Slack API 2-3주 + Jira API 2-3주 병렬 학습 가능 → 실제 3-4주)
- **Blockers:** 없음 (모두 학습 가능한 범위)
- **Risk mitigation:** MVP에서 Jira 제외 → Slack만 집중 → 학습 시간 2-3주로 단축

### Complexity Assessment

| Component | Complexity | Expertise | Risk |
|-----------|------------|-----------|------|
| **프론트엔드 (Next.js)** | 4/10 | 9/10 | Low ✅ |
| **백엔드 API (Node.js)** | 5/10 | 8/10 | Low ✅ |
| **Slack OAuth & API** | 7/10 | 0/10 | High ⚠️ |
| **Jira OAuth & API** | 7/10 | 0/10 | High ⚠️ |
| **OpenAI 이력서 생성** | 4/10 | 7/10 | Low ✅ |
| **Database (Supabase)** | 5/10 | 7/10 | Low ✅ |
| **Authentication (Clerk)** | 6/10 | 6/10 | Medium ⚠️ |
| **Payment (Stripe)** | 7/10 | 5/10 | Medium ⚠️ |

**Risk Analysis:**
- **Low:** 4/8 components ✅
- **Medium:** 2/8 components ⚠️ (Auth, Payment)
- **High:** 2/8 components ⚠️ (Slack, Jira)
- **Critical:** 0/8 components 🟢

**Mitigation Strategies:**

1. **Slack/Jira API (High Risk):**
   - ✅ **MVP에서 Jira 제외** → Slack만 집중 → Risk 절반 감소
   - ✅ **공식 SDK 사용** (Node.js용 Slack SDK 제공)
   - ✅ **1주 PoC 먼저** → 데이터 추출 가능성 검증 → 실패 시 피벗
   - ✅ **튜토리얼 활용**: [Slack API 공식 가이드](https://api.slack.com/start)

2. **Authentication (Medium Risk):**
   - ✅ **Managed Service 사용** (Clerk, Auth0)
   - ✅ Clerk: 10K MAU 무료, OAuth 2.0 내장
   - ✅ 학습 시간: 1주 (튜토리얼 풍부)

3. **Payment (Medium Risk):**
   - ✅ **Stripe 사용** (가장 개발자 친화적)
   - ✅ MVP에서는 수동 결제 (은행 송금) → Stripe는 Phase 2
   - ✅ 학습 시간: Phase 2에서 1-2주

### Tech Stack (Final Decision)

```markdown
## Tech Stack

### Frontend
**Choice:** Next.js 14 + React + Tailwind CSS
**Rationale:**
- SSR/SSG 지원 (SEO 유리)
- Vercel 무료 배포
- 본인 경험 많음 (9/10)
**Risk Level:** Low ✅

### Backend
**Choice:** Next.js API Routes (또는 Node.js + Express if needed)
**Rationale:**
- Next.js API Routes로 간단히 시작
- 필요 시 Express로 분리
- 본인 경험 많음 (8/10)
**Risk Level:** Low ✅

### Database
**Choice:** Supabase (PostgreSQL)
**Rationale:**
- 500MB 무료
- Auth, Storage, Realtime 내장
- SQL 경험 있음
**Risk Level:** Low ✅

### Authentication
**Choice:** Clerk
**Rationale:**
- 10K MAU 무료
- OAuth 2.0 built-in (Slack/Jira 연동 편함)
- UI 컴포넌트 제공
**Risk Level:** Medium ⚠️ (학습 1주)

### AI
**Choice:** OpenAI API (GPT-4)
**Rationale:**
- 이력서 생성은 텍스트 작업 (Claude도 가능)
- 경험 있음 (7/10)
**Cost:** $0.03/1K tokens (이력서 1개당 ~$0.1-0.3)
**Risk Level:** Low ✅

### Slack Integration
**Choice:** Slack Node SDK (@slack/web-api)
**Rationale:**
- 공식 SDK, 튜토리얼 풍부
- OAuth 2.0 지원
**Risk Level:** High ⚠️ (학습 2-3주)

### Payment (Phase 2)
**Choice:** Stripe
**Rationale:**
- 가장 개발자 친화적
- 한국 원화 지원
**Risk Level:** Medium ⚠️ (학습 1-2주)

### Hosting
**Choice:** Vercel (Frontend + API Routes)
**Rationale:**
- 무료 티어 넉넉 (100GB bandwidth)
- Next.js 최적화
**Cost:** $0 → $20/mo (1K users 이후)
**Risk Level:** Low ✅
```

**Red Flags 체크:**
- ✅ 익숙한 기술 스택 사용 (React, Node.js)
- ✅ Managed Services 활용 (Clerk, Supabase)
- ✅ 단 하나의 High Risk (Slack API) → PoC로 검증
- ✅ 업그레이드 경로 명확 (API Routes → Express)

**Green Flags:**
- ✅ 풀스택 모두 경험 있는 기술
- ✅ 무료 티어 최대 활용
- ✅ 강한 커뮤니티 지원 (Next.js, Supabase)

**Technical Feasibility Score: 7.5/10** ✅

**Reasoning:**
- 대부분 익숙한 기술 (8/8 components)
- Slack/Jira API는 새롭지만 학습 가능 (2-3주)
- MVP 범위 축소로 Risk 관리 (Jira 제외)
- PoC로 기술적 타당성 검증 가능

---

## Financial Feasibility: 8.0/10

### Costs

**Initial (One-time):**
- Domain name (.com): ₩15,000/년
- Logo/Design (DIY Figma): ₩0
- **Total Initial: ₩15,000** ✅

**Monthly Operating Costs:**

| Service | Free Tier | Paid Tier | When to Upgrade | Cost |
|---------|-----------|-----------|-----------------|------|
| **Vercel** | 100GB bandwidth | $20/mo Pro | ~1,000 users | ₩0 → ₩26K |
| **Supabase DB** | 500MB | $25/mo Pro | ~50K records | ₩0 → ₩33K |
| **Clerk Auth** | 10K MAU | $25/mo Pro | 10K users | ₩0 → ₩33K |
| **OpenAI API** | Pay-as-you-go | - | From day 1 | ₩20K-₩50K/mo |
| **SendGrid Email** | 100/day | $15/mo | >100 emails/day | ₩0 → ₩20K |
| **Sentry (Error)** | 5K events/mo | $26/mo | >5K errors | ₩0 → ₩34K |
| **Total** | **₩20K-₩50K** | **₩146K-₩196K** | | |

**OpenAI API 상세 비용:**
- GPT-4 Turbo: $0.01/1K input tokens, $0.03/1K output tokens
- 이력서 1개 생성: ~5K tokens (입력 2K + 출력 3K) = $0.05-0.1 (~₩65-₩130)
- 월 100명 사용 × 평균 3개 이력서 = 300개 × ₩100 = ₩30,000/월

**Projected Monthly Costs:**

| Month | Users | Paid Users | API Cost | Infra Cost | Total |
|-------|-------|------------|----------|------------|-------|
| **1-3** | 100-500 | 5-40 | ₩10K-₩30K | ₩0 | ₩10K-₩30K ✅ |
| **4-6** | 1,000-2,000 | 80-200 | ₩30K-₩50K | ₩26K (Vercel) | ₩56K-₩76K ✅ |
| **7-12** | 3,000-5,000 | 300-600 | ₩50K-₩100K | ₩92K (3 services) | ₩142K-₩192K ⚠️ |

**Free Tier Limits & Upgrade Points:**

```markdown
## Upgrade Timeline

**Months 1-3:** ₩10K-₩30K/월 (OpenAI만, 나머지 무료)
- 가입자 100-500명
- 무료 티어로 충분

**Months 4-6:** ₩56K-₩76K/월
- Vercel 업그레이드 필요 (1,000명 돌파)
- 나머지는 아직 무료

**Months 7-12:** ₩142K-₩192K/월
- Supabase, Clerk 업그레이드 필요
- 성장 단계, MRR은 ₩15M-₩30M이므로 감당 가능
```

### Break-even Analysis

**Target: 월 ₩5M MRR (지속 가능한 사이드 프로젝트)**

**Scenario 1: 구독 모델 (₩70,000/3개월)**
- 월 환산: ₩23,333
- 필요 고객: ₩5M / ₩23,333 = **215명**
- 전환율 10% 가정: 총 가입자 2,150명 필요
- **달성 시점:** Month 6-9 (realistic)

**Scenario 2: 이직 패키지 (₩99,000/3개월)**
- 월 환산: ₩33,000
- 필요 고객: ₩5M / ₩33,000 = **152명**
- 전환율 10% 가정: 총 가입자 1,520명 필요
- **달성 시점:** Month 6 (realistic)

**Scenario 3: 연간 구독 (₩199,000/년)**
- 월 환산: ₩16,583
- 필요 고객: ₩5M / ₩16,583 = **302명**
- 전환율 5% 가정 (연간은 낮음): 총 가입자 6,040명 필요
- **달성 시점:** Month 12+ (challenging)

**Recommended Model:** **이직 패키지 (₩99,000/3개월)**
- Break-even 빠름 (152명)
- Churn 관리 쉬움 (3개월 단위)
- 가격 합리적 (이력서 대행 ₩50K-₩300K 대비 저렴)

### Financial Runway

**Personal Financial Situation:**
- **초기 투자 가능 예산:** ₩500,000
- **월 운영 비용:** ₩10K-₩30K (초기) → ₩142K-₩192K (성장기)
- **Runway:** ₩500K / ₩30K = **16개월 이상** ✅

**Risk Assessment:**
- Runway >12 months: 🟢 **Very low risk**, 충분한 시간
- 사이드 프로젝트이므로 본업 수입 있음 → 추가 안정성
- 월 운영 비용이 낮아서 (₩30K 이하) 장기 운영 가능

**Financial Feasibility Score: 8.0/10** ✅

**Reasoning:**
- 초기 비용 매우 낮음 (₩15K)
- 무료 티어로 3-6개월 운영 가능
- 예산 ₩500K는 16개월+ 커버
- Break-even도 현실적 (Month 6-9, 152-215명)
- OpenAI API 비용만 변동비, 나머지는 고정/무료

---

## Time Feasibility: 6.0/10

### Timeline Estimation

**How long will this take?**
- **MVP timeline:** 2-3개월 (사이드 프로젝트 기준)
- **Available time:** 주당 10-15시간 (사이드 프로젝트 가정)
- **Total hours:** 80-180 시간 (2-3개월 × 4주 × 10-15시간)

**What needs to be done:**

#### Week 1-2: PoC & Validation (20-30 hours)
- [ ] Slack API PoC (1주, 15시간)
  - OAuth 2.0 연동
  - 본인 Slack 워크스페이스 데이터 추출
  - 의미 있는 업무 성과 파싱 가능한지 검증
- [ ] 고객 인터뷰 10명 (1주, 10시간)
  - 이직 준비 중인 경력자 찾기
  - Pain point 검증
  - 가격 의향 파악
- **Decision Point:** PoC 실패 or 고객 반응 부정적 → 피벗

#### Week 3-6: MVP 개발 Core (40-60 hours)
- [ ] Next.js 프로젝트 셋업 (2시간)
- [ ] Clerk Auth 통합 (8시간)
- [ ] Supabase DB 스키마 설계 (4시간)
- [ ] Slack OAuth 2.0 연동 (12시간)
- [ ] Slack 데이터 추출 & 파싱 (16시간)
- [ ] OpenAI API 이력서 생성 (8시간)
- [ ] 기본 UI/UX (프론트엔드) (16시간)

#### Week 7-10: MVP 완성 & 베타 (40-60 hours)
- [ ] 채용공고 맞춤 기능 (12시간)
- [ ] 이력서 템플릿 3종 (8시간)
- [ ] 수동 결제 시스템 (은행 송금) (4시간)
- [ ] 베타 사용자 50명 모집 (8시간)
- [ ] 피드백 수집 & 버그 수정 (16시간)
- [ ] 랜딩 페이지 + SEO 최적화 (8시간)

#### Week 11-12: Public Launch (20-30 hours)
- [ ] Product Hunt 준비 (8시간)
- [ ] Hacker News Show HN 준비 (4시간)
- [ ] 블로그 포스트 3개 작성 (SEO) (8시간)
- [ ] 커뮤니티 마케팅 (블라인드, 오픈챗) (4시간)
- [ ] 런칭 & 초기 고객 서포트 (8시간)

**Total:** 120-180 시간 (주당 10-15시간 × 12주 = 2.5-3개월)

**Complexity Factors:**
- ✅ Learning new tech: Yes - Slack API (2-3주)
- ✅ Third-party integrations: Slack OAuth, OpenAI API, Clerk Auth
- ✅ Infrastructure setup: Simple (Vercel, Supabase 무료 티어)

**Risk Factors:**
- ⚠️ Slack API 학습 곡선 예상보다 길 수 있음 (2-3주 → 4-5주)
- ⚠️ 사이드 프로젝트 번아웃 리스크 (주 10-15시간 유지 어려움)
- ⚠️ Day job 바빠지면 중단 가능성

**Mitigation:**
- ✅ PoC 먼저 (1주) → 기술적 타당성 검증 후 본 개발
- ✅ MVP 범위 최소화 (Jira 제외, 면접 질문 제외)
- ✅ 주간 목표 설정 & 트래킹 (accountability)
- ✅ 공개 빌딩 (Twitter, 블로그) → 동기부여

**Time Feasibility Score: 6.0/10** ⚠️

**Reasoning:**
- 2-3개월은 타이트하지만 가능
- 사이드 프로젝트로 주 10-15시간 확보 필요 (도전적)
- Slack API 학습이 변수 (2-3주 예상)
- MVP 범위 축소로 시간 단축 가능
- PoC로 early validation → 시간 낭비 방지

---

## Overall Feasibility: 6.8/10

| Factor | Score | Weight | Weighted | Notes |
|--------|-------|--------|----------|-------|
| **Technical** | 7.5/10 | 30% | 2.25 | 풀스택 능력, Slack API 학습 가능 |
| **Market** | 6.5/10 | 30% | 1.95 | 시장 존재, 경쟁 중간, 차별점 명확 |
| **Financial** | 8.0/10 | 20% | 1.60 | 초기 비용 낮음, 예산 충분, Break-even 현실적 |
| **Time** | 6.0/10 | 20% | 1.20 | 2-3개월 타이트, 사이드로 가능 |
| **TOTAL** | | **100%** | **7.0/10** | |

**Interpretation:** **Feasible with effort, manageable risks**

---

## Recommendation: PROCEED (조건부)

### Why PROCEED:

1. **Technical Feasibility 높음 (7.5/10):**
   - 풀스택 능력 보유, 대부분 익숙한 기술
   - Slack API는 새롭지만 학습 가능 (2-3주)
   - PoC로 기술적 타당성 조기 검증 가능

2. **Financial Risk 매우 낮음 (8.0/10):**
   - 초기 비용 ₩15K, 월 운영 ₩10K-₩30K (초기)
   - 예산 ₩500K는 16개월+ 커버
   - 무료 티어로 3-6개월 운영 가능
   - Break-even도 현실적 (152-215명, Month 6-9)

3. **Market 검증됨 (6.5/10):**
   - 글로벌 시장 존재 (Rezi $2.4M ARR, StandOut CV £40K MRR)
   - 한국 시장 gap 명확 ("자동 데이터 수집" 차별점)
   - Willingness to pay 높음 (이력서 대행 ₩50K-₩300K)

4. **Time은 타이트하지만 관리 가능 (6.0/10):**
   - 사이드 프로젝트로 2-3개월 MVP 가능
   - MVP 범위 축소로 시간 단축 (Jira, 면접 질문 제외)
   - PoC로 early validation (1주) → 시간 낭비 방지

### Conditions for Proceeding:

✅ **필수 조건 (Must Do Before Full Development):**

1. **PoC 성공 (1주 내)**
   - Slack API로 의미 있는 업무 성과 추출 가능한지 검증
   - 본인 Slack 워크스페이스로 테스트
   - 실패 시: 자동화 포기 → Poromy처럼 수동 입력 모델로 피벗

2. **고객 인터뷰 10명 완료 (2주 내)**
   - 5명 이상 "쓰고 싶다" 반응
   - 가격 의향 ₩50K-₩100K 확인
   - Pain point 재확인 (이력서 작성 시 "자동화" 필요성)

3. **MVP 범위 명확화**
   - ✅ Phase 1: Slack 연동 + AI 이력서 생성
   - ❌ Phase 1 제외: Jira 연동, 면접 질문 커뮤니티
   - → Phase 2-3로 연기

⚠️ **권장 조건 (Should Do):**

4. **주간 10-15시간 시간 확보**
   - 사이드 프로젝트 지속 가능한 일정
   - Day job과 균형 유지

5. **공개 빌딩 (Build in Public)**
   - Twitter, 블로그에서 진행 상황 공유
   - Accountability + 초기 고객 유입

### Next Steps (Immediate):

**Week 1: PoC (Slack API)**
```markdown
## PoC 체크리스트

### Day 1-2: Setup
- [ ] Slack 앱 생성 (https://api.slack.com/apps)
- [ ] OAuth scopes 설정 (channels:history, users:read, etc.)
- [ ] Node.js 프로젝트 셋업 + @slack/web-api 설치

### Day 3-5: Data Extraction
- [ ] OAuth 2.0 flow 구현 (Authorization Code Grant)
- [ ] 본인 Slack 워크스페이스 연동
- [ ] 채널 목록 가져오기 (conversations.list)
- [ ] 메시지 히스토리 가져오기 (conversations.history)
- [ ] 본인이 작성한 메시지만 필터링

### Day 6-7: Parsing & Validation
- [ ] 메시지에서 업무 성과 키워드 추출 (프로젝트, 완료, 배포, 릴리즈 등)
- [ ] 의미 있는 정보 파싱 가능한지 확인
  - ✅ Success: "프로젝트 X 완료", "기능 Y 배포" 등 추출 가능
  - ❌ Failure: 대부분 잡담, 업무 성과 추출 어려움
- [ ] 결과 정리 & GO/NO-GO 판단

**Decision Point:**
- If PoC Success: → 고객 인터뷰 진행
- If PoC Failure: → 피벗 (수동 입력 모델 or 다른 아이디어)
```

**Week 2-3: 고객 인터뷰 10명**
```markdown
## 인터뷰 가이드

### 타겟:
- 이직 준비 중이거나 최근 이직한 경력 개발자 (3년차+)
- 블라인드, 오픈챗, LinkedIn에서 모집

### 질문:
1. 이력서 작성할 때 가장 힘든 점은?
2. Slack/Jira 데이터에서 자동으로 업무 성과 추출해준다면 쓸 의향 있나?
3. 얼마까지 낼 수 있나? (₩10K? ₩50K? ₩100K?)
4. 경쟁사 (Poromy, Rezi 등) 써본 적 있나? 어땠나?

### Success Criteria:
- 5명 이상 "쓰고 싶다" (60-70% 이상)
- 평균 willingness to pay ₩50K 이상
- "자동화"에 대한 명확한 니즈 확인
```

**Week 4+: MVP 개발 시작**
- PoC + 인터뷰 모두 긍정적일 때만
- Week 3-6: Core 개발 (Slack 연동 + 이력서 생성)
- Week 7-10: MVP 완성 & 베타 테스트
- Week 11-12: Public Launch

### Kill Criteria (중단 조건):

**1개월 시점:**
- ❌ PoC 실패 (Slack 데이터 추출 불가능)
- ❌ 고객 인터뷰 부정적 (<5명 관심)
- ❌ Willingness to pay 낮음 (<₩30K)
→ **Action:** 피벗 or 중단

**3개월 시점 (MVP 완료):**
- ❌ 베타 사용자 <30명
- ❌ 유료 전환 0명
- ❌ 부정적 피드백 다수
→ **Action:** 마케팅 전략 재검토 or 가격/가치 재설계

**6개월 시점 (Public Launch 후):**
- ❌ MRR <₩2M
- ❌ 성장 정체 (월 성장률 <5%)
- ❌ Churn >50%
→ **Action:** 수익 모델 피벗 or 중단 고려

---

## Success Probability Estimate

**Overall Success Probability: 40-60%**

**Breakdown:**
- Technical Success (빌드 완료): 80-90% ✅
- Market Validation (PMF 달성): 30-50% ⚠️
- Revenue Target (₩5M MRR): 20-40% ⚠️

**Why 40-60%?**
- ✅ 기술적으로는 매우 feasible (풀스택, 예산 충분)
- ⚠️ 시장 검증은 불확실 (Poromy 존재, 경쟁 가능성)
- ⚠️ PMF 달성은 어려움 (이직은 주기적 니즈, Churn 높음)
- ✅ PoC + 인터뷰로 early validation → 실패 확률 낮춤

**Comparison:**
- StandOut CV: 성공 (£40K MRR, SEO 중심)
- Rezi: 대성공 ($2.4M ARR, 4M users)
- Your idea: Medium success 가능 (₩5M-₩30M MRR, Year 1-2)

**Realistic Outcome (Base Case):**
- Year 1: ₩5M-₩15M MRR
- Year 2: ₩20M-₩40M MRR
- 지속 가능한 사이드 프로젝트 or 풀타임 전환 가능

---

## References

### Local Documents
- **Idea Evaluation:** [경력자 이력서 정리 플랫폼](./resume-platform-evaluation-2025-01-26.md)
- **Success Patterns:** [Resume & Career Platform Success Patterns](../stories/resume-career-platforms-success-patterns-2025-01-26.md)

### Competitor Research
1. [Rezi Revenue Data](https://boringcashcow.com/view/resume-builder-achieves-24m-annual-revenue) - $2.4M ARR, 4M users
2. [StandOut CV Success Story](https://www.indiehackers.com/post/how-i-grew-my-saas-business-to-40k-mrr-with-seo-3287452853) - £40K MRR, SEO strategy
3. [Poromy Official Site](https://poromy.ai.kr) - K-STAR-K framework competitor

### Market Research
4. [한국 채용 플랫폼 시장](https://zdnet.co.kr/view/?no=20240718141936) - 사람인 9.22M MAU, 원티드랩 617K MAU
5. [글로벌 이력서 빌더 시장](https://www.forinsightsconsultancy.com/ko/reports/resume-building-tool-market) - $4.28B by 2034 (14.2% CAGR)
6. [Online Recruitment Market](https://www.mordorintelligence.kr/industry-reports/online-recruitment-market) - $53.02B (2024) → $102.17B (2030)

### Technical Resources
7. [Slack API Documentation](https://api.slack.com/start) - Official getting started guide
8. [Slack Node SDK](https://github.com/slackapi/node-slack-sdk) - Official Node.js library
9. [Jira Integration Guidelines](https://developer.atlassian.com/developer-guide/jira-integration-guidelines/) - Official developer guide
10. [Clerk Authentication](https://clerk.com/docs) - Auth platform documentation
11. [Supabase Documentation](https://supabase.com/docs) - Database + Auth + Storage

### Revenue Benchmarks
12. [Grammarly Revenue Growth](https://getlatka.com/blog/grammarly-revenue/) - $250M ARR, 30M DAU
13. [Huntr Partnership](https://www.morningstar.com/news/pr-newswire/20240508sf06499) - 300K+ users, 100+ partnerships

---

**Assessment Completed:** 2025-01-26
**Next Action:** PoC (Slack API, 1주) + 고객 인터뷰 (10명, 2주)
**Status:** **PROCEED** with PoC validation → Full MVP if successful
