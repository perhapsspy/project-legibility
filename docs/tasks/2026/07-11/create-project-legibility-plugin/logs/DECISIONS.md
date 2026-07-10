# 결정 기록

## 2026-07-11 · 저장소와 source ownership

- Background: 10개 스킬은 9개 공개 저장소에서 독립적으로 설치·관리되고 있다.
- Decision: 개별 저장소는 내용의 정본으로 유지하고, `project-legibility`는 포함 commit, generated snapshot, manifest와 통합 release만 소유한다.
- Why: 개별 스킬 접근성과 독립 릴리스를 보존하면서도 plugin 설치 결과를 완전하고 재현 가능하게 만들 수 있다.
- Impact: bundle의 `skills/`를 직접 고치지 않고 정본 변경 후 lock과 snapshot을 함께 갱신한다.

## 2026-07-11 · marketplace wrapper

- Background: repo root를 곧 plugin root로 두면 현재 CLI에서 local marketplace path `./`가 빈 경로로 거부된다.
- Decision: repo root를 marketplace로, `plugins/project-legibility/`를 실제 plugin root로 둔다.
- Why: 공식 repo marketplace 관례인 `./plugins/<name>`을 그대로 쓰고 별도 marketplace 저장소 없이 설치할 수 있다.
- Impact: marketplace 이름은 저장소와 같은 `project-legibility`, category는 개발용 제품 성격에 맞춘 `Developer Tools`로 둔다.

## 2026-07-11 · v0.1 제품 경계

- Background: manifest starter prompt와 기존 스킬 trigger만으로 전문 책임을 선택할 수 있다.
- Decision: umbrella skill, MCP, app, hook, lifecycle automation을 넣지 않는다.
- Why: 중복 router와 새 의미 owner를 만들지 않고 검증된 개별 스킬 책임을 그대로 보존한다.
- Impact: 실제 routing 실패 근거가 생기기 전까지 skills-only plugin으로 운영한다.
