# Project Legibility Architecture

[English](ARCHITECTURE.en.md)

이 문서는 Project Legibility의 source ownership, plugin assembly, lock 무결성과 release gate를 소유합니다. 제품의 사용법과 포함 스킬은 [README](../README.md), 실제 변경·release 순서는 [CONTRIBUTING](../CONTRIBUTING.md)을 따릅니다.

## 설계 목표

Project Legibility는 9개의 독립 canonical 저장소를 유지하면서 10개 스킬을 하나의 재현 가능한 Codex plugin으로 배포합니다.

- 스킬 author는 기존 저장소에서 독립적으로 개발·검증·release할 수 있어야 합니다.
- plugin 설치 결과는 network나 개발 checkout 상태에 의존하지 않아야 합니다.
- plugin release가 어떤 canonical commit을 포함하는지 full SHA로 감사할 수 있어야 합니다.
- 같은 스킬을 두 저장소에서 수동 유지하는 이중 source of truth가 없어야 합니다.

## Owner boundary

| Owner | 소유하는 것 | 소유하지 않는 것 |
|---|---|---|
| Canonical skill repositories | `SKILL.md`, trigger, reference, skill 전용 script·asset·test와 그 변경 이력 | plugin bundle 구성, marketplace metadata, bundle version |
| [`sources.lock.json`](../plugins/project-legibility/sources.lock.json) | 선택된 repository URL, full commit SHA, source·배포 path와 skill integrity digest | 스킬 내용의 의미, 자동으로 “최신”인 branch |
| [`plugins/project-legibility/skills/`](../plugins/project-legibility/skills/) | 설치 시 바로 사용할 수 있는 생성 snapshot | 직접 authoring되는 canonical 내용 |
| [`THIRD_PARTY_NOTICES.md`](../plugins/project-legibility/THIRD_PARTY_NOTICES.md) | lock에서 생성한 source, commit, bundled skill과 license 요약 | 별도 수동 provenance 기록 |
| [Plugin manifest](../plugins/project-legibility/.codex-plugin/plugin.json) | plugin 식별자, version, 공개 설명, capability와 starter prompt | 개별 skill trigger나 instruction |
| [Marketplace metadata](../.agents/plugins/marketplace.json) | repository 안에서 plugin을 찾는 marketplace entry | 설치된 사용자 상태, plugin runtime 동작 |
| `scripts/sync_skills.py` | lock 생성, source materialization, snapshot 조립과 차이 검증 | 스킬 간 의미 충돌 해결, trigger 재설계, release 승인 |

`project-context` repository는 `project-context`와 `project-context-migration` 두 스킬을 소유합니다. 따라서 10개 스킬은 9개 repository commit으로 고정됩니다.

## Assembly 흐름

```text
canonical repositories
        │  verified full commit SHA + source path
        ▼
  sources.lock.json
        │  scripts/sync_skills.py update
        ▼
plugins/project-legibility/skills/
        │  plugin manifest + marketplace metadata
        ▼
  installable plugin snapshot
```

1. 변경은 canonical repository에서 먼저 검증하고 push합니다.
2. `update`는 각 checkout의 commit과 source path를 lock하고 skill tree를 snapshot으로 복사합니다.
3. `sync`는 lock을 바꾸지 않고 locked local 또는 remote commit에서 snapshot과 third-party notice를 재생성합니다.
4. `check --projects-root`는 local canonical source, lock과 snapshot을 함께 비교합니다.
5. `check`는 임시 checkout으로 locked remote commit을 materialize해 release source와 비교합니다.
6. `check --offline`은 committed lock, snapshot과 notice의 자체 무결성을 빠르게 확인합니다.

Sync는 의미를 merge하지 않습니다. Canonical tree를 그대로 조립하고 차이가 있으면 실패시켜, 사람이 예상한 source와 release 대상이 다른 상태를 숨기지 않습니다.

## Lock과 무결성

Branch 이름이나 짧은 SHA는 release 입력으로 충분하지 않습니다. Branch는 이동하고 짧은 SHA는 전역에서 고유하다는 보장이 없기 때문에 lock은 40자리 commit SHA를 기록합니다.

무결성은 세 관계로 확인합니다.

1. **Repository identity:** lock의 repository URL과 commit이 의도한 canonical Git source에 존재합니다.
2. **Source selection:** lock의 source path가 해당 commit에서 정확한 skill tree를 가리킵니다.
3. **Snapshot equality:** skill별 SHA-256 integrity와 배포 snapshot이 선택된 tree와 byte-for-byte 일치합니다.

Local path나 working tree는 편의를 위한 입력일 뿐 release identity가 아닙니다. Release 재현성의 기준은 remote canonical repository와 full SHA입니다.

## 선택하지 않은 구조

### Git submodule

Submodule은 repository 관계를 보여주지만 marketplace snapshot과 plugin 설치에 추가 init/fetch 상태를 요구합니다. 설치물이 self-contained하지 않고 누락된 submodule이 빈 skill directory로 보일 수 있으므로 v0.1 assembly에는 사용하지 않습니다.

### 설치 시 remote assembly

설치나 runtime에 9개 repository를 fetch하면 network availability, branch 이동, 인증과 source 장애가 사용자 실행 경로에 들어옵니다. Release 시 생성 snapshot을 commit해 설치 결과를 고정하고, remote 검증은 CI와 release gate에서 끝냅니다.

### Umbrella skill

새 umbrella skill은 제품 수준 요청을 다시 route하면서 `project-context`, `structure-first`와 전문 스킬의 기존 trigger 위에 또 하나의 책임 계층을 만듭니다. v0.1은 manifest 설명과 starter prompt만 공통 진입점으로 사용하고, 실제 행동은 기존 스킬이 소유합니다.

## Release gate

Release는 다음 네 종류의 증거가 모두 있을 때만 가능합니다.

1. **Package:** manifest와 marketplace schema가 유효하고 plugin 이름·경로가 일치하며, manifest version은 CHANGELOG·Git tag와 일치합니다.
2. **Source:** full SHA가 remote canonical source에 존재하고 lock, source tree와 snapshot이 일치합니다.
3. **Skill:** 10개 skill validator, 상대 링크, companion 관계와 catalog 회귀가 통과합니다.
4. **Lifecycle:** install, 새 task load, update, remove round trip과 rollback tag가 검증됩니다.

Release tag는 manifest version과 같은 `v<version>` 형식의 immutable 기준점입니다. 실패한 release는 tag를 이동하지 않고 새 patch 또는 minor version으로 고칩니다.
