# 지침 판단 기준 교정 릴리스

## 목적과 범위

사용자가 승인한 `purpose-first-design`과 `source-owner-audit` 영문·한국어 판단 문구를 정본에서 반영하고 Project Legibility 0.14.2와 publisher catalog까지 게시한다.
역할·호출 조건·Final Reduction·읽기 전용 권한은 유지한다. 전역 AGENTS, 위임 설정, Compact 절차는 변경하지 않는다.

## 현재 상태

완료. [v0.14.2](https://github.com/perhapsspy/project-legibility/releases/tag/v0.14.2)는 release commit `925cecc97dfd6d65536e4cc8dc4a945449744baa`에 게시됐다. 같은 SHA의 main CI와 Release workflow가 성공했다.
publisher commit `f7106ce0ffc038476f9f3fdc3c53705ab4d0c55f`가 그 release SHA를 고정하며 catalog CI도 성공했다. 승인안·정본·bundle 일치, 스킬 형식·diff·offline lock·release metadata, Project Legibility 50개와 catalog 12개 테스트를 검증했다.
기존 main의 사용량 집계 교정도 태그에 포함됐으며 한영 CHANGELOG에 구분했다. 로컬 설치/cache 갱신과 모델 행동 개선 A/B는 수행하지 않았다.

## 후속 작업

이번 작업에 남은 게시 단계는 없다. 근거는 `logs/WORKLOG.md`에 있으며, 다음 변경은 새 요청으로 시작한다. 이후 저장소 운영 기록 commit은 0.14.2 release SHA나 publisher pin을 바꾸지 않는다.
