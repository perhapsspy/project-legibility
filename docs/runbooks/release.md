# Project Legibility 릴리스 런북

이 런북은 canonical 스킬 변경을 Project Legibility release와 publisher catalog까지 가장 짧은 검증 경로로 배포하는 실행 순서, version, release gate와 rollback을 소유합니다.

## 완료 조건

배포는 다음 상태에서 완료됩니다.

- 변경한 canonical commit이 공개 `main`에 존재합니다.
- Project Legibility release commit이 CI를 통과하고 같은 commit에 `v<version>` tag와 GitHub Release가 존재합니다.
- `perhapsspy/codex-plugins`가 그 release commit을 고정하고 catalog CI의 remote manifest 검증을 통과합니다.

## Version 선택

Version은 바뀐 파일 이름이나 diff 크기가 아니라 설치 사용자에게 공개된 호환성 계약으로 선택합니다. [제품 계약](../PRODUCT.md)은 제품 역할과 skill 구성을, 각 canonical skill description은 선택 조건을, plugin manifest는 공개 starter prompt와 source contract를 소유합니다. 특히 description이나 starter prompt를 수정했다는 사실만으로 minor가 되지는 않습니다.

| Version | 사용자 관점의 판정 |
|---|---|
| Patch | 공개된 skill 구성과 선택 계약을 유지합니다. 이미 약속된 선택이 description이나 routing 구현의 결함 때문에 어긋난 경우를 복구하거나, 선택된 skill의 실행 품질, bug, 문안, reference나 guardrail을 호환 가능하게 교정합니다. 조립 도구와 공개 절차의 호환 가능한 수정도 포함합니다. |
| Minor | 공개 선택 계약을 넓히거나 좁힙니다. skill 추가·제거, 제품 역할 관계 변경, canonical trigger가 선택하는 요청 종류의 변경, 명시 호출과 자동 참여 사이의 전환, 새로운 사용자 과업을 여는 starter prompt, lock·snapshot 구조의 호환 가능한 확장을 포함합니다. |
| Major | 기존 plugin source contract나 설치 소비 방식을 깨고 migration이 필요합니다. |

다음 순서로 판정합니다.

1. 변경 대상의 현재 정본에서 제품 역할, 선택 조건, starter prompt나 source contract를 확인합니다.
2. 같은 대표 요청 묶음에 대해 변경 전후 정본이 약속하는 선택 결과를 비교합니다.
3. 정본 계약은 같고 실제 description·routing이나 선택 후 행동만 그 계약에 맞게 복구하면 patch입니다.
4. 정본이 약속하는 결과가 `do-not-select → select` 또는 `select → do-not-select`로 바뀌면 minor입니다.
5. 기존 설치나 source 소비자가 migration 없이 사용할 수 없으면 major입니다.
6. 한 release에 여러 변경이 있으면 가장 높은 version 영향을 적용합니다.

경계 사례는 다음처럼 처리합니다.

- description을 더 정확히 쓰거나 기존 제품·trigger 계약과 어긋난 선택을 복구하되 공개 선택 계약이 같으면 patch입니다.
- starter prompt의 표현만 다듬고 같은 과업으로 연결하면 patch입니다. 새 과업이나 호출 경로를 제공하거나 제거하면 minor입니다.
- canonical trigger가 skill을 최종 문안 정리에만 선택하도록 약속하다가 의미가 정해진 문서의 초안 작성부터 선택하도록 넓히면 minor입니다.
- skill을 자동 선택에서 명시 호출 전용으로 바꾸거나 그 반대로 바꾸면 minor입니다.
- 이미 선택된 skill이 source ownership이나 failure handling을 더 정확히 수행하도록 고치되 trigger를 유지하면 patch입니다.

제품 역할, skill 구성이나 선택되는 요청 집합이 달라지면 [제품 계약](../PRODUCT.md)에 먼저 반영합니다. Manifest, 한영 changelog와 `v<version>` tag는 선택한 version을 함께 가리킵니다.

저장소 루트의 운영 문서만 바뀐 경우 즉시 plugin release는 필요하지 않습니다. 위 분류는 다음 release의 version을 선택할 때 적용합니다.

## 1. 한 번에 사전 점검

시작 전에 다음을 한 번만 결정합니다.

- 변경할 canonical repository와 배포할 skill
- patch, minor 또는 major version
- Project Legibility와 publisher catalog의 현재 `main`
- 각 변경 repository의 기대 GitHub login과 write remote
- CI 관찰 경로 하나: GitHub Actions 화면을 기본으로 사용하고, 인증된 `gh` 또는 공개 GitHub API 중 하나만 대안으로 선택

같은 GitHub host에 여러 계정이 등록된 환경에서는 저장소마다 기대 login을 명시하고 active account를 확인합니다.

```bash
expected_login="<github-login>"

gh auth status --active --hostname github.com
test "$(gh api user --jq .login)" = "$expected_login"
```

다른 계정이 active이면 해당 저장소에 쓰기 권한이 있는 계정으로 전환한 뒤 같은 검사를 다시 실행합니다.

```bash
gh auth switch --hostname github.com --user "$expected_login"
test "$(gh api user --jq .login)" = "$expected_login"
```

