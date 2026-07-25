# 두 스킬 편입과 실사용 검토

## Goal

- `codex-project-director`와 `ui-design-rigor`를 정본 경계를 보존한 채 Project Legibility에 편입하고, 실제 사용에서 호출 적합성과 고유 효용을 검토할 수 있는 가역적 운영 경로를 마련한다.

## Scope

- 두 스킬을 하나의 `0.6.0` 부 릴리스로 공개하고 publisher marketplace와 로컬 설치본을 갱신한다.
- 최종 플러그인 검증 뒤 겹치는 독립 스킬 설치를 정리한다.
- 새 스킬의 편입·실사용 검토·개선·제거 절차를 기여 문서가 소유한다.

## Current Facts

- `codex-project-director` 정본은 `7392d079b66bfe76d95336ba567ed460f8cdfc4e`다. 사용자가 명시한 여러 Codex 작업의 디렉터 역할만 맡으며 단일 작업·상태 요약·일반적인 하위 작업 사용에서는 선택하지 않는다.
- `ui-design-rigor` 정본은 `695c5e4ecd08e12e6d32da41fcf7fe770fc5c8d6`이다. 기존 화면의 검토·구조 보존형 개선과 방향이 정해진 구성 요소·영역 구현을 맡고, 새 화면·페이지 수준 결정·기계적 수정은 맡지 않는다.
- 두 정본은 깨끗한 원격 `main`, 자체 검증과 대표 행동·호출 근거를 갖췄다.
- 새 스킬은 별도 실험 상태 없이 기존 릴리스 관문을 통과한다. 배포 뒤 의미 있는 사례는 관찰 버전, 상황, 예상 선택·효용, 실제 결과, 문제와 현재 처리를 task 기록에 남긴다.
- 첫 중대한 실패, 반복되는 호출 경계 혼동이나 관련 변경 때 검토한다. 정본에서 개선하고, 해결되지 않은 실패·오호출이나 고유 효용 없는 중복은 부 릴리스에서 제거한다.

## Current State

- `0.6.0` 후보는 12개 원본·13개 스킬의 고정 정보, 생성 묶음, 출처 고지, 제품·공개·기여 문서와 선택·비선택 사례를 포함한다.
- 로컬·원격 원본 대조, 오프라인 무결성, 묶음·플러그인·저장소·작업 형태 검증이 통과했다.
- 독립 검토에서 발견한 구성 요소 구현, 일반 하위 작업 비선택, 실사용 증거 버전 연결과 현재 상태 문서 문제를 반영했다.
- 릴리스, publisher 고정값 갱신, marketplace 재설치와 중복 독립 스킬 정리가 남아 있다.

## Next Actions

- 최종 검증 뒤 `0.6.0`을 릴리스하고 publisher marketplace와 로컬 설치 구성을 갱신한다.

## Working Boundary

- `docs/tasks/2026/07-25/two-skill-integration-readiness/`
- `README*.md`, `docs/PRODUCT*.md`, `CONTRIBUTING*.md`
- `plugins/project-legibility/`
- `scripts/validate_bundle.py`
- `tests/catalog/`, `tests/routing/`
