# 과검증·작업 중단 지침 교정

## 목적과 범위

사용자가 승인한 공통 지침 두 항목과 structure-first 검증·tighten-docs 이관 문구를 한영 정본에 반영하고 게시·설치한다. 기존 미커밋 변경은 보존하며 이번 커밋에서 제외한다.

## 현재 상태

다섯 원본 파일을 수정·게시했다. personal-config eafb5ed, structure-first abf9442, tighten-docs 3f19881이 각 main에 반영됐다. Project Legibility 0.16.3은 release commit 58b7c004c944bcbab2f336b075f45730fa2b4aff에 게시됐으며 main CI와 Release가 성공했다. publisher db8a03fd4ed7022f62743be7562a08b6729f91ec의 pin과 CI도 확인했다.

Mac은 공통 지침 설치·readback과 공식 CLI의 0.16.3 플러그인 갱신을 완료했다. 설치된 한영 스킬 네 파일·lock·manifest가 게시본과 같다. personal-config 17개, Project Legibility 50개, catalog 12개 테스트와 remote manifest 검증을 통과했다. 기존 미커밋 변경은 그대로 남아 있다. 실행 중 세션의 플러그인 재로딩과 모델 행동 개선은 확인하지 않았다.

## 다음 행동

현재 연결된 실행 대상은 Mac뿐이므로 dot cloud 설치는 실행 경로 부재로 막혀 있다. Windows는 저장소를 fast-forward pull한 뒤 scripts/install.ps1과 scripts/verify.ps1을 실행하는 수동 반영 대기다. 새 작업에서 갱신된 플러그인을 사용한다. 게시 근거는 logs/WORKLOG.md에 있다.
