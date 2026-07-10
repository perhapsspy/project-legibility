# Semantic Boundary Design

## 목적

의미를 정하는 결정마다 owner를 하나만 두어 semantic drift를 막는다.

여러 계층이 같은 데이터를 observe, pass, render할 수는 있다. 하지만 identity, lifecycle, permission, command, route, event, compatibility, presentation의 의미를 결정하는 계층은 하나여야 한다.

## Use / Do Not Use

다음 cross-layer 작업 전이나 작업 중에 사용한다.

- 하나의 capability가 여러 representation을 지난다.
- alias, fallback, label, status, permission, lifecycle rule이 caller로 퍼진다.
- owner가 아닌 caller가 의미를 parse, normalize, translate, infer하기 시작한다.
- adapter가 shape translation을 넘어 product policy를 보존한다.
- test가 owner-boundary behavior가 아니라 helper internals를 고정한다.

다음 용도로는 쓰지 않는다.

- semantic boundary 이동이 없는 작은 local edit.
- 기존 owner를 읽기 전용으로 찾는 일. 이때는 `source-owner-audit`.
- owner가 명확한 뒤 local 변경 경계나 flow를 정리하는 일. 이때는 `structure-first`.
- 순수 async freshness, responsiveness, race-prone interaction 작업. 이때는 `interactive-state-flow`.
- change scope만 통제하는 일. 이때는 `structure-first`.

## 인접 스킬

- `source-owner-audit`는 현재 source owner를 근거로 찾는다. 이 스킬은 owner 배치가 설계 문제가 된 뒤 semantic decision을 배정한다.
- `structure-first`는 owner가 정해진 뒤 current unit의 경계를 잡고 구조를 다듬는다. 이 스킬은 capability-wide owner ledger에서 시작한다.
- `interactive-state-flow`는 freshness, pending, stale, async presentation behavior에 특화된다. 이 스킬은 freshness/fallback/revision이 representation 사이 semantic contract ownership일 때만 다룬다.

## Operating Flow

1. capability를 user/domain term으로 이름 붙인다.
2. representation crossings를 나열한다: source record, read model, UI draft, user intent, route/query state, command input, API payload, command result, realtime patch, presentation model, compatibility adapter.
3. semantic decisions를 나열한다: identity/alias, lifecycle/status, permission/capability, command grammar, route/navigation grammar, freshness/conflict/revision/pending/fallback, projection/presentation, compatibility.
4. decision마다 owner를 하나만 배정한다. 현재 source나 명시적 task context가 충분한 evidence와 authority를 보여줄 때만 가장 작은 durable owner를 고른다. 둘 중 하나라도 없으면 `decision needed -> missing evidence/authority`를 쓰고, 누가 결정해야 하는지는 그 decision owner가 근거로 확인되었거나 명시되었을 때만 적는다.
5. caller boundaries를 정한다: caller는 pass, select, invoke, display, render할 수 있다. owner가 아닌 caller는 interpret, normalize, re-decide, preserve policy를 하지 않는다.
6. 현재 task가 정당화하는 범위만 refactor한다.
7. semantic decision이 caller로 새면 실패하는 guard를 추가한다.
8. source discovery, local code shape, async freshness, scope control이 주제가 되면 해당 인접 스킬로 넘긴다.

## Owner Selection Rules

- Schema 또는 field alias -> record/contract owner.
- User intent shape -> UI surface 또는 command input owner.
- Final command payload -> session/command owner.
- API request parsing -> framework wrapper가 아니라 application route owner.
- Route 또는 query grammar -> navigation owner.
- Permission 또는 capability -> policy owner.
- Label과 action -> surface/view-model owner.
- Result envelope, patch, resync semantics -> application/realtime result owner.
- Stale, pending, fallback, conflict, revision acceptance -> freshness-owning route, session, screen owner.
- Compatibility behavior -> adapter는 shape를 translate한다. policy ownership은 명시적으로 배정해야 한다.

## Drift Smells

- record/contract owner 밖의 `x || y || z` fallback chain.
- 중복된 lifecycle 또는 status check.
- UI code가 record에서 final command payload를 직접 만든다.
- route component가 shared query grammar를 parse/build한다.
- API wrapper가 business request field를 읽는다.
- realtime 또는 event handler가 lifecycle, permission, policy를 다시 결정한다.
- revision, conflict, pending, fallback, freshness key가 중복된다.
- adapter가 owner에게 translate하지 않고 policy를 보존한다.
- test가 owner-boundary behavior가 아니라 helper internals를 assert한다.

## Required Guards

owner boundary를 보호하는 가장 작은 guard를 선택한다.

- alias normalization, command payload shape, route/query grammar, result envelope에 대한 contract test
- caller가 meaning을 reinterpret하지 않고 pass/render/invoke한다는 boundary test
- stale, fallback, permission, lifecycle, compatibility behavior에 대한 negative case
- 중복 해석을 표현하기 어렵게 만드는 type 또는 schema constraint
- semantic decision에 의존하는 user-visible behavior regression test

helper internals를 고정하지 않는다. owner가 meaning을 한 번만 결정하고 caller가 조용히 다른 meaning을 선택할 수 없다는 점을 검증한다.

## Output Contract

plan, review, implementation note에는 다음 형태를 짧게 사용한다.

- `Capability:` user/domain capability
- `Representation Crossings:` 관련 data 또는 control forms
- `Semantic Decisions:` drift될 수 있는 decisions
- `Owner Ledger:` `decision -> owner 또는 decision needed -> reason`
- `Caller Boundaries:` 허용된 caller behavior와 금지된 interpretation
- `Drift Smells:` 관찰되거나 예상되는 leak
- `Required Guards:` tests, schemas, checks
- `Handoffs:` adjacent skills 또는 follow-up owners

## Final Gates

- capability가 user/domain term으로 이름 붙었는가?
- 각 semantic decision에 owner가 정확히 하나이거나 `decision needed`가 명시되었는가?
- caller가 meaning을 결정하지 않고 observe, pass, render, invoke할 수 있는가?
- policy ownership이 명시되지 않은 adapter는 translation으로 제한되는가?
- fallback, freshness, lifecycle, permission, compatibility decision이 검증 가능한 owner에게 있는가?
- refactor scope가 현재 task로 제한되는가?
- guard가 helper internals가 아니라 owner-boundary behavior를 검증하는가?
