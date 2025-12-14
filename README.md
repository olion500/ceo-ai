# CEO AI - 전체 구조 Overview

## 📁 프로젝트 폴더 구조

```
ceo-ai/
│
├── .claude/skills/                           # Claude Code Skills (Multi-Agent System)
│   │
│   ├── success-story-researcher/             # 🔍 웹 리서치 Agent
│   │   └── SKILL.md                          # 검색 방법론 + 파일 저장 규칙
│   │
│   ├── success-formula-analyzer/             # 📊 패턴 분석 Agent
│   │   └── SKILL.md                          # 성공 방정식 추출 프레임워크
│   │
│   ├── business-idea-evaluator/              # ⭐ 아이디어 평가 Agent
│   │   └── SKILL.md                          # 8차원 평가 프레임워크
│   │
│   ├── feasibility-checker/                  # ✅ 실행 가능성 Agent
│   │   └── SKILL.md                          # 3-Pillar 검증 프레임워크
│   │
│   ├── business-orchestrator/                # 🎯 통합 조율 Agent
│   │   └── SKILL.md                          # Multi-agent 워크플로우
│   │
│   ├── skill-rules.json                      # Skills 자동 활성화 규칙
│   └── README.md                             # Skills 가이드
│
├── research/                                  # 📚 리서치 데이터 저장소
│   ├── stories/                              # 개별 제품 성공 스토리
│   │   ├── EXAMPLE-gumroad-2024-12-10.md
│   │   └── [product-slug]-[date].md
│   │
│   ├── reports/                              # 종합 분석 리포트
│   │   └── [topic]-analysis-[date].md
│   │
│   ├── patterns/                             # 추출된 성공 패턴
│   │   └── [pattern-name].md
│   │
│   └── README.md                             # 폴더 구조 및 사용 가이드
│
├── CEO_AI_QUICKSTART.md                      # 🚀 빠른 시작 가이드
├── SEARCH_QUERIES_CHEATSHEET.md              # 🔎 검색 쿼리 치트시트
└── README.md                                 # 프로젝트 메인 문서
```

---

## 🤖 Multi-Agent Network

```
                  ┌─────────────────────────────────────┐
                  │                                     │
                  │     👤 사용자 (You)                 │
                  │                                     │
                  └──────────────┬──────────────────────┘
                                 │
                                 │ "완전한 비즈니스 분석 실행"
                                 ▼
                  ┌─────────────────────────────────────┐
                  │  🎯 Business Orchestrator           │
                  │  (통합 조율 및 보고서 생성)         │
                  │                                     │
                  │  • 3개 agent 실행 조율              │
                  │  • 결과 종합 분석                   │
                  │  • 최종 추천 및 액션 플랜           │
                  └──────────────┬──────────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
  │ 🔍 Success Story │ │ 📊 Success       │ │ ⭐ Business Idea │
  │ Researcher       │ │ Formula Analyzer │ │ Evaluator        │
  │                  │ │                  │ │                  │
  │ • 웹 검색        │ │ • 패턴 추출      │ │ • 8차원 평가     │
  │ • 스토리 수집    │ │ • 재현 방정식    │ │ • 근거 기반      │
  │ • 파일 저장      │ │ • Tactics 도출   │ │ • 80점 스코어링  │
  └─────┬────────────┘ └─────┬────────────┘ └─────┬────────────┘
        │                    │                    │
        │                    │                    │
        ▼                    ▼                    ▼
  research/stories/    research/patterns/    evaluation.md
  [product].md        [pattern].md
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │ ✅ Feasibility Checker        │
                  │ (실행 가능성 검증)            │
                  │                              │
                  │ • Technical: 6/10            │
                  │ • Financial: 8/10            │
                  │ • Time: 7/10                 │
                  │ → Overall: 7.0/10 ✅         │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │ 📄 최종 통합 보고서          │
                  │                              │
                  │ • 종합 점수: 7.5/10          │
                  │ • 추천: GO ✅                │
                  │ • 4단계 액션 플랜            │
                  │ • 리스크 & 대응 전략         │
                  │ • Decision Points            │
                  └──────────────────────────────┘
```

---

## 🔄 Workflow Scenarios

### Scenario 1: 성공 스토리 리서치 & 패턴 학습

**User Input:**
```
"SaaS 분야에서 $10K MRR 달성한 스토리 3개 찾고 패턴 분석해줘"
```

