# Decisions

**2026-07-24**

- Background: 실제 감사에서 owner 탐색은 유효했지만, 확인된 owner 근거가 사용자 승인 없이 쓰기 범위 확대로 이어졌다.
- Decision: discovery trigger를 바꾸지 않고 소스 소유권과 쓰기 권한을 분리하는 일반 원칙 한 문장만 bundled skill에 반영한다.
- Why: 정상적인 owner 탐색을 약화하지 않으면서 실제 실패 지점인 read-only finding에서 write authorization으로의 오승격을 막는다.
- Impact: owner 근거는 사용자 승인 범위 밖의 수정 권한으로 해석할 수 없다.

**2026-07-24**
- bundle 반영만으로는 설치 사용자가 새 경계를 받지 못하며, CONTRIBUTING.md가 patch release부터 publisher pin과 install round trip까지의 절차를 소유한다.
- 호환 가능한 instruction 교정으로 분류해 Project Legibility 0.5.1 patch release와 publisher marketplace 갱신을 완료한다.
- trigger와 plugin 구성은 유지하면서 기존 설치 경로에 교정된 스킬을 전달하는 가장 작은 SemVer 변경이다.
- release commit·tag·publisher pin·로컬 설치본을 같은 0.5.1 tree로 검증한다.
