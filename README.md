<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="128" alt="Project Legibility 아이콘">
</p>

# Project Legibility

**의도·구조·맥락을 잃지 않고 프로젝트를 설계하고 구현·검증하며 이어가는 Codex 플러그인.**

[English](README.en.md)

Project Legibility는 코드 가독성 도구나 문서 스킬 모음이 아닙니다. Codex가 프로젝트의 목적과 현재 근거를 파악하고, 변경의 의미와 구현 구조를 지키고, 검증된 상태를 다음 작업으로 넘길 수 있게 하는 **skills-only plugin**입니다.

9개의 독립 저장소에서 유지되는 10개 스킬을 한 번에 설치합니다. `project-context`가 장기 작업의 연속성을, `structure-first`가 구현의 읽히는 구조를 맡는 두 core이고, 나머지 스킬은 source ownership, 설계 적합성, 의미 경계, 상호작용 상태, 문서와 저장소 지침처럼 실제 위험이 있을 때만 개입합니다. 모든 작업을 하나의 고정 pipeline으로 만들지 않습니다.

## 이런 작업에 맞습니다

- 여러 task나 agent에 걸친 기능 작업을 현재 근거에서 재개하고, 다음 변경을 검증한 뒤 다시 인계해야 할 때
- port, migration, integration 또는 refactor에서 따라야 할 source와 여러 계층을 지나는 의미의 owner를 확인해야 할 때
- async interaction, 문서 패키지 또는 `AGENTS.md`가 구현과 어긋나지 않도록 필요한 전문 점검만 적용해야 할 때

## 설치하고 시작하기

