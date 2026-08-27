# AGENTS.md

- 일반 문서와 작업 기록은 한국어를 기본으로 쓰고, 공개 진입 문서는 `*.en.md` 영어 pair를 함께 유지한다.
- 요청 범위 안의 구현과 검증은 직접 완료한다. 새 제품 정책, 영구 검증이나 release 전환처럼 별도 수명주기를 만드는 변경은 사용자 요청 또는 현재 정본의 승인된 결정에 연결한다.
- 개별 스킬 저장소가 정본이다. 제품 약속이나 bundle 구성을 바꿀 때는 `docs/PRODUCT.md`를 먼저 갱신한다. 정본 스킬 내용을 바꿨다면 해당 저장소에서 검증·push하고, 이후 `scripts/sync_skills.py`로 생성 bundle과 lock을 맞춘다. `plugins/project-legibility/skills/`는 직접 수정하지 않는다.
- 폐기할 실험·브라우저 검증 코드, 실행 상태와 원시 출력은 사용자 환경과 분리한 저장소 밖 임시 위치에 두고 확인 뒤 정리한다. 보존할 코드와 증거는 정식 소스, 테스트, 런북 또는 산출물 owner에 둔다.
- `docs/tasks/`에는 사람이 읽는 현재 상태, 목적, 방법, 결과, 결정과 간결한 근거 요약만 둔다.
- 삭제·교체는 현재 정본과 구성에서 대상을 제거해 표현한다. denylist나 tombstone은 현재 외부 안전·호환성 계약이 요구하고 범위와 해제 조건이 정해진 경우에만 둔다.
- plugin version, 한영 `CHANGELOG`, tag와 publisher pin은 실제 게시를 수행하는 별도 release 작업에서 [릴리스 런북](docs/runbooks/release.md)에 따라 함께 갱신한다. publisher marketplace는 `perhapsspy/codex-plugins`에서 push된 Project Legibility release commit만 고정한다.

## 검증

- `python3 scripts/sync_skills.py check --offline`
- `python3 scripts/validate_bundle.py`
- `python3 -m unittest discover -s tests -v`
