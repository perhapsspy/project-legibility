# Tighten Docs 조합 규칙 배포

## 목표

`tighten-docs`의 문서 경계·정본 소유·라우팅 규칙을 canonical 저장소에서 배포하고, Project Legibility plugin release와 marketplace 갱신까지 안전하게 연결한다.

## 범위

- `tighten-docs` canonical 문서 변경의 검증·commit·push
- Project Legibility의 lock, 생성 snapshot, patch release와 publisher catalog 갱신

## 현재 이해

- 문서 경계는 독립적인 독자 행동·소유권·변경 이유로 판단하며, 함께 쓰는 계약·절차를 인위적으로 나누지 않는다.
- plugin bundle은 canonical 저장소의 push된 full SHA에서 생성하며 snapshot과 notice를 직접 고치지 않는다.

## 현재 상태

- canonical 변경 `5158636`은 `main`에 push됐다.
- Project Legibility는 새 SHA, integrity, 생성 snapshot과 notice를 갱신했고 source·offline·bundle·plugin 검증과 31개 test가 통과했다.

## 다음 행동

- Project Legibility `0.2.4` 변경을 검토·commit·push하고 release tag를 만든다.

## 작업 경계

- canonical: `tighten-docs`의 README, 방향 문서, 배포 스킬 본문
- plugin: `plugins/project-legibility/sources.lock.json`, 생성 snapshot, manifest, changelog
