# Human-AI Interaction

사용자가 생성, 예측, 개인화 또는 자율 AI 동작과 직접 상호작용할 때만 읽는다.

## 기대를 설정한다

- 현재 맥락에서 AI가 할 수 있는 일을 설명한다.
- 중요한 한계나 불확실성이 결정에 영향을 주는 지점에서 알린다.
- AI 생성 콘텐츠를 사용자 작성, 측정 또는 공식 제품 데이터와 구분한다.
- 확률적 출력을 보장된 사실이나 완료된 행동처럼 제시하지 않는다.

## 수정과 제어를 지원한다

- 과업이 허용하면 사용자가 AI 결과를 닫고, 편집하고, 다시 시도하고, 범위를 좁히거나 대체할 수 있게 한다.
- 재생성이나 수정 실패에서도 사용자 작업을 보존한다.
- 제품 계약이 사람의 제어를 요구하는 중요한 외부 행동 전 명시적 확인을 받는다.
- 자율 행동의 범위와 중단 조건을 보이게 한다.

## 실패를 건설적으로 다룬다

- 알려진 것, 불확실한 것과 다음 행동을 보여준다.
- 의도된 범위를 안전하게 추론할 수 없으면 clarification을 요청한다.
- 결과를 믿거나 행동할지 판단하는 데 필요할 때 설명을 제공한다.
- 제공되지 않은 model confidence, source나 원인을 지어내지 않는다.

## 시간에 따른 변화를 관리한다

- 중요한 개인화 또는 model behavior 변화를 발견할 수 있게 한다.
- 관련 setting, history, feedback 또는 correction path를 제공한다.
- 제품 근거 없이 한 번의 행동을 지속적인 동의나 선호로 취급하지 않는다.

## 근거 경계

이 지침으로 상호작용 위험을 찾고 실제 AI 상태와 실패 경로를 검증한다. UI review만으로 model quality, safety, fairness, privacy나 factual accuracy를 확립할 수 없다.

## 출처

- Microsoft Research, [Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/)
- Microsoft Research, [HAX Toolkit](https://www.microsoft.com/en-us/research/project/hax-toolkit/)
