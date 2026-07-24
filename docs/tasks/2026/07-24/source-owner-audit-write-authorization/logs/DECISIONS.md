# Decisions

**2026-07-24**

- Background: 실제 감사에서 owner 탐색은 유효했지만, 확인된 owner 근거가 사용자 승인 없이 쓰기 범위 확대로 이어졌다.
- Decision: discovery trigger를 바꾸지 않고 소스 소유권과 쓰기 권한을 분리하는 일반 원칙 한 문장만 bundled skill에 반영한다.
- Why: 정상적인 owner 탐색을 약화하지 않으면서 실제 실패 지점인 read-only finding에서 write authorization으로의 오승격을 막는다.
- Impact: owner 근거는 사용자 승인 범위 밖의 수정 권한으로 해석할 수 없다.
