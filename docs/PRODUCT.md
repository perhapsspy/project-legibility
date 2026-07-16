# Project Legibility 제품 계약

[English](PRODUCT.en.md)

이 문서는 Project Legibility의 제품 약속, 스킬 구성 역할과 호출 모델을 소유합니다. 설치와 일반 사용법은 [README](../README.md), 플러그인 구성과 릴리스 경계는 [Architecture](ARCHITECTURE.md), 개별 스킬의 의미와 적용 조건·실행 흐름은 [README의 포함된 스킬 목록](../README.md#포함된-스킬)에 연결된 각 정본 저장소를 따릅니다.

## 제품 약속

Project Legibility는 에이전트의 변경이 빠르게 쌓여도 프로젝트를 계속 이해하고 검토하고 고칠 수 있게 돕습니다. 코드 구조, 판단 기준과 장기 작업 맥락을 필요한 작업에 연결해 프로젝트가 다음 변경을 받아낼 힘을 키웁니다.

## 구성 역할

| 역할 | 스킬 | 제품 수준의 역할 |
|---|---|---|
| Core practices | `structure-first`, `project-context` | 각각 비자명한 코드 변경과 여러 작업에 걸쳐 이어지는 작업에서 제품 약속을 직접 받치는 기본 작업 방식입니다. |
| Gateway | `purpose-fit-design` | 초기 설계나 구현 방향이 목적에서 벗어날 위험이 있을 때 적합성을 짧게 확인하고, 그대로 진행하거나 필요한 사실을 확인하거나 적합한 specialist로 연결합니다. |
| Specialists | `source-owner-audit`, `semantic-boundary-design`, `interactive-state-flow`, `design-user-interfaces`, `tighten-docs`, `agents-md-editor` | 정본의 적용 조건에 해당하는 구체적인 문제가 나타날 때 그 문제를 맡습니다. |
| Optional helpers | `codex-token-discipline`, `project-context-migration` | 높은 토큰 부담이나 기존 작업 맥락 이관처럼 별도의 운영·도입 문제가 있을 때 사용합니다. |

이 분류는 제품 안에서 각 스킬이 차지하는 역할을 정의합니다. 개별 스킬의 의미, 적용 조건, 책임 경계와 실행 방식은 정본 `SKILL.md`가 소유합니다.

## 호출 모델

- 사용자는 평소처럼 작업을 요청하고, Codex는 요청에서 드러난 문제에 맞는 스킬을 선택합니다.
- 선택된 스킬은 자신의 책임을 수행하고, 실제로 인접 문제가 나타날 때 다른 스킬로 넘기거나 함께 사용합니다.
- Core practice는 각 정본의 적용 조건이 나타날 때 선택합니다.
- `purpose-fit-design`은 초기 방향의 적합성이 불분명할 때 사용합니다. 전문 문제가 이미 분명하면 해당 specialist가 바로 작업을 맡습니다.
- `project-context`는 작업 맥락이 여러 세션이나 에이전트에 걸쳐 이어져야 할 때 선택합니다. 이런 작업이 반복되는 저장소는 `AGENTS.md`의 짧은 호출 지침으로 사용을 지속적으로 안내할 수 있습니다.

## 공개 설명 규칙

- README, manifest 설명과 시작 프롬프트는 이 계약을 독자가 평가하고 설치하고 시작할 수 있는 공개 문구로 표현할 수 있습니다.
- 공개 문구는 구성 역할의 소속과 위계, gateway의 조건부 성격과 optional helper의 보조적 성격을 유지합니다.
- 대표 사례와 적용 조건 예시는 적용 장면에 한정합니다. 스킬의 정체성은 정본 `SKILL.md`, 제품의 중심은 이 계약이 소유합니다.
- 국소적인 문구 교정은 영향을 받는 공개 문구에 적용합니다. 제품 약속, 구성 역할이나 호출 모델이 바뀌면 이 문서를 먼저 고칩니다.
