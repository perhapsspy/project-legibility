# 시각 구조

위계, 그룹화, 일관성, 타이포그래피, 색상이나 장식이 핵심일 때 읽는다.

## 의미에서 시작한다

- 시각적 강조를 바꾸기 전에 핵심 콘텐츠와 행동을 찾는다.
- 위계는 모든 섹션을 독특하게 만드는 대신 중요도를 드러내야 한다.
- 크기, 굵기, 대비, 위치, 간격, 깊이 중 한두 변수씩 바꾼다.
- 화면을 축소하거나 흐리게 보거나 grayscale로 볼 때도 핵심 콘텐츠와 행동이 드러나는지 확인한다. 이는 판단 보조 수단이지 자동 통과 조건이 아니다.

## 충분한 가장 약한 단서로 그룹화한다

다음 순서로 단서를 우선한다.

1. 간격
2. 정렬
3. 유사성
4. 공유 배경이나 경계

그룹 내부 간격을 그룹 사이보다 눈에 띄게 좁게 유지한다. Border, card나 background는 spacing과 alignment만으로 표현하기 어려운 독립 object, interaction boundary, state나 중요한 분리를 나타낼 때 정당화된다.

반응형 reflow 뒤 그룹화를 다시 확인한다. 넓은 화면에서 인접했던 요소가 쌓인 뒤 관계가 끊기거나 잘못된 그룹에 합쳐질 수 있다.

## 외형과 동작을 맞춘다

- 같은 역할과 동작에는 일관된 표현을 쓴다.
- 서로 다른 역할이 같은 동작으로 기대될 수 있으면 구분한다.
- 정적 텍스트나 아이콘을 control처럼 꾸미지 않는다.
- 선택 상태처럼 보이는 filled icon, badge나 surface를 중립 장식에 쓰지 않는다.
- 균일하게 보인다는 이유로 위험, 수명주기, 도메인이나 권한의 의도적 구분을 지우지 않는다.

## 기계적으로 획일화하지 않고 시스템을 재사용한다

다음 순서를 우선한다.

1. 기존 component
2. 기존 variant
3. 기존 token 조합
4. 정당화된 새 variant
5. 독립 책임이 있는 새 component

같은 primitive를 쓴다는 이유만으로 페이지 composition을 복제하지 않는다. 현재 과업과 정보 위계를 보존하며 컴포넌트 언어를 재사용한다.

## 역할을 가진 색상을 쓴다

Content, surface, border, action, selection, success, warning, danger 같은 의미 역할을 사용한다. 단독으로 보기 좋다는 이유만으로 색을 추가하지 않는다.

- 색상으로 구분한 상태, 선택, 오류와 상호작용에는 텍스트, 형태, 아이콘, 위치나 다른 비색상 단서를 함께 쓴다.
- 클릭 가능성을 암시할 수 있는 interaction color를 장식으로 재사용하지 않는다.
- Dark mode, gradient, image, disabled state와 overlay를 포함한 실제 상태와 배경에서 대비를 확인한다.
- 구현된 색을 측정하지 않았다면 대비 비율을 보고하지 않는다.

## 목적 있는 타이포그래피를 유지한다

제품에 더 강한 관습이 없을 때의 기본 휴리스틱이다.

- 작고 일관된 글꼴 family와 weight 집합을 쓴다.
- 긴 본문은 쓰기 방향의 시작점에 정렬한다.
- 본문과 대부분의 control은 문장형 표기를 쓴다.
- 작은 글자에 얇은 굵기를 피한다.
- 본문 line height는 `1.5` 부근에서 시작하고 글꼴, 언어, 줄 길이와 밀도에 맞춘다.
- 대문자와 장식적 글꼴은 글자 형태와 scanning이 유지되는 짧은 역할로 제한한다.

이는 출발점이지 접근성 요구사항이 아니다. 사용할 수 있는 기존 브랜드와 플랫폼 타이포그래피가 정본이다.

## 근거 없는 장식을 제거한다

새 border, surface, shadow, gradient, icon, animation, accent나 badge에는 다음 중 하나의 역할이 있어야 한다.

- 그룹화
- 위계
- 어포던스
- 상태
- 브랜드 표현

없애도 의미, 조작성과 정체성이 그대로면 제거한다.

## 출처

- Adham Dannaway, [16 little UI design tips that make a big impact](https://www.adhamdannaway.com/blog/ui-design/ui-design-tips)
- GOV.UK, [Government Design Principles](https://www.gov.uk/guidance/government-design-principles)
