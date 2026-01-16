# 에어드랍 파밍 사이드 비즈니스 - Feasibility 평가 보고서

**Project:** 체계적인 에어드랍 파밍 사이드 비즈니스
**Date:** 2025-01-11
**Overall Feasibility:** 6.4/10
**Recommendation:** 🟡 ITERATE (조건부 진행)

---

## Executive Summary

**Can I build this?** Yes, with modifications

**Confidence level:** Medium (65%)

**Key blockers:**
1. 높은 불확실성 (에어드랍 발생 확률 10-15%)
2. Sybil 탐지 고도화로 스케일 파밍 리스크 증가

**Recommended action:** Option A (개인 파밍)로 시작, 경험 축적 후 확장 검토

**Why this assessment:**
- Technical: 기본 기술 충분, 자동화는 부분적으로만 가능
- Market: 검증된 수익 사례 존재하나, 경쟁 심화 및 ROI 하락 추세
- Financial: 초기 비용 낮으나, 수익 불확실성 높음
- Time: 시간 투자 대비 수익 가능하나, 대기 시간 길음

---

## 1. Technical Feasibility: 7/10 ✅

### Skills Assessment

| 스킬 | 본인 수준 | 필요 수준 | Gap |
|------|-----------|-----------|-----|
| 크립토 지갑 사용 | 7/10 | 7/10 | None |
| DeFi 프로토콜 이해 | 5/10 | 7/10 | Small |
| 트랜잭션/가스 관리 | 5/10 | 6/10 | Small |
| 자동화 스크립팅 | 6/10 | 5/10 | None (초과) |
| 리스크 관리 | 5/10 | 7/10 | Medium |

**Learning required:** 2-4주 (DeFi 심화, 리스크 관리)

### Complexity Analysis

| 컴포넌트 | 복잡도 | 전문성 | 리스크 |
|----------|--------|--------|--------|
| 지갑 설정 & 관리 | 3/10 | 7/10 | Low |
| 프로토콜 상호작용 | 5/10 | 5/10 | Medium |
| 자동화 구현 | 6/10 | 6/10 | Medium |
| Sybil 회피 전략 | 7/10 | 4/10 | High |
| 수익 최적화 | 6/10 | 5/10 | Medium |

**Risk summary:**
- Critical risks: 0
- High risks: 1 (Sybil 탐지 회피)
- Medium/Low risks: 4

### 자동화 가능성 평가

| 활동 유형 | 자동화 수준 | 현실적 구현 |
|-----------|-------------|-------------|
| SNS 태스크 | ✅ 90% | 쉬움 |
| 테스트넷/파싯 | ✅ 80% | 쉬움 |
| 브릿지/스왑 | ⚠️ 50% | 부분적 (서명 필요) |
| 트레이딩 볼륨 | ⚠️ 40% | 제한적 |
| LP/스테이킹 | ❌ 20% | 수동 권장 |
| 거버넌스 | ❌ 10% | 수동 필수 |

**자동화 결론:** 핵심 온체인 활동은 부분 자동화만 가능. 완전 자동화는 비현실적.

**Technical feasibility score: 7/10** ✅

---

## 2. Market & Competition: 6/10 ⚠️

### Competitive Landscape

**참여자 유형:**

| 유형 | 규모 | 장점 | 위협도 |
|------|------|------|--------|
| 전문 파머 (풀타임) | 수천 명 | 시간, 자본, 도구 | High |
| 봇/자동화 운영자 | 수백 명 | 스케일, 효율성 | High |
| 캐주얼 파머 | 수백만 명 | 진정성, 탐지 회피 | Medium |
| 기관/VC | 소수 | 자본, 네트워크 | Medium |

**시장 트렌드:**

| 요소 | 방향 | 영향 |
|------|------|------|
| 에어드랍 규모 | ↑ 증가 | Positive |
| 참여자 수 | ↑ 급증 | Negative |
| 개인 할당량 | ↓ 감소 | Negative |
| Sybil 탐지 | ↑ 강화 | Negative |
| 커뮤니티 중심 분배 | ↑ 증가 | Positive |

