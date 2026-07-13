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

- `tighten-docs` canonical 변경 `5158636`과 Project Legibility `0.2.4` release `edffc73`가 공개됐다.
- publisher catalog `0125021`은 release commit을 고정하며, marketplace 재설치본은 canonical 영문·한국어 스킬과 일치한다.

## 다음 행동

- 완료. 후속 스킬 변경은 새 task에서 canonical 저장소부터 시작한다.

## 작업 경계

- canonical: `tighten-docs`의 README, 방향 문서, 배포 스킬 본문
- plugin: `plugins/project-legibility/sources.lock.json`, 생성 snapshot, manifest, changelog
