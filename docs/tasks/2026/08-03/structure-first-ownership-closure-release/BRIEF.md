# Goal

검증된 `structure-first` ownership closure 교정을 Project Legibility patch release와 publisher marketplace에 공개한다.

## Scope

- canonical source lock, generated snapshot와 provenance를 갱신한다.
- plugin patch version, 한·영 changelog, release와 publisher pin을 함께 맞춘다.

## Current Understanding

- 다른 owner의 증거가 있을 때만 가장 작은 관련 단위를 다시 열며 자동 재귀를 도입하지 않는다.
- 경계 owner의 safe witness가 없으면 경계를 미해결로 남기되 production이나 전체 end-to-end 검증을 자동 요구하지 않는다.
- trigger와 제품 구성 역할을 유지하는 instruction 교정이므로 `0.7.1` patch release다.

## Current State

- canonical `structure-first` commit `8388c0b3fb9899ab007fb4c2ce64686719df8ee6`이 공개 `main`에 존재한다.
- Project Legibility release commit `72bcd942eba363b825e33a12a7209aa079822859`가 `v0.7.1`과 GitHub Release로 공개됐고 main·release workflow가 통과했다.
- publisher commit `a92d578e9d07b6a6e729613ed1fdd671b5697a13`이 release commit을 고정했으며 catalog 검증과 CI가 통과했다.

## Next Step

- 설치 drift가 발견되거나 ownership closure 규칙이 실제 작업에서 회귀할 때 다시 연다.

## Working Boundary

- `plugins/project-legibility/`
- `CHANGELOG.md`
- `CHANGELOG.en.md`
- `docs/tasks/2026/08-03/structure-first-ownership-closure-release/`
