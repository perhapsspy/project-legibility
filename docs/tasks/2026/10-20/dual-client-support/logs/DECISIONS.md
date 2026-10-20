# 결정 기록

**2026-10-20**
- 사용자가 스킬 공통화와 rename을 마친 뒤 Claude 지원 작업 진행을 요청했다.
- 루트 Agent Plugins manifest가 공통 identity·version을 소유하고 Codex·Claude manifest를 생성한다. 기존 스킬 snapshot은 공유한다.
- 별도 스킬 tree·version을 만들지 않으면서 각 클라이언트의 실제 로더와 표시 메타데이터 규격을 충족한다.
- 양쪽 native manifest drift를 bundle 검사에서 거절하며 version 변경은 실제 release 때 루트에서 한 번 수행한다.

**2026-10-20**
- Publisher는 현재 Codex catalog의 기존 release pin만 제공하고 새 Claude manifest는 아직 게시되지 않았다.
- Claude catalog는 다음 Project Legibility release 뒤 생성하고 두 catalog를 같은 release SHA로 한 commit에서 갱신한다. 지금 공개 pin은 바꾸지 않는다.
- 기존 공개 버전에 새 지원을 잘못 연결하지 않고 구현·게시·설치 갱신을 구분한다.
- Publisher validator는 Claude catalog가 존재할 때 Codex source와의 일치 및 같은 SHA의 Claude manifest를 검증한다. 게시 실패 복구는 두 파일을 함께 처리한다.
