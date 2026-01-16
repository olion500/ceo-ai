---
title: Company Brain - Feasibility Assessment
assessment-date: 2025-01-13
type: Feasibility Check
overall-score: 6.15
recommendation: PROCEED with De-scoping
technical-score: 5.5
financial-score: 8.0
time-score: 5.5
market-score: 6.0
tags: [feasibility, ai, b2b, saas, company-analytics, decision-support]
---

# Feasibility Assessment: Company Brain

## Executive Summary

**아이디어:** "Company Brain" - 데이터 기반 경영 방향성 AI
- 스타트업~중소기업 대상 (10-500명)
- 다양한 데이터 연동 (HR, 재무, Slack, 프로젝트 관리)
- 핵심 메트릭 자동 추출
- "좋은 문화의 회사" 벤치마크 비교
- AI가 사업 방향성 제안

**최종 점수:** 6.15/10 (🟡 Feasible with effort)
**권장:** 범위 축소 후 진행

---

## Scores Overview

| Pillar | Score | Weight | Weighted | Status |
|--------|-------|--------|----------|--------|
| Technical | 5.5/10 | 30% | 1.65 | ⚠️ 학습 필요 |
| Financial | 8.0/10 | 20% | 1.60 | ✅ 저비용 |
| Time | 5.5/10 | 20% | 1.10 | ⚠️ 4-6개월 |
| Market | 6.0/10 | 30% | 1.80 | 🟡 빈 공간 있음 |
| **TOTAL** | **6.15/10** | **100%** | **6.15** | **🟡 Proceed** |

---

## Pillar 1: Technical Feasibility (5.5/10)

### Skills Assessment

| 스킬 영역 | 필요 | 현재 | Gap | 중요도 | Gap Score |
|-----------|------|------|-----|--------|-----------|
| 프론트엔드 (React/Next.js) | 7/10 | 8/10 | 0 | Core (3x) | 0 |
| 백엔드 (Node.js/API) | 7/10 | 8/10 | 0 | Core (3x) | 0 |
| LLM/AI 통합 | 7/10 | 7/10 | 0 | Core (3x) | 0 |
| 데이터베이스 (PostgreSQL) | 6/10 | 6/10 | 0 | Core (3x) | 0 |
| **OAuth 연동** | 7/10 | 4/10 | 3 | Core (3x) | **9** |
| **보안/암호화** | 6/10 | 3/10 | 3 | Important (2x) | **6** |
| 컴플라이언스 (SOC2) | 5/10 | 1/10 | 4 | Nice-to-have (1x) | 4 |

**Total Gap Score:** 19 (10-20 범위 = "Learn first")

### Tech Stack Decision

```
✅ 사용 (익숙함):
- Next.js + TypeScript
- PostgreSQL + Prisma
- OpenAI/Claude API
- Vercel

⚠️ 학습 필요:
- OAuth2 연동 (2-3주)
- 데이터 암호화 (1-2주)

✅ Managed Service:
- Clerk (인증)
- Stripe (결제)
- Resend (이메일)
```

### 🚨 Critical Blocker: 벤치마크 데이터

**문제:** "좋은 문화의 회사" 데이터 소스 불명확
- 공개 API 없음
- 옵션:
  1. 고객 데이터 풀링 (chicken-egg)
  2. 공개 데이터 스크래핑 (법적 리스크)
  3. 파트너십 (시간 오래 걸림)
  4. **정적 리서치 데이터로 시작** ← 권장

---

## Pillar 2: Financial Feasibility (8.0/10) ✅

### 초기 비용

| 항목 | 비용 |
|------|------|
| 도메인 | $15/년 |
| 호스팅 | $0 (Free tier) |
| 데이터베이스 | $0 (Free tier) |
| AI API | $50-100/월 |
| **TOTAL** | **~$100-200** |

### 월 운영 비용 (스케일별)

| 단계 | 사용자 | 비용 | Break-even |
|------|--------|------|------------|
| MVP | 0-50 | $50 | 1 customer |
| Early | 50-200 | $150 | 2 customers |
| Growth | 200-500 | $350 | 3 customers |

### 런웨이

```
예산: $5,000-10,000
월 비용: ~$100
런웨이: 50-100개월 ✅
```

---

## Pillar 3: Time Feasibility (5.5/10)

### 시간 가용성

```
주당 가용: 20-30시간
실제 코딩 (×0.6): 12-18시간/주
월간: 48-72시간
```

### MVP 타임라인 (Full Scope)

