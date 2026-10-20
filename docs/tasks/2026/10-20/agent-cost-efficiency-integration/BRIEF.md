# Agent Cost Efficiency 번들 통합

## 목표와 범위

승인된 스킬 개편을 Project Legibility의 제품 계약·catalog·호출 사례·lock과 생성 bundle에 반영했다. 정본 저장소는 perhapsspy/codex-token-discipline이며 배포 경로는 skills/agent-cost-efficiency다.

## 현재 상태

통합 완료. 정본 main은 3403d274771ea26eb9e1fcfed181c034d29f54f6로 push·readback했고 lock이 같은 commit을 고정한다. 새 스킬은 SKILL.md, SKILL.ko.md와 agents/openai.yaml만 포함한다. 다른 7개 source pin은 유지했다.

스킬 metadata·한영 지침 대조, offline bundle 무결성·bundle validator와 단위 테스트 50개를 통과했다. 정본과 bundle의 세 파일이 바이트 단위로 일치한다. Routing 사례 검사는 선언된 형식·커버리지 검증이며 실제 모델의 자동 선택이나 Claude Code 로딩을 입증하지 않는다.

## 후속 경계

스킬 개편은 끝났다. Codex·Claude Code 플러그인 동시 지원과 release는 후속 작업으로 남는다. Plugin version·CHANGELOG·tag·publisher pin과 기존 설치본은 이번 통합에서 바꾸지 않았다.
