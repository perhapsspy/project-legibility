# 스킬: Design User Interfaces (한국어 페어)

> 영문 기본 문서: `SKILL.md`

## 역할

제품 목적과 실제 콘텐츠를 의도적이고 완전한 화면으로 번역하고, 그 결정이 구현 중 기본값으로 퇴행하지 않도록 실제 렌더 검증까지 책임진다.

완성 화면부터 생성하지 않는다. `근거 -> 구조 -> 시각 체계 -> 상태 -> 렌더 -> 장식` 순서를 유지한다. 작은 화면에서는 각 단계를 짧게 수행하되 순서를 뒤집지 않는다.

## 책임 경계

웹·모바일·데스크톱의 화면 기반 사용자 인터페이스와 그 표현 상태를 다룬다. 기존 화면의 큰 재설계도 포함하지만, 단순 사후 평가나 국소 스타일 수정은 포함하지 않는다.

다음 문제는 필요할 때만 인접 전문 스킬로 넘긴다.

- 현재 디자인 시스템·컴포넌트·제품 동작의 정본이 불분명하면 source-owner 발견을 사용한다.
- UI·API·저장소 사이에서 상태·권한·명령의 의미가 갈리면 semantic-boundary 설계를 사용한다.
- 입력 지연, stale 결과, pending·freshness 경쟁이 핵심이면 interactive-state 흐름을 사용한다.
- 일반 코드 구조와 테스트 설계가 핵심이면 structure-focused 구현을 사용한다.
- 프레임워크나 플랫폼 전문 스킬은 구현 문법과 도구를 소유하고, 이 스킬은 사용자 과업과 화면 결정을 계속 소유한다.

단순한 화면 생성이 매번 여러 전문 스킬을 거쳐야만 완료된다면 경계를 과도하게 넓힌 것이다. 실제 문제가 드러난 경우에만 넘긴다.

## 기본 운영 규칙

- 기존 저장소와 사용자 자료에서 확인 가능한 근거를 먼저 사용한다.
- 되돌릴 수 있는 로컬 선택은 명시적인 가정과 함께 진행한다.
- 결과를 크게 바꾸는 목적·콘텐츠·브랜드 제약이 없을 때만 한 가지 집중 질문을 한다.
- 사용자가 매 단계에서 승인하도록 작업을 끊지 않는다.
- 실제 수치·후기·고객 로고·성능 주장을 발명하지 않는다. 근거가 없으면 빼거나 명확한 placeholder로 남긴다.
- existing work와 의도적인 표현을 존중한다. 새 디자인 시스템이나 전면 restyle을 편의상 만들지 않는다.
- AI가 새로 추가한 시각 motif에는 유지 근거가 필요하다. 기존 brand evidence나 정보·상호작용 역할이 없으면 기본적으로 생략한다.

## 제작 흐름

### 1. 근거를 고정한다

구현 전에 다음 중 결과를 바꾸는 항목만 확인한다.

- 대상 사용자와 현재 맥락
- 화면에서 완료할 한 가지 핵심 과업
- 관찰 가능한 성공 조건
- 실제 콘텐츠, 데이터 형태와 주장 근거
- 기존 brand voice, 디자인 token, component, 플랫폼 관례
- 의도적으로 피해야 할 인상이나 패턴
- surface contract: 제품 작업 화면·마케팅·콘텐츠 중 무엇인지, 플랫폼, 목표 밀도와 핵심 작업 성격

운영 화면에서 page-level composition을 재사용하기 전에는 운영자의 핵심 판단과 다음 행동, 그리고 위계를 실질적으로 바꾸는 위험이나 lifecycle 구분을 먼저 확인한다.

근거가 없는 상태에서 generic hero 문구, 통계, testimonial, 기능 카드로 빈칸을 채우지 않는다. 콘텐츠가 준비되지 않았다면 필요한 콘텐츠 구조를 먼저 만들고 미확정 상태를 표시한다.

사용자가 사실로 읽을 수 있는 식별자, 운영 metadata, 기간, 상태 이유와 오류 원인도 장식이 아니라 콘텐츠다. 입력, 제품 계약 또는 기존 source가 제공한 범위만 표시한다. 원인이 주어지지 않은 실패는 관찰 가능한 결과와 recovery만 말한다.

