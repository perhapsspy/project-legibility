**2026-08-24**
- Director 정본과 generated bundle은 공개됐지만 설치 사용자에게 도달하는 Project Legibility release가 누락됐다.
- 이번 교정을 patch release로 게시하고, user-visible bundled skill 변경은 catalog CI까지 완료되기 전에는 완료로 보고하지 않도록 release 런북에 명시한다.
- 선택 계약과 제품 구성을 바꾸지 않는 실행 품질·guardrail 교정이며, source sync와 배포 완료를 혼동한 동일 실패를 막아야 하기 때문이다.
- local install과 cache refresh는 기존대로 release gate 밖에 두되, manifest·changelog·tag·GitHub Release·catalog pin과 CI는 필수 완료 경계로 유지한다.
