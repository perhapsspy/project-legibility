# Codex·Claude Code 동시 지원

## 목표와 범위

공통 스킬 정본·snapshot·버전을 유지하며 Codex와 Claude Code가 같은 Project Legibility 패키지를 로드하게 한다. 공통 manifest·클라이언트별 생성 manifest, 검증·설치 안내와 양쪽 catalog를 반영하는 release 경로를 구현했다. 실제 release·publisher pin 전환·사용자 설치본 갱신은 별도 범위다.

## 현재 상태

구현과 로컬 검증 완료. 루트 plugin.json이 공통 identity·version을 소유하고 sync_plugin_metadata.py가 Codex·Claude manifest를 생성한다. Bundle 검사는 생성 drift를 거절한다. CI에는 Claude Code 2.1.304 strict validation을 추가했다.

격리된 임시 환경에서 Codex CLI 0.163.0과 Claude Code 2.1.304가 marketplace 등록·설치·제거에 성공했다. Claude는 9개 스킬을 인식했다. Project Legibility 테스트 57개와 publisher 테스트 17개, metadata·offline bundle 검사와 기존 공개 catalog의 원격 manifest 검증이 통과했다. 실제 모델 자동 선택·작업 수행과 클라이언트 간 작업 재개는 검증 범위에 포함하지 않았다.

Release는 tag·GitHub Release 확인 뒤 두 catalog의 Project Legibility source를 같은 full SHA로 한 commit에 반영한다. 새 Claude catalog는 그때 생성한다. Publisher validator는 같은 source identity·SHA와 Claude native manifest를 검사한다. 실제 Git fixture로 검증 실패 시 tracked catalog 복원과 신규 Claude 파일 제거를 확인했다.

## 다음 행동

후속 release에서는 루트 version과 한영 CHANGELOG를 반영하고 client manifest를 재생성한 뒤 release runbook을 따른다. 현재 공개 version·tag·publisher pin과 사용자 설치본은 유지한다.
