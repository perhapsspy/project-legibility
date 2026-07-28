# 배포 지연 분석

## 결론

0.6.7 배포에서 실제 build·test·network 명령은 대부분 수초 안에 끝났다. 전체 작업이 길어진 주된 이유는 release 경로를 시작 전에 고정하지 않아 인증, source root, 상태 관찰과 로컬 설치 확인을 중간에 다시 선택한 데 있다.

## 원인과 교정

| 원인 | 실제 영향 | Runbook 교정 |
|---|---|---|
| `sync_skills.py update`가 모든 canonical checkout의 clean `main`을 요구한다는 조건을 늦게 확인 | 관련 없는 dirty worktree 때문에 직접 update 경로를 버리고 임시 checkout을 뒤늦게 구성했다. | 사전 점검에서 source root를 한 번 선택하고, dirty checkout이 하나라도 있으면 처음부터 committed HEAD 기반 임시 clean root를 쓴다. |
| GitHub CLI 인증과 repository write remote가 서로 다른 계정을 가리킴 | CI 조회와 한 canonical push에서 실패 후 SSH·공개 API 경로로 전환했다. | 시작 전에 write remote와 CI 관찰 경로 하나를 확정한다. GitHub Actions 화면을 기본으로 두어 release에 CLI 인증을 필수화하지 않는다. |
| 검증이 여러 차례의 순차 호출로 흩어짐 | validator, source check와 test 결과를 여러 번 기다리고 같은 상태를 반복 확인했다. | 서로 독립적인 source·bundle, plugin, bundled skills와 remote source 검사를 한 wave에서 병렬 실행한다. |
| 실패 뒤 전체 검사를 반복 | 작은 문구 수정과 환경 실패 뒤 이미 통과한 검사까지 다시 실행했다. | 첫 actionable failure를 고치고 영향받은 검사 묶음과 최종 release-tag bundle만 다시 실행한다. |
| Release와 catalog 상태 확인 방법을 매번 다시 선택 | 잘못된 SHA 조회, shell 변수 충돌과 중복 polling이 생겼다. | commit SHA를 push 직후 한 번 기록하고 선택한 관찰 경로에서 CI·Release·catalog CI를 각각 한 번 완료까지 기다린다. |
| 로컬 plugin 수동 재설치를 release gate로 취급 | 이미 완료된 remote 배포 뒤 marketplace upgrade와 plugin add를 추가로 실행했다. | Release 완료를 GitHub Release와 publisher catalog CI에서 닫고, 설치본 갱신은 Codex 앱 lifecycle에 맡긴다. |
| 넓은 상태 출력 | 전체 plugin 목록처럼 결정에 필요하지 않은 출력이 검토 비용을 늘렸다. | 상태 확인은 대상 plugin, commit, workflow와 첫 실패만 필터링한다. |

## 기대 효과

정상 배포는 다섯 단계로 수렴한다.

1. 사전 점검과 경로 선택
2. canonical commit·push
3. clean source root에서 sync
4. 병렬 release gate와 tag·GitHub Release
5. catalog pin과 CI

이 구조는 실제 외부 대기 시간은 유지하면서 재시도, 중복 읽기와 로컬 client mutation을 제거한다.
