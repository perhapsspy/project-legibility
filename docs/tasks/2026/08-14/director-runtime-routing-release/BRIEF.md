# 디렉터 runtime 경로 복구 배포

## 목표

- 내부 agent runtime이 요청된 capability를 제공하지 못해도 디렉터가 실행을 인수하지 않고, 승인된 사용자 가시 작업자 경로로 이어지는 일반 계약을 정식 배포한다.

## 범위

- `codex-project-director` 정본과 Project Legibility의 해당 lock·snapshot·출처 고지를 갱신한다.
- Project Legibility patch release와 publisher catalog의 고정 SHA를 게시한다.
- 개인 Codex 설정 저장소에는 현재 multi-agent runtime이 지원하는 안전한 기본 model 안내를 게시한다.

## 현재 사실

- 문제를 드러낸 사례는 Luna였지만 runtime 계약은 role, model, tool, worker provisioning 실패 전체를 다룬다.
- 영문·한국어 계약은 독립 문구 리뷰와 일곱 개 실패 시나리오 검증을 통과했다.
- Project Legibility의 현재 공개 version은 `0.8.0`이며 이번 변경은 기존 선택 계약 안의 실행·failure-handling 교정이다.

## 현재 상태

- Director 정본 `5b6671e`과 개인 설정 안내 `89b1a60`은 공개 `main`에 게시됐다.
- Director만 갱신한 Project Legibility `0.8.1` release `ee9c771`이 source·bundle, plugin, bundled skill, remote source와 CI를 통과했고 같은 commit의 tag와 GitHub Release가 게시됐다.
- Publisher catalog `0c933f3`이 release SHA를 고정하며 원격 manifest 검사와 CI를 통과했다.

## 다음 행동

- 새 Codex 작업에서 갱신된 plugin이 로드된 뒤 실제 운영 사례가 계약과 다르게 동작할 때 이 작업을 다시 연다.

## 작업 경계

- `<codex-project-director-root>`
- `<codex-personal-config-root>/README.md`
- `plugins/project-legibility/`
- `CHANGELOG*.md`
- `docs/tasks/2026/08-14/director-runtime-routing-release/`
- `<codex-plugins-root>`의 Project Legibility source pin
