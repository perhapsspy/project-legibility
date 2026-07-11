# 배포자 마켓플레이스 전환

## 목표

Project Legibility의 제품 저장소와 perhapsspy의 플러그인 배포 카탈로그를 분리하고, 공개·로컬 설치 좌표를 `project-legibility@perhapsspy`로 완전히 전환한다.

## 범위

- Project Legibility에서 단일 제품용 marketplace 소유권을 제거하고 제품 bundle·release 책임만 남긴다.
- 별도 `perhapsspy/codex-plugins` 저장소가 marketplace 이름 `perhapsspy`와 원격 plugin pin을 소유한다.
- 기존 `project-legibility@project-legibility` 설치와 marketplace 등록은 제거하며 호환 채널을 유지하지 않는다.

## 현재 이해

- Codex는 plugin을 `<plugin>@<marketplace>`로 식별하며, marketplace 저장소와 plugin source 저장소는 분리할 수 있다.
- 원격 catalog entry는 `git-subdir`와 고정 commit SHA로 `plugins/project-legibility`를 가리킬 수 있다.
- 개별 스킬 저장소는 계속 스킬 내용의 정본이고 Project Legibility는 검증된 snapshot과 plugin release를 소유한다.

## 현재 상태

- Project Legibility `v0.2.0`과 publisher catalog의 exact release SHA pin이 공개됐고 두 원격 CI가 통과했다.
- 기존 marketplace와 plugin 설치는 제거됐으며 로컬에는 `project-legibility@perhapsspy` 0.2.0만 활성화돼 있다.
- 설치 cache는 release plugin tree와 일치하고 새 Codex 작업에서 `project-legibility:` 스킬 10개가 모두 로드됐다.

## 다음 행동

새 plugin을 catalog에 추가하거나 Project Legibility release pin을 갱신할 때 각 저장소의 contribution 절차로 다시 연다.

## 작업 경계

- `plugins/project-legibility/`
- `.agents/plugins/marketplace.json`
- `scripts/validate_bundle.py`
- `tests/test_bundle.py`
- 공개·운영 문서
