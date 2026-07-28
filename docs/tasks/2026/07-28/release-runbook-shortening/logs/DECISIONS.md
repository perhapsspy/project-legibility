# Decisions

**2026-07-28**

- **Background:** 0.6.7 배포는 각 검증 명령보다 source cleanliness, 인증·remote 경로, 상태 관찰과 로컬 설치 확인을 중간에 다시 선택하면서 길어졌다.
- **Decision:** release 실행은 별도 한영 runbook이 소유하고 `CONTRIBUTING`은 version·gate·rollback 정책을 소유한다. 배포 완료는 GitHub Release와 publisher catalog CI에서 닫는다.
- **Why:** 사전 경로 선택과 병렬 검증은 안전 관문을 유지하면서 재시도와 중복 출력을 줄이고, Codex 앱의 client update 책임을 release mutation과 분리한다.
- **Impact:** 기본 release는 로컬 plugin cache를 변경하지 않으며, client freshness 진단은 사용자가 지정한 환경과 시점의 별도 작업이 된다.


**2026-07-28**
- 문서 감사에서 CONTRIBUTING이 release 정책과 내부 라우팅을 함께 소유해 현재 정본을 분산시키는 문제가 확인됐다.
- Version, release gate, 게시와 rollback을 한국어 단일 release runbook에 합치고 CONTRIBUTING은 제거한다.
- 실행 판단과 절차를 한 문서에서 읽을 수 있고 공개 진입 문서의 내부 라우팅도 줄어든다.
- Release 계약 변경은 docs/runbooks/release.md에서 수행하며 과거 분석은 task archive에 보존한다.
