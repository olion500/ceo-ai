---
title: Open Core Model
pattern-category: monetization
tags: [pattern, monetization]
type: Pattern
---

# Open Core Model

## What Is This Pattern?

Open Core Model은 핵심 기능을 오픈소스로 공개하고, 엔터프라이즈 기능/지원/호스팅을 유료로 제공하는 수익화 전략입니다. 개인 개발자와 소규모 팀은 무료로 사용하고, 기업은 기꺼이 프리미엄 기능과 SLA에 지불합니다.

핵심은 **신뢰 구축**입니다. 오픈소스로 투명성을 제공하면서 상업적 성공도 달성합니다.

## How It Works

1. **오픈소스 코어**: 핵심 기능 무료 공개 (MIT, Apache, GPL, AGPL 등)
2. **커뮤니티 구축**: GitHub stars, contributors, 사용자 확보
3. **엔터프라이즈 기능**: 화이트 라벨, SLA, 우선 지원, 고급 기능 유료
4. **듀얼 라이선스**: 오픈소스(AGPL) + 상업용 라이선스
5. **서비스 수익**: 호스팅, 컨설팅, 커스터마이징

## Real Examples (Ranked by Success)

### 1. Filestash (2016-2024, 8+ years)

- **What happened**:
  - Self-hosted 파일 관리 플랫폼 오픈소스 (GNU AGPL-3.0)
  - 8년 지속 개발
  - 엔터프라이즈 라이선스 $500+/month
  - Near full-time income 달성
- **Why it worked**:
  - AGPL 라이선스 = 파생 작업 공개 강제 → 기업은 유료 라이선스 구매
  - 확장 가능한 아키텍처 (15+ storage backends)
  - 커스터마이징 서비스 추가 수익
- **Key metrics**:
  - Development: 8+ years
  - Revenue: Full-time income
  - Enterprise: $500+/month subscriptions
- **Key insight**: AGPL 선택이 상업화 핵심 (MIT/Apache보다 기업 라이선스 유도)

### 2. Video Hub App (2018-2025)

- **What happened**:
  - Video organization 도구 오픈소스 (GitHub)
  - 동시에 $5 상업 라이선스 판매
  - 8년간 $500/month 지속
- **Why it worked**:
  - 오픈소스 = 신뢰 구축
  - 상업 라이선스 = 편의성 (설치 패키지, 지원)
  - 70% 기부로 사회적 차별화
- **Key metrics**:
  - Users: 9,600+ (8 years)
  - Revenue: $300-500/month sustained
  - Open source + $5 lifetime purchase
- **Key insight**: 오픈소스와 상업이 양립 가능, 투명성이 신뢰 구축

### 3. GitLab, Sentry, MongoDB (참고)

- **What happened**:
  - 오픈소스 코어 + 엔터프라이즈 기능
  - 수백만 ~ 수십억 달러 기업으로 성장
- **Why it worked**:
  - 개발자 신뢰 (오픈소스)
  - 기업 지불 의지 (SLA, 지원, 고급 기능)
- **Key insight**: Open Core = 개발자 채택 + 기업 수익의 완벽한 균형

## Why This Works

### 양쪽 시장 공략

- **개인/스타트업**: 무료 사용 → 커뮤니티 구축
- **엔터프라이즈**: 기꺼이 지불 → 수익 창출

### 신뢰와 투명성

- 오픈소스 = 코드 검토 가능 = 신뢰
- 벤더 락인 우려 제거 (언제든 포크 가능)

### 마케팅 효과

- GitHub = 무료 마케팅 플랫폼
- 커뮤니티가 홍보 (입소문)

### 장기 지속성

- 커뮤니티 contributions = 무료 개발 인력
- 사용자 피드백 = 제품 개선 방향

## Prerequisites

### 필수 요소

1. **개발자 대상 제품**: B2B 개발 도구, 인프라
2. **명확한 엔터프라이즈 니즈**: SLA, 지원, 고급 기능
3. **장기 커밋**: 최소 1-2년 지속 개발 의지
4. **커뮤니티 관리**: Issue, PR 대응 능력