surface contract는 1~2문장이면 충분하다. viewport 변화는 배치를 바꿀 수 있지만, 제품 작업 화면을 근거 없이 marketing hero로 바꾸거나 작업 밀도를 크게 바꾸면 안 된다.

### 2. 콘텐츠와 구조를 결정한다

시각 스타일보다 먼저 사용자가 읽고 행동할 순서를 정한다.

1. 필요한 콘텐츠와 행동을 나열한다.
2. 중요도와 관계로 그룹을 만든다.
3. 핵심 과업의 primary flow를 잡는다.
4. 저충실도 화면 구조를 만든다.
5. 선택한 구조와 중요한 대안 기각 이유를 짧게 기록한다.

카드, 탭, modal, sidebar, 단계 번호는 외형이 아니라 정보 관계나 행동 계약이 있을 때만 사용한다.

큰 재설계나 새 화면에서는 distinctive styling 전에 structure checkpoint를 두고 surface contract, primary task, 콘텐츠 위계가 맞는지 확인한다. 작은 화면은 별도 문서를 만들지 않고 구현 안에서 짧게 확인한다.

### 3. 시각 체계에 결합한다

기존 token과 component를 우선 사용한다. 새 값은 현재 과업에 필요한 역할이 기존 체계에 없을 때만 추가한다.

공용 primitive는 token과 상호작용 계약의 어휘이지 page template가 아니다. 다른 도메인의 정보 위계나 list-to-detail 구성을 함께 물려받지 않고 재사용한다.

- 위계는 먼저 크기·굵기·간격·정렬로 만든다.
- 색은 브랜드와 상태 의미를 보조하며, 구조를 대신하지 않는다.
- 관련 항목은 가깝게, 무관한 그룹은 분명히 떨어뜨린다.
- surface, border, radius, shadow는 그룹과 상호작용 의미가 있을 때만 사용한다.
- typography와 icon은 제품·플랫폼 맥락에 맞는 이유가 있어야 한다.
- 한 화면 안의 voice와 강조 체계를 일관되게 유지한다.

기존 체계가 없다면 제품 목적과 콘텐츠에서 설명 가능한 최소 체계를 선택한다. 유행하는 template 조합을 브랜드 결정처럼 취급하지 않는다.

brand evidence가 없다는 사실은 새 brand personality를 발명할 허가가 아니다. 플랫폼 관례, 작업 환경, 정보 밀도와 상호작용 요구가 표현을 결정하게 하고, 근거 없는 미학 선택은 낮은 강도로 유지한다.

`paper + ink + single accent`, editorial, terminal, generic SaaS dashboard도 안전한 기본값이 아니다. 특정 미학을 금지하지는 않되, 화면 유형·환경·콘텐츠·플랫폼 근거 없이 clean fallback으로 자동 채택하지 않는다.

첫 styled render 전에 AI가 새로 추가하는 mark, kicker·eyebrow, ordinal, surface, effect, motion만 짧게 심사한다. 기존 디자인 시스템의 motif는 다시 증명하지 않는다. 새 motif가 정보·상호작용·정체성 중 맡는 역할과 근거가 없으면 넣지 않는다.

### 4. 관련 상태를 함께 구현한다

정상 상태만 예쁘게 만들고 끝내지 않는다. 현재 화면에 실제로 적용되는 상태를 함께 설계하고 구현한다.

error, empty, permission-denied를 이유 없이 별도 full-page surface로 재분류하지 않는다. 기본적으로 영향을 받은 범위만 대체하고 사용자가 과업의 위치, 대상과 recovery를 이해하는 데 필요한 맥락을 유지한다. 전체 surface나 session이 실제로 무효이거나, 보안·개인정보 때문에 기존 맥락을 숨겨야 하거나, 제품 계약이 명시한 경우에는 full-page takeover를 사용한다.

- loading 또는 progressive
- empty 또는 first-use
- error와 recovery
- success와 next action
- disabled, unavailable 또는 permission denied
- mobile·좁은 폭·긴 문구·큰 데이터
- keyboard focus, label, contrast, reduced motion 등 기본 접근성

모든 화면에 모든 상태를 억지로 추가하지 않는다. 사용자 과업에서 발생 가능한 상태와 경계만 선택한다.

### 5. 구현 중 실제 렌더를 확인한다

