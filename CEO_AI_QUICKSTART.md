
# CEO AI - Quick Start Guide

1인/소수 개발자를 위한 비즈니스 분석 Multi-Agent 시스템

## 🎯 핵심 철학

> **성공한 사람의 아이템을 카피하지 말고,
> 성공한 사람의 성공하는 방식을 카피해서
> 내 아이템에 적용하라**

## ⚡ 5분 시작하기

### 1단계: 시스템 확인

프로젝트에 다음 파일들이 있는지 확인:
```
.claude/skills/
├── success-formula-analyzer/SKILL.md  ✅
├── business-idea-evaluator/SKILL.md   ✅
├── feasibility-checker/SKILL.md       ✅
├── business-orchestrator/SKILL.md     ✅
└── skill-rules.json                   ✅
```

### 2단계: 첫 분석 실행

Claude Code에서 다음 중 하나를 입력:

**Option A: 완전 분석 (권장)**
```
완전한 비즈니스 분석 실행:

아이디어: [당신의 아이디어를 한 문장으로]
타겟: [누가 사용하나요?]
배경:
  - 스킬: [당신이 할 수 있는 것]
  - 시간: [주당 몇 시간?]
  - 예산: [얼마나 있나요?]
```

**Option B: 성공 사례 학습**
```
[성공한 제품명]이 어떻게 성공했는지 분석하고
내 아이디어에 적용해줘

내 아이디어: [간단 설명]
```

**Option C: 빠른 평가**
```
이 아이디어 평가해줘:

문제: [해결할 문제]
솔루션: [당신의 솔루션]
타겟: [대상 고객]
```

### 3단계: 결과 받기

10-15분 후, 다음을 받게 됩니다:

```markdown
# 비즈니스 분석 보고서

## Executive Summary
- 최종 점수: 7.2/10
- 추천: GO ✅
- 주요 강점: [3가지]
- 주요 리스크: [3가지]

## 상세 분석
[3개 Agent의 분석 결과]

## 액션 플랜
- Phase 0: 준비 (1-2주)
- Phase 1: MVP (3-10주)
- Phase 2: Beta (11-16주)
- Phase 3: Launch (17주)

## Decision Points
- 1개월: [체크포인트]
- 3개월: [체크포인트]
- 6개월: [체크포인트]
```

## 🤖 Agent 소개

### 0️⃣ Success Story Researcher (NEW!)
**하는 일:** 웹에서 성공 스토리 검색 → 제작 과정 추출 → 체계적으로 정리

**핵심 차별점:**
- 단순히 "성공했다"가 아니라 **"어떻게 만들었는지"** 집중
- 효과적인 검색 쿼리 패턴 제공
- Indie Hackers, Reddit, Twitter 등 tier별 소스 가이드

**예시:**
```
입력: "SaaS 분야에서 $10K MRR 달성한 스토리 3개 찾아줘"

Claude:
🔍 검색 중...
  ├─ Indie Hackers 검색
  ├─ Reddit r/SaaS 검색
  └─ Twitter #buildinpublic 검색

📊 발견한 스토리:

1. ConvertKit ($10K → $29M ARR)
   - MVP: 6개월
   - 초기 전략: Personal outreach to bloggers
   - 성장 tactic: Free migration service
   - Timeline: [상세 마일스톤]

2. Gumroad ($0 → $10K in 3 months)
   - [Journey 상세]

3. Bannerbear ($0 → $10K MRR in 18 months)
   - [Journey 상세]

공통 패턴:
✅ 모두 문제를 직접 경험
✅ 3개월 이내 MVP 출시
✅ Community-first 성장
```

**언제 사용:**
- 성공 사례를 찾고 싶을 때 (막연한 검색 대신 체계적으로)
- 특정 제품이 어떻게 만들어졌는지 알고 싶을 때
- 여러 사례에서 공통 패턴을 찾고 싶을 때

### 1️⃣ Success Formula Analyzer
**하는 일:** 성공한 사람들 분석 → 패턴 추출 → 당신에게 적용

**예시:**
```
입력: "Gumroad 성공 패턴 분석"

출력:
✅ Problem-first: 자신의 문제 해결
✅ Simple MVP: 주말에 출시
✅ Community-first: Twitter로 성장
✅ Transparent: Build in public

당신에게 적용하면:
1. [구체적 행동 1]
2. [구체적 행동 2]
```

