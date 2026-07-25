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

- Director 정본만 새 commit과 무결성으로 고정하고 생성 묶음을 제한 갱신했다. 정본 형식·사전 행동 검증과 Project Legibility Linux 지속 통합 검사가 통과했으며 `0.6.2` 출시를 준비했다.

## 다음 행동

- 출시 commit을 `main`에 게시하고 `v0.6.2` 태그 검증 뒤 배포 목록과 로컬 설치본을 갱신한다.

## 작업 경계

- `plugins/project-legibility/sources.lock.json`
- `plugins/project-legibility/skills/codex-project-director/`
- `plugins/project-legibility/THIRD_PARTY_NOTICES.md`
- `CHANGELOG*.md`
- `docs/tasks/2026/07-26/director-visible-worker-boundary/`