마지막 스크린샷 한 번에 의존하지 않는다. 구조가 보이는 첫 구현부터 이름 붙인 상태를 실제 렌더로 확인한다.

1. structure checkpoint에서 surface contract, 콘텐츠 위계와 primary action을 확인한다.
2. 대표 viewport와 핵심 상태를 확인한다.
3. 긴 콘텐츠와 좁은 폭에서 위계가 유지되는지 확인한다.
4. keyboard와 핵심 상호작용을 확인한다.
5. styled checkpoint에서 화면 유형·밀도·primary action이 바뀌지 않았는지와 새 motif의 근거를 확인한다.
6. 수정 후 같은 상태를 다시 확인한다.

capture는 직접 열어 내용과 크기를 확인하기 전에는 render 근거가 아니다. blank, 가림, 잘림, stale 상태가 있으면 다시 캡처한다. responsive continuity를 주장할 때는 핵심 영역 하나 이상을 같은 이름의 상태와 같은 데이터로 viewport 사이에서 비교한다.

여러 viewport·상태·주장 근거가 있는 작업에서는 [interface-evidence.ko.md](references/interface-evidence.ko.md)를 읽고 최소 검증 행렬을 고른다.

검증을 위한 state switcher, fixture selector와 debug control은 사용자가 실제로 상태를 선택하는 제품 계약이 아니면 제품 surface에 넣지 않는다. development-only harness나 surface 밖의 테스트 경로에서 상태를 만들고 release UI와 대표 capture에서는 제외한다.

렌더를 확인할 수 없으면 source-level 구현까지만 완료했다고 말하고, 시각 품질이나 상호작용 검증을 완료했다고 주장하지 않는다.

### 6. 장식을 마지막에 추가한다

콘텐츠, 위계, 상태가 성립한 뒤에만 장식과 motion을 추가한다. 각 장식은 정보, 상호작용, 정체성 중 하나의 역할을 설명할 수 있어야 한다.

다음은 금지 목록이 아니라 설명되지 않은 기본값의 후보다.

- 제품과 무관한 gradient·glow·glass surface
- 무엇이든 감싸는 card와 pill·badge
- 근거 없는 큰 통계와 testimonial
- 모든 제목 위의 kicker와 장식 번호
- 근거 없이 만든 logo·wordmark·날짜 tag·editorial metadata
- 의미 없는 emoji·icon tile·상태 pulse
- 한 값으로 반복되는 간격과 과도한 radius·shadow
- template voice와 추상적인 과장 문구

후보가 제품 목적과 실제 정보에 기여하면 유지한다. 단순히 흔하다는 이유로 다른 스타일로 일괄 교체하지 않는다.

첫 styled render 뒤에는 삭제 검사를 한다.

- kicker·eyebrow가 제목과 같은 말을 반복하면 삭제한다.
- 번호는 실제 순서, 우선순위 또는 이후 참조가 있을 때만 유지한다.
- status dot·pulse는 현재 상태를 전달할 때만 유지한다.
- card·surface는 안의 내용이 독립된 대상이나 상호작용 경계일 때만 유지한다.
- 색·효과·icon·motion을 제거해도 정보, 조작 가능성, 제품 정체성이 손상되지 않으면 삭제한다.

“디자인된 것처럼 보이게 한다”는 유지 근거가 아니다.

## 완료 근거

완료 시 작업 규모에 맞게 다음만 간결히 보고한다.

- 핵심 사용자 과업과 선택한 화면 구조
- 사용하거나 추가한 디자인 체계와 이유
- 확인한 이름 붙은 viewport·상태
- 새 motif를 실제로 추가했다면 그 역할과 근거
- 근거가 없어서 제외하거나 placeholder로 남긴 주장
- 렌더·상호작용 미검증 범위와 다음 확인점

## 최종 점검

- 실제 콘텐츠와 과업이 장식보다 먼저 결정되었는가?
- 사용자가 다음 행동과 상태를 색이나 아이콘 없이도 이해할 수 있는가?
- 새 token·component·surface가 실제 책임을 갖는가?
- 정상·실패·빈 상태와 좁은 화면에서 핵심 과업이 유지되는가?
- 의도적인 브랜드 선택과 설명되지 않은 template 기본값을 구분했는가?
- source, render, interaction, human judgment의 검증 경계를 과장하지 않았는가?
