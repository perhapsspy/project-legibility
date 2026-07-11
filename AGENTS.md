# AGENTS.md

- 일반 문서와 작업 기록은 한국어를 기본으로 쓰고, 공개 진입 문서는 `*.en.md` 영어 pair를 함께 유지한다.
- 개별 스킬 저장소가 스킬 내용의 정본이다. `plugins/project-legibility/skills/`는 생성 결과이므로 직접 수정하지 않는다.
- 스킬 변경은 정본 저장소에서 먼저 검증·push한 뒤 `scripts/sync_skills.py`로 lock과 bundle을 갱신한다.
- plugin manifest, lock과 generated snapshot의 이름·버전 경계를 서로 일치시킨다.
- publisher marketplace 변경은 `perhapsspy/codex-plugins`에서 하며, push된 Project Legibility release commit만 고정한다.
- 현재 task 상태는 `docs/tasks/`에 두고 always-read 지침에 넣지 않는다.

## 검증

- `python3 scripts/sync_skills.py check --offline`
- `python3 scripts/validate_bundle.py`
- `python3 -m unittest discover -s tests -v`
