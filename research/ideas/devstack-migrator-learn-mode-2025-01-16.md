---
title: DevStack Migrator + Learn Mode
generated-date: 2025-01-16
type: Business Idea
status: Generated
score: 9.0
recommendation: GO
base-idea: devstack-migrator-2024-12-15
enhancement: tech-transition-learning
success-patterns:
  - scratch-your-own-itch
  - ship-in-one-week
  - premium-pricing-from-day-one
  - developer-tools
expected-timeline:
  mvp: 5-7 days (CRA → Vite)
  phase2: +5-7 days (React Class → Hooks)
  phase3: +3-5 days (Jest → Vitest)
  first-revenue: 1-2 weeks
  target-mrr: $2K MRR in 3-6 months
mvp-migration: CRA → Vite
tags: [code-migration, ai-tools, developer-tools, automation, learning, education]
---

# DevStack Migrator + Learn Mode

## Quick Summary

**One-Liner:** AI 기반 코드 마이그레이션 도구 + 변환 과정을 설명해주는 학습 모드 (마이그레이션하면서 새 기술을 배운다)

**핵심 차별화:** 단순히 코드를 변환하는 것이 아니라, "왜 이렇게 변환되는지" 설명하여 개발자가 새로운 패턴을 자연스럽게 학습

**Success Pattern Applied:**
- Scratch Your Own Itch (80% success rate)
- Ship in One Week (Very high success rate)
- Premium Pricing from Day One (High success rate)
- Developer Tools (High success rate)

**Expected Timeline:**
- **Phase 1 MVP (CRA → Vite):** 5-7 days
- Phase 2 (+ React Hooks): +5-7 days
- Phase 3 (+ Jest → Vitest): +3-5 days
- First Revenue: 1-2 weeks
- $2K MRR: 3-6 months

---

## Problem & Solution

### The Problem

**Who:** 중급-시니어 개발자, 기술 리드, 개발 에이전시

**What:** 두 가지 문제를 동시에 겪음
1. 레거시 코드베이스 마이그레이션에 2주-2개월 소요
2. 새로운 기술/패턴을 제대로 이해하지 못한 채 변환만 함

**Current Pain:**

| 문제 | 현재 해결책 | 한계 |
|------|------------|------|
| 코드 마이그레이션 | 수동 작업 or Codemod | 2주+, $10K+ 비용, 지루함 |
| 새 기술 학습 | 문서/강의 따로 학습 | 실제 코드와 분리, 비효율적 |
| 변환 이유 이해 | ChatGPT에 하나씩 질문 | 맥락 없음, 시간 소모 |

**Why It Hurts:**
- **시간:** 2-3주 시니어 개발자 시간 ($10,000-$15,000)
- **학습 기회 손실:** 마이그레이션은 했지만 새 패턴을 이해 못함 → 나중에 같은 실수 반복
- **기회비용:** 마이그레이션 + 학습 따로 하면 2배 시간

### The Solution

**코드 마이그레이션 + 인라인 학습 설명을 결합한 AI 도구**

```bash
npx devstack-migrate react-class-to-hooks ./src --learn
```

**Core Features:**

1. **자동 코드 변환** (기존 DevStack Migrator)
   - React Class → Hooks
   - Vue 2 → Vue 3
   - JavaScript → TypeScript
   - Express → Next.js API Routes

2. **Learn Mode** (새로운 차별화 기능)
   - 각 변환에 대한 인라인 설명 생성
   - "왜 componentDidMount가 useEffect로 변환되는지"
   - 변환 전/후 비교 + 개념 설명
   - 개발자의 기존 코드 맥락에서 설명

**Value Proposition:**
> "2주 걸리는 마이그레이션을 1-3일로 단축하면서, 동시에 새로운 패턴을 마스터하세요"

---

## Core Innovation: Learn Mode

### 기존 도구와의 차이

