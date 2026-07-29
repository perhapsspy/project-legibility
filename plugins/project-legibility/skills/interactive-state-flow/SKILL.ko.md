# Skill: Interactive State Flow (Korean Pair)

> 영문 기본 문서: `SKILL.md`
>
> 설명 동기화: 사용자 의도, 기준 상태, 파생 표현, 비동기 IO, 스케줄링, 백그라운드 작업이 섞여 인터랙션이 느리거나 오래된 결과와 race가 생길 때 사용한다. 기준 상태를 빠르게 기록하고 긴급 경로를 보호하며, freshness를 소유한 경계만 비동기·표현 결과를 받아들이게 한다.

## 목적

사용자 의도, 비용이 큰 표현, 비동기 작업이 서로 다른 속도로 진행될 때도 인터랙티브 소프트웨어의 반응성과 정확성을 유지합니다.

입력, 선택, navigation, 검색, preview, streaming, realtime update, 파일·로그 뷰 등에서 관찰 가능한 지연, 오래된 결과 위험, 책임 혼합이 있을 때 사용합니다. async work, caching, effect가 있다는 이유만으로 작고 명확하며 반응성 좋은 코드에 상태나 스케줄링 경계를 추가하지 않습니다.

## 실행 계약

### 기준 상태를 빠르게 유지한다

비용이 큰 파생이나 표현을 기다리지 않고 interaction이 소유한 intent 또는 input state를 기록하며, authoritative source state는 그 owner를 통해 commit합니다. 이는 동기 렌더링이나 성급한 durable mutation을 요구하지 않으며, persistence는 자체 권한과 순서 계약을 따릅니다. 표현 상태에는 filtered rows, preview, rendered range, pending·cached·stale·progressive output이 포함됩니다.

표현은 반응성을 보존하면서 현재 진실을 오도하지 않을 때만 늦게 따라올 수 있습니다. 후속 비용을 줄이려고 UI 계약상 현재인 상태까지 debounce하지 말고 그 결과 작업을 지연합니다. 지연된 commit 자체가 명시된 제품 동작이면 예외입니다.

### 긴급 경로를 필요한 만큼만 보호한다

기법을 고르기 전에 사용자에게 보이는 계약을 정합니다.

- 무엇이 즉시 갱신되어야 하는가
- 무엇이 늦거나 생략되거나 stale로 남아도 되는가
- 어떤 맥락 변화가 결과를 폐기하게 하는가
- 어느 경계가 결과 커밋을 승인하는가

후속 작업을 책임, 긴급도, 비용, 가시성, freshness 위험으로 분류합니다. 그 뒤 사용자에게 보이는 계약을 만족하는 가장 단순한 수단을 선택합니다.

debounce, memoization, transition, worker 같은 기법에서 출발하지 않습니다. 다른 thread나 process로 작업을 옮기는 일은 상호작용 경로를 실제로 보호하고 입력, 출력, 소유권, 순서, 취소, 실패 동작이 명확할 때만 정당합니다. 전달과 조정 비용도 포함합니다. 백그라운드 작업은 candidate를 반환하며 accepting owner를 우회해 현재 UI나 표현을 바꾸면 안 됩니다.

### freshness owner를 통해 커밋한다

완료됐다고 현재 output이 되는 것은 아닙니다. 보이거나 공유된 상태에 영향을 줄 수 있는 지연 output은 그것을 틀리게, 권한 밖으로, 또는 더 이상 유용하지 않게 만드는 모든 변화를 관찰할 수 있는 가장 좁은 기존 owner를 통과해야 합니다. Superseding intent, operation lane, source revision, selection, lifecycle, session scope는 예시이지 필수 checklist가 아닙니다.

완료 순서가 바뀔 수 있으면 명시적 identity를 사용하고, 시작 시 캡처한 값만이 아니라 현재 owner가 가진 identity와 비교합니다. 취소는 불필요한 작업을 줄이지만 완료와 race할 수 있으므로 최종 commit gate를 대신하지 않습니다.

완료 전체를 gate합니다. 보이거나 공유된 상태를 바꿀 수 있는 data, progress, error, terminal state, follow-up effect가 모두 대상입니다. 오래된 operation이 다른 operation의 loading·error 상태를 끝내면 안 됩니다. 유한 operation에는 명시된 terminal transition이 있어야 합니다. Superseded·disposed lane은 살아 있는 상태가 영원히 pending으로 남지 않도록 pending ownership을 clear, transfer, retire해야 합니다.

Latest-intent 규칙은 operation이 서로를 대체하는 lane 안에서만 적용합니다. 독립적이거나 누적되는 operation에는 자체 identity, ordering, merge rule이 필요합니다.

Domain acceptance와 현재 화면의 presentation acceptance는 서로 다른 owner와 수명을 가질 수 있습니다. 유효한 upload, index, content-addressed cache 결과는 시작 화면이 바뀌었다고 버릴 필요가 없지만 presentation acceptance 없이 새 화면에 붙이면 안 됩니다. 지연 작업이 durable·shared state를 바꾸면 mutation owner가 effect 경계에서 필요한 ordering, serialization, deduplication, revision precondition을 보장해야 합니다. Stale response를 버리는 것만으로 이미 적용된 effect를 되돌릴 수는 없습니다.

필요한 admission을 기존 owner가 올바르게 판단할 수 없을 때만 새 ownership boundary를 만듭니다. 오래된 output이 최신 상태를 덮거나, 교체된 화면에 붙거나, 대체된 stream을 계속하게 두지 않습니다.

### 제품 정책은 정본을 따른다

이 스킬은 stale content를 계속 보여도 되는지, pending 표시가 필요한지, 어떤 cached·progressive 결과가 허용되는지 결정하지 않습니다. 제품 계약의 owner를 따릅니다. 이 정책이 미정이고 정확성에 영향을 주면 조용히 새로 정하지 말고 결정을 드러냅니다.

Stale output이 허용되더라도 차이가 사용자에게 중요하면 current output과 구분합니다. 존재하는 모든 상태가 아니라 현재 활성화됐거나 곧 유용할 맥락을 위한 표현만 만듭니다.

## 검증 계약

스케줄러 내부가 아니라 동작을 검증합니다.

- interaction이 소유한 intent 또는 input이 빠르게 최신이 된다.
- 비용이 큰 작업이 필요한 즉시 피드백을 막지 않는다.
- 하나의 superseding lane에서 request A가 B보다 먼저 시작하고 늦게 끝나도 B를 덮지 못한다.
- 오래된 data, progress, error, terminal, follow-up effect가 현재 lane을 바꾸지 못한다.
- 독립 operation이 전역 latest-wins 규칙 때문에 폐기되지 않는다.
- 허용된 stale, cached, pending, progressive 표현이 제품 계약과 맞는다.
- durable effect는 response handler만이 아니라 mutation owner에서 순서를 보장한다.
- 실행 경계의 실패와 disposal 뒤에도 현재 pending 상태가 정확하다.

구조를 refactor한 모양만으로 지연이나 race가 해결됐다고 판단하지 않습니다. 안정된 ownership 경계의 focused test와 가장 작은 유용한 interaction·performance 근거를 우선합니다. 검사를 실행할 수 없으면 이유와 다음으로 유용한 검사를 남깁니다.

## 경계

이 스킬을 일반 UI debugging, backend throughput tuning, 제품 정책 결정, background execution 의무로 사용하지 않습니다. 작업에서 근거가 확인된 인터랙티브 반응성, freshness, commit ownership 문제만 해결합니다.
