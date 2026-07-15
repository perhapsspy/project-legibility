# Backoffice Edge Ops skill guardrail

## Goal

- 운영 화면이 공용 컴포넌트, 최소 구현 경계, 문서 소유권 규칙을 화면 템플릿으로 오독하지 않도록 관련 canonical skill에 최소 guardrail을 추가한다.

## Scope

- `design-user-interfaces`, `structure-first`, `tighten-docs`의 canonical source와 Project Legibility 조립 경계를 감사하고 필요한 source만 수정한다.
- Conalog Backoffice의 `DESIGN.md`와 실제 화면 구현은 cross-repo 근거와 권고까지만 다룬다.
- 설치 cache는 수정하지 않으며 canonical 검증 뒤 plugin lock과 generated bundle의 동기화 여부를 명시한다.

## Current Understanding

- 공용 primitive 재사용은 화면 구조 복제가 아니라 제품 언어 재사용이며, 운영 화면 구조는 operator의 주 판단과 다음 행동, 위계를 실제로 바꾸는 위험·lifecycle 구분에서 시작해야 한다.
- 최소 구현 경계는 도메인 의미와 판단 소유 경계를 없애는 평탄화를 뜻하지 않는다.
- 문서 정본과 라우팅 소유권은 문서 체계를 지배하지만 runtime UX 조합을 자동 결정하지 않는다.
- Project Legibility의 `plugins/project-legibility/skills/**`는 generated snapshot이고 각 독립 skill 저장소가 canonical source다.

## Current State

- 세 canonical skill의 최소 guardrail이 검증·push됐고 Project Legibility lock과 generated snapshot이 해당 commit을 가리킨다.
- source, offline integrity, bundle과 repository 검증이 통과했으며 Project Legibility 공개 문서에는 중복 UX 규칙을 추가하지 않았다.
- Project Legibility 0.3.1 patch release를 준비 중이며, 설치된 0.3.0 runtime은 release·marketplace·재설치 전까지 유지된다.
- Backoffice `DESIGN.md`의 같은 방향 문구는 해당 저장소의 미커밋 변경이므로 이 task에서 수정하거나 정본으로 승격하지 않았다.

## Next Step

- 0.3.1 release gate를 통과한 뒤 release commit과 tag를 push한다.

## Working Boundary

- `docs/tasks/2026/07-14/backoffice-edge-ops-skill-guardrails/`
- `plugins/project-legibility/`
- `tests/catalog/`
