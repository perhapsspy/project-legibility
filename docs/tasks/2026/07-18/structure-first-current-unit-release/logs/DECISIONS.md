# Decisions

**2026-07-18**

- **Background:** canonical `structure-first`는 current unit을 증상 위치가 아니라 실제 behavior/rule 책임에서 고르도록 한 문장을 교정했으며 trigger와 plugin 구성은 그대로다.
- **Decision:** 변경을 Project Legibility `0.4.1` patch release로 조립하고 검증된 release commit을 publisher catalog에 고정한다.
- **Why:** 포함 스킬의 호환 가능한 instruction 교정은 patch 규칙에 맞고, canonical source → plugin release → publisher pin 순서를 지켜 재현성과 rollback 경계를 보존한다.
- **Impact:** 설치 사용자는 같은 스킬 구성과 trigger를 유지하면서 더 정확한 current-unit 선정 지침을 받는다.