### 선호 조건

- 복잡한 설정/운영 (→ 매니지드 서비스 판매)
- 보안/컴플라이언스 중요 (→ 엔터프라이즈 기능)
- 커스터마이징 수요 (→ 컨설팅 수익)
- 강력한 네트워크 효과

## Common Mistakes

### ❌ 너무 많이 무료 제공

- 문제: 엔터프라이즈도 오픈소스만 사용
- 해결: 핵심은 무료, 고급/지원은 유료

### ❌ 잘못된 라이선스

- 문제: MIT/Apache = 기업이 유료 라이선스 불필요
- 해결: AGPL (파생 작업 공개 강제) 또는 BSL

### ❌ 커뮤니티 무시

- 문제: Issue/PR 방치 = 신뢰 상실
- 해결: 최소 주 1회 응답, 핵심 기여자 인정

### ❌ 너무 이른 상업화

- 문제: 커뮤니티 구축 전 유료화 = 실패
- 해결: 1,000+ stars, 활발한 사용자 후 수익화

## When to Use This Pattern

### ✅ 이상적인 경우

- **개발자 도구**: CLI, 라이브러리, 플랫폼
- **Self-hosted 수요**: 기업이 온프레미스 선호
- **복잡한 운영**: DevOps, 데이터베이스, 인프라
- **보안 중요**: 금융, 의료, 정부

### ⚠️ 주의 필요

- **소비자 제품**: B2C는 오픈소스 이점 적음
- **단순한 제품**: 엔터프라이즈 기능 추가 어려움
- **빠른 수익 필요**: 커뮤니티 구축 시간 필요

### ❌ 피해야 할 경우

- **IP 보호 필수**: 알고리즘이 핵심 경쟁력
- **경쟁자 오픈소스**: 이미 무료 대안 존재
- **모바일 앱**: App Store 모델이 더 적합
- **콘텐츠 중심**: 오픈소스 이점 없음

## Related Patterns

- **Dual Licensing** - AGPL + 상업용 라이선스 분리
- **Community First** - 커뮤니티 구축 후 수익화
- **Enterprise Add-On** - 엔터프라이즈 전용 기능
- **Managed Hosting** - Self-hosted 제품의 호스팅 서비스
- **Building in Public** (common) - 오픈소스 = 궁극의 투명성

## Tactical Playbook

### 1단계: 오픈소스 준비 (1-2개월)

1. [ ] 라이선스 선택 (AGPL 권장, MIT/Apache 주의)
2. [ ] README 작성 (명확한 가치 제안, 설치 가이드)
3. [ ] CONTRIBUTING.md (기여 방법)
4. [ ] CODE_OF_CONDUCT.md (커뮤니티 규칙)
5. [ ] 이슈 템플릿, PR 템플릿

### 2단계: GitHub 최적화 (1주)

1. [ ] 매력적인 README (스크린샷, GIF, 데모)
2. [ ] Topics/Tags 설정 (검색 최적화)
3. [ ] GitHub Actions (CI/CD)
4. [ ] 릴리스 노트 자동화
5. [ ] Star/Fork 버튼 눈에 띄게

### 3단계: 커뮤니티 구축 (3-6개월)

1. [ ] Hacker News, Product Hunt 런칭
2. [ ] Reddit, Dev.to 커뮤니티 참여
3. [ ] Issue 빠른 응답 (< 24시간)
4. [ ] 첫 10명 기여자 환영 메시지
5. [ ] Discord/Slack 커뮤니티 (선택)

### 4단계: 엔터프라이즈 기능 정의 (2-3개월)

**오픈소스 (Core)**:

- [ ] 기본 기능 (80% 사용 케이스)
- [ ] Self-hosted 설치 가능
- [ ] 커뮤니티 지원

**엔터프라이즈 (Premium)**:

- [ ] SSO/SAML (Single Sign-On)
- [ ] RBAC (Role-Based Access Control)
- [ ] 감사 로그 (Audit Logs)
- [ ] SLA 지원 (24/7)
- [ ] 화이트 라벨링
- [ ] 우선 보안 패치
- [ ] 매니지드 호스팅

