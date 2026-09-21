# 지침 판단 기준 교정 릴리스

## 목적과 범위

사용자가 승인한 `purpose-first-design`과 `source-owner-audit` 영문·한국어 판단 문구를 정본에서 반영하고 Project Legibility 0.14.2와 publisher catalog까지 게시한다.
역할·호출 조건·Final Reduction·읽기 전용 권한은 유지한다. 전역 AGENTS, 위임 설정, Compact 절차는 변경하지 않는다.

## 현재 상태

두 정본의 승인된 수정과 main 게시를 완료했다. 선택한 두 source pin을 갱신했고 승인안·정본·bundle 일치, 스킬 형식·diff·offline lock·release metadata와 50개 단위 테스트를 검증했다. 0.14.2 release commit의 게시가 남아 있다.
기존 main의 사용량 집계 교정도 이번 태그에 포함되며 한영 CHANGELOG에 구분해 기록했다.

## 완료 조건과 재개

[릴리스 런북](../../../../runbooks/release.md)에 따라 같은 release SHA의 main CI·tag·GitHub Release와 publisher pin·CI가 모두 성공해야 완료다.
현재 단계의 근거는 `logs/WORKLOG.md`를 확인한다. 게시 준비가 끝나면 저장소 루트에서 `python3 scripts/release.py publish --version 0.14.2 --catalog-root ../codex-plugins`를 실행한다.
