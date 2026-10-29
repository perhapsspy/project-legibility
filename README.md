<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="96" alt="Project Legibility 아이콘">
</p>

# Project Legibility

[English](README.en.md)

**에이전트의 속도에서도 계속 고칠 수 있는 프로젝트.**

Project Legibility는 Codex와 Claude Code가 코드를 바꾸는 동안 프로젝트의 구조, 판단 기준과 작업 맥락도 함께 단단하게 만들도록 돕는 스킬 플러그인입니다.

- **코드:** 변경이 쌓여도 주 흐름과 책임이 읽히고 계속 고칠 수 있게 합니다.
- **판단:** 현재 동작이 사용자 목적과 설계 기준을 따르도록, 의미를 결정하는 책임을 분명히 합니다.
- **맥락:** 결정 이유와 검증 상태, 다음 행동이 세션과 에이전트를 넘어 이어지게 합니다.

## 설치

### Codex

```bash
codex plugin marketplace add perhapsspy/codex-plugins
codex plugin add project-legibility@perhapsspy
```

설치한 뒤 새 작업을 시작하세요. Codex는 요청에서 드러난 문제에 맞는 스킬을 선택합니다.

### Claude Code

```bash
claude plugin marketplace add perhapsspy/codex-plugins
claude plugin install project-legibility@perhapsspy
```

양쪽 클라이언트는 같은 10개 스킬을 사용합니다. Claude Code에서는 `/project-legibility:project-context`처럼 명시 호출할 수 있습니다. 로컬 개발 중 저장한 변경은 `/reload-plugins`로 다시 읽습니다.

설치 확인은 `claude plugin details project-legibility`로 합니다. 로컬 개발에서는 이 저장소 루트에서 `claude --plugin-dir ./plugins/project-legibility`로 패키지를 로드합니다.

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

Claude Code가 기존 `CLAUDE.md`를 읽고 있다면 그 파일에서 `@AGENTS.md`로 공통 지침을 가져옵니다. 지원되는 최신 버전에서는 `AGENTS.md`를 직접 읽을 수도 있으며 `/memory`에서 로딩 여부를 확인합니다.

이 설정 뒤에는 평소처럼 작업을 요청하면 됩니다. `project-context`가 현재 목표와 판단 근거, 검증 상태와 다음 행동을 저장소 안에서 이어갑니다.

## 포함된 스킬

두 핵심 작업 방식을 중심으로, 목적 우선 방향 결정과 구체적인 프로젝트 문제를 맡는 스킬, 별도의 운영·도입 보조를 제공합니다. 역할과 선택 방식은 [스킬 구성 원칙](docs/PRODUCT.md), 자세한 사용법은 각 원본 저장소에서 확인할 수 있습니다.

### 핵심 작업 방식

- [`structure-first`](https://github.com/perhapsspy/structure-first): 흐름·상태·책임·조합이나 경계 계약이 달라지는 코드 변경을 읽고 검증하기 쉽게 유지하며, 여러 표현에 걸친 확정 의미의 해석과 번역 경계도 한 owner에 둡니다.
- [`project-context`](https://github.com/perhapsspy/project-context): 장기 작업의 목표와 판단, 현재 상태와 다음 행동을 저장소에 남겨 세션과 에이전트 사이에서 이어갑니다.

### 목적 우선 방향 결정

- [`purpose-first-design`](https://github.com/perhapsspy/purpose-first-design): 제품 의미나 구현 계획의 방향이 실질적으로 열려 있을 때 새 기능·재사용 선택·임시 구현 등 중대한 선택의 초기 방향을 목적과 확정된 경계에서 정하고, 답변이 만든 불필요한 범위와 약속을 줄입니다.

### 결과 수용성 검토

- [`critical-review`](https://github.com/perhapsspy/critical-review): 코드·기획·설계와 관련 산출물의 검토를 요청받았을 때 목적 충족·충분함·과함을 근거와 반례로 판단하고, 지적 자체도 반증합니다.

Codex에서는 `$project-legibility:critical-review 이 코드가 원래 요구를 충족하는지 검토해줘`처럼 명시 호출할 수 있습니다.

### 문제별 전문 스킬

- [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit): 현재 무엇을 따라야 하는지, 무엇이 다른지, 어떤 결정이 남았는지를 실제 근거에서 읽기 전용으로 확인합니다.
- [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow): 복잡한 상호작용에서도 빠르게 반응하고 최신 사용자 의도가 화면 상태를 이끄는 흐름을 만듭니다.
- [`tighten-docs`](https://github.com/perhapsspy/tighten-docs): 의미가 정해진 사람이 작성하는 문서에 초안부터 최종 리뷰까지 참여해 현재 안내와 독자 경로를 분명히 하고, 폐기된 판단의 흔적을 제거합니다.
- [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor): `AGENTS.md` 같은 항상 읽는 지침을 작고 오래 유효하며 행동 가능한 시작 규칙으로 유지합니다.

### 필요할 때 쓰는 운영·도입 보조

- [`agent-cost-efficiency`](https://github.com/perhapsspy/agent-cost-efficiency): 필요한 검증과 결과 품질을 유지하며 읽기·출력·실행·관측·위임의 불필요한 비용을 줄입니다.
- [`project-context-migration`](https://github.com/perhapsspy/project-context): 작업 맥락이 흩어진 기존 저장소를 검토해 필요한 자료만 `project-context` 구조에 정착시킵니다.

## 업데이트와 제거

설치된 플러그인의 업데이트는 Codex 앱이 관리합니다. 게시된 새 버전은 앱의 plugin update lifecycle을 통해 반영되며, 반영 뒤 새 작업에서 갱신된 스킬을 사용합니다.

```bash
# 플러그인 제거
codex plugin remove project-legibility@perhapsspy
```

마켓플레이스 등록까지 지우려면 설치된 perhapsspy 플러그인을 모두 제거한 뒤 `codex plugin marketplace remove perhapsspy`를 실행하세요.

## 개발

각 스킬은 위 목록에 연결된 저장소에서 관리하며 이 저장소는 함께 배포할 커밋을 고정합니다. 제품 구성은 [PRODUCT](docs/PRODUCT.md), 조립 구조는 [Architecture](docs/ARCHITECTURE.md), 공개 변경 이력은 [CHANGELOG](CHANGELOG.md)에서 확인할 수 있습니다.

공통 플러그인 메타데이터는 `plugins/project-legibility/plugin.json`에서 고친 뒤 `python3 scripts/sync_plugin_metadata.py write`로 반영합니다. `.codex-plugin/plugin.json`과 `.claude-plugin/plugin.json`은 생성 파일입니다. `python3 scripts/validate_bundle.py`가 양쪽의 공통 식별자·버전·스킬 경로를 확인합니다.

Codex에서 공개 게시 전에 생성 bundle을 설치하려면 저장소 루트에서 다음 명령을 사용합니다.

```bash
codex plugin marketplace add .
codex plugin add project-legibility@project-legibility-local
```

이 로컬 marketplace는 `plugins/project-legibility`를 source로 사용합니다. 공개 설치본도 있다면 Codex의 플러그인 설정에서 `project-legibility@perhapsspy`를 비활성화하고 로컬 설치본만 활성화해 중복을 피합니다. 공개 설치로 돌아갈 때는 두 설치본의 활성화를 반대로 전환합니다. 공개 source pin과 release는 별도로 유지됩니다.

## 라이선스

[MIT](LICENSE)