[Codex plugin 명령](https://learn.chatgpt.com/docs/build-plugins)을 사용할 수 있는 환경에서 marketplace와 plugin을 등록합니다.

```bash
codex plugin marketplace add perhapsspy/project-legibility
codex plugin add project-legibility@project-legibility
```

설치한 스킬이 확실히 로드되도록 **새 task**를 시작한 뒤, 다음과 같이 요청할 수 있습니다.

```text
Resume this project and implement the next verified change.
```

```text
Review this repository for context, structure, meaning, and documentation drift.
```

```text
Leave this project verified and easy for the next agent to resume.
```

각 prompt는 각각 “현재 상태에서 다음 검증 가능한 변경 구현”, “맥락·구조·의미·문서 drift 점검”, “다음 agent가 재개할 수 있는 검증 상태로 인계”를 요청합니다. 필요한 전문 스킬은 작업 내용과 각 스킬의 trigger에 따라 선택됩니다.

## 포함 스킬

| 구분 | 스킬과 canonical source | 맡는 일 |
|---|---|---|
| **Core · Continuity** | [`project-context`](https://github.com/perhapsspy/project-context) | task brief, log, reference note로 장기 작업을 재개·인계할 수 있는 현재 상태를 남깁니다. |
| **Core · Implementation** | [`structure-first`](https://github.com/perhapsspy/structure-first) | 읽히는 primary flow, 필요한 만큼의 boundary, 계약 중심 검증으로 기능·수정·리팩터링을 구조화합니다. |
| Grounding | [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit) | 현재 따라야 할 코드, API, config, 문서 또는 동작을 읽기 전용 근거로 확인하고 차이와 미결정을 보고합니다. |
| Direction | [`purpose-fit-design`](https://github.com/perhapsspy/purpose-fit-design) | 구현 전에 방향이 사용자·도메인 목적, 제약, 현재 근거와 검증 가능한 성공 조건에 맞는지 점검합니다. |
| Semantics | [`semantic-boundary-design`](https://github.com/perhapsspy/semantic-boundary-design) | UI부터 storage까지 여러 표현을 지나는 사용자·도메인 의미의 결정 owner를 하나로 정리합니다. |
| Interaction | [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow) | 입력·선택·검색·streaming·realtime 흐름에서 intent, async 작업, freshness와 stale result의 소유권을 분리합니다. |
| Documentation | [`tighten-docs`](https://github.com/perhapsspy/tighten-docs) | 선택된 문서 범위의 최종 문안, 문서별 역할, reader route와 current/stale 구분을 정리합니다. |
| Project Guidance | [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor) | `AGENTS.md`류 always-read 지침을 작고 지속 가능하며 행동 중심인 계약으로 유지합니다. |
| Long-run Operations | [`codex-token-discipline`](https://github.com/perhapsspy/codex-token-discipline) | 긴 작업의 broad read, 출력, subagent, UI loop와 resume state를 통제해 유효한 맥락을 보존합니다. |
| Adoption Companion | [`project-context-migration`](https://github.com/perhapsspy/project-context) | 기존 저장소에 흩어진 작업 문서를 분류하고 필요한 맥락만 `project-context` 구조로 이관합니다. |

`project-context-migration`은 `project-context`와 같은 canonical 저장소에서 배포됩니다. 기존 프로젝트의 도입 작업에만 쓰는 companion이며 신규 프로젝트의 기본 단계는 아닙니다.

## v0.1의 범위

v0.1은 **10개 스킬만 포함**합니다.

- MCP server나 app이 없으므로 추가 서비스에 연결하지 않습니다.
- hook이나 lifecycle automation이 없으므로 plugin 자체가 background 작업을 시작하거나 프로젝트 파일을 자동 생성하지 않습니다.
- 새 umbrella skill이 없습니다. 제품 수준의 요청을 중복 router로 다시 해석하지 않고, 각 전문 스킬의 책임과 trigger를 그대로 사용합니다.
- 포함된 스킬은 사용자가 요청한 작업 안에서 Codex의 project file 읽기·쓰기를 안내합니다. plugin 자체의 별도 실행 서비스는 없습니다.

## 업데이트, 제거, rollback

최신 marketplace snapshot으로 갱신한 뒤 plugin을 다시 설치합니다. 갱신된 스킬은 새 task에서 사용합니다.

```bash
codex plugin marketplace upgrade project-legibility
codex plugin add project-legibility@project-legibility
```

plugin만 제거하려면 다음 명령을 사용합니다.

```bash
codex plugin remove project-legibility@project-legibility
```

marketplace 등록도 더 이상 필요 없다면 plugin을 제거한 뒤 함께 지웁니다.

```bash
codex plugin marketplace remove project-legibility
```

v0.1.0으로 rollback하려면 현재 설치와 marketplace를 제거하고 해당 tag를 고정해 다시 등록합니다.

```bash
codex plugin remove project-legibility@project-legibility
codex plugin marketplace remove project-legibility
codex plugin marketplace add perhapsspy/project-legibility --ref v0.1.0
codex plugin add project-legibility@project-legibility
```

## Source 모델

각 개별 스킬 저장소가 스킬 내용과 trigger의 canonical source이며 독립 설치·release 경로를 유지합니다. 이 저장소는 어떤 버전을 한 plugin으로 배포할지만 소유합니다.

- [`sources.lock.json`](plugins/project-legibility/sources.lock.json)은 canonical repository, skill path, 전체 commit SHA와 snapshot integrity digest를 고정합니다.
- [`plugins/project-legibility/skills/`](plugins/project-legibility/skills/)는 lock에 따라 생성한 배포 snapshot입니다.
- [`THIRD_PARTY_NOTICES.md`](plugins/project-legibility/THIRD_PARTY_NOTICES.md)는 포함 source, commit과 license를 사람이 읽을 수 있게 보여주는 생성 provenance입니다.
- 생성된 `skills/`는 직접 편집하지 않습니다. 변경은 canonical 저장소에서 먼저 검증·push한 뒤 sync합니다.
- lock과 snapshot의 차이는 release gate에서 실패해야 합니다.

구성과 무결성 원칙은 [Architecture](docs/ARCHITECTURE.md), 변경·release 절차는 [Contributing](CONTRIBUTING.md), 버전별 변경은 [Changelog](CHANGELOG.md)에서 확인할 수 있습니다.

## License

Project Legibility는 [MIT License](LICENSE)로 배포됩니다.
