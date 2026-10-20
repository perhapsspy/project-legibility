# Agent Cost Efficiency 번들 통합

## 목표와 범위

스킬 개편과 로컬 프로젝트·GitHub 저장소 명칭 통일을 제품 계약·catalog·호출 사례·source ID·URL·lock과 생성 bundle에 반영했다. 정본은 perhapsspy/agent-cost-efficiency의 skills/agent-cost-efficiency다.

## 현재 상태

스킬·소스 통합 완료. 정본 main 42157089eea8e488e8c0d739e9120637b3bbfcff를 push·readback했고 lock이 새 source ID와 URL로 같은 commit을 고정한다. 로컬 프로젝트 폴더·origin·설치 안내와 기존 Codex 신뢰 설정도 새 이름으로 맞췄다. 다른 7개 source pin은 유지했다.

스킬 정적 검사, offline bundle 검사, 새 로컬 source 경로와 bundle의 일치 검사, bundle validator와 단위 테스트 50개를 통과했다. GitHub repository ID 1262459856은 유지됐으며 과거 게시물의 옛 URL도 같은 저장소로 연결된다.

## 남은 경계

Codex 앱에 agent-cost-efficiency 프로젝트가 새 폴더 경로로 등록된 것을 list_projects로 확인했다. 명칭 통일과 앱 연결의 후속 작업도 완료됐다.

Codex·Claude Code 플러그인 동시 지원과 release는 후속 범위다. Plugin version·CHANGELOG·tag·publisher pin과 기존 설치본은 이번 통합에서 바꾸지 않았다. Routing 사례 검사는 형식·커버리지 증거이며 실제 모델 자동 선택이나 Claude Code 로딩을 입증하지 않는다.
