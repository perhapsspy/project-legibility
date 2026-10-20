# Codex·Claude Code 동시 지원

## 목표와 범위

공통 스킬 정본·snapshot·버전을 유지하며 Codex와 Claude Code가 같은 Project Legibility 패키지를 로드하게 한다. 공통 manifest·클라이언트별 생성 manifest, 검증·설치 안내와 양쪽 catalog를 반영하는 release 경로를 구현했다. 사용자의 후속 요청으로 0.17.0 release와 양쪽 publisher pin 게시까지 범위를 확장했다.

## 현재 상태

구현·0.17.0 릴리즈·양쪽 marketplace 게시 완료. 루트 plugin.json이 공통 identity·version을 소유하고 sync_plugin_metadata.py가 Codex·Claude manifest를 생성한다. Bundle 검사는 생성 drift를 거절한다. CI에는 Claude Code 2.1.304 strict validation을 추가했다.

격리된 임시 환경에서 Codex CLI 0.163.0과 Claude Code 2.1.304가 marketplace 등록·설치·제거에 성공했다. Claude는 9개 스킬을 인식했다. Project Legibility 테스트 57개와 publisher 테스트 17개, metadata·offline bundle 검사와 기존 공개 catalog의 원격 manifest 검증이 통과했다. 실제 모델 자동 선택·작업 수행과 클라이언트 간 작업 재개는 검증 범위에 포함하지 않았다.

0.17.0 release commit은 `5c856009133f2fc13c238fe4aa3a1d8a449c3010`이며, 같은 SHA의 main CI·tag·GitHub Release가 성공했다. Publisher commit `cf389349e174e7aef1b8b80ee521fc6d33431ca0`에서 Codex·Claude catalog를 이 SHA에 고정하고 CI·양쪽 원격 manifest 검증을 통과했다. Publisher validator는 같은 source identity·SHA와 Claude native manifest를 검사한다. 실제 Git fixture로 검증 실패 시 tracked catalog 복원과 신규 Claude 파일 제거를 확인했다.

## 공개 설치 확인

격리된 임시 환경에서 공개 `perhapsspy/codex-plugins`를 등록해 Codex CLI 0.163.0과 Claude Code 2.1.304로 설치했다. 양쪽 설치 version은 0.17.0이며 Claude inventory는 `agent-cost-efficiency`를 포함한 9개 스킬이다. 사용자 설치본 갱신과 모델 호출은 수행하지 않았다.

- [GitHub Release](https://github.com/perhapsspy/project-legibility/releases/tag/v0.17.0)
- [Release commit CI](https://github.com/perhapsspy/project-legibility/actions/runs/39401561792)
- [Publisher CI](https://github.com/perhapsspy/codex-plugins/actions/runs/39401650435)
