---
title: Research Directory
created: 2025-12-16
updated: 2025-12-16
---
# Research Directory

success-story-researcher skill이 수집한 성공 스토리와 분석 자료를 저장하는 곳입니다.

## 📁 폴더 구조

```
research/
├── stories/          # 개별 제품 성공 스토리
├── reports/          # 종합 분석 리포트
└── patterns/         # 추출된 공통 패턴
```

### stories/ - 개별 성공 스토리

**파일명 규칙:**
```
[product-slug]-[yyyy-mm-dd].md
```

**예시:**
- `gumroad-2024-12-10.md`
- `notion-2024-12-10.md`
- `raycast-2024-12-10.md`

**용도:**
- 한 제품의 성공 journey를 상세히 기록
- 제작 과정, 수익 timeline, 성장 tactics 포함
- 참고한 모든 링크 포함

### reports/ - 종합 분석 리포트

**파일명 규칙:**
```
[topic]-analysis-[yyyy-mm-dd].md
```

**예시:**
- `saas-10k-mrr-analysis-2024-12-10.md`
- `developer-tools-success-patterns-2024-12-10.md`
- `bootstrapped-startups-comparison-2024-12-10.md`

**용도:**
- 여러 스토리를 비교 분석
- 카테고리별 패턴 추출
- 공통점과 차이점 정리

### patterns/ - 추출된 패턴

**파일명 규칙:**
```
[pattern-name].md
```

**예시:**
- `problem-first-pattern.md`
- `community-driven-growth.md`
- `build-in-public-strategy.md`

**용도:**
- 재현 가능한 성공 패턴 정리
- 여러 사례에서 검증된 tactics
- 적용 가이드 포함

## 📝 파일 템플릿

### Individual Story Template

```markdown
# [Product Name] Success Story

**Research Date:** YYYY-MM-DD
**Category:** [SaaS / App / Tool / etc]
**Revenue Range:** [$X - $Y MRR]
**Team Size:** [Solo / X people]

---

## Quick Facts

- **Product:** [Name]
- **Founded:** [Date]
- **Founder:** [Name]
- **Current Status:** [$X/month, Y customers]
- **Time to First Revenue:** [X months]
- **Time to $10K MRR:** [X months]

---

## The Story

### Problem Discovery
[How they found the problem]

### MVP Development
- **Timeline:** [X weeks/months]
- **Features:** [List]
- **Tech Stack:** [Technologies]

### Launch Strategy
[How they launched]

### Growth Journey
[Month-by-month or phase-by-phase]

### Key Decisions
1. [Decision 1]
2. [Decision 2]

---

## Reproducible Tactics

1. [Tactic 1]
2. [Tactic 2]

---

## Lessons Learned

- [Lesson 1]
- [Lesson 2]

---

## Sources

1. [Title](URL) - [Date accessed]
2. [Title](URL) - [Date accessed]
```

### Analysis Report Template

```markdown
# [Topic] Analysis Report

**Research Date:** YYYY-MM-DD
**Stories Analyzed:** [Number]
**Category:** [Category]

---

## Executive Summary

[2-3 paragraphs]

---

## Stories Analyzed

1. [Product 1] - [Link to story file]
2. [Product 2] - [Link to story file]
3. [Product 3] - [Link to story file]

---

## Common Patterns

### Pattern 1: [Name]
[Description]
**Frequency:** X out of Y stories

### Pattern 2: [Name]
[Description]
**Frequency:** X out of Y stories

---

## Timeline Benchmarks

- Average time to MVP: [X weeks]
- Average time to first revenue: [X months]
- Average time to $10K MRR: [X months]

---

## Recommendations

1. [Recommendation 1]
2. [Recommendation 2]

---

## Sources

1. [Story 1 file](../stories/product-1.md)
2. [Story 2 file](../stories/product-2.md)
3. [External source](URL)
```

## 🎯 사용 방법

### 1. 개별 스토리 리서치

```
Claude에게:
"Gumroad 성공 스토리를 웹에서 찾아서 정리해줘"

→ research/stories/gumroad-2024-12-10.md 생성
```

### 2. 카테고리 분석

```
Claude에게:
"SaaS 분야에서 $10K MRR 달성한 스토리 5개 찾고 분석해줘"

→ research/stories/ 에 5개 파일 생성
→ research/reports/saas-10k-mrr-analysis-2024-12-10.md 생성
```

### 3. 패턴 추출

```
Claude에게:
"지금까지 수집한 스토리에서 공통 패턴을 추출해줘"

→ research/patterns/ 에 패턴 파일들 생성
```

## 📊 파일 네이밍 가이드

### Product Slug 규칙

- 소문자만 사용
- 공백은 하이픈(-)으로
- 특수문자 제거

**예시:**
- "Notion" → `notion`
- "ConvertKit" → `convertkit`
- "Dev Utils" → `dev-utils`
- "TablePlus" → `tableplus`

### Topic Slug 규칙

- 설명적이고 구체적으로
- 단어 구분은 하이픈(-)

**예시:**
- `saas-10k-mrr-analysis`
- `developer-tools-success-patterns`
- `bootstrapped-startups-comparison`
- `mobile-apps-growth-tactics`

## 🔍 검색 및 참조

### 파일 찾기

```bash
# 특정 제품 찾기
ls research/stories/*gumroad*

# 특정 날짜 리서치
ls research/stories/*2024-12-10*

# 모든 리포트
ls research/reports/
```

### 링크 참조

다른 파일에서 참조할 때:
```markdown
자세한 내용: [Gumroad Success Story](../stories/gumroad-2024-12-10.md)
```

## 🎨 Best Practices

### ✅ DO

- **항상 날짜 포함:** 정보의 시점 명확히
- **참고 링크 필수:** 모든 출처 명시
- **구체적인 숫자:** 막연한 표현 대신 정확한 데이터
- **Timeline 포함:** 언제 무엇이 일어났는지
- **실패도 기록:** 성공만이 아니라 실패/어려움도

### ❌ DON'T

- 날짜 없이 저장
- 출처 링크 누락
- 막연한 정보 ("많이 벌었대요")
- 검증 안 된 정보
- 중복 파일 (같은 제품, 같은 날짜)

## 📈 활용 시나리오

### Scenario 1: 경쟁사 분석

```
1. research/stories/ 에서 경쟁 제품 스토리 수집
2. research/reports/ 에 비교 분석 리포트 작성
3. 차별화 포인트 도출
```

### Scenario 2: 아이디어 검증

```
1. 유사 카테고리 성공 스토리 수집
2. 공통 패턴 추출
3. 내 아이디어와 비교
4. Feasibility 평가
```

### Scenario 3: 로드맵 수립

```
1. 유사 제품들의 timeline 분석
2. 일반적인 마일스톤 파악
3. 내 프로젝트 로드맵 작성
```

## 🔄 업데이트 규칙

### 정보 업데이트 시

- 새 파일 생성 (날짜 변경)
- 이전 파일은 유지 (히스토리)
- 새 파일에 "Updated from: [이전 파일]" 명시

**예시:**
```
gumroad-2024-12-10.md  (원본)
gumroad-2024-12-15.md  (업데이트)
  └─ 맨 위에: "Updated from: gumroad-2024-12-10.md"
```

---

**Version:** 1.0.0
**Last Updated:** 2024-12-10

**Next:** success-story-researcher skill을 사용해서 첫 스토리를 수집해보세요!
