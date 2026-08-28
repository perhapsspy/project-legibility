**2026-08-28**
- v1은 3과제 단일 표본이라 activation과 반복 안정성을 판정하지 못했다.
- v2는 6과제 × 6arm × 4회로 실행하고 staged arm만 같은 workspace의 독립 2-pass로 구성한다.
- correctness non-regression을 LOC보다 먼저 판정하고 동시 결합과 단계형 결합을 분리해야 runtime core 효과를 해석할 수 있다.
- 제품 변경은 제외하며 원시 출력은 저장소 밖에 두고 runner와 간결한 결과만 정식 owner에 보존한다.

**2026-08-28**
- Ponytail의 ponytail-review 정본은 finding만 반환하며 파일을 수정하지 않는다.
- staged arm은 Structure First full 구현 뒤 새 세션에서 Ponytail full을 current diff 축소 edit pass로 적용한다.
- read-only review를 수정 스킬처럼 사용하는 것보다 실제 변경 결과를 비교하면서 두 단계의 contract 우선순위를 유지할 수 있다.
- 결과 문서에서 staged를 ponytail-review 실행으로 부르지 않고 2-pass simplification으로 명시한다.

**2026-08-28**
- runtime core만 24/24 contract를 통과했고 staged는 21/24와 두 배 호출을 기록했다.
- runtime core를 후속 canonical source 후보로 승격하고 staged를 제외하되 이번 task에서는 정본·bundle을 변경하지 않는다.
- 차이가 root-cause 한 fixture에 집중돼 즉시 production 교체 근거는 부족하지만 짧은 owner-first 루프의 전달 효과는 반복 증거를 얻었다.
- 다음 source 작업은 모호한 owner·completion fixture를 늘려 core non-regression을 재검증한 뒤 progressive disclosure 구조를 canonical repository에서 적용한다.

**2026-08-28**
- 후속 A/B는 새 owner·completion 사례에서 세 arm 8/8, 판별 root-cause에서 current full 2/4·candidate main 4/4·candidate routed 3/4를 기록했다.
- runtime core의 의미를 main contract와 조건부 reference로 나눈 progressive-disclosure 후보를 정본에 반영한다.
- Structure First 정본과 Project Legibility source pin은 `11819e82afdb70f94bd5f7b8c1eb6df686eafcc2`로 맞춘다.
- 제품 역할·선택 조건은 유지하고 plugin version·release·publisher pin은 별도 release 작업에 둔다.
