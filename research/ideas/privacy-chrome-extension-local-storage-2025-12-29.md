---
title: 프라이버시 중심 Chrome Extension (로컬 저장)
idea-date: 2025-12-29
business-model: One-Time Purchase Browser Extension
revenue-timeline: Week 2-3부터 가능
difficulty: ⭐⭐ (쉬움-중간)
risk-level: Low
estimated-month-1-revenue: ₩495,000 - 990,000
tags: [idea, chrome-extension, privacy, one-time-purchase]
type: Business Idea
---

# 프라이버시 중심 Chrome Extension

## 한 줄 요약

YouTube/Instagram 등 시청/활동 기록을 100% 로컬 저장하는 Chrome Extension. 서버 전송 0, 프라이버시 보장.

## 비즈니스 모델

**타입:** One-Time Purchase (평생 사용)
**가격:** ₩9,900 - 19,900
**플랫폼:** Chrome Web Store
**수익:** 판매당 순수익 (Google 수수료 5%)

## 아이디어 예시

### #1: YouTube History Keeper
```
문제: YouTube 시청 기록 → Google 서버 (추적)
해결: 100% 로컬 저장, Google 추적 차단

기능:
- 시청한 영상 자동 저장 (로컬)
- 검색 가능 (제목, 채널)
- Export (JSON, CSV)
- Google 서버 전송 0%
```

### #2: Instagram Feed Archiver
```
문제: 인스타 피드 사라짐 (계정 삭제 시)
해결: 피드를 로컬에 아카이브

기능:
- 피드 자동 백업 (이미지 + 텍스트)
- 오프라인 열람
- 검색 기능
```

### #3: Naver Search History Local Backup
```
문제: 네이버 검색 기록 → 네이버 서버
해결: 로컬 저장 + 통계

기능:
- 검색어 로컬 저장
- 통계 (많이 검색한 키워드)
- 서버 전송 차단
```

## 실행 계획 (2주)

### Week 1: 개발
```yaml
Day 1-3: ChatGPT로 코드 생성
  - Manifest V3 (최신 Chrome Extension)
  - LocalStorage API
  - YouTube Data 파싱

Day 4-5: 테스트 및 버그 수정
  - 로컬 테스트 (chrome://extensions)
  - 10명 베타 테스터

Day 6-7: 패키징
  - Chrome Web Store 리스팅
  - 스크린샷 5장
  - 설명 작성 (프라이버시 강조)
```

### Week 2: 런칭
```yaml
Day 8: Chrome Web Store 제출
  - 등록비: $5
  - 검수: 1-3일

Day 9-10: Show HN 런칭
  - Reddit r/privacy 홍보

Day 11-14: 첫 판매 및 리뷰 축적
  - 목표: 5-star 리뷰 10개
```

## 차별화

### 1. 100% 로컬 (No Server)
```
경쟁자: 대부분 서버에 데이터 전송
나: 100% 로컬, 서버 0%

신뢰: Open source (GitHub 공개)
```

### 2. 한국 플랫폼 지원
```
독특한 포지셔닝:
- "네이버 검색 기록 로컬 백업"
- "카카오톡 웹 대화 백업"

경쟁: 없음 (한국 특화)
```

### 3. Export 기능
```
데이터 소유권:
- JSON/CSV 내보내기
- 다른 도구로 분석 가능
```

## 예상 수익

### Month 1
```
Show HN + Reddit:
- Day 1-7: 50 판매 × ₩9,900 = ₩495,000
- Week 2-4: 50 판매 × ₩9,900 = ₩495,000

총: ₩990,000
Google 수수료 (5%): -₩49,500
순수익: ₩940,500
```

### Month 3
```
유기적 판매:
- Chrome Web Store 검색
- 월 100-200 판매

수익: ₩990,000 - 1,980,000/월
```

## 리스크

**Chrome Extension 정책 위반**
- 완화: Manifest V3 준수
- 완화: Privacy Policy 명확히

**경쟁 Extension 등장**
- 완화: 한국 특화 (진입 장벽)
- 완화: Open source (신뢰)

## 확장 경로

**Month 2:** Firefox 버전
**Month 3:** Safari Extension
**Month 6:** 프리미엄 기능 (₩29,900)

## Success Metrics

- [ ] Week 2: Chrome Web Store 등록
- [ ] Month 1: 100 판매
- [ ] Month 3: 5-star 평점 30+개

## 관련 패턴

- **Monetization:** [One-Time Purchase](../patterns/monetization/one-time-purchase.md)
- **MVP:** [Ship in One Week](../patterns/mvp-building/ship-in-one-week.md)

---

**추천도:** ⭐⭐⭐⭐ (4/5) - 빠른 개발, 프라이버시 트렌드
**난이도:** ⭐⭐ (2/5) - ChatGPT로 코드 생성 가능