### 5단계: 수익화 시작 (커뮤니티 성숙 후)

1. [ ] Pricing 페이지 생성 (무료 vs. 엔터프라이즈)
2. [ ] 라이선스 키 시스템 구축
3. [ ] 영업 이메일 (sales@) 설정
4. [ ] 첫 5개 엔터프라이즈 고객 타겟팅
5. [ ] 케이스 스터디 작성

## License Selection Guide

### AGPL-3.0 (가장 권장)

- **효과**: 파생 작업 공개 강제 → 기업 유료 라이선스 구매
- **예**: Filestash, MongoDB (과거), Grafana
- **Trade-off**: 기업 채택 약간 느림, 커뮤니티는 환영

### MIT/Apache (주의)

- **효과**: 매우 관대함, 기업 채택 빠름
- **문제**: 기업이 유료 라이선스 불필요 → 수익화 어려움
- **예**: React, Vue (Meta/Evan You는 다른 수익원 있음)

### BSL (Business Source License)

- **효과**: 일정 기간 후 오픈소스로 전환
- **예**: CockroachDB, MariaDB MaxScale
- **Trade-off**: 진정한 오픈소스 아님, 커뮤니티 우려

## Pricing Strategy

### Tier 1: Free (Open Source)

- Self-hosted
- 커뮤니티 지원
- 기본 기능
- **Target**: 개인, 스타트업, 오픈소스 프로젝트

### Tier 2: Pro ($50-200/month)

- 모든 오픈소스 기능
- 우선 이메일 지원
- 고급 기능 일부
- **Target**: 소규모 팀, SMB

### Tier 3: Enterprise ($500-5,000/month)

- 모든 기능
- SLA 지원 (24/7)
- 화이트 라벨링
- SSO/RBAC
- 감사 로그
- 매니지드 호스팅 (선택)
- **Target**: 대기업, 규제 산업

### Add-ons

- 커스터마이징: $5,000-50,000 (프로젝트당)
- 컨설팅: $200-500/hour
- 트레이닝: $2,000-10,000/day

## Success Metrics

### 커뮤니티 지표

- GitHub Stars: 100 → 1,000 → 10,000+
- Contributors: 10 → 50 → 100+
- Monthly Active Users: 100 → 1,000 → 10,000+

### 수익 지표

- 첫 유료 고객: 3-6개월 (커뮤니티 성숙 후)
- $1K MRR: 1-2년
- $10K MRR: 2-4년
- Full-time income: 2-3년

### 전환율 (벤치마크)

- Open Source Users → Enterprise: 0.1-1%
- 10,000 오픈소스 사용자 → 10-100 엔터프라이즈 고객
- 100 엔터프라이즈 × $500/month = $50,000/month

## Case Study: Filestash

### Timeline

- **2016**: 프로젝트 시작, GNU AGPL-3.0 공개
- **2016-2024**: 8년 지속 개발
- **현재**: Near full-time income, $500+/month 엔터프라이즈 라이선스

### Key Decisions

1. **AGPL 라이선스**: 파생 작업 공개 강제
2. **확장 가능한 아키텍처**: 15+ storage backends
3. **엔터프라이즈 번들**: SLA + 화이트라벨 + 우선 패치
4. **커스터마이징 서비스**: 추가 수익원

### Revenue Streams

1. Enterprise licenses: $500+/month
2. Custom plugin development: Project-based
3. Configuration hardening: Consulting
4. Managed hosting (via partners)

### Results

- 8+ years sustained development
- Full-time income achieved
- Community trust established

## Sources

- Filestash (8 years, full-time income): HN thread 2024
- Video Hub App ($500/month, open source): HN threads 2018-2025
- Open Core Summit: <https://opencoresummit.com/>
- AGPL licensing guide: <https://www.gnu.org/licenses/agpl-3.0.en.html>

---

**Last Updated:** 2024-12-20
**Pattern Strength:** ⭐⭐⭐⭐ (개발자 도구에 매우 효과적)
**Reproducibility:** ⭐⭐⭐ (커뮤니티 구축 시간 필요, 인내심 요구)
