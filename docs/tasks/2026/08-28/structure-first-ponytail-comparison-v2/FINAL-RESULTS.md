# Structure First와 Ponytail 비교 v2 결과

## 결론

177단어의 Structure First runtime core가 유일하게 24/24 contract를 통과했다. 현재 Structure First 전체 전문은 22/24, baseline·Ponytail·동시 combined는 23/24, 2-pass staged는 21/24였다. 모든 arm의 일반 correctness는 24/24였다.

contract 실패는 모두 root-cause 과제에서 보고된 `transfer` caller만 고치고 공유 `ledger.debit` owner를 놓친 사례였다. runtime core는 네 번 모두 `ledger.debit`를 선택해 같은 `+4/−1` 변경으로 수렴했다. 현재 전체 전문은 2/4만 공유 owner를 선택했다. 전체 전문에도 같은 원칙이 있지만, 짧은 실행 루프에서 “증상이 아닌 owner”가 더 두드러져 실제 선택 안정성이 높아진 것으로 해석한다.

Ponytail은 contract 23/24로 runtime core보다 한 번 덜 통과했지만, async·native·stdlib에서 가장 작거나 combined와 같은 diff를 만들고 총 output과 합산 실행 시간이 가장 낮았다. 구현 경제성 효과는 재현됐다.

runtime core를 Structure First 정본의 progressive-disclosure 후보로 승격했다. 다만 contract 차별력이 root-cause 한 과제에 집중됐으므로 모호한 owner·completion 과제의 후속 source A/B를 반영 조건으로 두었다. staged 후보는 제외하고 동시 combined도 기본 구성으로 채택하지 않는다.

## 후속 반영

별도 source 작업에서 모호한 owner와 completion owner 사례를 추가해 현재 전체 스킬, 후보 본문, 후보 본문과 관련 reference를 각각 4회 비교했다. 새 두 사례는 세 arm 모두 8/8 contract를 통과했다. 기존 판별 root-cause 사례는 현재 전체 2/4, 후보 본문 4/4, 후보와 관련 reference 3/4였다.