### Revenue Model Reality Check

**단기 수익 (Month 1-3):**
- 예상 참여 프로젝트: 5-10개
- 에어드랍 발생 확률: 10-15%
- 예상 수령 프로젝트: 0-1개
- 예상 수익: $0 ~ $500 (운에 따라)

**중기 수익 (Month 6-12):**
- 누적 참여 프로젝트: 15-30개
- 예상 수령 프로젝트: 2-4개
- 예상 연간 총 수익: **$1,000 ~ $10,000**
- 시간당 수익 환산: $5 ~ $50/시간

**Long-tail 대박 가능성:**
- 확률: 5-10%
- 잠재 수익: $10,000 ~ $50,000+

### 2026년 기회 평가

| 프로젝트 | 확정도 | 예상 규모 | 참여 난이도 | 기회 점수 |
|----------|--------|-----------|-------------|-----------|
| OpenSea (SEA) | ★★★★☆ | ★★★★★ | ★★★☆☆ | 8/10 |
| Polymarket (POLY) | ★★★★☆ | ★★★★★ | ★★★☆☆ | 8/10 |
| MetaMask (MASK) | ★★★★★ | ★★★★★ | ★★☆☆☆ | 9/10 |
| MegaETH (MEGA) | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | 7/10 |
| Lighter (LIT) | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | 6/10 |

**Market feasibility score: 6/10** ⚠️

---

## 3. Financial Feasibility: 7/10 ✅

### Costs

**Initial (Option A - 개인 파밍):** $500 ~ $2,000 ✅

| 항목 | 최소 | 권장 |
|------|------|------|
| 운영 자금 (가스비 등) | $300 | $1,500 |
| 도구 (지갑 등) | $0 | $0 |
| 학습 비용 | $0 | $0 |

**Monthly Operating Costs:**

| 항목 | Option A | Option B (스케일) |
|------|----------|-------------------|
| 가스비/수수료 | $50-150 | $200-500 |
| Proxy/VPN | $0 | $50-100 |
| Antidetect 브라우저 | $0 | $100-300 |
| 총 월간 비용 | **$50-150** | **$350-900** |

### ROI 시나리오 분석

**보수적 시나리오 (하위 25%):**
- 연간 투자: $1,500 (자금 + 비용)
- 연간 수익: $500
- ROI: -67% ❌

**현실적 시나리오 (중간값):**
- 연간 투자: $2,000
- 연간 수익: $3,000
- ROI: +50% ✅

**낙관적 시나리오 (상위 25%):**
- 연간 투자: $2,500
- 연간 수익: $15,000
- ROI: +500% ✅✅

**Personal runway:** 충분 (사이드 비즈니스로 손실 감당 가능)

**Break-even:** 월 $100-200 수익 시 (Option A 기준)

**Financial feasibility score: 7/10** ✅

---

## 4. Time Feasibility: 5/10 ⚠️

### Timeline

**첫 수익까지:** 3-12개월 (에어드랍 타이밍 의존)

**Major tasks:**

| Phase | 기간 | 주간 시간 |
|-------|------|-----------|
| 학습 & 설정 | 2주 | 10-15시간 |
| 초기 파밍 | 1개월 | 10-15시간 |
| 확장 & 최적화 | 3개월 | 10-15시간 |
| 유지 관리 | 지속 | 5-10시간 |

**문제점:**
- 수익 실현까지 **대기 시간이 김** (에어드랍 배포까지)
- 지속적인 모니터링 필요
- 시장 변화에 빠른 대응 필요

### Opportunity Cost 분석

| 대안 | 예상 시간당 수익 | 확실성 |
|------|-----------------|--------|
| 에어드랍 파밍 | $5-50/시간 | Low |
| 프리랜싱 | $30-100/시간 | High |
| 사이드 프로젝트 | $0-∞ | Medium |
| 코인 트레이딩 | -∞ ~ +∞ | Very Low |

