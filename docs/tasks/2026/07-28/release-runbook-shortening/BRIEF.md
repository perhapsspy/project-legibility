# Goal

- Project Legibility 배포 지연 원인을 현재 release owner와 실제 실행 근거에서 설명한다.
- 반복 배포를 더 짧게 만드는 한국어 release runbook과 Codex 앱 업데이트 경계를 정본 문서에 반영한다.

# Scope

- 공개·기술 문서에 흩어져 있던 release·업데이트 계약
- `docs/runbooks/release.md`와 이 작업의 분석·검증 기록

# Current Understanding

- 지연의 중심은 release command 자체보다 늦게 발견한 source cleanliness, 인증·remote 경로와 중복 검증이었다.
- Release 완료는 canonical source, GitHub Release와 publisher catalog CI로 판정한다.
- 설치본 갱신 시점은 Codex 앱이 소유하며 release 작업은 로컬 plugin cache를 직접 변경하지 않는다.

# Current State

- `docs/runbooks/release.md`가 version, GitHub 계정·write remote 확인, clean source root, 병렬 gate, release·catalog 게시와 rollback을 소유한다.
- 배포 지연 근거는 `archive/RELEASE-DELAY-ANALYSIS.md`에 보존한다.

# Next Step

- 같은 배포 지연이 반복되거나 release contract가 바뀔 때 다시 연다.
