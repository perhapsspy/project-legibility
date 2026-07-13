# 결정 기록

**2026-07-11**

- **Background:** 독립 저장소의 스킬을 재현 가능한 플러그인으로 함께 배포하면서도 각 스킬의 원본과 독립 설치 경로를 유지해야 했다.
- **Decision:** 개별 저장소를 내용의 원본으로 유지하고, `project-legibility`는 고정 commit, generated snapshot, manifest와 통합 release만 소유하는 skills-only plugin으로 구성했다.
- **Why:** 중복 router나 새 의미 owner를 만들지 않고 기존 스킬 책임을 보존하며, `plugins/project-legibility/` 구조로 표준 marketplace 경로를 사용할 수 있다.
- **Impact:** generated `skills/`는 직접 수정하지 않고 원본 변경 후 lock과 snapshot을 함께 갱신하며, 실제 routing 실패 근거가 생기기 전에는 MCP, app, hook이나 umbrella skill을 추가하지 않는다.
