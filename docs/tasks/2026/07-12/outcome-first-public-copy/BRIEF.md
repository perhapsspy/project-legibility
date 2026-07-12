# 사용자 중심 설명 정리

## 목표

사용자에게 노출되는 설명을 구현 용어보다 문제와 결과가 먼저 보이도록 고치고, 메타 저장소가 canonical 스킬 설명을 중복 소유하지 않게 한다.

## 범위

- canonical 스킬 저장소의 README와 UI 카드
- Project Legibility의 plugin-level 설명, README와 GitHub 양식
- publisher marketplace의 라우팅 README와 공개 metadata

## 현재 이해

- 각 canonical 저장소가 스킬의 효용, 사용 예시와 UI 카드를 소유한다.
- Project Legibility는 묶음 전체가 주는 결과와 설치·구성 경로만 소유한다.
- publisher marketplace는 설치 좌표와 source 링크만 소유한다.
- 일반 효용 문구에서는 Codex를 제거하되, 명령·고유 식별자나 Codex 자체가 대상인 설명에는 남긴다.

## 현재 상태

- canonical README와 UI 카드 변경을 각 저장소 main에 push했다.
- Project Legibility v0.2.2 snapshot, plugin-level 설명과 사용자 양식을 갱신했다.
- trigger 의미와 스킬 구성은 바뀌지 않았다.

## 다음 행동

- remote source 검증 뒤 v0.2.2 release와 publisher catalog를 공개한다.

## 작업 경계

- `SKILL.md` frontmatter와 trigger 의미는 바꾸지 않는다.
- 생성된 bundle snapshot은 직접 편집하지 않고 canonical commit에서 다시 만든다.