```
    │
    ▼
┌─────────────────────────────────────────┐
│ 🔍 success-story-researcher             │
│                                         │
│ 1. WebSearch: 관련 스토리 검색          │
│ 2. WebFetch: 상세 정보 추출             │
│ 3. 정보 정리 및 구조화                  │
│ 4. Markdown 파일 생성                   │
└─────────────────┬───────────────────────┘
                  │
                  ▼
        ┌─────────────────────┐
        │ research/stories/   │
        ├─────────────────────┤
        │ • product-1.md      │
        │ • product-2.md      │
        │ • product-3.md      │
        └─────────┬───────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│ 📊 success-formula-analyzer             │
│                                         │
│ 1. 3개 스토리 읽기                      │
│ 2. 공통 패턴 추출                       │
│ 3. 재현 가능한 tactics 정리             │
│ 4. 성공 방정식 도출                     │
└─────────────────┬───────────────────────┘
                  │
                  ▼
        ┌─────────────────────┐
        │ research/reports/   │
        ├─────────────────────┤
        │ analysis-report.md  │
        └─────────────────────┘
        ┌─────────────────────┐
        │ research/patterns/  │
        ├─────────────────────┤
        │ common-pattern.md   │
        └─────────────────────┘
```

---

### Scenario 2: 아이디어 완전 검증

**User Input:**
```
"완전한 비즈니스 분석 실행:
 아이디어: [설명]
 타겟: [고객]
 배경: [스킬/시간/예산]"
```

```
    │
    ▼
┌──────────────────────────────────────────┐
│ 🎯 business-orchestrator                 │
│ (Multi-agent 조율 시작)                  │
└─────────┬────────────────────────────────┘
          │
          ├─ Parallel Execution ─┐
          │                       │
          ▼                       ▼
┌────────────────────┐  ┌────────────────────┐
│ 📊 Pattern Match   │  │ ⭐ Idea Evaluation │
│                    │  │                    │
│ 유사 성공 사례     │  │ 8차원 평가:        │
│ 찾기 및 패턴 추출  │  │ • Problem: 7/10    │
│                    │  │ • Market: 8/10     │
│ Output:            │  │ • Competition: 6/10│
│ • 3-5 patterns     │  │ ...                │
│ • Tactics          │  │ Total: 58/80       │
└─────────┬──────────┘  └──────────┬─────────┘
          │                        │
          └────────┬───────────────┘
                   ▼
          ┌────────────────────┐
          │ ✅ Feasibility     │
          │                    │
          │ • Technical: 7/10  │
          │ • Financial: 8/10  │
          │ • Time: 6/10       │
          │ Overall: 7.0/10    │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │ 🎯 Synthesis       │
          │                    │
          │ Final Score: 7.2/10│
          │ Recommendation: GO │
          │                    │
          │ 📄 Action Plan:    │
          │ • Phase 0 (준비)   │
          │ • Phase 1 (MVP)    │
          │ • Phase 2 (Beta)   │
          │ • Phase 3 (Launch) │
          └────────────────────┘
```

---

### Scenario 3: 경쟁사 리버스 엔지니어링

**User Input:**
```
"Notion이 어떻게 성공했는지 웹에서 찾아보고
 내 프로젝트에 적용 가능한지 분석해줘"
```

```
    │
    ▼
┌─────────────────────────────────────┐
│ 🔍 success-story-researcher         │
│                                     │
│ 1. WebSearch: Notion 관련 검색      │
│    • Indie Hackers                  │
│    • Founder blog                   │
│    • Interviews                     │
│ 2. WebFetch: 상세 정보 추출         │
│ 3. Save: notion-2024-12-10.md       │
└──────────────┬──────────────────────┘
               │
               ▼
        research/stories/
        notion-2024-12-10.md
               │
               ▼
┌─────────────────────────────────────┐
│ 📊 success-formula-analyzer         │
│                                     │
│ Notion 성공 공식:                   │
│ • Product-first                     │
│ • Community-driven                  │
│ • Bottom-up                         │
│ • Ambassador program                │
│ • Content marketing                 │
│                                     │
│ 재현 가능한 tactics:                │
│ ✅ 템플릿 마켓플레이스              │
│ ✅ 파워 유저 레퍼럴                 │
│ ✅ 유튜브 튜토리얼                  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ ⭐ business-idea-evaluator          │
│                                     │
│ "내 아이디어에 적용하면?"           │
│                                     │
│ ✅ 적용 가능: Template 전략         │
│ ⚠️ 수정 필요: Community 규모        │
│ ❌ 불가능: 대규모 팀 필요한 부분    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ ✅ feasibility-checker              │
│                                     │
│ "내가 실행 가능한가?"               │
│                                     │
│ Technical: 6/10                     │
│ • Community 기능 개발 필요          │
│                                     │
│ Financial: 9/10                     │
│ • Template은 저비용                 │
│                                     │
│ Time: 5/10                          │
│ • 3-6개월 필요                      │
│                                     │
│ Overall: 6.7/10                     │
│ → Proceed with de-scoped plan       │
└─────────────────────────────────────┘
```

