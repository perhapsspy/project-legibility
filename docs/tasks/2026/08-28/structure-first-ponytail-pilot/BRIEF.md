# Structure First와 Ponytail 적용 파일럿

## 상태

격리된 Codex 4-arm 파일럿과 scorer selftest를 완료했다. 세 과제에서 baseline, Ponytail, Structure First를 각각 1회 실행했고 combined의 `root_cause` 실패만 2회 추가 확인했다.

이번 표본에서는 Ponytail이 correctness를 높이지는 않았지만 공유 owner와 비동기 과제의 구현량을 줄였다. Structure First는 공유 owner 과제에서 가장 작은 올바른 변경을 만들었으나 비동기 과제에서는 가장 큰 변경을 만들었다. 두 전문을 한 prompt에 결합한 arm은 한 번 잘못된 owner를 선택해 단순 결합의 안정성을 입증하지 못했다.

## 현재 판단

Structure First의 의미 체계나 제품 구성을 지금 바꾸지 않는다. 다음 비교에서는 짧은 runtime core와 단계형 결합을 별도 후보로 두고 반복 수를 늘려 activation, contract 준수, 구현 경제성을 분리해 검증한다.

## 근거와 재현

- 방법, 결과와 한계: [FINAL-RESULTS.md](FINAL-RESULTS.md)
- 재현 runner와 숨은 scorer: [`tests/evaluation/structure_first_ponytail/run.py`](../../../../../tests/evaluation/structure_first_ponytail/run.py)
