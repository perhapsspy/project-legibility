<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="96" alt="Project Legibility 아이콘">
</p>

# Project Legibility

[English](README.en.md)

Project Legibility는 긴 저장소 작업에서도 맥락과 기준을 잃지 않고, 다음에 이어서 작업하기 쉬운 변경을 남기도록 돕습니다.

중단된 작업을 이어받고, 무엇을 따라야 할지 확인하고, 복잡한 코드와 문서를 읽기 좋은 상태로 정리하는 일을 각 문제에 맞는 스킬이 맡습니다.

## 설치

```bash
codex plugin marketplace add perhapsspy/codex-plugins
codex plugin add project-legibility@perhapsspy
```

설치한 뒤 새 작업을 시작하면 적용됩니다. 평소처럼 요청하면 필요한 스킬이 자동으로 선택됩니다.

```text
이 저장소에서 마지막으로 멈춘 곳을 확인하고 안전하게 이어서 해줘.

코드를 바꾸기 전에 이번 변경이 따라야 할 기존 동작과 제약을 확인해줘.

다음 작업에서도 이해하고 이어갈 수 있게 구현하고 검증해줘.
```

특정 스킬을 직접 지정할 수도 있습니다.

```text
$source-owner-audit 현재 기준 구현과 이 코드의 차이를 확인해줘.
```

## 포함된 스킬

각 스킬의 자세한 목적, 사용 시점과 예시는 연결된 canonical 저장소에서 확인할 수 있습니다.

- [`project-context`, `project-context-migration`](https://github.com/perhapsspy/project-context)
- [`structure-first`](https://github.com/perhapsspy/structure-first)
- [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit)
- [`purpose-fit-design`](https://github.com/perhapsspy/purpose-fit-design)
- [`semantic-boundary-design`](https://github.com/perhapsspy/semantic-boundary-design)
- [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow)
- [`tighten-docs`](https://github.com/perhapsspy/tighten-docs)
- [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor)
- [`codex-token-discipline`](https://github.com/perhapsspy/codex-token-discipline)

이 플러그인은 스킬 지침만 설치합니다. 외부 서비스에 연결하거나 백그라운드 작업을 실행하지 않습니다.

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

각 스킬은 위 표에 연결된 저장소에서 따로 관리합니다. 이 저장소는 함께 배포할 커밋만 고정합니다.

- [플러그인 구성과 검증](docs/ARCHITECTURE.md)
- [스킬 갱신과 릴리스](CONTRIBUTING.md)
- [현재 포함된 커밋](plugins/project-legibility/sources.lock.json)
- [perhapsspy 플러그인 카탈로그](https://github.com/perhapsspy/codex-plugins)

## 라이선스

[MIT](LICENSE)
