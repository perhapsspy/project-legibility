# Structure First와 Ponytail 비교 v2

## 목표

Structure First의 전체 전문과 짧은 runtime core, Ponytail, 동시 결합과 2-pass 단계형 결합을 동일한 격리 Codex 과제에서 비교해 contract 준수와 구현 경제성의 차이를 반복 가능한 증거로 판정한다.

## 범위

- `gpt-5.6-luna` medium, arm별·과제별 4회 실행
- root cause, async lifecycle, native platform, stdlib, migration, cross-representation policy 과제
- correctness와 과제별 contract를 LOC보다 먼저 판정
- task·arm·반복별 독립 workspace와 숨은 결정론적 scorer
- 실행 로그와 생성 workspace는 저장소 밖 임시 output에 둔다.

제품 구성, Structure First 정본과 bundle snapshot은 이번 비교 결과만으로 변경하지 않는다. 후보 변경은 결과가 non-regression과 반복 안정성을 지지할 때 별도 source 작업으로 연다.

## 현재 상태

비교와 결과 해석을 완료했다. 일반 correctness는 모든 arm이 24/24였고 contract는 runtime core 24/24, baseline·Ponytail·combined 23/24, Structure First full 22/24, staged 21/24였다. 후속 source A/B에서 새 owner·completion 사례는 current full·candidate main·candidate routed가 모두 8/8을 통과했고, 판별 root-cause 사례는 각각 2/4·4/4·3/4였다.

검증된 progressive-disclosure 후보는 Structure First 정본 `11819e82afdb70f94bd5f7b8c1eb6df686eafcc2`에 반영됐다. Project Legibility bundle도 같은 SHA를 고정한다. 제품 역할과 선택 조건은 유지하며 plugin release는 별도 작업이 맡는다.

## 다음 단계

현재 task는 [최종 결과](FINAL-RESULTS.md)와 세 재현 runner를 근거로 종료한다.
