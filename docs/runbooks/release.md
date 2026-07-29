# Project Legibility 릴리스 런북

이 런북은 canonical 스킬 변경을 Project Legibility release와 publisher catalog까지 가장 짧은 검증 경로로 배포하는 실행 순서, version, release gate와 rollback을 소유합니다.

## 완료 조건

배포는 다음 상태에서 완료됩니다.

- 변경한 canonical commit이 공개 `main`에 존재합니다.
- Project Legibility release commit이 CI를 통과하고 같은 commit에 `v<version>` tag와 GitHub Release가 존재합니다.
- `perhapsspy/codex-plugins`가 그 release commit을 고정하고 catalog CI의 remote manifest 검증을 통과합니다.

## Version 선택

| Version | 적용 범위 |
|---|---|
| Patch | 제품 약속과 설치 구성을 유지하는 skill bug fix·문안·reference, trigger 의미를 유지하는 교정, 조립 도구와 공개 절차의 호환 가능한 수정 |
| Minor | skill 추가·제거, 제품 역할이나 trigger 의미 변경, starter prompt 변경, lock·snapshot 구조의 호환 가능한 확장 |
| Major | plugin source contract를 깨는 변경과 그 migration |

새 skill의 역할과 선택 경계는 [제품 계약](../PRODUCT.md)에 먼저 반영합니다. Manifest, 한영 changelog와 `v<version>` tag는 선택한 version을 함께 가리킵니다.

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
