# 공개 설명 정리

## 목표

사용자와 기여자가 읽는 현재 문서를 간결하게 만들고, 구성 변경 때 함께 고쳐야 하는 설명을 줄인다.

## 범위

- README, plugin manifest, Architecture, contribution guide와 CHANGELOG
- GitHub issue·pull request 양식
- publisher catalog의 README와 공개 metadata

## 현재 이해

- 실제 포함 구성은 README의 스킬 표와 `sources.lock.json`이 소유한다.
- 일반 설명에 스킬·저장소 개수를 적으면 구성 변경 때 쉽게 낡는다.
- 문서마다 사용법, 소유권, 절차의 역할을 분리해야 같은 설명이 반복되지 않는다.

## 현재 상태

- 공개 문서와 metadata 정리를 마쳤다.
- v0.2.1 release와 publisher catalog 공개가 완료됐다.
- 로컬 marketplace와 설치된 plugin이 v0.2.1 release SHA를 가리킨다.

## 다음 행동

- 없음. 이후 구성 변경에서도 일반 설명은 개수를 복제하지 않고 포함 스킬 표와 lock을 따른다.

## 작업 경계

- canonical skill 내용과 trigger는 바꾸지 않는다.
- 과거 task 기록, 생성 snapshot, license와 machine data는 문안 정리 대상에서 제외한다.
