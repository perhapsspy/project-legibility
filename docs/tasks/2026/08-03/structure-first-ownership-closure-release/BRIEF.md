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
- lock, generated snapshot와 provenance가 해당 commit으로 갱신됐고 `structure-first` 관련 파일만 변경됐다.
- manifest와 한·영 changelog를 `0.7.1`로 준비했다.
- local·remote·offline source check, release-tag bundle validation, plugin·skill validation과 repository test 31개가 통과했다.

## Next Step

- Project Legibility release commit, `v0.7.1`, GitHub Release와 publisher pin을 순서대로 공개한다.

## Working Boundary

- `plugins/project-legibility/`
- `CHANGELOG.md`
- `CHANGELOG.en.md`
- `docs/tasks/2026/08-03/structure-first-ownership-closure-release/`
