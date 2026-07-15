<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="96" alt="Project Legibility 아이콘">
</p>

# Project Legibility

[English](README.en.md)

**다음 작업까지 맥락과 기준이 이어지는 AI 코딩.**

Project Legibility는 Codex가 긴 저장소 작업의 맥락과 기준을 유지하고, 사람이 이해하고 검토하고 이어갈 수 있는 변경을 남기도록 돕는 스킬 플러그인입니다.

- 중단된 작업의 맥락을 찾아 이어갑니다.
- 코드 변경이 따라야 할 현재 동작과 기준 구현을 확인합니다.
- 다음 변경을 쉽게 이어갈 수 있는 구조와 검증 근거를 남깁니다.

문제마다 범위가 분명한 스킬이 필요한 순간에 작업을 안내합니다.

## 설치

```bash
codex plugin marketplace add perhapsspy/codex-plugins
codex plugin add project-legibility@perhapsspy
```

설치한 뒤 새 작업을 시작하세요. 평소처럼 요청하면 목적이 맞는 스킬이 선택되며, 특정 스킬을 직접 지정할 수도 있습니다.

## 먼저 이렇게 써보세요

### 멈춘 곳에서 이어가기

```text
이 저장소에서 마지막으로 멈춘 곳을 확인하고 안전하게 이어서 해줘.
```

### 현재 기준 확인하기

```text
코드를 바꾸기 전에 이번 변경이 따라야 할 기존 동작과 제약을 확인해줘.
```

### 다음 작업이 이어받을 수 있게 남기기

```text
다음 작업에서도 이해하고 이어갈 수 있게 구현하고 검증해줘.
```

명시적으로 작업 방식을 고르고 싶다면 스킬 이름을 함께 요청하세요.

```text
$source-owner-audit 현재 기준 구현과 이 코드의 차이를 확인해줘.

$design-user-interfaces 새 권한 관리 화면을 상태와 모바일까지 포함해 설계하고 구현해줘.
```

## 구성

Project Legibility는 지침과 그에 필요한 reference·script로 구성된 skills-only 플러그인입니다.

- 각 스킬은 적용할 문제와 작업 범위를 명확히 설명합니다.
- 각 스킬의 원본 저장소와 배포에 포함된 고정 commit을 공개합니다.
- [MIT 라이선스](LICENSE)로 배포합니다.

## 포함된 스킬

각 스킬의 자세한 목적, 사용 시점과 예시는 연결된 원본 저장소에서 확인할 수 있습니다.

- [`project-context`, `project-context-migration`](https://github.com/perhapsspy/project-context)
- [`structure-first`](https://github.com/perhapsspy/structure-first)
- [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit)
- [`purpose-fit-design`](https://github.com/perhapsspy/purpose-fit-design)
- [`semantic-boundary-design`](https://github.com/perhapsspy/semantic-boundary-design)
- [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow)
- [`tighten-docs`](https://github.com/perhapsspy/tighten-docs)
- [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor)
- [`codex-token-discipline`](https://github.com/perhapsspy/codex-token-discipline)
- [`design-user-interfaces`](https://github.com/perhapsspy/design-user-interfaces)

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
- [플러그인 구성과 검증](docs/ARCHITECTURE.md)
- [스킬 갱신과 릴리스](CONTRIBUTING.md)
- [현재 포함된 커밋](plugins/project-legibility/sources.lock.json)
- [perhapsspy 플러그인 카탈로그](https://github.com/perhapsspy/codex-plugins)

## 라이선스

[MIT](LICENSE)
