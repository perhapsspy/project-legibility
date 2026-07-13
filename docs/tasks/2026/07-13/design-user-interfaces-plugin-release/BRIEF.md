# Design User Interfaces 플러그인 편입

## Goal

- `design-user-interfaces`를 canonical source 경계를 유지한 채 Project Legibility에 추가하고 publisher marketplace와 로컬 설치본까지 배포한다.

## Scope

- 최신 `tighten-docs`를 독립 patch release로 먼저 반영한다.
- `design-user-interfaces` 추가는 다음 minor release로 격리한다.
- Project Legibility bundle, release와 publisher catalog pin을 검증한다.

## Current Understanding

- 새 스킬은 새 화면과 큰 재설계의 실제 인터페이스 결정을 맡으며 `purpose-fit-design`의 목적 판단과 `structure-first`의 구현 구조 사이에 위치한다.
- canonical source는 공개된 `perhapsspy/design-user-interfaces`이고 plugin snapshot은 생성 결과다.
- 스킬 추가와 기존 source 갱신은 서로 다른 release로 분리해야 rollback 원인이 선명하다.

## Current State

- `design-user-interfaces` canonical `main`은 공개 원격과 commit `bab4b92`에서 일치하고 skill validator와 routing fixture 형식 검사를 통과한다.
- Project Legibility 0.2.5와 publisher pin이 공개됐고 원격 CI를 통과했다.
- Project Legibility 0.3.0과 publisher pin이 공개됐고 원격 CI·release workflow를 통과했다.
- 로컬 설치본은 release tree와 일치하며 새 Codex 실행에서 `design-user-interfaces`가 새 화면·큰 재설계 trigger로 로드된다.

## Next Step

- 실제 사용에서 routing 또는 인터페이스 완성도 회귀가 보고되면 다시 연다.

## Working Boundary

- `plugins/project-legibility/`
- `README.md`, `README.en.md`
- `CHANGELOG.md`, `CHANGELOG.en.md`
- `tests/catalog/`
- `docs/tasks/2026/07-13/design-user-interfaces-plugin-release/`
