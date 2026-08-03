# Decisions

**2026-08-03**

- **Background:** canonical `structure-first`는 다른 owner의 증거가 드러난 경우에만 가장 작은 관련 단위를 다시 열고, safe owner witness가 없는 경계를 국소 테스트만으로 닫지 않도록 교정됐다.
- **Decision:** 제품 역할과 trigger를 유지한 채 Project Legibility `0.7.1` patch release로 조립한다.
- **Why:** 기존 smallest-current-unit 경계를 유지하는 호환 가능한 instruction 교정이며 자동 재귀나 production·전체 end-to-end 기본 요구를 추가하지 않는다.
- **Impact:** 설치 사용자는 국소 검증의 장점을 유지하면서 cross-boundary ownership 누락으로 성급히 완료되는 작업을 줄일 수 있다.
