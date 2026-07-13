# 인터페이스 검증 근거 (한국어 페어)

> 영문 기본 문서: `interface-evidence.md`

복수의 viewport, 상태, 실제 주장 또는 상호작용을 포함한 인터페이스를 설계·구현할 때 이 문서를 읽는다. 모든 행을 의례적으로 검사하지 말고 핵심 사용자 과업을 깨뜨릴 수 있는 최소 행렬을 고른다.

## 근거 종류

| 근거 | 답하는 질문 | 완료로 과장하면 안 되는 것 |
|---|---|---|
| Source | 콘텐츠·token·component·상태가 구현되어 있는가? | 실제로 읽기 쉽고 조작 가능한가? |
| Render | 지정 viewport와 상태에서 위계와 배치가 유지되는가? | keyboard·screen reader로 사용할 수 있는가? |
| Interaction | focus, 입력, navigation, recovery가 동작하는가? | 모든 접근성 기준을 준수하는가? |
| Provenance | 수치·후기·로고·주장의 owner와 출처가 있는가? | 주장이 외부 세계에서 사실인가? |
| Human judgment | 선택이 목적·정체성·맥락에 맞는가? | 취향 판단이 보편적 규칙인가? |

## 최소 상태 행렬 고르기

먼저 primary task의 대표 성공 상태 하나를 고른다. 다음으로 실패 비용이 가장 큰 경계 상태와 레이아웃을 가장 많이 압박하는 viewport·콘텐츠 조합을 추가한다.

예시:

| 이름 | 목적 |
|---|---|
| `desktop-success` | 핵심 과업과 기본 위계 확인 |
| `mobile-empty` | 첫 사용과 좁은 화면 확인 |
| `narrow-long-copy` | wrapping과 그룹 관계 확인 |
| `error-recovery` | 실패 설명과 재시도 확인 |
| `permission-denied` | 접근 불가 이유와 다음 행동 확인 |
| `keyboard-primary-flow` | focus 순서와 조작 가능성 확인 |

작업과 관계없는 상태를 채우기 위해 mock을 늘리지 않는다. 반대로 실제 발생 가능한 오류나 권한 상태를 정상 화면 뒤로 미루지 않는다.

## 콘텐츠와 주장

- 실제 수치에는 출처 owner, 측정 조건, 기준 시점이 필요하다.
- testimonial과 고객 로고에는 실제 출처와 사용 권한이 필요하다.
- 성능 비교에는 비교 대상과 측정 조건이 필요하다.
- 식별자, 운영 기간, 상태 이유와 오류 원인도 사실로 읽히면 같은 provenance 경계를 적용한다.
- 실패 원인이 확인되지 않았다면 추정 설명 대신 관찰 가능한 영향과 가능한 recovery를 쓴다.
- 근거가 없으면 일반적인 숫자로 바꾸지 않는다. 해당 블록을 제거하거나 `검증 전 placeholder`로 표시한다.
- 실제 데이터가 아직 없으면 형태와 범위를 설명하는 neutral fixture를 사용하고 실제 값처럼 제시하지 않는다.

## 렌더 확인 순서

1. 구조 checkpoint에서 heading, body, primary action과 그룹 관계를 확인한다.
2. styled checkpoint에서 token, contrast, surface, density를 확인한다.
3. boundary checkpoint에서 좁은 폭, 긴 콘텐츠, 빈 상태와 오류 recovery를 확인한다.
4. interaction checkpoint에서 keyboard, focus, input과 주요 navigation을 확인한다.
5. 변경 후 같은 이름의 상태를 다시 확인한다.

상태를 재현하는 test harness와 debug control은 제품 UI가 아니다. 별도 URL, fixture, query나 development-only 도구로 상태를 만들고 대표 capture가 실제 사용자 surface를 보여 주도록 한다.

저장된 capture를 다시 열어 blank, 불투명 가림, viewport 밖 잘림과 stale 상태가 없는지 확인한다. responsive claim에는 같은 상태와 같은 데이터의 viewport 비교를 최소 하나 포함하되 모든 상태를 모든 폭에서 중복 캡처하지 않는다.

환경이나 도구 제약으로 일부 checkpoint를 실행하지 못하면 확인한 근거와 미확인 범위를 분리해 보고한다.

## 실패 신호

- 실제 콘텐츠가 없는데 polished marketing copy와 수치가 완성되어 있다.
- 구조 checkpoint 없이 styled hero와 card grid부터 완성했다.
- 정상 desktop 한 장만 보고 responsive와 상태 완성을 주장한다.
- scanner나 lint 통과를 더 좋은 화면의 증거로 사용한다.
- 의도적인 브랜드 표현을 generic pattern이라는 이유로 제거한다.
- 모든 화면에 같은 검증 행렬을 적용해 비용만 늘린다.
