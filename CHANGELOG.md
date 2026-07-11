# Changelog

Project Legibility의 사용자에게 보이는 주요 변경을 기록합니다.

## [Unreleased]

## [0.2.0] - 2026-07-11

### Changed

- 공개 설치 좌표를 publisher marketplace의 `project-legibility@perhapsspy`로 변경했습니다.
- Plugin 카드 설명과 starter prompt를 구체적인 사용 문장으로 다시 썼습니다.
- Project Legibility release와 publisher catalog의 검증·공개 절차를 분리했습니다.

### Removed

- 제품 저장소가 직접 소유하던 단일 plugin marketplace를 제거했습니다.

## [0.1.0] - 2026-07-11

### Added

- 의도·구조·맥락을 잃지 않고 프로젝트를 설계·구현·검증·재개하는 skills-only Codex plugin을 처음 공개했습니다.
- 9개 canonical 저장소에서 고정한 10개 스킬을 포함했습니다.
- `project-context`와 `structure-first`를 continuity와 implementation의 두 core로 구성했습니다.
- full commit SHA를 기록하는 `sources.lock.json`과 self-contained generated skill snapshot을 추가했습니다.
- local, remote와 offline source/snapshot 검증을 위한 sync workflow를 추가했습니다.
- 세 가지 project-level starter prompt와 marketplace metadata를 추가했습니다.
- 한국어·영어 README, architecture와 contribution guide를 추가했습니다.

### Scope

- v0.1에는 MCP server, app, hook, lifecycle automation과 umbrella skill이 없습니다.

[Unreleased]: https://github.com/perhapsspy/project-legibility/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.0
[0.1.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.1.0
