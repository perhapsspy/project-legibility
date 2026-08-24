# Project Legibility 제품 계약

[English](PRODUCT.en.md)

이 문서는 Project Legibility의 제품 약속과 스킬 구성 원칙을 정의합니다.

## 제품 약속

Project Legibility는 에이전트의 변경이 빠르게 쌓여도 프로젝트를 계속 이해하고 검토하고 고칠 수 있게 돕습니다. 코드 구조, 판단 기준과 장기 작업 맥락을 필요한 작업에 연결해 프로젝트가 다음 변경을 받아낼 힘을 키웁니다.

## 스킬 구성과 선택

| 역할 | 스킬 | 참여 조건과 역할 |
|---|---|---|
| 핵심 작업 방식 | `structure-first`, `project-context` | `structure-first`는 변경이 흐름·상태·책임·조합이나 경계 계약을 만들거나 바꿀 때 이들을 읽고 검증하기 쉽게 유지합니다. 확정된 동일 도메인 의미가 여러 표현에서 달라질 실질적 위험이 있으면 해석 owner와 허용된 projection·호환 번역 경계도 같은 구조 계약 안에서 지킵니다. `project-context`는 작업 맥락을 여러 세션이나 에이전트에 걸쳐 이어야 할 때 사용합니다. |
| 초기 방향 점검 | `purpose-fit-design` | 초기 설계나 구현 방향의 적합성이 중요한 선택으로 남아 있을 때 목적·제약·근거와 성공 조건을 확인합니다. 구체적인 전문 문제는 해당 전문 스킬이 맡습니다. |
| 전문 스킬 | `source-owner-audit`, `interactive-state-flow`, `design-user-interfaces`, `ui-design-rigor`, `tighten-docs`, `agents-md-editor` | 정본의 적용 조건에 해당하는 구체적인 문제가 나타날 때 그 문제를 맡습니다. `design-user-interfaces`는 새 화면과 큰 재설계를, `ui-design-rigor`는 기존 화면의 검토·구조 보존형 개선과 방향이 정해진 구성 요소·영역 구현을 맡습니다. `tighten-docs`는 의미가 정해진 현재 정본 문서를 만들거나 크게 고치거나 마무리할 때 초안부터 참여하며, 미해결 제품·정책·설계·구현 의미를 대신 결정하지 않습니다. |
| 선택형 보조 | `codex-project-director`, `codex-token-discipline`, `project-context-migration` | `codex-project-director`는 사용자가 `$codex-project-director`로 명시 호출한 세션에서 여러 Codex 작업을 지휘합니다. `codex-token-discipline`은 넓거나 예측하기 어려운 출력, 브라우저 루프, subagent, 반복 compaction처럼 명확한 초과 비용 위험이 있을 때 자동 참여합니다. 기존 작업 맥락 이관은 `project-context-migration`이 맡습니다. |

## 공통 선택 원칙

- 사용자는 평소처럼 작업을 요청하고, Codex는 요청에서 드러난 문제에 맞는 스킬을 선택합니다.
- 선택된 스킬은 자신의 책임을 수행하고, 실제로 인접 문제가 나타날 때 다른 스킬로 넘기거나 함께 사용합니다.

## 구성 변경

새 스킬은 기존 구성에서 맡지 못한 역할과 인접 스킬의 선택 경계가 분명하고, 정본 검증과 대표 호출 사례가 준비됐을 때 maintainer가 제품 역할과 호출 경계를 승인해 편입합니다. 배포 뒤 구성 검토는 중대한 실패, 반복되는 선택 혼동이나 고유 효용이 없는 역할 중복을 근거로 진행합니다.

개별 스킬의 의미·적용 조건·실행 방식은 각 정본 `SKILL.md`가 소유합니다. 이 문서는 스킬 추가·제거와 제품 수준의 역할 관계를 소유합니다.