`GH_TOKEN`이나 `GITHUB_TOKEN`이 설정된 셸은 저장된 active account와 다른 인증을 사용할 수 있습니다. 위의 `gh api user` 결과를 실제 계정 판정으로 사용합니다. SSH remote나 별도 credential helper를 사용하는 `git push`는 `gh auth switch`와 독립적이므로, push 직전에 `git push --dry-run origin HEAD:refs/heads/main`으로 해당 remote의 쓰기 권한과 대상 branch를 확인합니다.

각 작업 tree는 `git status -sb`와 path-scoped diff로 확인합니다. 관련 없는 dirty worktree는 그대로 보존하고 아래의 임시 clean source root를 사용합니다.

## 2. Canonical 변경 게시

각 canonical repository에서 자체 validator와 test를 실행한 뒤 의도한 파일만 commit·push합니다. 서로 독립적인 repository는 검증과 push를 병렬로 진행합니다.

Push가 끝나면 full commit SHA를 기록합니다. Project Legibility lock은 공개 remote `main`에 존재하는 commit만 받습니다.

## 3. Clean source root에서 bundle 조립

모든 canonical checkout이 clean `main`이고 remote `main`과 같으면 공통 projects root를 바로 사용합니다.

```bash
release_sources_root="<projects-root>"
python3 scripts/sync_skills.py update --projects-root "$release_sources_root"
```

하나라도 dirty하거나 다른 작업의 checkout 상태를 보존해야 하면 committed HEAD만 담은 임시 root를 만듭니다.

```bash
release_sources_root=$(mktemp -d /private/tmp/project-legibility-release-sources.XXXXXX)

jq -r '.sources[] | [.id,.repository] | @tsv' \
  plugins/project-legibility/sources.lock.json |
while IFS=$'\t' read -r source_id repository_url; do
  git clone --quiet "<projects-root>/$source_id" "$release_sources_root/$source_id"
  git -C "$release_sources_root/$source_id" remote set-url origin "$repository_url"
done

python3 scripts/sync_skills.py update --projects-root "$release_sources_root"
```

`update` 뒤에는 `git diff --stat`과 `git diff --name-status`를 한 번 확인합니다. 변경한 skill의 snapshot만 byte 변경되어야 합니다. 하나의 canonical source가 여러 skill을 제공하면 연결된 snapshot diff를 모두 확인합니다. 문서 전용 canonical commit으로 source SHA가 이동하는 경우 snapshot integrity가 유지되는지도 함께 확인합니다.

Manifest version과 한영 changelog를 같은 release version으로 갱신합니다.

## 4. Release gate를 한 wave로 실행

다음 네 묶음은 서로 독립적이므로 병렬로 실행합니다.

### Source와 bundle

```bash
python3 scripts/sync_skills.py check --projects-root "$release_sources_root"
python3 scripts/sync_skills.py check --offline
python3 scripts/validate_bundle.py --release-tag "v<version>"
python3 -m unittest discover -s tests -v
git diff --check
```

### Plugin

```bash
python3 "$CODEX_HOME/skills/.system/plugin-creator/scripts/validate_plugin.py" \
  plugins/project-legibility
```

### Bundled skills

```bash
for skill_dir in plugins/project-legibility/skills/*; do
  python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" \
    "$skill_dir"
done
```

### Remote source

```bash
python3 scripts/sync_skills.py check
```

각 검사는 한 번의 최종 결과만 기록합니다. 실패하면 첫 actionable failure를 고친 뒤 영향받은 묶음과 최종 release-tag bundle만 다시 실행합니다.

## 5. Release와 catalog 게시

1. 검증된 Project Legibility 변경을 commit하고 `main`에 push합니다.
2. 그 commit의 CI 성공을 확인합니다.
3. 같은 commit에 annotated `v<version>` tag를 만들고 push합니다.
4. Release workflow와 GitHub Release 성공을 확인합니다.
5. `perhapsspy/codex-plugins`에서 `project-legibility`의 `source.sha`만 release commit의 40자리 SHA로 갱신합니다.
6. Catalog unit test와 `python3 scripts/validate_marketplace.py --verify-remote`를 병렬로 실행합니다.
7. Catalog 변경을 commit·push하고 catalog CI 성공을 확인합니다.

여기서 배포가 완료됩니다. 로컬 설치 version이나 cache freshness는 Codex 앱의 plugin lifecycle이 소유합니다. 클라이언트 갱신을 별도로 진단하는 작업은 사용자가 요청한 환경과 시점에서 수행합니다.

PR은 필수 릴리스 단계가 아닙니다. 별도 검토나 협업이 필요할 때만 선택적으로 사용합니다.

## 중단 조건

다음 상태에서는 release commit이나 tag를 만들기 전에 멈춥니다.

- canonical commit이 공개 remote `main`과 다름
- 의도하지 않은 skill snapshot byte 변경
- manifest, changelog와 `v<version>` 불일치
- local, remote 또는 offline source 검사 실패
- plugin·skill validator 또는 repository test 실패
- active GitHub login이 해당 repository의 기대 login과 다르거나 write remote의 dry-run push가 실패함
- catalog가 release 전 commit이나 움직이는 branch를 가리킴

## Rollback

1. 마지막으로 검증된 Project Legibility release commit을 확인합니다.
2. Publisher catalog의 `project-legibility` SHA를 그 commit으로 되돌리고 catalog CI를 통과시킵니다.
3. 문제를 canonical source 또는 assembly owner에서 수정합니다.
4. 새 patch 또는 minor release를 게시하고 catalog pin을 전진시킵니다.

Release tag는 immutable 기준점으로 유지합니다.
