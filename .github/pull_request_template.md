## 변경 요약

- 무엇을 왜 바꿨는지 간단히 적어 주세요.

## 확인

- [ ] 스킬 변경은 canonical 저장소에서 먼저 검증하고 push했다.
- [ ] `sources.lock.json`과 generated skill diff를 함께 검토했다.
- [ ] `plugins/project-legibility/skills/**`를 직접 편집하지 않았다.
- [ ] `python -m unittest discover -s tests -p 'test_*.py' -v`를 통과했다.
- [ ] `python scripts/validate_bundle.py`를 통과했다.
- [ ] `python scripts/sync_skills.py check`를 통과했다.
- [ ] 릴리스 대상이면 manifest version과 `CHANGELOG.md`를 함께 갱신했다.
