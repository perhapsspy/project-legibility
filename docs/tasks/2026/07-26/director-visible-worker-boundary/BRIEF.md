# 디렉터 사용자 가시 작업자 경계 갱신

## 목표

- `codex-project-director`의 사용자 가시 작업자 우선 경계를 게시된 정본에 맞춰 Project Legibility 묶음에 반영한다.

## 범위

- 디렉터 출처 잠금, 생성 스킬, 출처 고지와 한영 변경 기록을 갱신한다.
- 다른 포함 스킬의 잠금과 생성 결과는 유지한다.

## 현재 사실

- 정본 `main`은 `cc52505d5770e681a25478e06710e4588e49fe0a`이며 형식 검사와 세 가지 독립 사전 검증이 통과했다.
- 다른 정본 다수가 현재 잠금보다 앞서 있어 전체 출처 갱신은 이번 범위를 벗어난다.

## 현재 상태

- Director 정본만 새 commit과 무결성으로 고정하고 생성 묶음을 제한 갱신했다. 첫 Linux 검사에서 Windows가 계산한 무결성 값의 파일 모드 차이를 확인해 정본 Git 트리 기준 값으로 교정했다.

## 다음 행동

- 교정 commit을 게시하고 Linux 지속 통합 검사에서 묶음 무결성과 전체 단위 검사를 다시 판단한다.

## 작업 경계

- `plugins/project-legibility/sources.lock.json`
- `plugins/project-legibility/skills/codex-project-director/`
- `plugins/project-legibility/THIRD_PARTY_NOTICES.md`
- `CHANGELOG*.md`
- `docs/tasks/2026/07-26/director-visible-worker-boundary/`