**참고:**
- [Gumroad](https://gumroad.com)
- [Sahil Lavingia Blog](https://sahillavingia.com/)
- [Indie Hackers Interview](https://www.indiehackers.com/podcast/114-sahil-lavingia-of-gumroad)

**Workflow:** success-story-researcher로 먼저 스토리 수집 → 그 다음 패턴 분석

### 2️⃣ Business Idea Evaluator
**하는 일:** 아이디어를 8개 차원에서 평가 (80점 만점)

**평가 항목:**
- 🔥 Problem Intensity (얼마나 아픈 문제?)
- 📊 Market Size (시장이 얼마나 큰가?)
- ⚔️ Competition (경쟁이 얼마나 치열한가?)
- 💰 Monetization (돈 버는 게 명확한가?)
- ✨ Differentiation (얼마나 다른가?)
- ⏱️ Time to Market (얼마나 빨리 만들까?)
- 👤 Solo Fit (혼자 가능한가?)
- 🎯 Skills Match (내 스킬이 맞나?)

**점수 해석:**
- 56-80점: 강력 추천 ✅
- 41-55점: 괜찮음 🟢
- 26-40점: 개선 필요 🟡
- 0-25점: 재고 권장 🔴

### 3️⃣ Feasibility Checker
**하는 일:** 당신이 **실제로** 만들 수 있는지 검증

**체크 항목:**
1. **기술적:** 스킬 갭, 복잡도, 학습 시간
2. **재정적:** 초기 비용, 월 비용, Runway
3. **시간적:** 가용 시간, 개발 기간, 기회 비용

**결과 예시:**
```
Technical: 6/10 (Node.js 학습 필요)
Financial: 8/10 (Free tier로 시작 가능)
Time: 7/10 (주말 작업 3개월)

종합: 7.0/10 → 실행 가능 ✅

제안:
- MongoDB 대신 Supabase 사용 (학습 시간 단축)
- AI 직접 구현 대신 OpenAI API 사용
- 예상 타임라인: 3개월 → 2개월로 단축
```

### 4️⃣ Business Orchestrator
**하는 일:** 위 3개를 조율 + 종합 보고서 생성

**제공하는 것:**
- ✅ 통합 점수 및 추천
- ✅ 단계별 액션 플랜
- ✅ 리스크 & 대응 전략
- ✅ Kill criteria (언제 그만둘지)

## 📖 실전 예시

### 예시 1: 아이디어 처음 떠올렸을 때

```
당신: "개발자용 스크린샷 자동 정리 앱 만들고 싶어"

Claude (orchestrator 실행):

📊 Idea Score: 52/80
  - Problem: 6/10 (moderate pain)
  - Market: 7/10 (developers + designers)
  - Competition: 5/10 (some exist but not great)
  - Monetization: 7/10 ($5-10/month clear)

🎯 Success Pattern: "Problem-first builder"
  - Similar: CleanShot X, Zappy
  - Key tactic: Free tier + pro features
  - Timeline: 2-3 months to revenue

✅ Feasibility: 7.8/10
  - Technical: 8/10 (Electron + simple backend)
  - Financial: 9/10 (<$50/month to run)
  - Time: 7/10 (8 weeks full-time)

🎯 RECOMMENDATION: GO with modifications

Action Plan:
Week 1-2: Basic screenshot capture
Week 3-4: Auto-tagging (simple keywords)
Week 5-6: Search functionality
Week 7-8: Polish + landing page
Week 9: Launch on Product Hunt
```

### 예시 2: 기존 아이디어 검증

```
당신: "블로그 글을 SNS 포스트로 자동 변환하는 SaaS"

Claude:
❌ Score: 38/80 - ITERATE 필요

문제점:
- Competition 2/10 (Buffer, Hootsuite 등 강력)
- Differentiation 4/10 (명확하지 않음)

개선 제안:
1. 더 좁은 니치 타겟 (예: 개발자 블로그 → Dev.to)
2. AI 기반 자동 해시태그 (차별화)
3. Tech 업계 특화 (시장 축소, 경쟁 회피)

수정 후 재평가:
"개발 블로그를 Dev.to + Twitter 개발자 포스트로
자동 변환 + 적절한 해시태그 자동 생성"

Score: 58/80 → GO ✅
```

### 예시 3: 웹에서 성공 스토리 리서치 (NEW!)

```
당신: "개발자 도구 카테고리에서 성공한 indie product 찾아줘.
      특히 어떻게 만들었는지 과정이 상세한 걸로"

Claude (success-story-researcher):

🔍 웹 리서치 시작...

검색 전략:
✓ Indie Hackers: "developer tools" interview
✓ Reddit: site:reddit.com/r/SideProject developer tool
✓ Twitter: #buildinpublic developer tools
✓ Hacker News: Show HN developer tool

📊 발견한 스토리 3개:

---
Story 1: Raycast (Spotlight alternative)
출처: indiehackers.com/interviews/raycast

Journey:
- 문제: Spotlight가 너무 느림 (자신의 문제)
- MVP: 3개월 (Swift로 macOS 앱)
- 런칭: Product Hunt (1위)
- 성장: Community extensions 전략
- Timeline:
  * Month 0-3: MVP 개발
  * Month 4: Product Hunt 런칭 (5000 users in 1 day)
  * Month 6: Extension store 오픈
  * Month 12: $500K ARR
- 핵심 tactic: 개발자 커뮤니티가 extension 만들게 함

재현 가능성: ⭐⭐⭐⭐

**참고:**
- [Raycast](https://www.raycast.com/)
- [Product Hunt](https://www.producthunt.com/posts/raycast)
- [Indie Hackers](https://www.indiehackers.com/product/raycast)

---
Story 2: TablePlus (Database GUI)
출처: reddit.com/r/SideProject

Journey:
- 문제: 기존 DB 툴이 너무 느리고 비쌈
- MVP: 6개월 (개인 프로젝트로 시작)
- 가격: $79 one-time (경쟁사는 subscription)
- Timeline:
  * Month 0-6: 혼자 개발
  * Month 7: Soft launch to friends
  * Month 8: Product Hunt
  * Month 12: $5K MRR
  * Year 2: $50K MRR
- 핵심 tactic: One-time payment (경쟁 차별화)

재현 가능성: ⭐⭐⭐⭐⭐

**참고:**
- [TablePlus](https://tableplus.com/)
- [Reddit Discussion](https://www.reddit.com/r/SideProject/search?q=tableplus)

---
Story 3: DevUtils (Developer utilities)
출처: twitter.com/tdinh_me (Tony Dinh)

Journey:
- 문제: 매번 online tool 찾기 귀찮음
- MVP: 1개월 (macOS 앱, 10개 utils)
- Build in public: 매일 Twitter 업데이트
- Timeline:
  * Week 1-4: MVP 개발
  * Day 1: Twitter에 공개, Product Hunt 준비
  * Week 5: Product Hunt 런칭
  * Month 2: $1K MRR
  * Month 6: $5K MRR
- 핵심 tactic: Build in public으로 런칭 전 audience

재현 가능성: ⭐⭐⭐⭐⭐

**참고:**
- [DevUtils](https://devutils.com/)
- [Tony Dinh Twitter](https://twitter.com/tdinh_me)
- [Product Hunt](https://www.producthunt.com/posts/devutils-app)

---

공통 패턴 추출:
✅ 모두 자신이 겪은 문제 해결
✅ macOS 네이티브 앱 (개발자 타겟)
✅ 빠른 MVP (1-6개월)
✅ Product Hunt 런칭
✅ One-time 또는 저렴한 가격
✅ Developer community에 먼저 노출

추천:
당신도 개발자 도구를 만든다면:
1. 당신이 매일 겪는 불편함 찾기
2. 1-2개월 안에 만들 수 있는 것으로 시작
3. Build in public (Twitter)
4. Product Hunt 런칭 준비
5. 개발자 커뮤니티 (Reddit, HN) 활용
```

### 예시 4: 성공 사례 학습 (심화)

```
당신: "Notion이 어떻게 성공했는지 웹에서 찾아보고 분석해줘"

Claude:
1️⃣ success-story-researcher 실행
   → 웹 검색으로 Notion founder 인터뷰, 블로그 포스트 수집

2️⃣ success-formula-analyzer 실행
   → 수집한 자료에서 패턴 추출

🎯 Notion 성공 공식:

1. Product-first: 제품 퀄리티에 집착
2. Community-driven: 템플릿 커뮤니티 육성
3. Bottom-up: 개인 → 팀 → 회사
4. Ambassador program: 열렬한 유저가 홍보
5. Content marketing: 유튜브 튜토리얼

재현 가능한 tactics:
✅ 공식 템플릿 마켓플레이스 만들기
✅ 파워 유저에게 레퍼럴 인센티브
✅ 유튜브 "How to" 시리즈
✅ 무료 → 유료 업그레이드 경로

당신의 [프로젝트]에 적용:
1. Month 1: 10개 템플릿 제작
2. Month 2: 첫 5명 파워 유저 발굴
3. Month 3: 유튜브 채널 시작
```

**참고:**
- [Notion](https://www.notion.so/)
- [Notion Founder Ivan Zhao Interview](https://www.theverge.com/2021/10/7/22710408/notion-ivan-zhao-interview-notion-community)
- [Notion Community](https://www.notion.so/templates)

## 🚀 고급 사용법

### 성공 스토리 기반 아이디어 발굴 (NEW!)

```
워크플로우:
1. 관심 분야 성공 사례 리서치
2. 공통 패턴 추출
3. Underserved 니치 발견
4. 새 아이디어 평가

예시:
"SaaS 분야 성공 사례 10개 찾고,
공통점 분석해서 아직 안 만들어진
기회 영역 찾아줘"
```

### 경쟁사 리버스 엔지니어링

```
"[경쟁 제품]이 어떻게 성장했는지
웹에서 찾아보고,
내가 다르게 할 수 있는 부분 찾아줘"

→ success-story-researcher가 경쟁사 journey 추출
→ 차별화 포인트 발견
→ feasibility-checker로 실행 가능성 검증
```

### 여러 아이디어 비교

```
A안: [아이디어 A]
B안: [아이디어 B]
C안: [아이디어 C]

이 3개를 비교 평가해줘
```

→ 각각 평가 + 비교표 + 최종 추천

### 특정 차원만 개선

```
내 아이디어가 Differentiation 점수가 낮게 나왔어.
어떻게 개선할 수 있을까?
```

→ 차별화 전략 10가지 + 실행 가능성 평가

### 타임라인 최적화

```
3개월 안에 런칭해야 해.
어떻게 scope를 줄여야 할까?
```

→ Critical features 식별 + 단계별 출시 전략

## 💡 팁 & 요령

### ✅ 효과적인 질문

**좋은 예:**
```
"Todo 앱을 만들고 싶은데,
나는 React 중급자고 주말에만 시간 내고,
예산은 한 달에 $50 이하야.
경쟁자는 Todoist, Any.do가 있어."
```

**나쁜 예:**
```
"앱 만들고 싶어"
```

### 🎯 분석 요청 시 포함할 정보

1. **아이디어:** 문제 + 솔루션 (2-3 문장)
2. **타겟:** 누가 사용? (구체적으로)
3. **당신:** 스킬, 시간, 예산
4. **경쟁사:** 알고 있다면 (몰라도 OK)
5. **목표:** 언제까지? 얼마 벌고 싶나?

### ⚡ 빠른 체크리스트

**아이디어가 떠올랐을 때:**
- [ ] Orchestrator로 완전 분석 실행
- [ ] 점수 55점 이상? → 진행
- [ ] 55점 미만? → 개선 또는 다른 아이디어

**성공 사례 보고 영감 받았을 때:**
- [ ] Success-formula-analyzer로 패턴 추출
- [ ] 내 아이디어에 적용 가능한지 체크
- [ ] Feasibility-checker로 실행 가능성 검증

**이미 만들기 시작했는데 확신이 안 설 때:**
- [ ] Evaluator로 현재 방향 평가
- [ ] 약한 차원 개선 방법 물어보기
- [ ] Kill criteria 설정 (언제 포기할지)

## 🤔 FAQ

**Q: 점수가 낮으면 무조건 포기해야 하나요?**
A: 아니요! 점수는 개선할 부분을 알려주는 신호입니다. Iterate 과정을 거쳐 개선하세요.

**Q: 분석이 얼마나 정확한가요?**
A: Claude의 분석은 근거 기반이지만, 최종 판단은 당신이 해야 합니다. 참고 자료로 활용하세요.

**Q: 여러 번 분석하면 비용이 많이 드나요?**
A: Claude Code는 로컬에서 실행되며, API 비용은 사용량에 따라 다릅니다.

**Q: 분석 결과를 저장할 수 있나요?**
A: 네! Claude가 생성한 보고서를 복사해서 마크다운 파일로 저장하세요.

**Q: 한국어로 사용 가능한가요?**
A: 네! 완전히 한국어로 대화 가능합니다.

## 📚 더 알아보기

- **상세 문서:** `.claude/skills/README.md`
- **각 Agent 매뉴얼:** `.claude/skills/{agent-name}/SKILL.md`
- **설정 파일:** `.claude/skills/skill-rules.json`

## 🎉 시작하세요!

지금 바로 Claude Code를 열고 이렇게 말해보세요:

```
"완전한 비즈니스 분석을 실행해줘"
```

그리고 당신의 아이디어를 설명하세요.
10-15분 후, 명확한 답을 얻게 될 것입니다.

---

**만든이:** CEO AI Project
**버전:** 1.0.0
**날짜:** 2025-12-10

**Remember:**
> 성공한 사람의 아이템을 카피하지 말고,
> 성공하는 방식을 카피하세요! 🚀
