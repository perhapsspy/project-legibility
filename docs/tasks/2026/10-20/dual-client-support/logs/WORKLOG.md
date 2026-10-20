# 작업 기록

**2026-10-20**
- 공통 Agent Plugins manifest와 Codex·Claude 생성 manifest, drift 검사, 한영 제품·설치·구조 문서를 구현했다. 개별 skill snapshot과 source lock은 바꾸지 않았다. 기존 앱 프로젝트 등록 경계는 list_projects의 새 agent-cost-efficiency 경로 확인으로 닫았다.
- 격리된 임시 config·marketplace에서 Claude Code 2.1.304 strict manifest·marketplace validation, 9개 skill inventory, 등록·설치·제거를 확인했다. Codex CLI 0.163.0도 같은 package를 등록·설치·제거했다. 사용자 설치본·전역 설정은 변경하지 않았다. 모델 자동 선택이나 실제 과업 동등성은 이 증거로 주장하지 않는다.
- Project Legibility 단위·회귀 테스트 57개와 publisher 테스트 17개, metadata·offline bundle 검사·bundle validator·기존 공개 catalog 원격 검증을 통과했다. 양쪽 pin 갱신·중복 실행·push 실패 재개와 실제 Git rollback을 확인했다. 공개 Claude catalog 생성과 pin 변경은 release 이후로 연결했다.
- Publisher의 새 validator·테스트·한영 안내를 main 41d9e4593860ee8adbffe16e467f2442dd0b8a13로 push했다. release rollback은 remote 검증 실패뿐 아니라 두 번째 catalog 파일 쓰기 실패도 실제 Git fixture에서 복원함을 확인했고 관련 release 테스트 19개가 통과했다. 공개 catalog pin은 유지했다.