| 도구 | 코드 변환 | 학습 설명 | 프로젝트 맥락 |
|------|---------|---------|-------------|
| **Codemod** | ✅ | ❌ | ✅ |
| **ChatGPT** | ❌ (파일별) | ✅ (질문시) | ❌ |
| **Learn X in Y Minutes** | ❌ | ✅ (일반적) | ❌ |
| **DevStack Migrator + Learn** | ✅ | ✅ (자동) | ✅ |

### Learn Mode 동작 방식

**Input (기존 React Class 컴포넌트):**
```jsx
class UserProfile extends Component {
  state = { user: null, loading: true };

  componentDidMount() {
    this.fetchUser();
  }

  componentDidUpdate(prevProps) {
    if (prevProps.userId !== this.props.userId) {
      this.fetchUser();
    }
  }

  fetchUser = async () => {
    const user = await api.getUser(this.props.userId);
    this.setState({ user, loading: false });
  }

  render() { ... }
}
```

**Output (변환된 코드 + 학습 설명):**
```jsx
// 📚 LEARN: Class → Function Component 변환
// Class 컴포넌트는 함수 컴포넌트로 변환됩니다.
// React 18+에서는 함수 컴포넌트가 권장되며, 더 간결하고 테스트하기 쉽습니다.

function UserProfile({ userId }) {
  // 📚 LEARN: this.state → useState Hook
  // Class의 state 객체는 개별 useState 훅으로 분리됩니다.
  // 각 상태를 독립적으로 관리하면 불필요한 리렌더링을 줄일 수 있습니다.
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // 📚 LEARN: componentDidMount + componentDidUpdate → useEffect
  // 두 라이프사이클 메서드가 하나의 useEffect로 통합됩니다.
  // 의존성 배열 [userId]는 userId가 변경될 때만 effect가 실행되게 합니다.
  // 이전: componentDidMount (마운트시) + componentDidUpdate (업데이트시)
  // 이후: useEffect with deps (마운트 + userId 변경시)
  useEffect(() => {
    const fetchUser = async () => {
      const userData = await api.getUser(userId);
      setUser(userData);
      setLoading(false);
    };
    fetchUser();
  }, [userId]);

  // 📚 LEARN: this.props → 함수 파라미터
  // Class에서 this.props로 접근하던 것이 함수의 파라미터로 직접 전달됩니다.
  // 구조분해 할당으로 필요한 props만 명시적으로 받습니다.

  return ...;
}
```

### 학습 콘텐츠 유형

1. **인라인 주석 (기본)**
   - 코드 내 `// 📚 LEARN:` 주석
   - 변환 직후 바로 이해 가능
   - 코드 리뷰 시 팀원도 학습

2. **마이그레이션 리포트 (Pro)**
   - 전체 프로젝트 변환 요약
   - 패턴별 설명 문서 생성
   - 팀 교육 자료로 활용 가능

3. **인터랙티브 비교 (Enterprise)**
   - 웹 대시보드에서 before/after 비교
   - 클릭하면 상세 설명
   - 팀별 학습 진도 추적

---

## Market Analysis

### Target Customer

**Primary:** 시니어 개발자 + 기술 리드
- 마이그레이션 책임자
- 새 기술 도입 결정권자
- 팀 교육도 고려해야 함

**Secondary:** 개발 에이전시 + 컨설팅
- 클라이언트 프로젝트 마이그레이션
- 마이그레이션 후 인수인계 시 설명 필요
- Learn Mode = 클라이언트에게 교육 자료 제공

**Tertiary:** 중급 개발자
- 기술 전환 필요 (회사 요구 or 이직 준비)
- 실제 코드로 배우고 싶음
- 이론만 있는 강의에 질림

### Market Validation

**기존 DevStack Migrator 검증 (2024-12-15):**
- AI Code Migration Market: $1.43B (2024) → $13.74B (2033)
- Codemod: $49.3M 매출, 500+ 고객
- Google: 내부적으로 AI 마이그레이션 사용 ("수백 명의 엔지니어 시간 절약")