| 단계 | Base | ×2 Buffer | 실제 |
|------|------|-----------|------|
| 기획/설계 | 1주 | 3주 | 3주 |
| 인증/UI | 1주 | 3주 | 3주 |
| Slack 연동 | 1주 | 4주 | 4주 |
| 대시보드 | 2주 | 6주 | 6주 |
| AI 분석 | 1주 | 3주 | 3주 |
| 테스트 | 1주 | 3주 | 3주 |
| **TOTAL** | **7주** | **22주** | **~5-6개월** |

### De-scoped MVP 타임라인

**~3개월** (주 20시간 기준)

### 기회비용

```
프리랜싱 대안: 500시간 × $50 = $25,000 확정
Company Brain: $0-50,000 (불확실)
Expected Value (50%): $25,000 ≈ 비슷
```

---

## Pillar 4: Market Feasibility (6.0/10)

### 경쟁 현황

| 플레이어 | 카테고리 | 매출 | 당신과 차이 |
|----------|----------|------|-------------|
| [ChartMogul](https://chartmogul.com/) | SaaS 메트릭 | $5M+ ARR | 재무만 |
| [Baremetrics](https://baremetrics.com/) | SaaS 메트릭 | $2M+ ARR | 재무만 |
| [Culture Amp](https://www.cultureamp.com/) | HR Analytics | $100M+ | HR만 |
| [Ambient](https://www.ambient.us/) | CEO Assistant | Seed | 일정 중심 |

### Market Gap ✅

```
기존: 재무 OR HR OR 일정 (분리됨)
당신: 통합 + 벤치마크 + AI 방향 제안 ← 빈 공간
```

### 가격 검증

- 경쟁사 범위: $50-500/월
- 당신의 가격: $99-499/월 ✅ 적절

### 수요 미검증 ⚠️

- 통합 플랫폼 수요 확인 필요
- SMB 지불 의사 확인 필요

---

## Critical Issues & Mitigations

### 1. 🚨 벤치마크 데이터 (Critical)

**문제:** 데이터 소스 불명확
**해결:**
- Phase 1: 정적 리서치 데이터 사용
- Phase 2+: 고객 데이터 풀링으로 전환

### 2. ⚠️ OAuth 연동 학습

**문제:** Slack, HRIS API 경험 부족
**해결:**
- Slack API 먼저 2-3주 학습
- 다른 연동은 Phase 2로 이연

### 3. ⚠️ MVP 범위 과다

**문제:** 원래 범위로는 6개월+
**해결:** 아래 De-scoped MVP로 진행

---

## Recommended MVP Scope (De-scoped)

### Phase 1: "경영 건강 점검" (3개월)

**포함:**
- Slack 연동 (활동 데이터)
- 수동 메트릭 입력 (매출, 이직률)
- 5개 핵심 메트릭 대시보드
- 업계 평균 비교 (정적 데이터)
- AI 분석 리포트 (월 1회)

**제외 (Phase 2):**
- HR 시스템 연동
- 재무 시스템 연동
- 실시간 벤치마크
- 다중 사용자

### 타임라인

| 주 | 산출물 |
|----|--------|
| 1-2 | 설계, 와이어프레임 |
| 3-4 | 인증, 기본 UI |
| 5-6 | Slack OAuth 연동 |
| 7-8 | 메트릭 계산 로직 |
| 9-10 | AI 분석 기능 |
| 11-12 | 테스트, 베타 런칭 |

---

## Go/No-Go Checklist

**진행 전 확인:**
- [ ] Slack OAuth 프로토타입 (1주)
- [ ] 잠재 고객 5명 인터뷰
- [ ] 벤치마크 데이터 소스 확보
- [ ] $99-149/월 지불 의사 확인 (3명+)
- [ ] 랜딩페이지 50+ signups

**충족 시:** ✅ 진행
**미충족 시:** 피벗 또는 추가 축소

---

## Next Steps

1. **즉시 (이번 주):**
   - Slack API 문서 검토
   - OAuth 연동 프로토타입 시작

2. **1-2주:**
   - 잠재 고객 5명 인터뷰 진행
   - 랜딩페이지 제작

3. **3-4주:**
   - Go/No-Go 결정
   - MVP 개발 시작 또는 피벗

---

## References

- [ChartMogul](https://chartmogul.com/) - SaaS 메트릭 분석
- [Baremetrics](https://baremetrics.com/) - SaaS 메트릭 + 벤치마크
- [Culture Amp](https://www.cultureamp.com/) - HR Analytics
- [Lattice](https://lattice.com/) - People Management
- [Ambient](https://www.ambient.us/) - AI Chief of Staff
- [re:cap](https://www.re-cap.com/) - SaaS 벤치마킹 도구
- [Tomasz Tunguz Metrics Template](https://tomtunguz.com/saas-startup-metrics-template/)
