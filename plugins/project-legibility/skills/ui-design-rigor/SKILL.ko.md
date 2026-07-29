# UI Design Rigor

## 경계

범위가 정해진 품질 개선 작업을 새로운 제품 설계로 키우지 않으면서, 기존 UI 또는 이미 방향이 정해진 UI를 더 이해하고 조작하기 쉽게 만든다.

**Review**는 사용자가 변경을 요청하지 않으면 읽기 전용이다. **Refine**은 화면 목적, 정해진 핵심 과업, 페이지 수준 위계와 디자인 시스템을 보존한다. **Bounded build**는 목적과 주변 구조가 정해진 component나 region에만 적용한다.

화면 목적, 핵심 과업, 페이지 수준 콘텐츠 위계나 전체 layout을 새로 결정해야 한다면 이를 국소 개선으로 결정하지 않는다. 더 넓은 UI 작업으로 분리해 보고하고, 그 결정에 의존하지 않는 독립적인 bounded scope만 계속한다.

의도적인 브랜드, 도메인, 위험, 수명주기와 권한 구분을 보존한다. 인접 재설계, component library 정리, 추측성 추상화나 새 product flow로 확장하지 않는다.

## 작업

현재 구현과 가장 가까운 제품 pattern을 확인하고 관찰한 결함과 취향을 구분한다. 기존 시스템을 우선하되, 결함이 그 사용법이나 shared component에 있으면 시스템을 재설계하지 않고 실제 소유하는 가장 작은 layer를 고친다.

적용되는 참조만 읽는다.

- 위계, 그룹화, 일관성, 색상, 타이포그래피나 장식은 [visual-structure.md](references/visual-structure.ko.md)를 읽는다.
- 과업 완료, 피드백, 오류, 복구나 cognitive walkthrough는 [interaction-and-task-review.md](references/interaction-and-task-review.ko.md)를 읽는다.
- 폼, custom widget, 키보드, 포커스, 의미 구조, 대비, 확대나 반응형 검사는 [component-behavior.md](references/component-behavior.ko.md)를 읽는다.
- 브라우저 또는 computer-use agent가 의도된 조작자일 때만 [agent-compatible-ui.md](references/agent-compatible-ui.ko.md)를 읽는다.
- 사용자가 확률적, 생성형, 개인화 또는 자율 AI 동작과 직접 상호작용할 때만 [human-ai-interaction.md](references/human-ai-interaction.ko.md)를 읽는다.

의도된 과업과 중요한 실패·복구 경로를 추적하고, polish보다 과업·구조·상태·의미 구조를 먼저 다룬다. 실제로 도달 가능하거나 중요한 상태와 반응형 조건만 확인하며, 요청이나 참조를 보편 checklist로 만들지 않는다.

## 근거와 출력

주장을 실제 근거에 따라 분류한다.

- **Verified:** 이름을 밝힌 명령, 도구, viewport, 상태나 상호작용으로 테스트 또는 측정했다.
- **Observed:** source나 렌더 결과에서 직접 확인했지만 완전히 실행하지 않았다.
- **Inferred:** 현재 근거상 가능성이 높지만 런타임, 콘텐츠, 브라우저나 보조 기술에 의존한다.
- **Not tested:** 필요한 근거가 없거나 범위 밖이다.

정적 검사는 keyboard behavior, responsive continuity, screen-reader behavior, WCAG 준수나 agent compatibility를 검증하지 못한다. 자동 검사는 상호작용 테스트와 사람 판단을 보조할 뿐 대체하지 않는다. 가능하면 변경한 주장을 검증하고, 그렇지 않으면 실제 근거 수준에 따라 `Observed`, `Inferred`, `Not tested`로 보고한다.

Review는 사용자 영향 순 finding, 위치, 근거, 결과, 가장 작은 권고와 확인·미확인 범위를 보고한다. 변경 작업은 보존한 불변 조건, 바꾼 영역, 근거와 남은 위험을 보고한다. 답은 작업 크기에 맞추며 hard failure를 숨기는 점수나 내부 worksheet를 쓰지 않는다.