---

## 📊 데이터 흐름

```
┌─────────────┐
│   Internet  │ (Indie Hackers, Reddit, Twitter, etc)
└──────┬──────┘
       │ WebSearch / WebFetch
       ▼
┌─────────────────────────────┐
│ success-story-researcher    │
│ • 정보 수집                 │
│ • 구조화                    │
│ • 검증                      │
└──────┬──────────────────────┘
       │ Save as Markdown
       ▼
┌─────────────────────────────┐
│ research/                   │
│ ├── stories/                │
│ │   ├── product-1.md        │ ◄─┐
│ │   ├── product-2.md        │   │
│ │   └── product-3.md        │   │
│ ├── reports/                │   │
│ │   └── analysis.md         │   │
│ └── patterns/               │   │
│     └── pattern.md          │   │
└──────┬──────────────────────┘   │
       │ Read & Analyze          │
       ▼                          │
┌─────────────────────────────┐   │
│ success-formula-analyzer    │   │
│ • 패턴 추출                 │   │
│ • Tactics 도출              │   │
│ • 재현 가능성 평가          │   │
└──────┬──────────────────────┘   │
       │ Feed into               │
       ▼                          │
┌─────────────────────────────┐   │
│ business-idea-evaluator     │   │
│ • 아이디어 평가             │   │
│ • 패턴 매칭                 │   │
│ • 점수화                    │   │
└──────┬──────────────────────┘   │
       │                          │
       ▼                          │
┌─────────────────────────────┐   │
│ feasibility-checker         │   │
│ • 실행 가능성 검증          │   │
│ • 리소스 요구사항           │   │
│ • 타임라인 추정             │   │
└──────┬──────────────────────┘   │
       │                          │
       ▼                          │
┌─────────────────────────────┐   │
│ business-orchestrator       │   │
│ • 모든 결과 통합            │   │
│ • 최종 추천                 │   │
│ • 액션 플랜 생성            │   │
└──────┬──────────────────────┘   │
       │ Create Report            │
       ▼                          │
┌─────────────────────────────┐   │
│ Final Report                │   │
│ • 종합 분석                 │   │
│ • Go/No-go                  │   │
│ • 4-Phase Action Plan       │   │
└──────┬──────────────────────┘   │
       │                          │
       │ Optional: Save           │
       └──────────────────────────┘
```

---

## 🎯 Agent별 책임 & 출력

### 🔍 success-story-researcher

```
┌────────────────────────────────────────────────────────┐
│ 🔍 success-story-researcher                            │
├────────────────────────────────────────────────────────┤
│ Input:  제품명 or 카테고리 or 검색 조건                │
│ Process: WebSearch → WebFetch → 정리 → 검증            │
│ Output:  research/stories/[product].md                 │
│         • 상세 journey                                 │
│         • Timeline                                     │
│         • Tactics                                      │
│         • Sources (모든 링크)                          │
└────────────────────────────────────────────────────────┘
```

### 📊 success-formula-analyzer

```
┌────────────────────────────────────────────────────────┐
│ 📊 success-formula-analyzer                            │
├────────────────────────────────────────────────────────┤
│ Input:  성공 스토리 (파일 or raw data)                 │
│ Process: 패턴 추출 → 방정식 도출 → Tactics 정리        │
│ Output:  • 5가지 성공 패턴 분류                        │
│         • 재현 가능한 tactics                          │
│         • Timeline benchmarks                          │
│         • research/patterns/[pattern].md (optional)    │
└────────────────────────────────────────────────────────┘
```

### ⭐ business-idea-evaluator

```
┌────────────────────────────────────────────────────────┐
│ ⭐ business-idea-evaluator                             │
├────────────────────────────────────────────────────────┤
│ Input:  아이디어 설명 + 타겟 + 경쟁사                  │
│ Process: 8차원 평가 → 근거 수집 → 점수화               │
│ Output:  • 8개 차원 점수 (각 1-10)                     │
│         • Total: X/80                                  │
│         • 리스크 분석                                  │
│         • 개선 제안                                    │
└────────────────────────────────────────────────────────┘
```

### ✅ feasibility-checker

