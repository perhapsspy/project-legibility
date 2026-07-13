# 공개 문서 리뷰 후속 수정

## 목표

전체 공개 문서 리뷰에서 확인한 동작 계약, 문서 소유권과 독자 경로 문제를 canonical owner에서 바로잡는다.

## 범위

- canonical 스킬의 예시, README, 실행 계약과 유지보수 문서
- Project Legibility와 publisher catalog의 사용자·릴리스 라우팅
- 로컬 standalone skills와 plugin 설치 동기화

## 현재 이해

- GitHub 이슈·PR 양식은 현재 필요하지 않아 모두 제거한다.
- Trigger frontmatter와 스킬 구성은 바꾸지 않는다.
- 역사 자료는 현재 reference처럼 보이지 않게 격하하고, 특정 프로젝트 관측은 일반 사실과 분리한다.
- 리팩터링 예시는 기존 관찰 가능 동작을 보존해야 한다.

## 현재 상태

- canonical 저장소의 공개 문서와 예시를 수정하고 `main`에 push했다.
- generated plugin snapshot과 source lock을 최신 canonical commit에서 다시 만들었다.
- GitHub issue·PR 양식을 제거하고 한국어·영어 changelog 경로를 추가했다.
- Project Legibility 검증과 저장소 test가 통과했다.

## 다음 행동

- patch release를 commit·tag·push하고 publisher catalog pin과 로컬 설치본을 갱신한다.

## 작업 경계

- 과거 task 로그는 정리하지 않는다.
- generated plugin snapshot은 직접 편집하지 않고 canonical commit에서 다시 만든다.
