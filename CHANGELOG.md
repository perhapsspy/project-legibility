# Changelog

Project Legibility의 사용자에게 보이는 주요 변경을 기록합니다.

## [Unreleased]

## [0.5.1] - 2026-07-24

### Changed

- bundled `source-owner-audit`가 소스 소유권 근거와 쓰기 권한을 분리하고, owner 확인만으로 실행 범위를 사용자 승인 밖으로 넓히지 않도록 보강했습니다.

## [0.5.0] - 2026-07-23

### Changed

- `purpose-fit-design`은 새 기능, 기존 구현 재사용과 임시 구현의 초기 방향을 목적·제약·근거와 성공 조건에 맞춰 판단하는 간결한 스킬로 정리했습니다.
- `structure-first`는 기능 구현·버그 수정·리팩터링 전반에서 현재 구조 유지, 국소 변경과 구조 개선 중 문제에 맞는 결과를 선택하도록 조정했습니다.
- 위험 징후와 경험칙을 조사 단서로 삼고, 공개 플러그인 설명과 스킬 선택 검증 사례를 새 호출 모델에 맞췄습니다.

## [0.4.1] - 2026-07-18

### Changed

- bundled `structure-first`가 증상이나 결과가 나타난 위치가 아니라 바꾸려는 동작이나 규칙의 실제 책임을 기준으로 가장 작은 current unit을 고르도록 보강했습니다.

## [0.4.0] - 2026-07-16

### Added

- 제품 약속, 스킬 구성 역할과 호출 모델의 정본인 제품 계약을 추가했습니다.

### Changed

- 공개 README와 plugin 설명을 에이전트 변경이 쌓여도 코드 구조, 판단 기준과 작업 맥락을 함께 강화하는 제품 방향으로 다시 구성했습니다.
- 일반적인 기능 변경, 버그 수정, 리팩터링과 작업 재개 요청에서 canonical trigger에 맞는 스킬이 선택되도록 사용 예시와 starter prompt를 갱신했습니다.
- Core practices, 조건부 Gateway, Specialists와 Optional helpers의 제품 역할을 구분하고 개별 스킬의 의미와 trigger는 각 canonical 저장소가 소유하도록 경계를 명시했습니다.
- bundled `purpose-fit-design`이 사용자 정정의 국소·관계·광범위 도달 범위를 구분하고, 영향받지 않은 목적·제약·확인된 owner 경계를 보존하도록 보강했습니다.

## [0.3.2] - 2026-07-15

### Changed

- 공개 README가 긴 저장소 작업에서 얻는 결과, 대표 사용 장면과 plugin 구성을 먼저 보여주도록 정리했습니다.
- bundled `tighten-docs`가 대상의 역할과 독자 결과를 긍정형 최종 문장으로 직접 쓰고, 실제 금지·한계·안전 경계가 있을 때 부정과 대비를 사용하도록 보강했습니다.

## [0.3.1] - 2026-07-15

### Changed

- 운영 화면이 공용 primitive를 page template로 복제하지 않고 핵심 판단과 다음 행동, 위계를 실질적으로 바꾸는 위험·lifecycle 구분에서 구조를 정하도록 bundled `design-user-interfaces`를 보강했습니다.
- 최소 구현 경계가 서로 다른 도메인 의미와 판단 소유자를 보존하고, 문서 정본 소유권이 그 자체로 runtime UX composition을 규정하지 않도록 bundled `structure-first`와 `tighten-docs`를 보강했습니다.

## [0.3.0] - 2026-07-13

### Added

- 새 화면과 큰 재설계에서 사용자 과업, 실제 콘텐츠, 정보 구조, 관련 상태와 렌더 검증을 함께 다루는 `design-user-interfaces`를 추가했습니다.

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

[Unreleased]: https://github.com/perhapsspy/project-legibility/compare/v0.5.1...HEAD
[0.5.1]: https://github.com/perhapsspy/project-legibility/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/perhapsspy/project-legibility/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/perhapsspy/project-legibility/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/perhapsspy/project-legibility/compare/v0.3.2...v0.4.0
[0.3.2]: https://github.com/perhapsspy/project-legibility/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/perhapsspy/project-legibility/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.3.0
[0.2.5]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.5
[0.2.4]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.4
[0.2.3]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.3
[0.2.2]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.2
[0.2.1]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.1
[0.2.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.0
[0.1.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.1.0
