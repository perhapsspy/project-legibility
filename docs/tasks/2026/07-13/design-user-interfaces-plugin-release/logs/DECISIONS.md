# Decisions

**2026-07-13**

- **Background:** 새 인터페이스 제작 스킬은 기존 개발 워크플로와 이어지지만 독립 플러그인으로 분리할 만큼 디자인 스킬 묶음이 아직 크지 않다.
- **Decision:** `design-user-interfaces`를 Project Legibility에 독립 canonical source로 추가한다.
- **Why:** 목적 판단, 인터페이스 설계와 구현 구조의 책임을 분리하면서 사용자가 하나의 개발 워크플로에서 선택할 수 있다.
- **Impact:** 공개 canonical commit만 lock하고 생성 snapshot을 직접 수정하지 않으며, 디자인 계열이 독립 제품으로 커질 때 별도 플러그인을 재검토한다.

**2026-07-13**

- **Background:** plugin lock의 `tighten-docs`가 최신 canonical commit보다 뒤에 있고 스킬 추가는 minor release가 필요하다.
- **Decision:** `tighten-docs` 갱신을 0.2.5 patch로 먼저 내고 `design-user-interfaces` 추가를 0.3.0 minor로 분리한다.
- **Why:** 기존 source 갱신과 신규 catalog 항목의 회귀·rollback 경계를 분리할 수 있다.
- **Impact:** 두 release gate와 publisher pin 갱신을 순서대로 완료한 뒤 최종 설치본을 0.3.0으로 맞춘다.
