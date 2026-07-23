<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="96" alt="Project Legibility 아이콘">
</p>

# Project Legibility

[English](README.en.md)

**에이전트의 속도에서도 계속 고칠 수 있는 프로젝트.**

Project Legibility는 Codex가 코드를 바꾸는 동안 프로젝트의 구조, 판단 기준과 작업 맥락도 함께 단단하게 만들도록 돕는 스킬 플러그인입니다.

- **코드:** 변경이 쌓여도 주 흐름과 책임이 읽히고 계속 고칠 수 있게 합니다.
- **판단:** 현재 동작이 사용자 목적과 설계 기준을 따르도록, 의미를 결정하는 책임을 분명히 합니다.
- **맥락:** 결정 이유와 검증 상태, 다음 행동이 세션과 에이전트를 넘어 이어지게 합니다.

## 설치

```bash
codex plugin marketplace add perhapsspy/codex-plugins
codex plugin add project-legibility@perhapsspy
```

설치한 뒤 새 작업을 시작하세요. Codex는 요청에서 드러난 문제에 맞는 스킬을 선택합니다.

## 평소 하던 일을 요청하세요

### 기능 변경

```text
이 기능을 구현하고 기존 동작이 보존되는지 검증해줘.
```

### 버그 수정

```text
이 버그가 왜 생기는지 확인하고 고쳐줘.
```

### 리팩터링

```text
이 코드를 더 읽고 고치기 쉬운 구조로 정리해줘.
```

### 중단된 작업 재개

```text
이 저장소에서 진행 중인 작업을 찾아서 이어서 해줘.
```

기능 구현, 버그 수정, 리팩터링, 설계, UI, 문서 정리와 장기 작업을 평소처럼 요청하세요. Project Legibility는 각 작업에 필요한 코드 구조, 판단 기준과 작업 맥락을 연결합니다.

## 긴 작업을 시작할 때

여러 세션이나 에이전트가 계속 이어갈 저장소라면 `AGENTS.md`에 다음 한 줄을 두세요.

```md
- 여러 세션이나 에이전트가 참여하는 작업에는 `project-legibility:project-context`를 사용해 현재 목표, 결정, 검증 상태와 다음 행동을 저장소에 유지한다.
```

이 설정 뒤에는 평소처럼 작업을 요청하면 됩니다. `project-context`가 현재 목표와 판단 근거, 검증 상태와 다음 행동을 저장소 안에서 이어갑니다.

## 포함된 스킬

두 핵심 작업 방식을 중심으로, 초기 방향 점검과 구체적인 설계·구현 문제를 맡는 스킬, 별도의 운영·도입 보조를 제공합니다. 역할과 선택 방식은 [스킬 구성 원칙](docs/PRODUCT.md), 자세한 사용법은 각 원본 저장소에서 확인할 수 있습니다.

### 핵심 작업 방식

- [`structure-first`](https://github.com/perhapsspy/structure-first): 흐름·상태·책임·조합이나 경계 계약이 달라지는 코드 변경을 읽고 검증하기 쉽게 유지합니다.
- [`project-context`](https://github.com/perhapsspy/project-context): 장기 작업의 목표와 판단, 현재 상태와 다음 행동을 저장소에 남겨 세션과 에이전트 사이에서 이어갑니다.

### 초기 방향 점검

- [`purpose-fit-design`](https://github.com/perhapsspy/purpose-fit-design): 초기 설계나 구현 방향의 적합성이 중요한 선택으로 남아 있을 때 목적·제약·근거와 성공 조건을 확인합니다.

### 문제별 전문 스킬

- [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit): 현재 무엇을 따라야 하는지, 무엇이 다른지, 어떤 결정이 남았는지를 실제 근거에서 읽기 전용으로 확인합니다.
- [`semantic-boundary-design`](https://github.com/perhapsspy/semantic-boundary-design): 하나의 의미가 여러 표현과 계층에서 일관되도록 그 의미의 소유자와 변환 경계를 세웁니다.
- [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow): 복잡한 상호작용에서도 빠르게 반응하고 최신 사용자 의도가 화면 상태를 이끄는 흐름을 만듭니다.
- [`design-user-interfaces`](https://github.com/perhapsspy/design-user-interfaces): 새 화면과 큰 재설계에서 실제 콘텐츠, 사용자 과업, 필요한 상태와 반응형 동작을 갖춘 완전하고 검증된 인터페이스를 만듭니다.
- [`tighten-docs`](https://github.com/perhapsspy/tighten-docs): 선택한 문서와 문서 묶음의 역할, 지금 따라야 할 내용과 독자가 이동할 경로를 분명하게 정리합니다.
- [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor): `AGENTS.md` 같은 항상 읽는 지침을 작고 오래 유효하며 행동 가능한 시작 규칙으로 유지합니다.

### 필요할 때 쓰는 운영·도입 보조

- [`codex-token-discipline`](https://github.com/perhapsspy/codex-token-discipline): 긴 세션과 큰 출력, 반복 작업으로 token budget이 빠르게 소모될 때 읽기와 출력을 줄이고 이어갈 상태를 압축합니다.
- [`project-context-migration`](https://github.com/perhapsspy/project-context): 작업 맥락이 흩어진 기존 저장소를 검토해 필요한 자료만 `project-context` 구조에 정착시킵니다.

## 업데이트와 제거

```bash
# 업데이트
codex plugin marketplace upgrade perhapsspy
codex plugin add project-legibility@perhapsspy

# 플러그인 제거
codex plugin remove project-legibility@perhapsspy
```

마켓플레이스 등록까지 지우려면 설치된 perhapsspy 플러그인을 모두 제거한 뒤 `codex plugin marketplace remove perhapsspy`를 실행하세요.

## 개발

각 스킬은 위 목록에 연결된 저장소에서 따로 관리합니다. 이 저장소는 함께 배포할 커밋만 고정합니다.

- [변경 내역](CHANGELOG.md)
- [제품 계약](docs/PRODUCT.md)
- [플러그인 구성과 검증](docs/ARCHITECTURE.md)
- [스킬 갱신과 릴리스](CONTRIBUTING.md)
- [현재 포함된 커밋](plugins/project-legibility/sources.lock.json)
- [perhapsspy 플러그인 카탈로그](https://github.com/perhapsspy/codex-plugins)

## 라이선스

[MIT](LICENSE)