이 결과와 사용자 문구 리뷰를 반영한 progressive-disclosure 구조를 Structure First 정본 [`11819e82afdb`](https://github.com/perhapsspy/structure-first/commit/11819e82afdb70f94bd5f7b8c1eb6df686eafcc2)에 확정했다. main runtime contract는 항상 필요한 owner·flow·completion·verification 판단을 보유하고, public I/O·ownership·async·representation·migration과 boundary evidence 세부 규칙은 적용 조건이 맞을 때만 reference에서 읽는다. Description과 invocation policy는 유지했다.

## 실험 설계

`gpt-5.6-luna` medium의 격리 Codex 실행에서 여섯 과제와 여섯 arm을 각각 4회 비교했다.

| 축 | 구성 |
|---|---|
| 과제 | root cause, async lifecycle, native platform, stdlib, migration, cross-representation policy |
| arm | baseline, Ponytail full, Structure First full, Structure First runtime core, simultaneous combined, staged |
| 반복 | task×arm별 4회, 총 144개 논리 셀 |
| 호출 | 단일-pass arm 120회, staged 48회, 총 168회 |
| 격리 | 셀별 새 Git workspace, `--ephemeral`, `--ignore-user-config`, `--ignore-rules` |
| 판정 | 숨은 결정론적 scorer의 correctness와 contract를 LOC보다 먼저 판정 |

staged는 Structure First full 구현 뒤 같은 workspace의 새 Codex 세션에서 Ponytail full로 current diff를 축소했다. 실제 `ponytail-review`는 finding만 반환하는 read-only 스킬이므로 staged edit pass에 사용하지 않았다.

runtime core는 현재 Structure First 전체 전문 905단어의 약 20%인 177단어다. `owner 선택 → observable completion → flow 추적 → structural demand → 국소 변경 우선 → 비경쟁 resolution path·migration → stable owner 검증`의 7단계와 async·cross-representation 핵심 규칙을 유지했다. 정확한 본문은 [`run_v2.py`](../../../../../tests/evaluation/structure_first_ponytail/run_v2.py)의 `RUNTIME_CORE`가 소유한다.

## Contract 결과

root-cause 외 다섯 과제는 모든 arm이 4/4를 통과했다.

| 과제 | baseline | Ponytail | SF full | SF core | combined | staged |
|---|---:|---:|---:|---:|---:|---:|
| root cause | 3/4 | 3/4 | 2/4 | **4/4** | 3/4 | 1/4 |
| async lifecycle | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 |
| native | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 |
| stdlib | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 |
| migration | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 |
| representation | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 |
| **합계** | **23/24** | **23/24** | **22/24** | **24/24** | **23/24** | **21/24** |

root-cause 실패 8개는 모두 `transfers.py`에 balance guard를 넣었다. 일부는 insufficient funds를 예외가 아닌 조용한 return으로 바꿨고 staged 한 표본은 요청하지 않은 lock까지 추가했다. 공유 `ledger.debit`는 그대로여서 이름이 언급되지 않은 withdrawal이 계속 overdraft를 허용했다.

staged는 첫 pass의 owner 선택을 두 번째 축소 pass가 교정하지 못했다. 단계 분리는 첫 단계가 올바른 contract를 확정했다는 전제에서만 안전하며, 별도 correctness gate 없이 Ponytail pass를 붙이는 방식은 이 결과에서 가장 비싸고 가장 불안정했다.

## 구현 경제성

표의 값은 test를 제외한 net LOC 중앙값이며 대괄호는 4회 범위다. 음수는 삭제가 추가보다 많다는 뜻이다.

| 과제 | baseline | Ponytail | SF full | SF core | combined | staged |
|---|---:|---:|---:|---:|---:|---:|
| root cause | 5 [4,10] | **2 [2,3]** | 4.5 [3,7] | 3 [3,3] | **2 [2,4]** | 3 [1,11] |
| async lifecycle | 30.5 [21,38] | 16 [11,28] | 27 [14,32] | 21.5 [11,35] | **14 [11,19]** | 20.5 [10,27] |
| native | 6 [0,6] | **0 [0,0]** | 6 [6,6] | **0 [0,0]** | **0 [0,0]** | **0 [0,0]** |
| stdlib | 8 [7,8] | **6 [6,6]** | 7.5 [7,10] | 7 [6,8] | **6 [6,6]** | 8 [6,8] |
| migration | −11 | −11 | −11 | −11 | −11 | −11 |
| representation | 3 | 3 | 3 | 3 | 3 | 3 |

native의 LOC 차이는 기능량보다 formatting 영향이 크다. Ponytail·runtime core·combined·staged는 `<input>` 속성을 한 줄에 유지했고 Structure First full은 여러 줄로 포맷했다. 모든 arm이 native `type=date`, min/max와 접근 가능한 label을 사용했으며 custom calendar나 dependency를 만들지 않았다.

stdlib은 모든 표본이 Python `csv`를 사용했다. migration과 representation은 prompt와 기존 owner가 명확해 모든 arm이 같은 결과에 수렴했다. 이 두 과제는 runtime core의 non-regression은 보여주지만 arm 차별력은 낮다.

async는 모든 arm이 contract를 지켰다. Ponytail과 combined가 가장 작은 편이었고 runtime core는 net +11 두 번과 +32 이상 두 번으로 변동이 컸다. runtime core가 contract 안정성은 유지했지만 항상 Ponytail 수준으로 구현량을 줄이지는 않았다.

## 사용량

CLI가 보고한 cell별 usage의 합계다. input은 turn 누적이고 cached input을 제외한 값만 표에 사용했으므로 실제 청구 비용과 동일하지 않다. duration도 병렬 실행의 실제 wall time이 아니라 각 cell 시간의 합이다.

| arm | calls | 합산 duration | non-cached input | output |
|---|---:|---:|---:|---:|
| baseline | 24 | 1,161s | 275,705 | 43,252 |
| Ponytail | 24 | **928s** | 294,462 | **33,719** |
| SF full | 24 | 1,326s | 314,609 | 43,866 |
| SF core | 24 | 1,091s | **258,480** | 39,280 |
| combined | 24 | 1,110s | 328,259 | 42,282 |
| staged | 48 | 2,357s | 599,938 | 89,607 |

전체 실험은 non-cached input 2,071,453, output 292,006 token을 사용했다. Ponytail은 가장 빠르고 output이 적었다. runtime core는 full보다 합산 duration 18%, non-cached input 18%, output 10% 낮았다. staged는 호출·input·output이 거의 두 배면서 contract 결과도 가장 낮아 지배되는 후보로 본다.

## 제품 판단

1. **Structure First runtime core를 canonical source 후보로 채택했다.** 현재 의미를 줄이지 않고 main `SKILL.md`를 짧은 실행 계약으로 만들고, async·representation·migration·verification 세부 규칙을 필요한 reference로 이동하는 방향이다. 후속 A/B와 사용자 리뷰를 통과해 정본에 반영됐다.
2. **v2 결과만으로 현재 Structure First full을 바로 교체하지 않았다.** 24/24 결과는 유망하지만 discriminating failure가 root-cause 한 fixture에 집중됐기 때문이다. 후속 owner·completion 검증이 이 보류 조건을 닫았다.
3. **Ponytail을 Structure First 대체재나 Project Legibility 기본 조합으로 넣지 않는다.** 경제성은 강하지만 owner contract는 1회 실패했고 Structure First가 소유하는 async·representation·migration 의미를 대체하지 않는다.
4. **simultaneous combined를 기본값으로 채택하지 않는다.** async와 stdlib에서는 작았지만 root-cause contract가 3/4이고 input도 단일 arm보다 높다.
5. **staged 후보는 제외한다.** correctness gate 없이 첫 pass의 contract를 신뢰한 채 축소하는 순서는 owner 오류를 고착시켰다.

## 재현과 정본

- 실행 runner: [`run_v2.py`](../../../../../tests/evaluation/structure_first_ponytail/run_v2.py)
- 후속 source A/B runner: [`run_v3.py`](../../../../../tests/evaluation/structure_first_ponytail/run_v3.py)
- results-only 집계: [`summarize_v2.py`](../../../../../tests/evaluation/structure_first_ponytail/summarize_v2.py)
- Project Legibility checkout: `d5c0968f8ad5b0cd7de86ad3deba95db6e50b920`
- v2 비교 당시 Structure First source: `40385d8e2bc421dbac8d958826a732c811faf028`
- 반영된 Structure First source: `11819e82afdb70f94bd5f7b8c1eb6df686eafcc2`
- Ponytail source: `2ed6c52c9d7e5e56942508591085fd45dea277d3`
- Codex CLI: `0.150.1`

```bash
python3 tests/evaluation/structure_first_ponytail/run_v2.py \
  --ponytail /path/to/ponytail/skills/ponytail/SKILL.md \
  --structure plugins/project-legibility/skills/structure-first/SKILL.md \
  --output /tmp/structure-first-ponytail-v2 \
  --selftest

python3 tests/evaluation/structure_first_ponytail/run_v2.py \
  --ponytail /path/to/ponytail/skills/ponytail/SKILL.md \
  --structure plugins/project-legibility/skills/structure-first/SKILL.md \
  --output /tmp/structure-first-ponytail-v2 \
  --model gpt-5.6-luna \
  --reasoning medium \
  --workers 4 \
  --runs 4

python3 tests/evaluation/structure_first_ponytail/summarize_v2.py \
  /tmp/structure-first-ponytail-v2/results.json
```

## 저장소 검증

- v2 good/bad reference selftest: 통과 (`12/12`)
- results-only summary 재계산: 통과 (`144 cells`, failure `0`)
- `python3 scripts/sync_skills.py check --offline`: 통과
- `python3 scripts/validate_bundle.py`: 통과 (`9 sources`, `10 skills`)
- `python3 -m unittest discover -s tests -v`: 통과 (`50 tests`)
- current task `WORKLOG`·`DECISIONS` latest-block check: 통과
- `git diff --check`: 통과

project-context 전역 runtime-shape 검사는 기존 `docs/tasks/2026/08-25/interface-design-skill-experiment-v3/`의 `logs/WORKLOG.md`와 `logs/DECISIONS.md` 부재만 보고했다. 이번 v2와 직전 파일럿 task의 core file과 latest log block은 유효하다. 기존 UI 실험 task는 이번 비교 범위에서 변경하지 않았다.

## 한계

- task별 4회는 방향성 반복이지 통계적 일반화에 충분한 표본이 아니다.
- root-cause만 arm 간 contract 차이를 만들었고 나머지 다섯 과제는 모두 수렴했다.
- migration·representation prompt가 목표 owner와 종료 조건을 비교적 명시적으로 제공해 실제 모호한 요구보다 쉽다.
- native LOC는 HTML formatting에 민감하다.
- 직접 전문을 주입했으므로 description 기반 activation, hook persistence와 subagent propagation을 측정하지 않았다.
- deterministic scorer는 observable contract를 판정하지만 장기 maintainability와 가독성을 blind judge로 평가하지 않았다.
- 원시 JSONL과 생성 workspace는 저장소 밖 임시 output에서 확인했으며 저장소에는 보존하지 않는다.
