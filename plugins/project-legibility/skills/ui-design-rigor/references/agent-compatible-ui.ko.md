# 에이전트 호환 UI

브라우저 자동화 또는 computer-use agent가 의도된 조작자일 때만 읽는다. 사람의 사용성이나 접근성을 약화시키지 않는 추가 관점으로 적용한다.

## 안정적이고 명시적인 상태를 노출한다

- 과업에 중요한 상태를 화면과 의미 구조에 노출한다.
- 동등한 화면에서 안정적인 label, name과 control 위치를 우선한다.
- Success, failure, pending과 partial completion을 명시한다.
- 중요한 정보를 순간적, hover-only, animation-only로 두거나 장식에서 시각적으로 추론하게 하지 않는다.

## 진행과 복구를 명시한다

- 과업에 전이가 있다면 label이 있는 next, back, cancel, retry와 finish action을 제공한다.
- 현재 단계와 완료 결과를 관찰할 수 있게 한다.
- 결과가 다른 여러 개의 시각적으로 동등한 탈출·복구 경로를 피한다.
- 익숙한 플랫폼 관습이고 accessible name이 있는 경우가 아니라면 중요한 icon-only control에 label을 제공한다.

## 의미 있는 조작을 보존한다

- 가능하면 native role과 state를 쓴다.
- Accessible name을 안정적이고 target으로 삼을 만큼 고유하게 유지한다.
- Object context가 programmatically 연결되지 않은 모호한 중복 label을 피한다.
- Overlay, menu와 dialog를 명확한 invoking control과 예측 가능한 focus path에 연결한다.

## 근거 경계

이 검사는 호환성을 높일 수 있지만 안정적인 자동화를 증명하지 않는다. 실제 agent와 환경으로 의도된 과업을 검증한다. 실패를 task, state, locator 또는 recovery 근거로 기록하고 보편적 agent compatibility를 주장하지 않는다.

## 출처 상태

다음 자료는 2026년 preprint다. 제안된 확장 휴리스틱을 보편 표준이 아닌 잠정 지침으로 취급한다.

- Liu et al., [Augmenting Interface Usability Heuristics for Reliable Computer-Use Agents](https://arxiv.org/abs/2605.02729)
