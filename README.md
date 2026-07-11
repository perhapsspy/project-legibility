<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="96" alt="Project Legibility 아이콘">
</p>

# Project Legibility

[English](README.en.md)

Project Legibility는 Codex로 저장소 작업을 여러 세션에 걸쳐 이어갈 때 쓰는 스킬 묶음입니다.

`project-context`는 중단한 곳부터 다시 시작할 수 있게 현재 상태를 기록하고, `structure-first`는 코드 변경의 주 흐름과 검증 기준을 잡습니다. 그 밖의 스킬은 포팅 기준이 모호할 때, UI와 API의 ID·상태·권한이 어긋날 때, 늦게 도착한 검색 결과가 현재 화면을 덮을 때, 문서와 `AGENTS.md`가 낡았을 때 사용합니다.

## 설치

```bash
codex plugin marketplace add perhapsspy/codex-plugins
codex plugin add project-legibility@perhapsspy
```

설치한 뒤 새 작업을 시작하면 적용됩니다. 평소처럼 요청하면 Codex가 필요한 스킬을 고릅니다.

```text
이 저장소의 최근 작업 기록을 읽고 구현을 이어서 해줘.

원본 저장소와 비교해서 이 포팅이 어긋난 곳을 찾아줘.

이번 변경을 검증하고 다음 작업에서 여기부터 이어갈 수 있게 기록해줘.
```

특정 스킬을 직접 지정할 수도 있습니다.

```text
$source-owner-audit 현재 기준 구현과 이 코드의 차이를 확인해줘.
```

## 포함된 스킬

| 스킬 | 쓰는 경우 |
|---|---|
| [`project-context`](https://github.com/perhapsspy/project-context) | 작업이 여러 세션이나 에이전트에 걸칠 때 |
| [`project-context-migration`](https://github.com/perhapsspy/project-context) | 기존 메모와 작업 문서를 `project-context` 구조로 옮길 때 |
| [`structure-first`](https://github.com/perhapsspy/structure-first) | 기능·수정·리팩터링의 주 흐름을 정하고 검증할 때 |
| [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit) | 포팅·마이그레이션에서 따라야 할 기준을 확인할 때 |
| [`purpose-fit-design`](https://github.com/perhapsspy/purpose-fit-design) | 제안한 설계가 사용자 요구와 제약에 맞는지 코딩 전에 확인할 때 |
| [`semantic-boundary-design`](https://github.com/perhapsspy/semantic-boundary-design) | ID·상태·권한의 뜻이 UI·API·저장소에서 어긋날 때 |
| [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow) | 입력·검색·스트리밍 결과가 뒤늦게 도착해 최신 상태를 덮을 때 |
| [`tighten-docs`](https://github.com/perhapsspy/tighten-docs) | 문서가 중복되거나 낡았고 어디서 읽기 시작할지 불분명할 때 |
| [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor) | `AGENTS.md` 같은 상시 지침이 길어지거나 중복될 때 |
| [`codex-token-discipline`](https://github.com/perhapsspy/codex-token-discipline) | 긴 작업이 파일·로그·도구 출력에 파묻힐 때 |

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
