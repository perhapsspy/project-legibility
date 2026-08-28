# Structure First와 Ponytail 적용 파일럿 결과

## 결론

이 파일럿은 “Structure First의 내용이 더 강하고 Ponytail이 에이전트에 더 잘 먹힌다”는 가설을 부분적으로만 지지한다.

- baseline도 세 과제의 contract를 모두 통과해 두 스킬의 correctness 우위를 확인하지 못했다.
- Ponytail은 `root_cause`와 `async_lifecycle`에서 baseline보다 작은 올바른 diff를 만들었다.
- Structure First는 `root_cause`의 공유 write owner를 가장 작은 변경으로 고쳤지만 `async_lifecycle`에서는 가장 큰 diff를 만들었다.
- combined는 비동기 과제에서 Structure First보다 작았지만, `root_cause` 3회 중 1회 공유 owner를 놓치고 보고된 caller만 고쳤다. 전문 두 개를 한 prompt에 이어 붙이는 방식은 안정적인 결합으로 간주할 수 없다.

현재 증거는 Structure First의 의미를 줄이거나 Ponytail 방식으로 교체할 근거가 아니다. 다음 후보는 의미 체계를 유지한 짧은 runtime core와 `Structure First로 contract 확정 → Ponytail review로 구현 수단 축소`의 단계형 결합이다.

## 실험 질문과 판정 기준

파일럿은 서로 다른 지침 효용을 드러내는 세 과제를 사용했다.

| 과제 | 관찰할 실패 | 숨은 contract |
|---|---|---|
| `reuse` | 프로젝트 helper 재구현 | accent가 있는 제목도 기존 `slugify`와 같은 slug를 만들고 충돌 suffix를 처리한다. |
| `root_cause` | 보고된 `transfer` caller만 patch | 공유 `ledger.debit`가 overdraft를 막아 이름이 언급되지 않은 withdrawal도 안전하다. |
| `async_lifecycle` | stale result만 막고 loading·동등 입력을 놓침 | 최신 결과, stale completion, in-flight 동등 입력 no-op, 실패 시 balanced completion을 함께 지킨다. |

각 scorer는 올바른 reference와 contract를 놓친 reference를 구분하는 selftest를 먼저 통과했다. scorer와 reference는 agent workspace 밖에 있어 실행 agent가 숨은 판정을 읽을 수 없었다.

## 실행 조건

- Codex CLI: `0.150.1`
- model: `gpt-5.6-luna`, reasoning `medium`
- Project Legibility checkout: `d5c0968f8ad5b0cd7de86ad3deba95db6e50b920`
- Structure First source: `40385d8e2bc421dbac8d958826a732c811faf028`
- Ponytail source: `2ed6c52c9d7e5e56942508591085fd45dea277d3`
- isolation: task·arm별 새 Git workspace, `--ephemeral`, `--ignore-user-config`, `--ignore-rules`
- arms: no-skill baseline, Ponytail 전체 `SKILL.md`, Structure First 전체 `SKILL.md`, 두 전문과 우선순위 문장을 함께 넣은 combined

이 실행은 skill discovery나 lifecycle hook을 비교하지 않는다. 각 전문이 이미 선택된 뒤 한 번 직접 주입됐을 때의 구현 결과를 비교한다.

## 결과

`C`는 일반 correctness, `K`는 과제별 핵심 contract다. LOC는 test를 제외한 source diff다.

| 과제 | arm | C | K | source diff | 시간 |
|---|---|---:|---:|---:|---:|
| reuse | baseline | 1 | 1 | `+10/−1` | 36.8s |
| reuse | Ponytail | 1 | 1 | `+10/−1` | 37.5s |
| reuse | Structure First | 1 | 1 | `+12/−1` | 46.6s |
| reuse | combined | 1 | 1 | `+11/−1` | 31.0s |
| root cause | baseline | 1 | 1 | `+11/−1` | 54.0s |
| root cause | Ponytail | 1 | 1 | `+4/−1` | 48.6s |
| root cause | Structure First | 1 | 1 | `+2/−0` | 42.6s |
| root cause | combined r1 | 1 | 0 | `+3/−1` | 60.4s |
| root cause | combined r2 | 1 | 1 | `+2/−0` | 63.9s |
| root cause | combined r3 | 1 | 1 | `+2/−0` | 49.3s |
| async lifecycle | baseline | 1 | 1 | `+32/−2` | 90.2s |
| async lifecycle | Ponytail | 1 | 1 | `+13/−2` | 72.9s |
| async lifecycle | Structure First | 1 | 1 | `+38/−4` | 88.3s |
| async lifecycle | combined | 1 | 1 | `+18/−2` | 95.6s |

