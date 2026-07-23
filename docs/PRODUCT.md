# Project Legibility 제품 계약

[English](PRODUCT.en.md)

이 문서는 Project Legibility의 제품 약속과 스킬 구성 원칙을 정의합니다.

## 제품 약속

Project Legibility는 에이전트의 변경이 빠르게 쌓여도 프로젝트를 계속 이해하고 검토하고 고칠 수 있게 돕습니다. 코드 구조, 판단 기준과 장기 작업 맥락을 필요한 작업에 연결해 프로젝트가 다음 변경을 받아낼 힘을 키웁니다.

## 스킬 구성과 선택

| 역할 | 스킬 | 참여 조건과 역할 |
|---|---|---|
| 핵심 작업 방식 | `structure-first`, `project-context` | `structure-first`는 변경이 흐름·상태·책임·조합이나 경계 계약을 만들거나 바꿀 때 이들을 읽고 검증하기 쉽게 유지합니다. `project-context`는 작업 맥락을 여러 세션이나 에이전트에 걸쳐 이어야 할 때 사용합니다. |
| 초기 방향 점검 | `purpose-fit-design` | 초기 설계나 구현 방향의 적합성이 중요한 선택으로 남아 있을 때 목적·제약·근거와 성공 조건을 확인합니다. 구체적인 전문 문제는 해당 전문 스킬이 맡습니다. |
| 전문 스킬 | `source-owner-audit`, `semantic-boundary-design`, `interactive-state-flow`, `design-user-interfaces`, `tighten-docs`, `agents-md-editor` | 정본의 적용 조건에 해당하는 구체적인 문제가 나타날 때 그 문제를 맡습니다. |
| 선택형 보조 | `codex-token-discipline`, `project-context-migration` | 높은 토큰 부담이나 기존 작업 맥락 이관처럼 별도의 운영·도입 문제가 있을 때 사용합니다. |

## 공통 선택 원칙

- 사용자는 평소처럼 작업을 요청하고, Codex는 요청에서 드러난 문제에 맞는 스킬을 선택합니다.
- 선택된 스킬은 자신의 책임을 수행하고, 실제로 인접 문제가 나타날 때 다른 스킬로 넘기거나 함께 사용합니다.

## 문서 경계

제품의 중심과 구성은 이 문서가 소유합니다. 설치와 일반 사용법은 [README](../README.md), 플러그인 구성과 릴리스 경계는 [Architecture](ARCHITECTURE.md), 개별 스킬의 의미·적용 조건·실행 방식은 각 정본 `SKILL.md`가 소유합니다. 공개 문구는 이 역할 관계를 따라 요약합니다.
