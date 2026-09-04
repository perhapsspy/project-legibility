# Purpose-First Design 코어 채택 결과

## 결정

`purpose-fit-design`을 `purpose-first-design`으로 바꾸고, 목적과 확정 경계에서 가장 작은 충분한 방향을 정하는 역할을 코어로 채택한다. 답변이 새로 만든 불필요한 범위·약속·가정·열린 결정을 제거하는 `Final Reduction`을 필수 완료 검사로 포함한다.

소거는 스킬의 이름이나 호출 조건이 아니라 방향 결정 뒤에 수행하는 완료 검사다. 확정 의미를 다시 열거나 보안, 롤백, 소유권, 운영과 입증된 실패 대응에 필요한 복잡성을 제거해서는 안 된다.

## 근거

V2는 같은 fixture와 두 개의 독립 block에서 기존 스킬과 개선된 core를 비교하고, 개선된 core가 만든 frozen draft에 동일주의 placebo와 `Final Reduction`을 각각 적용했다. 전체 70회 호출은 모두 완료됐다.

- 개선 core 대 기존 스킬: `8승 / 6무 / 2패`, 서로 다른 fixture의 반복 승리 2개, 반복 패배와 hard failure 0. 사전등록 core gate를 통과했다.
- `Final Reduction` 대 placebo: `9승 / 7무 / 0패`, 반복 승리 1개, 반복 패배·hard failure·필요 복잡성의 과잉 제거 0.
- reduction gate는 서로 다른 fixture의 반복 승리 2개를 요구했으나 1개만 확인되어 통과하지 못했다.

## 해석

실험의 사전등록 판정은 `revised_core_only_supported`로 보존한다. reduction gate를 사후에 통과로 바꾸거나 모든 설계 문제에 일반화된 효과가 입증됐다고 주장하지 않는다.

V2는 synthetic forced-invocation 평가이므로 routing이나 이름만의 효과를 입증하지 않는다. 이름 변경은 역할을 목적 우선 방향 결정으로 명확히 하려는 제품 결정이며, 별도의 실험 결과로 표현하지 않는다.

사용자는 0패와 안전성 위반 0, placebo 대비 일관된 개선 신호를 근거로 `Final Reduction`을 제한적으로 채택했다. 이후 새로운 사례에서 필요한 경계를 제거하거나 불필요한 범위를 추가하는 실패가 반복되면 문구와 적용 범위를 다시 검토한다.
