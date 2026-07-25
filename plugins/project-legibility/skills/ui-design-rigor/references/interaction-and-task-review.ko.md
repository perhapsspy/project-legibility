# 상호작용과 과업 검토

과업 완료, 피드백, 오류, 복구나 학습 가능성이 핵심일 때 읽는다.

## 대표 과업을 선택한다

사용자 언어로 목표를 적는다. 가장 짧은 의도된 행동 순서와 비용이 큰 실패 또는 복구 경로를 나열한다. Control을 고립된 object로 보는 대신 이 경로를 검토한다.

중요한 단계마다 묻는다.

1. 사용자가 의도한 효과를 달성하려 할 것인가?
2. 올바른 행동이 가능함을 발견할 수 있는가?
3. 올바른 행동을 원하는 효과와 연결할 수 있는가?
4. 목표를 향한 진행을 확인할 수 있는가?

실패한 단계의 근거를 기록한다: 숨겨진 행동, 익숙하지 않은 언어, 약한 연결, 누락된 피드백, 기억 부담이나 막힌 복구.

## 시스템 상태를 보이게 유지한다

- 사용자가 원인과 결과를 연결할 수 있는 시간 안에 행동을 확인한다.
- 과업에서 구분이 중요하면 idle, pending, success, partial success, failure와 stale state를 구분한다.
- 진행과 완료를 영향받는 object 또는 영역에 연결한다.
- 중요한 결과의 유일한 기록으로 순간적인 toast를 쓰지 않는다.
- 무엇이 바뀌었고 무엇이 남았는지 이해할 맥락을 유지한다.

## 사용자 언어와 mental model을 쓴다

- 내부 구현 용어보다 사용자가 아는 도메인 언어를 우선한다.
- 과업이 요구하는 순서로 정보를 둔다.
- 관련 화면에서 label을 안정적으로 유지한다.
- 다른 화면의 정보를 기억하게 하는 대신 필요한 시점에 option과 constraint를 보인다.
- 낯설거나 중요한 결정에는 맥락형 도움을 제공한다.

## 제어와 복구를 보존한다

- Mode, dialog와 multi-step task에서 명확히 나갈 수 있게 한다.
- 되돌릴 수 있는 행동에는 undo를 우선한다.
- 비용이 크고 되돌리기 어려운 행동에만 confirmation을 선택적으로 쓰고 대상과 결과를 설명한다.
- Cancel, back, retry와 대안 경로를 발견할 수 있게 한다.
- 닫기, 삭제나 실패 뒤 합리적인 위치로 focus와 맥락을 돌린다.

## 설명하기 전에 예방한다

다음 순서를 우선한다.

1. 오류가 나기 쉬운 조건 제거
2. 잘못된 입력 제한
3. 안전한 기본값이나 preview 제공
4. 비용이 큰 commit 전 경고
5. 실패 뒤 설명과 복구

오류 메시지는 영향받은 input 또는 action을 가리키고, 평이한 언어로 문제를 설명하며, 다음 유용한 행동을 제공해야 한다. 시스템이 확인하지 않은 기술적 원인을 지어내지 않는다.

## 작업에 맞게 검토한다

휴리스틱은 넓은 판단 보조 수단이지 결정론적 점수가 아니다. 핵심 과업과 중요한 위험에 맞는 질문만 쓴다. Cognitive walkthrough는 전문가 inspection이며 대표 사용자를 관찰하는 일을 대체하지 않는다.

## 출처

- Jakob Nielsen, [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/)
- Wharton, Rieman, Lewis, and Polson, “The Cognitive Walkthrough Method: A Practitioner's Guide,” in *Usability Inspection Methods* (1994)
- GOV.UK, [Government Design Principles](https://www.gov.uk/guidance/government-design-principles)