**결론:** 시간 투자 대비 수익 불확실성이 높음. 다만, 패시브 인컴 성격이 있어 다른 활동과 병행 가능.

**Time feasibility score: 5/10** ⚠️

---

## Overall Feasibility: 6.4/10

```
Feasibility = (Technical × 30%) + (Market × 30%) + (Financial × 20%) + (Time × 20%)
            = (7 × 0.3) + (6 × 0.3) + (7 × 0.2) + (5 × 0.2)
            = 2.1 + 1.8 + 1.4 + 1.0
            = 6.3/10 → 반올림 6.4/10
```

**Interpretation:** 🟡 Feasible with effort, manageable risks

---

## Risk Assessment

### Critical Risks 🔴 (Must address)

1. **Sybil 탐지로 전체 에어드랍 탈락**
   - Impact: Critical (투자 시간/비용 전액 손실)
   - Probability: 30-50% (스케일 파밍 시)
   - Mitigation:
     - Option A (1-5 지갑)로 시작
     - 20개 미만 지갑 유지
     - 자연스러운 패턴 유지
   - Timeline: 항상 준수

2. **88% 토큰 가치 하락**
   - Impact: High (기대 수익 대폭 감소)
   - Probability: 88%
   - Mitigation:
     - 조기 매도 전략 수립
     - 클레임 즉시 50-80% 매도
     - 매도 타이밍 사전 결정
   - Timeline: 에어드랍 수령 직후

### High Risks 🟡 (Address early)

1. **에어드랍 미발생/취소**
   - Mitigation: 10+ 프로젝트 분산 참여, 확정된 프로젝트 우선

2. **가스비/수수료 손실**
   - Mitigation: 저비용 L2 활용, 가스 추적, 예산 엄수

3. **사기 프로젝트 참여**
   - Mitigation: VC 백업된 프로젝트만, 커뮤니티 검증 확인

### Monitored Risks 🟢 (Track)

1. **규제 리스크**: 세금 준비, 법적 변화 모니터링
2. **시장 변화**: 에어드랍 트렌드 지속 모니터링
3. **기술 변화**: 새로운 탐지 기법 등장 시 전략 수정

---

## Recommendation: 🟡 ITERATE (조건부 진행)

### Why ITERATE (not full PROCEED):

1. **높은 불확실성**: 수익 타이밍과 규모 예측 어려움
2. **시간 투자 vs 수익**: 확정적 ROI가 아님
3. **스케일 리스크**: 확장 시 Sybil 탐지 위험 급증

### What needs improvement:

| Dimension | 현재 | 목표 | 개선 방법 |
|-----------|------|------|-----------|
| Time | 5/10 | 7/10 | 자동화 도구 도입으로 시간 효율화 |
| Market 지식 | 6/10 | 8/10 | 1-2개월 실전 경험 축적 |
| 리스크 관리 | - | - | 손절 기준, 매도 전략 사전 수립 |

### 조건부 진행 조건:

**Option A (개인 파밍)으로 시작 시 진행 권장:**

- [ ] 초기 투자 $500 이하로 제한
- [ ] 1-3개 지갑으로 시작
- [ ] 3개월 후 수익 분석 및 재평가
- [ ] 손실 감당 가능한 금액만 투자

**Option B (스케일 파밍)는 현재 비권장:**
- Sybil 탐지 리스크 높음
- 추가 비용 발생
- Option A 경험 후 재검토

---

## Action Plan

### Immediate Actions (This Week)

1. **지갑 설정**
   - MetaMask, Phantom 설치
   - 버너 지갑 2-3개 생성
   - 시드 구문 안전하게 백업

2. **초기 자금 배치**
   - $200-500 투입
   - Ethereum, Arbitrum, Solana 분산

