# Project Legibility 릴리스 런북

이 런북은 canonical 스킬 변경을 Project Legibility release와 publisher catalog까지 게시하는 최소 실행 경로를 소유합니다.

## 완료 조건

- Project Legibility release commit의 `main` CI가 성공하고, 같은 commit에 `v<version>` tag와 GitHub Release가 존재합니다.
- `perhapsspy/codex-plugins`가 그 commit의 full SHA를 고정하고 catalog CI가 성공합니다.

## Version 선택

Version은 diff 크기가 아니라 설치 사용자에게 공개된 호환성 계약으로 선택합니다.

| Version | 판정 |
|---|---|
| Patch | 공개된 skill 구성과 선택 계약을 유지하며 bug, 문안, 실행 품질, reference, guardrail 또는 조립·배포 도구를 호환 가능하게 교정합니다. |
| Minor | skill 추가·제거, 제품 역할, canonical trigger, 명시 호출과 자동 참여, starter prompt 과업 또는 lock·snapshot 구조의 공개 계약을 넓히거나 좁힙니다. |
| Major | plugin source contract나 설치 소비 방식을 깨서 migration이 필요합니다. |

여러 변경이 있으면 가장 높은 영향을 적용합니다. 제품 역할, skill 구성 또는 선택되는 요청 집합이 바뀌면 [제품 계약](../PRODUCT.md)을 먼저 갱신합니다. Manifest, 한영 changelog와 tag는 같은 version을 가리켜야 합니다. 저장소 운영 문서만 바뀌었다면 즉시 plugin release할 필요는 없습니다.

## 준비

1. 변경한 canonical source를 공개 `main`에 push하고 full SHA를 확정합니다.
2. 필요한 source만 갱신합니다. `--source`는 반복할 수 있습니다.

   ```bash
   python3 scripts/sync_skills.py update --source <source-id>=<40-character-sha>
   ```

3. version과 한영 `CHANGELOG`의 `Unreleased`를 release section으로 반영합니다.
4. 생성 diff와 배포 문구를 충분히 검토하고 commit합니다.

게시 전 Project Legibility와 catalog checkout은 각각 clean `main`이어야 합니다. `publish`는 Project Legibility의 현재 `HEAD`를 release commit으로 사용하므로, 검토하지 않은 문구를 자동 생성하거나 변경하지 않습니다.

## 게시

```bash
python3 scripts/release.py publish \
  --version <version> \
  --catalog-root ../codex-plugins
```

명령은 다음 순서만 수행합니다.

1. Project Legibility `HEAD`를 `main`에 push하고 그 exact SHA의 CI 성공을 기다립니다.
2. 같은 SHA에 immutable tag를 push하고 GitHub Release 성공을 확인합니다.
3. catalog의 Project Legibility pin만 그 full SHA로 갱신·push하고 exact SHA의 catalog CI 성공을 기다립니다.

중간 확인, candidate branch, 별도 상태 파일과 수동 catalog 편집은 없습니다. 이미 완료된 단계는 remote `main`, tag, GitHub Release와 catalog pin에서 확인해 건너뜁니다.

## 실패와 재실행

같은 인자로 같은 명령을 다시 실행합니다. 별도 `resume` 명령은 없습니다.

- CI 실패: 원인을 고쳐 새 release commit으로 다시 게시합니다.
- tag가 다른 SHA를 가리킴: 자동으로 이동하거나 삭제하지 않고 중단합니다.
- tag·Release 뒤 catalog 실패: release는 유지하고 같은 명령으로 catalog 단계부터 이어갑니다.
- 공개 뒤 결함: tag를 바꾸지 않습니다. 필요하면 catalog pin을 마지막 정상 release로 되돌리고 patch release로 전진합니다.

완료 뒤 별도 작업 기록 commit, local install 또는 cache refresh는 배포 gate가 아닙니다.
