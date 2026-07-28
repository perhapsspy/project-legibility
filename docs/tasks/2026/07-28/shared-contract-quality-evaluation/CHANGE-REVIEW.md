# 변경 검토

## 결론

`project-context`와 `codex-project-director`의 기존 역할 안에 필요한 규칙을 반영했다.

이번 변경은 다음 문제를 직접 다룬다.

- 여러 작업이 같은 해석에 의존하면서도 각자 다른 계약을 따르는 문제
- 코드 영역은 나뉘지만 사용자 가시 품질은 따로 판정할 수 없는 작업을 병렬화하는 문제
- 리뷰어의 관찰과 원인 추측이 같은 구현 지시로 소비되는 문제
- 높은 품질 비교 대상이 완료를 끝없이 미루는 관문으로 바뀌는 문제
- 반복할 때마다 비교 기준이 바뀌어 퇴행을 진전으로 오인하는 문제

정본 변경은 두 source 저장소에만 적용했다. Project Legibility의 `plugins/project-legibility/skills/**`는 생성 snapshot이므로 사용자 리뷰, 정본 commit·push 뒤 `scripts/sync_skills.py`로 갱신한다.

## 실제 차이

| 영역 | 이전 계약 | 변경한 계약 | 행동 차이 |
|---|---|---|---|
| 공유 해석의 정본 | task root와 `docs/reference/**`의 역할은 있었지만 공유 해석이 정본을 필요로 하는 조건은 암묵적이었다. | 여러 작업·담당·단계가 구현이나 승인 판정을 바꾸는 해석에 함께 의존하면 현재 정본 담당자 하나를 둔다. 기존 code·API·config·test·project document를 우선하고, 작업 전용 계약은 task root, 재사용 계약은 `docs/reference/**`가 맡는다. | 공통 용어나 작은 사실마다 문서를 만드는 대신 실제 구현·완료 차이를 만드는 해석만 정본화한다. |
| brief와 인계 | subagent brief가 필요한 맥락을 직접 전달했다. | 공유 계약이 있으면 `BRIEF.md`와 인계가 같은 정본 경로를 가리키고 작업별 상태·차이·다음 행동만 더한다. | 계약 복사본이 여러 작업에서 갈라지는 위험을 줄인다. |
| migration의 `REFERENCE` | 원칙·규칙·최근 신뢰 가능한 사실을 재사용 맥락으로 분류했다. | 이후 작업이 직접 따를 재사용 shared contract도 `REFERENCE`에 포함한다. | 기존 문서 이관 때 공유 계약을 단순 task note로 남기는 판단 공백을 메운다. |
| 작업 흐름 독립성 | 실행 영향, 의존성, 되돌림과 변경 영역으로 병렬화 여부를 판단했다. | 각 작업 흐름의 승인 결과를 독립성 조건에 추가했다. | 디렉터리가 달라도 하나의 사용자 가시 결과로만 평가되는 품질 작업은 한 담당자나 순차 통합 패스로 수렴한다. |
| 완료 관문과 비교 목표 | 완료 기준은 있었지만 높은 비교 기준의 종료 지위가 명확하지 않았다. | 사용자가 승인한 품질 기준을 필수 완료 관문 또는 지향 비교 목표로 분류한다. `COMPLETE`는 관문으로 판정하고 비교 목표는 품질 우선순위와 남은 거리 보고에 쓴다. | 비교 대상의 방향성은 유지하면서 명시된 관문을 통과한 작업의 종료 가능성을 보존한다. |
| 리뷰 증거와 진단 | 리뷰어는 독립 반증자였지만 관찰과 해법 제안의 지위가 분리되지 않았다. | 실제 산출물 또는 정본 증거 경로에서 확인한 불일치는 완료 주장을 반증한다. 원인과 수정 제안은 변경 담당자가 검증할 가설이다. | 리뷰의 센서 역할은 강화하고 root-cause 판단과 구현 책임은 기존 담당자에게 유지한다. |
| 반복 품질 기준선 | 승인 사실마다 정본 증거 출처를 두었지만 상대 품질 비교의 기준선 갱신 규칙은 없었다. | 반복 품질 주장에 현재 승인 baseline 경로와 정본 비교 경로 하나를 두고, 각 판본을 그 쌍으로 판정하며 승인 뒤 baseline을 갱신한다. | 퇴행한 판본이나 정보가 없는 반복이 현재 승인 결과를 대체하지 않는다. |
| Director Charter | 현재 제품 해석·완료 기준·경계·권한·정본 경로를 보유했다. | 프로젝트별 해석, 완료 관문·비교 목표와 권한은 직접 소유하고 지속 공유 계약은 정본 담당자 경로로 기록한다. | Charter의 재개 가능성은 유지하면서 프로젝트 계약의 복제 정본화를 줄인다. |

