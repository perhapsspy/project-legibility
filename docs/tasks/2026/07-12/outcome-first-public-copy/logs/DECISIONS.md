# 결정 기록

**2026-07-12**

- **Background:** bundle과 marketplace가 개별 스킬의 목적을 다시 설명해 canonical 문구 변경 때 drift가 생겼다.
- **Decision:** canonical 저장소는 개별 스킬 의미를, Project Legibility는 조합 가치를, marketplace는 설치 좌표와 링크를 소유한다.
- **Why:** 사용자 설명을 정본에서 개선하면서 메타 저장소의 중복 유지보수를 없애기 위해서다.
- **Impact:** bundle과 catalog README는 개별 스킬 목적을 재서술하지 않고 canonical 링크로 안내한다.

**2026-07-12**

- **Background:** 제품 용도를 설명할 때마다 Codex를 반복해 문구가 도구 소개처럼 보였다.
- **Decision:** 일반 효용 문구에서는 Codex를 빼고, 설치 명령·고유 식별자·제품 자체가 의미의 대상인 경우에만 남긴다.
- **Why:** 도구 이름보다 사용자가 얻는 결과를 먼저 보이면서 사실성은 유지하기 위해서다.
- **Impact:** `codex-token-discipline`처럼 제품 자체를 다루는 스킬과 공식 명령에는 Codex가 남을 수 있다.
