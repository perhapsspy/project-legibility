# Goal

- 현재 문서가 맡는 역할을 다시 나누고 중복 라우팅과 장황한 설명을 줄인다.
- 독립적인 소유 내용이 없는 `CONTRIBUTING*`를 제거하고 필요한 정책만 적절한 정본에 합친다.

# Scope

- 저장소 루트 공개 문서, `docs/*.md`, `docs/runbooks/*.md`
- `docs/tasks/**`는 작업 기록 구조와 현재 정본 여부만 점검한다.

# Current Understanding

- `CONTRIBUTING*`의 owner·개발·release 설명은 Architecture와 release runbook에 대부분 겹친다.
- Version 분류, 새 스킬 편입 기준과 rollback 세부는 다른 정본으로 옮겨야 보존된다.
- README는 사용자 진입, PRODUCT는 제품 구성, ARCHITECTURE는 조립 구조, runbook은 배포 실행만 소유하는 구성이 가장 작다.

# Current State

- `CONTRIBUTING*`의 제품 구성 판단은 PRODUCT, version·gate·게시·rollback은 `docs/runbooks/release.md`로 이동했고 두 파일은 제거됐다.
- README의 내부 개발 경로는 PRODUCT, Architecture와 CHANGELOG로 줄었으며 Architecture는 source·assembly·integrity·release evidence만 소유한다.
- 완료된 task root 자료는 `archive/`로 이동했고 전체 project-context runtime shape가 통과한다.

# Next Step

- 현재 문서 역할이 다시 겹치거나 외부 contributor 진입점이 필요해질 때 재검토한다.
