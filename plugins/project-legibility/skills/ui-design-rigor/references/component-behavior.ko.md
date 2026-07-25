# 컴포넌트 동작

폼, custom widget, 키보드 상호작용, 포커스, 의미 구조, 대비, 확대나 반응형 검토에 사용한다.

## 네이티브 동작을 우선한다

필요한 역할과 동작을 표현할 수 있으면 native HTML과 플랫폼 control을 쓴다. 네이티브 의미 구조는 구현이 다시 만들어야 할 키보드, 상태와 보조 기술 동작을 줄인다.

Custom widget에서는 다음을 따른다.

- 해당 WAI-ARIA Authoring Practices pattern을 따른다.
- 올바른 accessible name, role, value와 state를 노출한다.
- 그 역할의 관습적인 키보드 상호작용을 구현한다.
- DOM 순서, 읽기 순서와 시각 순서를 일관되게 유지한다.
- attribute만 보는 대신 실제 focus 이동을 테스트한다.

ARIA만으로 generic element의 상호작용 모델이 고쳐지지는 않는다.

## 포커스를 예측 가능하게 유지한다

- 플랫폼이 키보드 사용을 지원하면 모든 행동에 키보드로 도달하고 조작할 수 있어야 한다.
- 활성 focus indicator가 계속 보여야 한다.
- Focus, hover, selection, pressed와 disabled state를 구분한다.
- Dialog가 닫히면 invoking control 또는 다음 논리적 과업 위치로 focus를 돌린다.
- Focus된 item이 삭제되면 예상 가능한 남은 요소로 focus를 옮긴다.
- 확립된 pattern이 방향키 탐색을 쓴다면 composite widget을 하나의 tab stop으로 유지한다.
- 별도 탐색 순서를 만드는 양수 `tabindex`를 피한다.

## 폼과 오류에 label을 제공한다

- 모든 input에 지속되는 programmatic label을 준다.
- Help와 error text를 영향받은 field와 연결한다.
- 보안상 제거가 필요하지 않다면 validation failure 뒤 입력값을 유지한다.
- 가능한 경우 commit 전에 허용 format과 constraint를 설명한다.
- Summary error와 field error를 일관되고 발견 가능한 관계로 둔다.
- Placeholder text를 유일한 label로 쓰지 않는다.

## 상태를 완성한다

구현한 control마다 실제로 생길 수 있는 상태를 선택한다.

- default
- hover
- focus-visible
- active 또는 pressed
- selected 또는 current
- disabled 또는 unavailable
- loading 또는 busy
- invalid 또는 error

플랫폼에 대응하는 semantic state가 있으면 상태를 programmatically 노출한다. 다음 행동에 영향을 주는 차이라면 disabled control과 pending 또는 unavailable control을 똑같이 보이게 하지 않는다.

## 대비와 비색상 단서를 확인한다

WCAG 2.2 요구사항을 시각적 추측이 아니라 테스트 가능한 threshold로 쓴다.

- 일반 텍스트: 배경 대비 최소 `4.5:1`
- large-scale text: 최소 `3:1`
- 의미 있는 control, state와 graphic을 식별하는 데 필요한 시각 정보: 인접 색상 대비 최소 `3:1`
- 정보, 행동, 응답이나 구분을 색상만으로 전달하지 않음

문서화된 예외를 적용하고 모든 장식 edge나 inactive control에 수치를 일괄 적용하지 않는다. 구현된 foreground와 인접 background를 측정한다. 실패한 비율을 반올림해 통과시키지 않는다.

## 반응형 연속성을 확인한다

- 대표 너비에서 같은 이름의 과업과 상태를 확인한다.
- 관련 있다면 긴 label, 번역 문구, zoom, validation message, 대량 데이터와 software keyboard 압력을 확인한다.
- Reflow에서도 콘텐츠, 행동, 관계와 읽기 순서를 보존한다.
- Hover-only 정보와 pointer-only action을 피한다.
- 대상 플랫폼과 과업 빈도에 충분한 touch 및 pointer target을 유지하고 채택한 플랫폼 또는 디자인 시스템 기준을 따른다.
- 하나의 viewport로 반응형 완결성을 주장하지 않는다.

## 근거를 구분한다

Source inspection은 의미 구조와 state branch를 보여줄 수 있지만 신뢰할 수 있는 focus movement나 최종 대비를 증명하지 못한다. Screenshot은 위계를 보여줄 수 있지만 키보드 조작이나 accessible name을 증명하지 못한다. 자동 접근성 도구는 일부 문제만 찾으며 전체 준수를 확립하지 못한다.

## 출처

- W3C, [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- W3C, [Developing a Keyboard Interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/)
- W3C, [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- W3C, [Understanding Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color)
- W3C, [Understanding Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast)
