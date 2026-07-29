# Semantic Boundary Design

## 역할과 경계

의미를 정하는 결정마다 owner 하나를 배정해 semantic drift를 막는다. 여러 계층이 같은 데이터를 관찰, 전달, 표시할 수 있지만 identity, lifecycle, permission, command, route, event, compatibility, presentation의 의미는 한 곳에서만 결정한다.

하나의 사용자·도메인 capability가 여러 representation을 지나며 의미 규칙이 중복되거나 caller가 추론하거나 adapter가 보존하기 시작할 때 쓴다. 현재 owner를 읽기 전용으로 찾는 일, owner 확정 뒤 local 코드 구조화, 순수 async 반응성·최신성, 변경 범위 통제는 각각 source-owner 감사, 구조 작업, interactive-state flow, 범위 소유 workflow로 넘긴다. 제외된 concern이 주 문제라면 여기서 owner ledger나 해법을 만들지 말고, 구현 메커니즘 없이 관찰된 동작과 제약만 넘긴다.

## Owner Ledger

1. capability를 사용자 또는 도메인 용어로 이름 붙인다.
2. 관련 representation crossing만 확인한다. record/read model, UI draft·intent, route/query state, command input, API payload, result/event/patch, presentation model, compatibility adapter가 해당할 수 있다.
3. drift될 결정을 나열한다. identity/alias, lifecycle/status, permission/capability, command·navigation grammar, projection/presentation, compatibility, representation 사이 freshness/fallback/revision 의미가 해당할 수 있다.
4. decision마다 owner 하나만 배정한다. 현재 근거와 권한이 모두 뒷받침할 때만 가장 작은 durable owner를 고른다. 그렇지 않으면 `decision needed -> missing evidence/authority`로 남기고, 결정 주체도 근거가 있거나 명시됐을 때만 적는다.
5. caller 경계를 정한다. caller는 전달, 선택, 호출, 표시, 렌더링할 수 있지만 자신이 소유하지 않은 의미를 해석, 정규화, 재결정하거나 policy로 보존하지 않는다.

현재 task가 정당화하는 범위만 refactor한다. 의미 소유권은 더 넓은 정리나 구현 우선순위를 허가하지 않는다.

## 배치 규칙

- record identity와 field alias는 record 또는 contract owner가 맡는다.
- 사용자 intent는 UI surface나 command-input owner가, 최종 command payload는 session 또는 command owner가 맡는다.
- business request parsing은 framework wrapper가 아니라 application route가 맡는다. 공용 route/query grammar는 navigation owner가 맡는다.
- permission과 capability는 policy owner가, label과 action은 surface 또는 view-model owner가 맡는다.
- result envelope, event, patch, resync 의미는 application/realtime result owner가 맡는다.
- representation 사이 stale, pending, fallback, conflict, revision 수용은 해당 의미 계약을 소유한 route, session, screen이 맡는다. 순수 async behavior는 이 스킬 밖에서 다룬다.
- adapter는 shape를 변환한다. 제품 policy는 근거 있는 명시적 배정이 있을 때만 소유한다.

근거로 확인된 owner 밖의 fallback chain, 중복 status check, caller가 만든 최종 payload, wrapper의 business parsing, 반복된 freshness key, policy를 보존하는 adapter는 결정이 owner 밖으로 샜다는 근거다. 새 계층을 만들라는 자동 지시는 아니다.

## Guard와 이관

안정된 owner 경계를 보호하는 가장 작은 contract, boundary, negative, type/schema, user-visible regression test를 둔다. owner가 의미를 한 번만 결정하고 caller가 조용히 다른 의미를 고를 수 없음을 검증하며 helper 내부 구현은 고정하지 않는다.

task에 필요한 만큼만 capability, 주요 crossing, owner ledger, caller 경계, 관찰된 누수, guard, 미확정 결정을 보고한다. 기준 source 탐색, 확정된 local 구조, 순수 async interaction, 범위 통제가 주 문제가 되면 owner ledger를 보존해 해당 workflow로 넘기고, 새 근거나 권한 없이 의미를 재배정하지 않게 한다.
