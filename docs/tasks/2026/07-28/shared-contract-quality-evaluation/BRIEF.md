# Goal

- `project-context`와 `codex-project-director` 정본에 공유 계약과 품질 평가 운영 규칙을 최소 변경으로 반영한다.
- 사용자가 변경 이유와 실제 차이를 검토할 수 있는 한글 설명을 제공한다.

# Scope

- `project-context`, `project-context-migration`, `codex-project-director`의 배포 계약과 한글 companion
- 정본 변경을 검토하기 위한 이 작업의 비교 문서와 검증 기록
- Project Legibility source lock·생성 snapshot과 0.6.7 patch release

# Current Understanding

- 여러 담당자가 같은 해석에 의존할 때는 해석의 현재 정본 소유자가 필요하다.
- 작업 분리는 변경 영역뿐 아니라 사용자 가시 결과의 독립 판정 가능성까지 충족해야 한다.
- 리뷰의 직접 관찰은 완료 주장을 반증할 수 있고, 원인과 수정안은 변경 담당자가 검증할 가설이다.
- 완료 관문, 지향 비교 기준과 반복 품질 작업의 승인 기준선은 서로 다른 역할을 가진다.

# Current State

- `project-context` 정본 `b1394c9c54470109855fbae2b8b7a0c9275f88da`와 `codex-project-director` 정본 `9a18b665a96afb5787328aaf799437882533aea6`이 공개 `main`에 게시됐다.
- Project Legibility 0.6.7 후보가 두 정본, 최신 canonical source lock과 생성 snapshot을 가리키며 local·remote·offline source, release-tag bundle, plugin·skill validator와 unit test 31개를 통과했다.
- `CHANGE-REVIEW.md`가 변경 전후 행동 차이와 축소 결정을 설명한다.

# Next Step

- 검증된 release commit을 push하고 `v0.6.7` tag와 GitHub Release를 만든 뒤 publisher catalog 고정값을 갱신한다.