**Learn Mode 추가 가치:**
- 개발자 교육 시장: $50B+ (2025)
- "Python for JS developers" 등 전환 학습 수요 검증됨
- LinkedIn Learning, Pluralsight 등 유료 학습 의향 존재

**차별화 포인트:**
- Codemod: 변환만, 설명 없음 (Enterprise $10K+)
- ChatGPT: 파일별만, 프로젝트 맥락 없음
- 강의/문서: 실제 코드 맥락 없음
- **DevStack + Learn: 변환 + 설명 + 프로젝트 맥락 = 유일무이**

### Competition Analysis

| 경쟁사 | 변환 | 학습 | 가격 | 우리 우위 |
|--------|------|------|------|----------|
| Codemod | ✅ | ❌ | Enterprise | 학습 모드 + 인디 가격 |
| Moderne | ✅ | ❌ | Enterprise | 학습 모드 + 인디 가격 |
| ChatGPT | △ | △ | $20/mo | 프로젝트 전체 맥락 |
| Learn X in Y Minutes | ❌ | ✅ | 무료 | 실제 코드 변환 |
| Pluralsight | ❌ | ✅ | $45/mo | 내 코드로 학습 |

**Market Gap:**
> "실제 내 코드를 변환하면서 새로운 패턴을 배울 수 있는 도구가 없다"

---

## Migration Options Analysis

### 마이그레이션 유형별 비교

8가지 주요 마이그레이션 옵션을 조사하여 수요, 자동화 난이도, 경쟁 상황을 분석했습니다.

| 순위 | 마이그레이션 | 수요 | 자동화 난이도 | 경쟁 | MVP 시간 | **총점** |
|------|-------------|------|--------------|------|----------|---------|
| 🥇 | **CRA → Vite** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 5-7일 | **9.0** |
| 🥈 | **React Class → Hooks** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 7-10일 | **8.5** |
| 🥉 | **JavaScript → TypeScript** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 10-14일 | **8.0** |
| 4 | **Jest → Vitest** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 3-5일 | **8.0** |
| 5 | **Vue 2 → Vue 3** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 10-14일 | **7.5** |
| 6 | **Redux → Zustand** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 5-7일 | **7.0** |
| 7 | **AngularJS → Angular** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | 21일+ | **6.5** |
| 8 | **Express → Next.js** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | 7-10일 | **6.5** |

### 🥇 1위: CRA → Vite (MVP 권장)

