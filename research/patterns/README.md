# Success Pattern Library

이 디렉토리는 성공한 인디 개발자와 소규모 팀의 사업에서 추출한 재현 가능한 패턴들을 저장합니다.

## 디렉토리 구조

### `common/` - 공통 필수 패턴
모든 성공한 사업이 공통적으로 적용한 필수 패턴들입니다. 사업을 할 때 **반드시** 고려해야 하는 방법들입니다.

예시:
- `validate-before-build.md` - 만들기 전에 검증하기
- `build-in-public.md` - 공개적으로 만들기
- `focus-on-distribution.md` - 유통에 집중하기

### `idea-discovery/` - 아이디어 발견
사업 아이템을 찾는 방법들입니다. **성공 확률 높은 순서**로 정렬됩니다.

예시:
- `scratch-your-own-itch.md` - 자신의 문제 해결하기
- `observe-market-gaps.md` - 시장 공백 관찰하기
- `productize-services.md` - 서비스를 제품화하기

### `validation/` - 아이디어 검증
아이디어를 빌드하기 전에 검증하는 방법들입니다. **신뢰도 높은 순서**로 정렬됩니다.

예시:
- `landing-page-test.md` - 랜딩 페이지 테스트
- `manual-first-approach.md` - 수동으로 먼저 해보기
- `pre-sell-validation.md` - 사전 판매로 검증하기

### `mvp-building/` - MVP 개발
최소 기능 제품을 만드는 전략들입니다. **출시 속도 빠른 순서**로 정렬됩니다.

예시:
- `no-code-first.md` - 노코드 도구 먼저 사용
- `manual-behind-curtain.md` - 뒤에서 수동으로 처리
- `feature-prioritization.md` - 기능 우선순위 정하기

### `customer-acquisition/` - 초기 고객 확보
첫 10-100명의 고객을 확보하는 방법들입니다. **냉시작 효과성 높은 순서**로 정렬됩니다.

예시:
- `direct-outreach.md` - 직접 연락하기
- `founder-led-sales.md` - 창업자가 직접 영업
- `niche-community-targeting.md` - 틈새 커뮤니티 타겟팅

### `product-market-fit/` - 제품-시장 적합성
PMF를 달성하고 인식하는 방법들입니다. **신호 명확성 높은 순서**로 정렬됩니다.

예시:
- `iterate-with-feedback.md` - 피드백으로 반복 개선
- `retention-over-acquisition.md` - 획득보다 유지에 집중
- `find-power-users.md` - 파워 유저 찾기

### `growth/` - 성장 전략
PMF 달성 후 확장하는 전략들입니다. **ROI 높은 순서**로 정렬됩니다.

예시:
- `content-marketing.md` - 콘텐츠 마케팅
- `seo-driven-growth.md` - SEO 기반 성장
- `viral-mechanics.md` - 바이럴 메커니즘

### `monetization/` - 수익화 모델
비즈니스 모델과 가격 전략입니다. **예측 가능성 높은 순서**로 정렬됩니다.

예시:
- `freemium-to-paid.md` - 프리미엄에서 유료로
- `usage-based-pricing.md` - 사용량 기반 가격
- `lifetime-deals.md` - 평생 이용권

### `distribution/` - 유통 채널
고객에게 도달하는 채널과 플랫폼입니다. **레버리지 높은 순서**로 정렬됩니다.

예시:
- `app-store-optimization.md` - 앱 스토어 최적화
- `marketplace-strategy.md` - 마켓플레이스 전략
- `integration-ecosystem.md` - 통합 생태계

### `retention/` - 고객 유지
장기적으로 고객을 유지하는 전략들입니다. **임팩트 높은 순서**로 정렬됩니다.

예시:
- `onboarding-excellence.md` - 온보딩 최적화
- `habit-forming-features.md` - 습관 형성 기능
- `community-engagement.md` - 커뮤니티 참여

### `differentiation/` - 차별화
경쟁이 많은 시장에서 차별화하는 전략들입니다. **방어 가능성 높은 순서**로 정렬됩니다.

예시:
- `niche-specialization.md` - 틈새 전문화
- `unique-positioning.md` - 독특한 포지셔닝
- `design-as-differentiator.md` - 디자인으로 차별화

## 패턴 사용법

### 1. 사업 아이템 찾을 때
`idea-discovery/` 폴더의 패턴들을 성공 확률 순서대로 확인하고 적용합니다.

### 2. 아이디어 검증할 때
`validation/` 폴더의 방법들을 신뢰도 순서대로 사용합니다.

### 3. MVP 만들 때
`mvp-building/` 폴더의 전략들을 속도 순서대로 고려합니다.

### 4. 성장시킬 때
`growth/` 폴더의 전략들을 ROI 순서대로 테스트합니다.

### 5. 비즈니스 모델 정할 때
`monetization/` 폴더의 모델들을 예측 가능성 순서대로 평가합니다.

## 패턴 조합

성공한 사업들은 보통 여러 패턴의 조합을 사용합니다:

**예시 조합:**
```
idea-discovery/scratch-your-own-itch.md
→ validation/manual-first-approach.md
→ mvp-building/no-code-first.md
→ customer-acquisition/direct-outreach.md
→ product-market-fit/iterate-with-feedback.md
→ growth/content-marketing.md
```

각 패턴 파일에서 "Related Patterns" 섹션을 확인하여 자연스러운 조합을 찾을 수 있습니다.

## 패턴 파일 구조

각 패턴 파일은 다음 구조를 따릅니다:

- **What Is This Pattern?** - 패턴 설명
- **How It Works** - 단계별 실행 방법
- **Real Examples** - 실제 사례 (성공도 순 정렬)
- **Why This Works** - 작동 원리 분석
- **Prerequisites** - 필요 조건
- **Common Mistakes** - 흔한 실수
- **When to Use** - 적합한/부적합한 상황
- **Related Patterns** - 관련 패턴
- **Sources** - 출처

## 업데이트 규칙

1. 새로운 성공 스토리 분석 시, 해당되는 패턴 파일에 사례 추가
2. 각 카테고리 내에서 성공 확률/효과성/속도 등으로 재정렬
3. 패턴이 여러 스토리에서 검증되면 "Success Rate" 업데이트
4. 새로운 패턴 발견 시, 적절한 카테고리에 새 파일 생성

## 생성 도구

이 패턴들은 `success-formula-analyzer` 스킬이 자동으로 생성하고 업데이트합니다.
