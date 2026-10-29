# Critical Review 플러그인 편입과 0.18.0 배포

## 목적과 범위

범용 결과 수용성 검토 스킬 `critical-review`를 Project Legibility의 정본·pin·생성 snapshot 구조에 추가하고 정식 배포한다. 코드·기획·설계의 목적 충족, 충분함과 과함, 지적 자체의 반증을 다룬다. 사용자 승인 범위는 정본 공개 main, Project Legibility 0.18.0 release, publisher 양 catalog pin과 Mac 공식 설치 갱신·새 일반 세션 검증이다. 진행 중 세션은 변경하지 않는다.

## 배포 입력

정본 저장소는 critical-review이고 제품 계약은 docs/PRODUCT.md다. source pin은 plugins/project-legibility/sources.lock.json이 소유한다. 생성 bundle은 공통 스킬 10개를 제공한다. 격리 환경의 독립 합성 실행 5개와 Mac 사용자 local marketplace의 새 일반 Codex 실행에서 discovery·명시 호출·승인 경계를 확인했다. 근거와 제한은 logs/WORKLOG.md에 있다.

## 게시와 설치 상태 확인

정상 배포는 docs/runbooks/release.md를 따른다. 완료 증거의 정본은 GitHub v0.18.0 release·동일 SHA의 main CI와 codex-plugins의 양 catalog pin·CI다. 작업 로그나 local install만으로 배포 완료를 판단하지 않는다. Mac 설치는 공식 perhapsspy marketplace를 갱신하고 임시 local 설치를 비활성화해 새 일반 Codex 세션에서 확인한다.
