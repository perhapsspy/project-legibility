# project-context 작업 단위 검사

## 목적과 범위

결정이 없는 작업을 정상으로 인정하고, 현재 작업만 검사할 수 있게 한다. `project-context` 정본과 해당 bundle snapshot·pin을 갱신한다.

## 현재 상태

정본 `8dfff66`을 검증·push하고 bundle에 동기화했다. 빈 결정 로그를 조회·검사할 수 있고, `--task-root`로 선택한 작업만 검사한다. 옵션을 생략하면 기존 전체 검사를 수행한다. 정본 테스트 68개와 Linux bundle 테스트 50개, 스킬 형식·전체 runtime·선택 runtime·bundle 검사가 통과했다.

## 다음 단계

사용자 요청에 따라 `0.13.1` 게시를 진행한다. release commit의 main CI, 동일 SHA의 tag·GitHub Release, publisher pin·CI를 확인한다.
