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
- Project Legibility bundle은 새 정본을 고정했고 release gate 실행을 앞두고 있다.

## Next Step

- `v0.7.2` release gate를 통과한 뒤 release와 publisher pin을 게시한다.

## Working Boundary

- `plugins/project-legibility/`
- `CHANGELOG.md`
- `CHANGELOG.en.md`
- `docs/tasks/2026/08-10/project-context-closed-task-release/`
