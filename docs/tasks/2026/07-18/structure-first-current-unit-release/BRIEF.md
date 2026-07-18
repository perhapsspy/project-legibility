# Goal

검증된 `structure-first` current-unit 선정 원칙을 Project Legibility patch release와 publisher marketplace에 공개한다.

## Scope

- canonical source lock, generated snapshot와 provenance를 갱신한다.
- plugin patch version, 한·영 changelog, release와 publisher pin을 함께 맞춘다.

## Current Understanding

- 변경은 기존 trigger나 제품 구성 역할을 바꾸지 않는 bundled skill instruction 교정이므로 patch release다.
- Project Legibility는 공개 canonical commit의 snapshot만 조립하고 publisher는 검증된 plugin release commit만 고정한다.

## Current State

- canonical `structure-first` commit `0974f2d`가 공개됐고 lock·generated snapshot·provenance가 해당 source로 갱신됐다.
- Project Legibility `0.4.1` release candidate의 manifest와 한·영 changelog가 준비됐다.
- local·remote·offline source check, release-tag bundle validation, repository test와 task shape check가 통과했다.

## Next Step

- 전체 release gate를 통과한 뒤 `v0.4.1`을 공개하고 publisher catalog pin과 설치본을 갱신한다.

## Working Boundary

- `plugins/project-legibility/`
- `CHANGELOG.md`
- `CHANGELOG.en.md`
- `docs/tasks/2026/07-18/structure-first-current-unit-release/`
