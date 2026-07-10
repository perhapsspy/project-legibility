# Project Legibility에 기여하기

[English](CONTRIBUTING.en.md)

이 문서는 canonical 스킬 변경을 plugin release로 가져오는 절차를 소유합니다. 구성과 source ownership의 이유는 [Architecture](docs/ARCHITECTURE.md), 사용법과 제품 범위는 [README](README.md)를 따릅니다.

## 먼저 변경 owner를 찾기

`plugins/project-legibility/skills/`는 생성된 배포 snapshot이고 `plugins/project-legibility/THIRD_PARTY_NOTICES.md`는 생성된 provenance입니다. 두 경로를 직접 수정하지 마세요.

- 스킬의 내용, trigger, reference, 자체 test는 표준 GitHub 저장소에서 변경합니다.
- 이 저장소에서는 `sources.lock.json`, 생성 snapshot, plugin manifest, release 문서와 조립·검증 도구만 변경합니다.
- 하나의 변경을 canonical 저장소와 생성 snapshot에서 따로 수동 구현하지 않습니다.

Canonical 저장소 목록은 [README의 포함 스킬 표](README.md#포함-스킬)에 있습니다.

## 개발 환경

로컬 sync에는 Python 3, Git과 `~/Projects/<repo>`처럼 하나의 공통 상위 경로에 checkout한 canonical 저장소가 필요합니다. `--projects-root`로 그 상위 경로를 지정할 수 있습니다.

현재 checkout들의 HEAD를 full SHA로 lock하고 snapshot을 다시 만들려면 다음 명령을 사용합니다.

```bash
python3 scripts/sync_skills.py update --projects-root ~/Projects
```

`update`는 각 canonical checkout이 clean `main`이고 HEAD가 remote `main`에 push된 경우에만 진행됩니다.

고정된 version을 바꾸지 않고 기존 lock에서 snapshot과 third-party notice만 다시 만들려면 다음 명령을 사용합니다. `--projects-root ~/Projects`를 덧붙이면 remote 대신 local checkout의 locked commit을 사용합니다.

```bash
python3 scripts/sync_skills.py sync
```

로컬 canonical checkout과 lock, 생성 snapshot이 모두 일치하는지 검사합니다.

```bash
python3 scripts/sync_skills.py check --projects-root ~/Projects
```

remote source를 확인할 수 있는 CI에서는 다음을 사용합니다.

```bash
python3 scripts/sync_skills.py check
```

네트워크나 canonical checkout 없이 committed lock과 snapshot의 자체 무결성만 빠르게 검사하려면 다음을 사용합니다.

```bash
python3 scripts/sync_skills.py check --offline
```

`--offline`은 `--projects-root`와 함께 사용할 수 없으며, canonical source와의 동일성을 증명하는 release gate를 대신하지 않습니다.

조립된 plugin contract와 repository test도 함께 실행합니다.

```bash
python3 scripts/validate_bundle.py
python3 -m unittest discover -s tests -v
```

## 스킬 변경을 반영하는 순서

1. 변경할 스킬의 canonical 저장소에서 내용과 trigger, reference, 자체 test를 수정합니다.
2. 그 저장소의 validation을 통과시키고 변경을 commit·push합니다. plugin lock에는 아직 push하지 않은 commit을 넣지 않습니다.
3. 이 저장소에서 `sync_skills.py update`를 실행해 full SHA, skill integrity와 snapshot을 함께 갱신합니다.
4. 생성 diff에 의도한 canonical 변경만 있는지 검토합니다. 예상하지 않은 파일이나 다른 스킬 변경이 섞였으면 중단합니다.
5. 로컬 source check, offline check, bundle validation과 repository test를 모두 실행합니다.
6. 아래 version 규칙에 따라 plugin manifest의 SemVer와 [CHANGELOG](CHANGELOG.md)를 갱신합니다.
7. test와 plugin validation을 포함한 전체 CI를 통과시킵니다.
8. review와 merge 뒤 동일 commit에 `v<version>` tag를 만들고 push합니다.

한 canonical 저장소가 여러 스킬을 제공할 수 있습니다. 현재 `project-context`와 `project-context-migration`은 같은 repository SHA를 함께 사용하므로 둘 중 하나를 갱신할 때 두 snapshot의 diff를 모두 확인합니다.

## Version 규칙

### Patch (`0.1.x`)

다음처럼 기존 제품 약속과 설치 구성을 호환되게 유지하는 변경입니다.

- 포함 스킬의 bug fix, 문안 개선 또는 reference 보강
- trigger 의미를 바꾸지 않는 좁은 교정
- 조립·검증 도구의 호환 가능한 수정
- 공개 문서의 사실 또는 사용 절차 교정

### Minor (`0.x.0`)

사용자가 선택하거나 경험하는 plugin 구성이 의미 있게 달라지는 변경입니다.

- 스킬 추가 또는 제거
- core 역할이나 스킬 책임 경계의 변경
- trigger 동작의 의미 있는 확대·축소
- starter prompt나 제품 수준의 요청 흐름 변경
- lock, snapshot 또는 marketplace 구조의 호환 가능한 확장

설치 식별자나 source contract를 깨는 변경은 major 후보입니다. major release가 필요하면 먼저 architecture와 migration 경로를 명시합니다.

## Release gate

Release commit은 다음 조건을 모두 만족해야 합니다.

- manifest와 marketplace metadata의 plugin 이름·경로가 일치하고, manifest version은 CHANGELOG·Git tag와 일치합니다.
- 10개 skill validator와 plugin validator가 통과합니다.
- full SHA lock이 canonical Git source와 일치합니다.
- 생성 snapshot이 lock의 source tree와 byte-for-byte 일치합니다.
- snapshot 내부 상대 링크와 companion 관계가 유효합니다.
- `work-board`, `structure-first-docs`, `justified-change` 같은 폐기 스킬이 catalog, lock과 snapshot에 없습니다.
- sync test와 catalog trigger/non-trigger 회귀 test가 통과합니다.
- install → 새 task → update → remove round trip이 통과합니다.
- release commit과 Git tag가 같은 검증 결과를 가리킵니다.

## Rollback

배포 후 문제가 생기면 문제가 있는 version을 덮어쓰거나 기존 tag를 이동하지 않습니다.

1. 마지막으로 검증된 tag를 확인합니다. 최초 기준점은 `v0.1.0`입니다.
2. 사용자에게 [README의 rollback 명령](README.md#업데이트-제거-rollback)을 안내합니다.
3. canonical source 또는 assembly 문제를 원래 owner에서 수정합니다.
4. patch 또는 minor version으로 새 release를 냅니다.

Tag는 immutable release 기준점입니다. 같은 version의 snapshot이나 manifest를 바꾸지 않습니다.
