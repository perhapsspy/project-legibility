# Changelog

Project Legibility의 사용자에게 보이는 주요 변경을 기록합니다.

## [Unreleased]

## [0.2.5] - 2026-07-13

### Changed

- 공개 README와 목록 설명이 확인된 사용자 상황·결과·다음 행동을 먼저 제시하도록 bundled `tighten-docs`를 갱신했습니다.

## [0.2.4] - 2026-07-13

### Changed

- bundled `tighten-docs`가 독립적인 문서 경계, 정본 소유, 조합 라우팅을 구분하도록 갱신했습니다.

## [0.2.3] - 2026-07-13

### Changed

- 공개 문서에서 변경 내역과 각 스킬의 원본 설명으로 바로 이동할 수 있게 경로를 정리했습니다.
- 리팩터링 예제가 기존 동작을 보존하도록 교정하고, 실행되지 않은 테스트를 검증 완료로 표현하지 않도록 고쳤습니다.
- 스킬 유지보수, 편집 승인과 토큰 감사 안내를 실제 실행 범위와 권한 경계에 맞게 다듬었습니다.
- 생성 배포본을 최신 원본 스킬 커밋으로 갱신했습니다.

### Removed

- 현재 운영에 필요하지 않은 GitHub issue와 pull request 양식을 제거했습니다.

## [0.2.2] - 2026-07-12

### Changed

- 플러그인과 canonical 스킬 설명을 내부 구조보다 사용자가 얻는 결과가 먼저 보이도록 다시 썼습니다.
- bundle과 marketplace가 개별 스킬 목적을 재서술하지 않고 canonical 저장소로 안내하도록 설명 소유권을 정리했습니다.
- 개선 제안과 버그 양식에서 maintainer용 용어와 판단 항목을 제거했습니다.

## [0.2.1] - 2026-07-11

### Changed

- README와 plugin 카드에서 현재 스킬·저장소 개수를 중복해 적지 않도록 정리했습니다.
- Architecture, contribution guide와 GitHub 양식의 표현을 더 짧고 명확하게 다듬었습니다.

## [0.2.0] - 2026-07-11

### Changed

- 공개 설치 좌표를 publisher marketplace의 `project-legibility@perhapsspy`로 변경했습니다.
- Plugin 카드 설명과 starter prompt를 구체적인 사용 문장으로 다시 썼습니다.
- Project Legibility release와 publisher catalog의 검증·공개 절차를 분리했습니다.

### Removed

- 제품 저장소가 직접 소유하던 단일 plugin marketplace를 제거했습니다.

## [0.1.0] - 2026-07-11

### Added

- 독립적으로 관리되는 canonical 저장소의 스킬을 하나의 skills-only Codex plugin으로 배포했습니다.
- `project-context`와 `structure-first`를 중심으로 작업 재개와 코드 변경 흐름을 다루도록 구성했습니다.
- full commit SHA를 기록하는 `sources.lock.json`과 self-contained generated skill snapshot을 추가했습니다.
- local, remote와 offline source/snapshot 검증을 위한 sync workflow를 추가했습니다.
- 세 가지 project-level starter prompt와 marketplace metadata를 추가했습니다.
- 한국어·영어 README, architecture와 contribution guide를 추가했습니다.

### Scope

- v0.1에는 MCP server, app, hook, lifecycle automation과 umbrella skill이 없습니다.

[Unreleased]: https://github.com/perhapsspy/project-legibility/compare/v0.2.5...HEAD
[0.2.5]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.5
[0.2.4]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.4
[0.2.3]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.3
[0.2.2]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.2
[0.2.1]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.1
[0.2.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.0
[0.1.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.1.0