## 딥 리즈너 검토로 축소한 부분

딥 리즈너는 여섯 후보를 같은 강도로 추가하는 안보다 기존 계약에 최소한으로 합치는 안을 권고했다. 다음처럼 반영했다.

- shared contract는 자동 문서 생성 규칙이 아니라 `기존 정본 → task-local 정본 → 재사용 reference`의 선택 순서로 만들었다.
- 병렬화에는 추상적인 `quality independence` 용어 대신 각 작업 흐름의 `acceptance result`만 추가했다.
- baseline 규칙은 모든 작업이 아니라 반복 품질 주장에만 적용했다.
- Director Charter는 pointer만 모으는 router가 아니라 프로젝트별 적용 해석과 완료 기준을 계속 직접 소유한다.
- reviewer의 직접 증거는 원본 로그 전체가 아니라 실제 산출물 또는 정본 증거 경로에 연결된 최소 증거로 한정했다.

## 표현 원칙

새 규칙은 금지형 부정문을 추가하는 방식 대신 소유·분류·판정 행동을 긍정형으로 지정했다.

- `assign one current canonical owner`
- `classify ... as completion gates or comparison targets`
- `judge each revision against that pair`
- `proposed causes and fixes are hypotheses ... to verify`

기존 안전 경계의 부정문은 이번 범위에서 재작성하지 않았다. 이번 diff에는 새 `do not` 또는 “~하지 않는다” 형식의 금지 조항이 없다.

## 변경 파일

`project-context` 정본:

- `skills/project-context/SKILL.md`
- `skills/project-context-migration/SKILL.md`
- `docs/skill-direction.md`

`codex-project-director` 정본:

- `skills/codex-project-director/SKILL.md`
- `skills/codex-project-director/SKILL.ko.md`
- `docs/skill-direction.md`

Project Legibility 작업 기록:

- `docs/tasks/2026/07-28/shared-contract-quality-evaluation/`

## 검증

- 딥 리즈너 읽기 전용 비판 검토: 채택 2건, 축소 채택 4건으로 반영
- `project-context`: unit test 73개 통과
- `project-context`: runtime shape 검사 통과
- `project-context`, `project-context-migration`, `codex-project-director`: skill validator 통과
- 두 정본 저장소: `git diff --check` 통과
- 이번 Project Legibility 작업 문서: 격리된 runtime shape 검사 통과
- 현재 Project Legibility bundle: offline lock·snapshot 검사, bundle validator와 unit test 31개 통과

Project Legibility 전체 task tree의 runtime shape 검사는 기존 `docs/tasks/2026/07-26/director-visible-worker-boundary/logs/DECISIONS.md` 최신 블록이 4개 bullet 형식과 맞지 않는 선행 문제 한 건을 보고한다. 이번 작업 문서는 해당 문제와 독립적으로 통과했으며 기존 기록은 이번 변경 범위에서 유지했다.

## 배포 대상

검토된 문구는 `project-context` 정본 `b1394c9c54470109855fbae2b8b7a0c9275f88da`와 `codex-project-director` 정본 `9a18b665a96afb5787328aaf799437882533aea6`으로 공개 `main`에 게시됐다. Project Legibility 0.6.7은 두 정본과 생성 snapshot을 포함하는 patch release다.
