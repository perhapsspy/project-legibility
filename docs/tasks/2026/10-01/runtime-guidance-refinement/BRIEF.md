# Runtime guidance refinement

## 목표와 범위

기존 공개 스킬의 실행 품질을 최소 문안으로 개선하고 정본에서 bundle·publisher로 게시한다. 구성·trigger·모델·역할 계약은 유지한다.

## 현재 상태

project-context는 목표·쓰기 범위·산출물에 따른 세션 재사용과 재사용 도구 owner를 명확히 했다. structure-first는 기존 재현의 작업량·단계 시간, 검사 결과에 따른 완료 범위, 배포의 기존 인증·설정 owner와 실제 접근 경로를 보완했다. source-owner-audit는 도구·workflow·접근·연결·인증 상태를 구분한다. 세 정본 commit을 선택 동기화했다. 한영 pair·diff·runtime shape, project-context 68개, bundle 50개, offline integrity와 bundle validation은 통과했다.

## 게시와 재개

0.16.1 문안과 생성 bundle을 릴리스 런북으로 게시한다. 게시 상태는 remote main·동일 SHA의 tag/Release·publisher pin과 CI에서 확인한다. 이 문안 묶음의 후속 기능은 자동 시작하지 않으며, 추가 의미 변경은 새 목표로 정한다. 모델·역할 설정과 관리형 스킬은 유지한다.
