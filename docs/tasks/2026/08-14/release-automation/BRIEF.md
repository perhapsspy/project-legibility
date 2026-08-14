# 릴리스 자동화와 지연 제거

## 목표

특정 canonical source 변경부터 Project Legibility release와 publisher catalog 게시까지의 수동 경로 선택과 중복 대기를 제거하되, 실제 병목보다 복잡한 배포 체계를 만들지 않는다.

## 현재 결론

- `sync_skills.py update --source ID=SHA`가 선택 source만 canonical public `main`의 full SHA로 갱신한다.
- 배포 문구와 version은 사람이 충분히 검토해 release commit에 확정한다.
- `release.py publish` 하나가 Project Legibility main CI, 같은 SHA의 tag·Release, catalog full-SHA pin·CI를 순서대로 소유한다.
- 재실행은 remote main·tag·Release·catalog pin을 읽으며, candidate ref와 private journal은 쓰지 않는다.

## 현재 상태

완료. Candidate 병렬화와 journal 상태기계를 제거하고 구현·workflow·문서를 단일 publish 계약으로 축소했다. 전체 저장소·catalog 검증과 독립 최종 리뷰를 통과했으며 열린 finding은 없다.

## 다음 행동

없음. 다음 실제 release는 [릴리스 런북](../../../../runbooks/release.md)을 사용한다. Hosted CI 시간이 다시 실제 병목으로 측정될 때만 candidate 병렬화를 별도 판단한다.

## 작업 경계

- `scripts/`, `tests/`, `.github/workflows/`
- `docs/runbooks/release.md`, 이 task 기록
- `<codex-plugins-root>`의 Project Legibility pin과 catalog CI 경계