**왜 최고인가:**
- [CRA 공식 Sunset (2025년 2월)](https://react.dev/blog/2025/02/14/sunsetting-create-react-app) → **강제 마이그레이션 수요**
- [Vite 주간 다운로드 1500만+](https://www.tweag.io/blog/2024-12-19-cra-to-vite/), State of JS 2024 #1 Most Adopted
- 빌드 시간 **3.2배 빠름**, 개발 서버 **12.9배 빠름**
- 마이그레이션 상대적으로 간단 (설정 파일 + 의존성 변경)

**Learn Mode 가치:**
- Webpack → Vite 개념 설명
- ES Modules, HMR 차이점
- 환경 변수, 플러그인 시스템 학습

**시장 증거:**
- "2025년 React 개발자 논의 최다 주제" - [Code Ki Pathshala](https://www.codekipathshala.com/switching-to-vite-from-cra-2025/)
- 기존 CRA 프로젝트 수백만 개 존재

### 🥈 2위: React Class → Hooks

**왜 좋은가:**
- [React 19 (2024년 12월)](https://react.dev/blog/2024/12/05/react-19) - Server Components, Compiler 등 Hooks 기반
- 레거시 코드베이스 다수 존재 (2018-2020년 작성)
- 코드 26줄 → 15줄 등 **40-50% 감소**

**Learn Mode 가치:**
- componentDidMount → useEffect 설명
- 라이프사이클 → Hooks 매핑
- 상태 관리 패러다임 전환 학습

**시장 증거:**
- Reddit r/reactjs에서 "migration" 관련 질문 지속적
- [CircleCI](https://circleci.com/blog/class-components-to-react-hooks/), [Medium](https://medium.com/@ignatovich.dm/from-class-components-to-hooks-a-migration-strategy-28fe50b69669) 등 가이드 다수

### 🥉 3위: JavaScript → TypeScript

**왜 좋은가:**
- [38.5% 개발자가 TypeScript 사용](https://jeffbruchado.com.br/en/blog/typescript-dominance-2025-javascript-migration) (Stack Overflow 2024)
- [2020년 이후 기업 채택 400%+ 성장](https://www.index.dev/blog/javascript-vs-typescript-popularity)
- 버그 15-30% 감소, 연봉 10-15% 프리미엄

**Learn Mode 가치:**
- 타입 시스템 기초 → 고급
- 점진적 마이그레이션 전략
- 제네릭, 유틸리티 타입 설명

**주의:** 복잡도가 높음 (any → strict 타입 추론)

### 4위: Jest → Vitest

**왜 좋은가:**
- [Vitest 4 출시 (2025년 10월)](https://blog.logrocket.com/vitest-adoption-guide/) - 성숙한 대안
- 테스트 실행 **30-70% 빠름**
- ESM, TypeScript 네이티브 지원
- 자동 마이그레이션 codemod 존재

**Learn Mode 가치:**
- jest.fn() → vi.fn() 매핑
- Vite 생태계 통합 이해

**장점:** MVP가 가장 빠름 (3-5일), CRA→Vite와 시너지

### 5위: Vue 2 → Vue 3

**왜 좋은가:**
- Vue 2 EOL 이후에도 [35%가 여전히 사용 중](https://www.monterail.com/stateofvue) (2024년 11월)
- 번들 23% 감소, 성능 향상

**문제점:**
- [마이그레이션에 수개월-2년 소요](https://www.monterail.com/blog/vue-3-migration-case-study)
- @vue/compat로 하이브리드 필요
- Nuxt 2 → Nuxt 3 모듈 호환성 문제

### 6위: Redux → Zustand + React Query

**왜 좋은가:**
- "2025년 Redux 이탈 트렌드" - [Medium](https://medium.com/@mernstackdevbykevin/state-management-in-2025-why-developers-are-ditching-redux-for-zustand-and-react-query-b5ecad4ff497)
- 보일러플레이트 대폭 감소

**문제점:**
- Redux 대형 프로젝트는 여전히 유효
- 마이그레이션 필요성이 "nice-to-have"

### 7위: AngularJS → Angular

**왜 좋은가:**
- [주간 41.9만 다운로드](https://www.thefrontendcompany.com/posts/angularjs-to-angular-migration) (EOL 3년 후에도!)

**문제점:**
- 완전히 다른 프레임워크 (재작성 수준)
- 엔터프라이즈 규모 → 1년+ 소요
- 자동화 매우 어려움

### 8위: Express → Next.js

**문제점:**
- 완전히 다른 아키텍처 (REST API vs Full-stack)
- 대부분 "마이그레이션"보다 "새로 구축" 선택

---

### 제품 로드맵 (권장)

```
Phase 1 (MVP): CRA → Vite
├── 이유: 강제 수요 (CRA Sunset), 간단, 높은 ROI
├── 시간: 5-7일
└── 출시 후 피드백 수집

Phase 2: React Class → Hooks
├── 이유: Learn Mode 가치 가장 높음
├── 시간: +5-7일
└── Phase 1과 번들 가능

Phase 3: Jest → Vitest
├── 이유: Vite 생태계 시너지
├── 시간: +3-5일
└── CRA→Vite 고객 upsell

Phase 4: JavaScript → TypeScript
├── 이유: 시장 규모 가장 큼
├── 시간: +7-10일
└── 복잡도 높아 나중에
```

### 번들 전략

**번들 A: "React Modernization Pack" (권장)**
- CRA → Vite
- React Class → Hooks
- Jest → Vitest
- **가격: $499** (개별 $249 × 3 = $747 대비 33% 할인)

**번들 B: "TypeScript Upgrade Pack"**
- JavaScript → TypeScript
- 타입 검사 점진적 도입
- **가격: $349**

---

## Product Specification

### MVP Scope (Build in 5-7 days)

**Core Features (MUST HAVE):**

1. **Project Analysis Engine**
   - package.json, 설정 파일 스캔
   - CRA 의존성 감지

2. **AI-Powered Config Transformation**
   - Claude API 통합
   - CRA → Vite 설정 변환

3. **Learn Mode** (핵심 차별화)
   - 각 변환에 인라인 설명 생성
   - `--learn` 플래그로 활성화
   - "왜 Webpack 대신 Vite인지" 설명

4. **Migration Report**
   - 변환 요약 + 학습 포인트 문서 생성
   - Markdown 형식으로 출력

**MVP Scope (Phase 1):**
- **CRA → Vite ONLY** (강제 수요, CRA Sunset)
- CLI 도구 (GUI 없음)
- 인라인 주석 + 기본 리포트

**Phase 2 (출시 후 1-2주):**
- React Class → Hooks 추가
- 번들 옵션 제공

**Phase 3 (출시 후 3-4주):**
- Jest → Vitest 추가 (Vite 시너지)

**Excluded from MVP:**
- ❌ Vue, TypeScript 지원 (Phase 4+)
- ❌ 웹 대시보드 (v3에서)
- ❌ 팀 협업 기능
- ❌ 인터랙티브 학습

### Technical Requirements

**Stack:**
- Node.js CLI (Commander.js)
- Babel/TypeScript Compiler API (AST 파싱)
- Claude API (변환 + 설명 생성)

**Learn Mode 구현:**
```javascript
// Claude API 프롬프트 예시
const prompt = `
당신은 시니어 React 개발자입니다.
다음 Class 컴포넌트를 Hooks로 변환하고,
각 변환에 대해 "// 📚 LEARN:" 주석으로 설명을 추가하세요.

설명은 다음을 포함해야 합니다:
1. 무엇이 변환되었는지
2. 왜 이렇게 변환되는지
3. 새로운 패턴의 장점

코드:
${sourceCode}
`;
```

---

## Business Model

### Pricing Tiers

| Tier | 가격 | 변환 | Learn Mode | 타겟 |
|------|------|------|-----------|------|
| **Starter** | $249 | 1 프로젝트 | 인라인 주석 | 개인 개발자 |
| **Pro** | $599 | 무제한 | + 리포트 생성 | 프리랜서, 소규모 팀 |
| **Team** | $1,499 | 무제한 | + 팀 교육 자료 | 에이전시, 스타트업 |
| **Enterprise** | $4,999 | 무제한 | + 커스텀 + 지원 | 대기업 |

**가격 정당화:**
- 수동 마이그레이션: $10,000-50,000 (2-8주)
- 팀 교육/온보딩: $5,000+ (외부 교육)
- DevStack + Learn: $249-599 = **ROI 20-100X**

**Learn Mode 프리미엄:**
- 기존 DevStack Migrator: $199-499
- Learn Mode 추가: +$50 (약 25% 프리미엄)
- 교육 가치 = 추가 비용 정당화

### Revenue Projections

| 월 | 고객 수 | 평균 가격 | 월 매출 | 누적 매출 |
|----|---------|----------|---------|----------|
| 1 | 5 | $349 | $1,745 | $1,745 |
| 3 | 25 | $399 | $9,975 | $20,000 |
| 6 | 50 | $449 | $22,450 | $80,000 |
| 12 | 100 | $499 | $49,900 | $250,000 |

**Growth Drivers:**
- Learn Mode = 차별화 → 더 높은 전환율
- 팀 라이선스 = 더 높은 ARPU
- 교육 콘텐츠 = SEO + 바이럴

---

## Go-to-Market Strategy

### Launch Message

**Before (기존 DevStack Migrator):**
> "2주 걸리는 마이그레이션을 1-3일로"

**After (+ Learn Mode):**
> "마이그레이션하면서 새로운 기술을 마스터하세요.
> 코드 변환 + 패턴 학습을 한 번에."

### Distribution Channels

1. **Product Hunt** - "AI Migration Tool with Built-in Learning"
2. **Hacker News** - "Show HN: Migrate your code and learn the new patterns"
3. **Reddit** - r/reactjs, r/webdev, r/learnprogramming
4. **Twitter** - #buildinpublic, 변환 예시 공유
5. **SEO** - "React class to hooks migration", "learn hooks from your code"

### Content Strategy

Learn Mode를 활용한 콘텐츠 마케팅:

1. **블로그 시리즈:** "React Hooks 패턴 10가지 (실제 마이그레이션 예시)"
2. **트위터 스레드:** 변환 전/후 + 설명 스크린샷
3. **YouTube:** "Watch AI migrate and explain 1000 lines of code"
4. **무료 샘플:** 10개 컴포넌트 무료 변환 + 설명 → 리드 생성

---

## Success Metrics

### Month 1 Goals
- [ ] MVP 출시 (React Class → Hooks + Learn Mode)
- [ ] 10 베타 유저 피드백
- [ ] 첫 유료 고객 5명
- **Success Metric:** Learn Mode 만족도 > 4/5

### Month 3 Goals
- [ ] 50 유료 고객
- [ ] $15K 누적 매출
- [ ] Vue 2 → 3 지원 추가
- **Success Metric:** 30% 고객이 Learn Mode 때문에 선택

### Month 6 Goals
- [ ] 150 유료 고객
- [ ] $80K 누적 매출
- [ ] Team 라이선스 10개+
- **Success Metric:** 학습 콘텐츠가 SEO 트래픽 30% 기여

---

## Risk Analysis

### Technical Risks

**Risk 1: Learn Mode 설명 품질**
- Probability: Medium
- Impact: High
- Mitigation:
  - Claude API 프롬프트 엔지니어링에 집중
  - 베타 유저 피드백으로 반복 개선
  - 설명 템플릿 + 예시 제공

**Risk 2: 설명이 너무 길어 코드 가독성 저하**
- Probability: Medium
- Impact: Medium
- Mitigation:
  - `--learn=minimal` 옵션 (간단한 설명만)
  - 별도 리포트 파일로 분리 옵션
  - 설명 접기/펼치기 (IDE 플러그인 v2)

### Market Risks

**Risk 1: "학습은 무료여야 한다" 인식**
- Probability: Medium
- Impact: Medium
- Mitigation:
  - 핵심 가치는 "마이그레이션"임을 강조
  - Learn Mode는 "bonus" 포지셔닝
  - 마이그레이션 ROI로 가격 정당화

---

## Comparison: Before vs After Enhancement

| 항목 | DevStack Migrator (기존) | + Learn Mode (향상) |
|------|------------------------|-------------------|
| 점수 | 9.2/10 | 9.0/10 (복잡도 증가) |
| 차별화 | 인디 가격 유일 | 학습 기능 유일 |
| 가격 | $199-499 | $249-599 (+25%) |
| 타겟 | 마이그레이션 필요한 개발자 | + 기술 전환 학습 원하는 개발자 |
| 마케팅 메시지 | "빠른 마이그레이션" | "마이그레이션하며 배우기" |
| 콘텐츠 잠재력 | 낮음 | 높음 (학습 콘텐츠) |
| MVP 일정 | 7-10일 | 10-14일 (+50%) |

---

## Next Steps

**Phase 1: CRA → Vite MVP (5-7일)**

1. **Day 1-2:** 프로젝트 분석 엔진
   - CLI 셋업 (Commander.js)
   - package.json, 설정 파일 파싱
   - CRA 의존성 감지 로직

2. **Day 3-4:** 변환 + Learn Mode
   - Claude API 연동
   - CRA → Vite 설정 변환
   - Learn Mode 프롬프트 엔지니어링
   - 인라인 설명 생성

3. **Day 5-6:** 테스트 & 폴리시
   - 실제 CRA 프로젝트 3개로 테스트
   - 설명 품질 개선
   - 문서화, 데모 비디오

4. **Day 7:** 런칭 준비
   - 랜딩 페이지
   - 결제 연동 (Gumroad)
   - Product Hunt, Reddit r/reactjs 런칭

**Phase 2: React Class → Hooks (+5-7일)**

5. **Week 2:** Hooks 마이그레이션 추가
   - AST 파싱 (Babel)
   - Class → Hooks 변환 로직
   - Learn Mode 확장 (라이프사이클 설명)
   - 번들 옵션 출시

**Phase 3: Jest → Vitest (+3-5일)**

6. **Week 3:** 테스트 마이그레이션 추가
   - Jest → Vitest 변환
   - "React Modernization Pack" 번들 출시

---

## References

### Base Documents
- [DevStack Migrator 원본 아이디어](./devstack-migrator-2024-12-15.md)
- [DevStack Migrator Feasibility](./devstack-migrator-feasibility-2024-12-15.md)
- [Tech Transition Tool 평가](../evaluations/tech-transition-tool-2025-01-16.md)

### Market Research
- [AI Code Migration Market - $13.74B by 2033](https://dataintelo.com/report/code-migration-assistant-ai-market)
- [Codemod - $49.3M Revenue](https://getlatka.com/companies/tango-1)
- [Programming Language Learning Market - $50B](https://www.verifiedmarketreports.com/product/programming-language-learning-platform-market/)

### Competitors
- [Codemod](https://codemod.com/) - Enterprise 마이그레이션
- [Learn X in Y Minutes](https://learnxinyminutes.com/) - 무료 학습
- [Exercism](https://exercism.org/) - 실습 기반 학습

### Migration Options Research
- [CRA Sunset Announcement (2025년 2월)](https://react.dev/blog/2025/02/14/sunsetting-create-react-app)
- [CRA to Vite Migration Guide - Tweag](https://www.tweag.io/blog/2024-12-19-cra-to-vite/)
- [Why Everyone is Switching to Vite](https://www.codekipathshala.com/switching-to-vite-from-cra-2025/)
- [React Class to Hooks Migration - CircleCI](https://circleci.com/blog/class-components-to-react-hooks/)
- [TypeScript Adoption 2025](https://jeffbruchado.com.br/en/blog/typescript-dominance-2025-javascript-migration)
- [State of Vue.js 2025 - Vue 2 Usage](https://www.monterail.com/stateofvue)
- [Jest to Vitest Migration - LogRocket](https://blog.logrocket.com/vitest-adoption-guide/)
- [Redux to Zustand Trend](https://medium.com/@mernstackdevbykevin/state-management-in-2025-why-developers-are-ditching-redux-for-zustand-and-react-query-b5ecad4ff497)
- [AngularJS Migration Challenges](https://www.thefrontendcompany.com/posts/angularjs-to-angular-migration)

---

**Status Log:**
- 2025-01-16: Option A (결합 아이디어) 문서 생성
- 2025-01-16: 마이그레이션 옵션 분석 추가 (8가지 비교)
- 2025-01-16: MVP를 CRA → Vite로 변경 (강제 수요)
- 2025-01-16: 제품 로드맵 및 번들 전략 추가
- Base: devstack-migrator-2024-12-15 + tech-transition-tool-2025-01-16