`root_cause`의 baseline은 요청하지 않은 음수 deposit 검증까지 추가했다. Ponytail은 공유 owner를 고치면서 이를 추가하지 않았고, Structure First는 balance lookup을 새 변수로 만들지 않아 더 작았다. combined r1은 `ledger.debit` 대신 `transfer`에만 guard를 넣고 실패를 예외가 아닌 조용한 return으로 바꿨다. r2와 r3은 Structure First와 같은 공유 owner의 `+2` 변경으로 통과했다.

`async_lifecycle`에서 baseline과 Structure First는 별도 task·in-flight 상태를 도입했다. Ponytail은 request id와 `try/finally`만으로 contract를 통과했다. combined는 하나의 current task를 freshness owner로 사용해 Ponytail보다 5줄 크고 Structure First보다 20줄 작았다.

## 사용량 신호

아래 수치는 최초 12개 셀의 CLI 보고값이다. input은 turn 누적이며 cached input을 포함하므로 API 비용으로 해석하지 않는다. 시간은 arm별 세 셀의 평균 wall time이다.

| arm | 평균 시간 | input | non-cached input | output |
|---|---:|---:|---:|---:|
| baseline | 60.3s | 283,963 | 40,763 | 7,803 |
| Ponytail | 53.0s | 347,653 | 42,501 | 5,870 |
| Structure First | 59.2s | 376,326 | 40,966 | 7,038 |
| combined | 62.3s | 454,183 | 48,679 | 7,910 |

Ponytail은 이 표본에서 output과 평균 시간을 줄였지만 전체 input은 늘었다. Structure First의 non-cached input은 baseline과 비슷했고 combined는 가장 높았다. 긴 전문 상시 결합보다 짧은 runtime core와 필요한 단계에서만 재주입하는 후보를 비교할 이유가 있다.

## 한계

- 과제 3개, 기본 1회 실행이므로 통계적 우열이나 실제 사용자 분포로 일반화할 수 없다.
- combined의 실패만 2회 추가해 arm별 반복 수가 같지 않다.
- native platform, stdlib, migration, cross-representation policy와 장기 변경 용이성을 측정하지 않았다.
- 직접 주입 실험이므로 description 기반 자동 activation, session persistence와 subagent propagation은 평가하지 않았다.
- deterministic scorer는 contract와 diff를 판정하지만 가독성·유지보수성을 독립 blind judge로 평가하지 않았다.
- 원시 JSONL과 생성 workspace는 저장소 밖 임시 위치에서 확인했으며 저장소에는 보존하지 않는다.

## 재현

Ponytail을 해당 revision으로 checkout한 뒤 runner의 selftest를 먼저 실행한다.

```bash
python3 tests/evaluation/structure_first_ponytail/run.py \
  --ponytail /path/to/ponytail/skills/ponytail/SKILL.md \
  --structure plugins/project-legibility/skills/structure-first/SKILL.md \
  --output /tmp/structure-first-ponytail-selftest \
  --selftest
```

실행 로그와 workspace는 저장소 밖 output 경로에 둔다.

```bash
python3 tests/evaluation/structure_first_ponytail/run.py \
  --ponytail /path/to/ponytail/skills/ponytail/SKILL.md \
  --structure plugins/project-legibility/skills/structure-first/SKILL.md \
  --output /tmp/structure-first-ponytail-run \
  --model gpt-5.6-luna \
  --reasoning medium \
  --workers 4
```

## 다음 비교

다음 실험은 같은 모델·과제·scorer에서 각 arm을 최소 4회 반복하고 아래 후보를 분리한다.

1. baseline
2. Ponytail full
3. 현재 Structure First full
4. Structure First의 짧은 runtime core
5. 현재 두 전문의 동시 결합
6. Structure First 적용 뒤 별도 Ponytail review를 수행하는 단계형 결합

native·stdlib 과제와 migration·cross-representation 과제를 추가하되 correctness와 contract non-regression을 LOC보다 먼저 판정한다.
