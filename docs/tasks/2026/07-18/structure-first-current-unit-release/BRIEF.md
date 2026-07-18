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
- Project Legibility commit `c1d84be`가 `v0.4.1`과 GitHub Release로 공개됐고 main·release workflow가 통과했다.
- publisher commit `57aeb53`가 release commit을 고정했으며 publisher CI와 marketplace upgrade·설치 검증이 통과했다.
- 설치된 `0.4.1`의 manifest와 `structure-first` skill이 release bundle과 일치한다.

## Next Step

- 설치 drift가 발견되거나 current-unit 선정 원칙이 실제 작업에서 회귀할 때 다시 연다.

## Working Boundary

- `plugins/project-legibility/`
- `CHANGELOG.md`
- `CHANGELOG.en.md`
- `docs/tasks/2026/07-18/structure-first-current-unit-release/`
