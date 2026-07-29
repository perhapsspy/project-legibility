# 스킬: Design User Interfaces (한국어 페어)

> 영문 기본 문서: `SKILL.md`
>
> 설명 동기화: 새 화면이나 큰 재설계에서 콘텐츠, 위계, 레이아웃, 반응형 동작과 관련 상태를 결정해 polished mockup이 아닌 완전하고 사용 가능한 인터페이스를 만든다. 기존 브랜드 체계를 보존하고 실제 렌더를 확인한다. 국소 스타일 수정, 확정 스펙의 기계적 구현, 일반 refactor, 읽기 전용 리뷰, 문서·슬라이드·이메일·CLI·독립 그래픽에는 사용하지 않는다.

## 목적

제품 목적과 실제 콘텐츠를 완전하고 사용 가능한 화면이나 흐름으로 만들고 실제 렌더 결과를 확인합니다.

`근거 -> 구조 -> 시각 체계 -> 관련 상태 -> 렌더 -> 장식`의 의존 순서를 유지합니다. 이는 승인 절차가 아니며, 되돌릴 수 있는 probe로 반복 판단하되 뒤 단계를 일찍 확정하지 않습니다.

사용자 과업과 화면 결정은 이 스킬이 소유하고, 구현 문법과 도구는 선택한 framework·platform을 따릅니다.

## 디자인 계약

### 판단을 근거에 묶는다

대상 사용자와 맥락, primary task 또는 운영을 조직하는 핵심 decision, 관찰 가능한 성공, 실제 콘텐츠와 동작, surface 종류와 밀도, 관련 제약, 기존 제품·브랜드 어휘에 인터페이스를 묶습니다.

되돌릴 수 있는 로컬 선택은 명시적 가정과 함께 진행합니다. 목적, 콘텐츠, 브랜드 제약의 부재가 결과를 크게 바꿀 때만 한 가지 집중 질문을 합니다.

수치, testimonial, 고객 logo, identifier, 운영 기간, 상태 이유, 성능 주장, error cause를 발명하지 않습니다. 근거 없는 주장은 제거하거나 검증 전 placeholder로 표시합니다. 실패 원인을 모르면 관찰 가능한 영향과 가능한 recovery를 설명합니다.

### 구조를 설계하면서 surface를 보존한다

distinctive styling 전에 읽기와 행동 순서를 정합니다. 필요한 콘텐츠와 행동을 중요도와 관계에 따라 묶고 primary task와 next action을 분명히 합니다.

Surface contract는 product workspace, marketing, content 중 무엇인지, platform, density, task character를 짧게 정합니다. 반응형 reflow에서도 이 계약을 유지합니다. 근거 없이 운영 화면을 marketing hero로 바꾸거나 작업 밀도를 크게 바꾸지 않습니다.

Page-level composition을 재사용하기 전에 새 surface의 primary decision, next action, 중요한 risk·lifecycle hierarchy를 지원하는지 확인합니다. Container는 template를 채우는 장식이 아니라 정보 관계나 interaction boundary를 표현해야 합니다.

### 위계를 복사하지 않고 체계를 재사용한다

기존 token, component, platform convention과 의도적인 brand expression을 우선합니다. Shared primitive는 visual vocabulary와 interaction contract를 제공하지만 다른 domain의 정보 위계까지 가져오지는 않습니다.

현재 과업에 필요하고 기존 체계에 없는 역할이 있을 때만 token, component, visual motif를 추가합니다. 체계가 없다면 제품 목적, 플랫폼, 환경과 콘텐츠가 지지하는 가장 작은 일관된 체계를 선택합니다.

Brand evidence가 없다는 사실은 brand personality를 발명하거나 유행하는 fallback을 채택할 허가가 아닙니다. 근거 없는 미학 선택은 낮은 강도로 유지합니다. 익숙한 pattern은 기본값도 금지 사항도 아니며, 이해·상호작용·제품 정체성에 실질적으로 기여할 때 motif를 유지합니다.

### 관련 상태를 올바른 경계에 구현한다

선택한 flow가 실제로 만날 수 있는 상태와 adaptation을 다룹니다. 여기에는 관련 loading, empty, error, success, availability·permission, 콘텐츠·viewport pressure와 accessibility가 포함됩니다.

모든 상태를 모든 화면에 강제하지 않습니다. 요청에 상태 목록이 있다는 이유만으로 relevant state가 되지는 않으며, 실제 dependency, permission, lifecycle, failure boundary에 연결해야 합니다. 실제 boundary를 happy path 뒤로 숨기지도 않습니다.

기본적으로 영향을 받은 region만 교체해 task location, object, recovery context를 보존합니다. 전체 surface나 session이 무효이거나, security·privacy상 이전 context를 숨겨야 하거나, 제품 계약이 요구할 때만 full-page takeover를 사용합니다.

사용자가 제품 계약에 따라 실제로 상태를 제어하는 경우가 아니면 state switcher, fixture selector, debug control은 release UI 밖에 둡니다.

### 주장에 맞는 검증을 한다

시각적 완료와 품질 주장은 중요한 상태와 viewport의 실제 렌더를 열어 확인해야 합니다. 코드 정합성, component 존재, 열어 보지 않은 capture는 시각 근거가 아닙니다. 여러 state, viewport, claim, interaction이 중요하면 [interface-evidence.ko.md](references/interface-evidence.ko.md)를 읽고 core task의 실패를 드러낼 수 있는 가장 작은 근거 집합을 선택합니다.

Source, render, interaction, provenance, human judgment 근거를 구분하며 어느 하나도 나머지 전부를 증명하지 않습니다. 렌더를 확인할 수 없으면 source-level 완료와 검증하지 못한 visual·interaction scope를 보고합니다.

## 완료

Design decision, 실제로 확인한 중요한 state와 viewport, 근거가 없거나 검증하지 못한 claim을 작업 크기에 맞게 보고합니다.

Core task가 관련 상태와 layout pressure에서 이해 가능하고 조작 가능하며, 정한 surface, evidence boundary, 의도적인 product identity를 잃지 않을 때 완료입니다.
