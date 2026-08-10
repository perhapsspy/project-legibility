# Goal

완료된 작업의 인접 후보 승격을 막는 `project-context` 교정을 Project Legibility patch release와 publisher marketplace에 공개한다.

## Scope

- canonical source lock, generated snapshot와 provenance를 갱신한다.
- plugin patch version, 한·영 changelog, release와 publisher pin을 함께 맞춘다.

## Current Understanding

- 모호한 완료 사례에서 현재안은 0/2, 교정안은 3/3이었고 명확한 진행 중 작업은 계속 수행했다.
- 교정은 BRIEF 구조나 상태 체계를 늘리지 않고 목표·현재 상태·재개 지점을 행동 전에 맞춘다.
- 제품 역할과 trigger를 유지하는 instruction 교정이므로 `0.7.2` patch release다.

## Current State

- canonical `project-context` commit `0cad6e2110b51d06651b4840abce0a5877580065`이 공개 `main`에 존재한다.
- Project Legibility release commit `e48402c167790135afb181285998e24d55c6201d`가 `v0.7.2`와 GitHub Release로 공개됐고 main·release workflow가 통과했다.
- publisher commit `8231a71e1d659a5fd0b449f10277c7010f6eee34`이 release commit을 고정했으며 catalog 검증과 CI가 통과했다.

## Next Step

- 완료된 작업의 인접 후보 승격이 실제 재개에서 다시 나타날 때 이 작업을 연다.

## Working Boundary

- `plugins/project-legibility/`
- `CHANGELOG.md`
- `CHANGELOG.en.md`
- `docs/tasks/2026/08-10/project-context-closed-task-release/`
