**2026-07-13**
- Background: tighten-docs 변경은 canonical 저장소에만 있고 현재 plugin은 이전 full SHA snapshot을 포함한다.
- Decision: canonical commit을 먼저 push한 뒤 기존 source lock 재생성·release 절차로 plugin을 갱신한다.
- Why: 생성 snapshot을 직접 고치지 않고 full SHA, integrity와 third-party notice를 함께 갱신해야 재현성과 provenance를 유지할 수 있다.
- Impact: Project Legibility는 patch release로 새 canonical commit을 고정하고, marketplace는 검증된 release commit만 가리킨다.
