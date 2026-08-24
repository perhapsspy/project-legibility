# 디렉터 실행 경계와 병렬 frontier 배포

## 목표

- `codex-project-director`의 실행 소유권과 병렬 dispatch 교정을 Project Legibility 새 patch version과 publisher catalog까지 정식 배포한다.
- user-visible bundled skill 변경을 source sync에서 닫지 않도록 release 런북의 완료 경계를 보강한다.

## 범위

- Project Legibility manifest, 한영 changelog, release 런북과 현재 작업 기록을 갱신한다.
- release gate를 통과한 commit에 tag와 GitHub Release를 게시하고 publisher catalog pin과 CI를 완료한다.

## 현재 사실

- Director 정본 `1ec35238e6b98b526319f4f4d1b147e6737e5f20`은 공개 `main`에 게시됐다.
- Project Legibility `acd7e11dabab1468c5d3bbbd67173f61b172f1de`은 해당 source pin과 generated bundle을 반영했지만 version, changelog, tag, GitHub Release와 publisher catalog가 아직 갱신되지 않았다.
- 변경은 기존 명시 호출과 skill 구성을 유지하며 실행 소유권과 scheduling guardrail을 호환 가능하게 교정한다.

## 현재 상태

- Project Legibility release `f5416f2`에 `v0.9.2` tag와 GitHub Release가 존재하며 exact-SHA main CI와 release workflow가 성공했다.
- Publisher catalog `7aa3e3d`이 release full SHA를 고정하며 원격 manifest 검증과 catalog CI를 통과했다.
- source sync를 완료 조건으로 오인하지 않게 하는 릴리스 런북과 always-read 라우팅을 함께 게시했다.

## 다음 행동

- 새 Codex 작업에서 갱신된 plugin이 로드된 뒤 실제 운영 사례가 계약과 다르게 동작할 때 이 작업을 다시 연다.

## 작업 경계

- `plugins/project-legibility/.codex-plugin/plugin.json`
- `CHANGELOG*.md`
- `docs/runbooks/release.md`
- `docs/tasks/2026/08-24/director-frontier-release/`
- `<codex-plugins-root>`의 Project Legibility source pin