3. **정보 채널 구독**
   - Airdrops.io 즐겨찾기
   - Twitter/X 에어드랍 계정 팔로우
   - DC 에어드랍 갤러리 가입

### Week 2-4: 첫 파밍 시작

1. **MetaMask 포인트 파밍**
   - 지갑 내 스왑/브릿지 사용
   - 난이도: 쉬움, 리스크: 낮음

2. **Hyperliquid 트레이딩**
   - Arbitrum에서 USDC 브릿지
   - 소액 ($50-100) 트레이딩 시작

3. **활동 기록**
   - 스프레드시트로 모든 활동 추적
   - 가스비, 예상 에어드랍, 참여일 기록

### Month 2-3: 확장

1. 추가 프로젝트 참여 (LayerZero, Linea 등)
2. 테스트넷 참여
3. 자동화 도구 테스트 (선택사항)

### Month 3: 재평가

- [ ] 총 투자 vs 수익 분석
- [ ] 시간 투자 효율성 평가
- [ ] Option B 전환 여부 결정
- [ ] 계속/중단/확장 결정

---

## Success Probability & Expected Value

### 확률 기반 수익 예측 (Option A, 연간)

| 시나리오 | 확률 | 순수익 | 기대값 |
|----------|------|--------|--------|
| 손실 | 25% | -$1,000 | -$250 |
| 손익분기 | 30% | $0 | $0 |
| 소득 | 35% | +$2,000 | +$700 |
| 대박 | 10% | +$15,000 | +$1,500 |
| **총 기대값** | | | **+$1,950/년** |

### 결론

**Expected Value: +$1,950/년** (시간당 ~$4-8 환산)

- 고정 수입 대비 낮은 시간당 수익
- 그러나 **패시브 성격** + **대박 가능성** 포함
- 학습 + 경험 축적 가치 고려 시 합리적

---

## References

### Local Documents
- **Related idea spec:** [airdrop-farming-business-idea-2025-01-11.md](./airdrop-farming-business-idea-2025-01-11.md)
- **Success story research:** [crypto-airdrop-success-guide-2025-01-11.md](../stories/crypto-airdrop-success-guide-2025-01-11.md)

### Market Research
1. [Yahoo Finance - Five crypto airdrops 2026](https://finance.yahoo.com/news/five-crypto-airdrops-watch-2026-095648298.html)
2. [Bitget - Top Crypto Airdrops 2026 Guide](https://www.bitget.com/academy/top-crypto-airdrops-2026-complete-guide-upcoming-token-distributions-how-to-qualify)
3. [DL News - Five upcoming airdrops](https://www.dlnews.com/articles/defi/five-upcoming-crypto-airdrops-to-watch-for-in-2026/)

### Automation & Tools
4. [NFT Copilot - Airdrop Farming Bot](https://nftcopilot.com/airdrop-farming)
5. [Multilogin - Scale Airdrop Farming](https://multilogin.com/crypto/scale-your-airdrop-farming/)

### Sybil Detection
6. [Nansen - Linea Airdrop Sybil Detection](https://research.nansen.ai/articles/linea-airdrop-sybil-detection)
7. [Medium - Avoiding Being Flagged as Sybil](https://medium.com/@trialsincrypto/the-airdrop-farmers-guide-to-avoiding-being-flagged-as-sybil-c8a13e4a2c30)
8. [CoinGecko - What Sybil Attacks Are](https://www.coingecko.com/learn/sybil-attack)

### Success Cases
9. [The Block - Airdrop farmers make millions](https://www.theblock.co/post/225215/we-made-close-to-1-million-inside-the-murky-world-of-airdrop-farming)
10. [Decrypt - Hyperliquid $1.6B Airdrop](https://decrypt.co/294067/hyperliquid-airdrop-1-6-billion)

---

**Assessment completed:** 2025-01-11
**Next action:** Option A로 MetaMask 포인트 파밍 시작
**Status:** 조건부 진행 권장 - 소규모 시작 후 3개월 후 재평가
