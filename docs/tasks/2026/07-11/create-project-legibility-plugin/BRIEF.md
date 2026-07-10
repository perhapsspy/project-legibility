# Project Legibility 플러그인 구현

## 목적

기존 9개 개별 스킬 저장소를 정본으로 유지하면서 10개 스킬을 하나의 설치 가능한 Codex 플러그인으로 배포한다. 처음 보는 사용자가 제품 약속, 포함 책임, 설치·업데이트 방법과 source provenance를 바로 이해할 수 있어야 한다.

## 현재 상태

- 공식 Codex plugin 구조, marketplace, manifest, 설치·업데이트 규칙을 확인했다.
- 저장소는 하나의 marketplace root이며 실제 plugin은 `plugins/project-legibility/`에 둔다.
- 개별 저장소의 full commit SHA를 lock하고 generated snapshot을 커밋하는 구조를 채택했다.
- `source-owner-audit`에 남아 있던 `work-board` 활성 문구를 정본에서 제거하고 설치본까지 갱신했다.
- plugin scaffold와 기본 manifest, marketplace, visual asset을 생성했다.
- 9개 full SHA와 skill별 integrity를 고정하고 10개 generated snapshot을 조립했다.
- local·remote source check, offline integrity, 공식 plugin·skill validator와 32개 unit test가 통과했다.
- local marketplace에서 install → cachebuster update → remove round trip을 통과했다.
- 공개 `perhapsspy/project-legibility` 저장소, 성공한 CI, immutable `v0.1.0` tag와 GitHub Release를 발행했다.
- tag rollback 설치와 main 설치가 모두 성공했고, 새 ephemeral Codex 실행에서 `project-legibility:` namespace의 10개 스킬을 확인했다.

## 완료 조건

- 9개 source commit에서 10개 스킬 bundle을 결정적으로 재조립할 수 있다.
- plugin·marketplace·catalog·lock validator와 unit test가 통과한다.
- local install/update/remove와 GitHub release install round trip을 확인한다.
- 공개 README, 영어 pair, 기여·아키텍처·릴리스 문서가 실제 명령과 일치한다.
- `v0.1.0`과 GitHub Release를 발행하고 remote 설치본을 로컬에 남긴다.

## 범위 밖

- umbrella/router skill
- MCP server, app, connector, hook
- lifecycle automation과 자동 프로젝트 파일 생성
- 개별 스킬 저장소 통합 또는 폐기
- 공식 public Plugins Directory 제출

## 다음 행동

현재 task는 완료됐다. 후속 스킬 변경은 canonical 저장소에서 먼저 검증·push한 뒤 contribution runbook에 따라 새 plugin version으로 가져온다.