```
┌────────────────────────────────────────────────────────┐
│ ✅ feasibility-checker                                 │
├────────────────────────────────────────────────────────┤
│ Input:  아이디어 + 당신의 상황 (스킬/시간/예산)        │
│ Process: 3-Pillar 검증 → 리소스 계산 → Timeline 추정   │
│ Output:  • Technical: X/10                             │
│         • Financial: X/10                              │
│         • Time: X/10                                   │
│         • Overall: X/10                                │
│         • Mitigation strategies                        │
└────────────────────────────────────────────────────────┘
```

### 🎯 business-orchestrator

```
┌────────────────────────────────────────────────────────┐
│ 🎯 business-orchestrator                               │
├────────────────────────────────────────────────────────┤
│ Input:  완전한 비즈니스 분석 요청                      │
│ Process: 4개 agent 조율 → 결과 통합 → 종합 분석        │
│ Output:  • 최종 점수: X/10                             │
│         • 추천: GO / ITERATE / NO-GO                   │
│         • 통합 인사이트                                │
│         • 4-Phase Action Plan                          │
│         • Decision Points                              │
│         • research/reports/[topic]-analysis.md         │
└────────────────────────────────────────────────────────┘
```

---

## 📚 핵심 문서

```
├── CEO_AI_QUICKSTART.md
│   • 5분 시작 가이드
│   • Agent 소개
│   • 실전 예시
│   • FAQ
│
├── SEARCH_QUERIES_CHEATSHEET.md
│   • 목적별 검색 쿼리
│   • 플랫폼별 베스트 쿼리
│   • 황금 쿼리 조합
│   • 고급 검색 기법
│
├── research/README.md
│   • 폴더 구조 설명
│   • 파일명 규칙
│   • 템플릿 가이드
│   • Best practices
│
└── .claude/skills/README.md
    • 전체 Skills 가이드
    • 각 Agent 상세 설명
    • 사용 예시
    • Customization
```

---

## 🚀 전체 시스템 플로우 요약

### 1. 사용자 요청
```
└─→ "완전한 비즈니스 분석" or "성공 스토리 찾기"
```

### 2. Skill 자동 활성화 (skill-rules.json)
```
└─→ 키워드/인텐트 매칭
```

### 3. Agent 실행
```
├─→ success-story-researcher: 웹 스크랩
├─→ success-formula-analyzer: 패턴 추출
├─→ business-idea-evaluator: 평가
└─→ feasibility-checker: 실행 가능성
```

### 4. 데이터 저장
```
├─→ research/stories/ (개별 스토리)
├─→ research/reports/ (분석 리포트)
└─→ research/patterns/ (추출 패턴)
```

### 5. Orchestrator 통합
```
└─→ 모든 결과 종합 → 최종 보고서
```

### 6. 사용자에게 전달
```
└─→ 명확한 추천 + 액션 플랜
```

---

## 💡 핵심 철학

> **성공한 사람의 아이템을 카피하지 말고,
> 성공하는 방식을 카피해서 내 아이템에 적용하라**

---

## 📋 빠른 시작

1. **성공 사례 리서치하기**
   ```
   "간단한 웹사이트나 chrome extension 2022년 이후 사례 10개 찾아줘"
   ```

2. **아이디어 평가하기**
   ```
   "완전한 비즈니스 분석 실행:
    아이디어: [당신의 아이디어]
    타겟: [타겟 고객]
    배경: [스킬/시간/예산]"
   ```

3. **경쟁사 분석하기**
   ```
   "[경쟁사명]이 어떻게 성공했는지 찾아보고 내 프로젝트에 적용 가능한지 분석해줘"
   ```

---

## 📖 참고 자료

- [CEO_AI_QUICKSTART.md](./CEO_AI_QUICKSTART.md) - 5분 시작 가이드
- [SEARCH_QUERIES_CHEATSHEET.md](./SEARCH_QUERIES_CHEATSHEET.md) - 검색 쿼리 모음
- [research/reports/simple-tools-2022-2024-analysis-2025-12-10.md](./research/reports/simple-tools-2022-2024-analysis-2025-12-10.md) - 실전 분석 예시

---

## 🏆 실전 사례

최근 분석 완료:
- ✅ **2022-2024 간단한 웹툴/Chrome Extension 10개 사례**
  - Easy Folders: $3.7K MRR (6개월)
  - Tailscan: $4K-5K MRR
  - ShipFast: $133K/월
  - TypingMind: $83K/월
  - Photo AI: $157K/월
  - 그 외 5개 사례

결과: 공통 패턴 6가지, 재현 가능한 전략 4가지, 실행 플랜 도출

---

**버전:** 1.0.0
**최종 업데이트:** 2024-12-10
**만든이:** CEO AI Multi-Agent System
