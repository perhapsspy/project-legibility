# 문서 감사표

| 경로 | 종류 | 상태 | 분류 | 처리 |
|---|---|---|---|---|
| `README*.md` | 공개 진입 | 현재 | LEAVE | 사용자 설치·사용·구성 요약을 유지하고 내부 개발 링크 목록을 축소 |
| `docs/PRODUCT*.md` | 제품 계약 | 현재 | LEAVE | 제품 약속과 스킬 구성만 유지하고 새 스킬 편입 판단을 짧게 흡수 |
| `docs/ARCHITECTURE*.md` | 기술 계약 | 현재 | LEAVE | source owner·assembly·무결성을 유지하고 release 정책 라우팅과 반복 설명을 제거 |
| `docs/runbooks/release.md` | 운영 런북 | 현재 | REFERENCE 성격의 LEAVE | version, release gate, 게시와 rollback 실행을 한곳에서 소유 |
| `CONTRIBUTING*.md` | 혼합 라우터·정책 | 중복 | ARCHIVE | 고유 정책을 PRODUCT와 runbook에 합친 뒤 삭제 |
| `CHANGELOG*.md` | 공개 변경 이력 | 현재 누적 | LEAVE | release별 이력이 목적이므로 유지 |
| `docs/tasks/**` | 작업 맥락·이력 | 현재 및 완료 | TASK | 일괄 이동 없이 구조만 검증하고 완료 이력을 현재 정본처럼 연결하지 않음 |

`docs/reference/**`는 새로 만들지 않는다. 현재 재사용 계약은 이미 PRODUCT, ARCHITECTURE와 release runbook에 명확한 인간 독자와 소유 역할이 있다.

완료된 task root의 분석·검토 자료는 해당 task의 `archive/`로 옮겼다. 내용이 없는 미완성 task shell은 제거하고, 기존 decision log의 형식 오류는 기록 내용을 유지한 채 block 경계만 복구했다.
