# UI 전용 스킬 실험 최종 보고서

## 결론

Gate 1 전체 판정은 `INCONCLUSIVE`다. 16개 candidate run과 browser 검증은 완료됐지만 blind judge가 유효한 vote를 만들지 못했다.

다만 blind vote보다 앞선 non-regression 조건에서 `ui-compose`는 baseline 대비 mandatory failure 6개, `ui-refine`은 1개를 추가했다. 두 tested 후보는 vote와 무관하게 release gate를 통과할 수 없다. 이 결과는 name과 description만 바꾼 후보에 한정되며, 현재 production skill과 no-skill의 직접 비교는 아니다.

실험은 rename successor를 지지하지 못했다. 별도의 제품 구성 판단에 따라 현재 저장소의 다음 Project Legibility bundle에서 `design-user-interfaces`와 `ui-design-rigor`를 제거했고 rename·merged successor는 추가하지 않았다. 이 결정은 UI 스킬이나 split 구조가 일반적으로 무효라는 결론이 아니다.

## 비교와 검증 근거

Gate 1은 두 역할에서 fixture 2개를 2회씩 실행하고, rename candidate와 no-skill baseline을 paired 비교했다. 총 `2 roles × 2 fixtures × 2 repetitions × 2 arms = 16` model calls다. 환경은 Codex CLI `0.149.1`, `gpt-5.6-sol` medium, Chrome `151.0.7922.174`였고 browser 검증은 desktop `1280×900`과 mobile `390×844`에서 수행했다.

| 역할 | fixture | tested candidate | 결과 |
|---|---|---|---|
| compose | delivery reschedule, incident command | `ui-compose` | baseline 대비 mandatory failure 6개 추가, baseline failure 제거 0 run |
| refine | checkout recovery, member invite | `ui-refine` | baseline 대비 mandatory failure 1개 추가, baseline failure 제거 1 run |

추가 failure는 `delivery-reschedule` r2의 `requiredRegions`, `selectionReview`, `confirmWorks`, `incident-command` r1의 `permissionBoundary`, `keyboardShortcut`, `treatmentBoundary`, `checkout-recovery` r2의 `announcement`다. 실험 당시 자동 검사에서는 16개 run 모두 source integrity, event log와 output 검사를 통과한 것으로 기록됐다.

### 실험 대상과 기준 revision

- Project Legibility baseline: tag `v0.9.3`, commit `95514eeffa9367de2493de243fe8b0e8f91b2128`
- `design-user-interfaces` source commit: `1a84858c829014b522c5760895f9df1f9bc8588d`
- `ui-design-rigor` source commit: `f02450f8967c8068c96183a1082c4a7bb92b0bf4`
- `ui-compose` description: “Use for a new screen or major redesign when page structure, hierarchy, or interaction decisions remain open.”
- `ui-refine` description: “Use for read-only review or bounded improvement of an existing UI after page structure and core interactions are settled.”

두 후보는 대응하는 source revision에서 frontmatter의 name과 description만 바꾸고 나머지 본문은 동일하게 유지했다.

실행 산출물은 보존하지 않았다. 결과 수치와 failure 목록은 당시 검증에서 남긴 요약이며, 이 저장소만으로 run-level 결과를 다시 계산할 수 없다.

## 무효·제외된 증거

- 최초 파일럿은 routing corpus의 경계 판별력이 없고 Git·browser·skill-loading 조건이 arm 사이에서 통제되지 않았으며 mode별 1회뿐이어서 전체를 `INVALID`로 처리했다.
- Gate 1 blind judge는 output schema가 API에서 거부돼 vote 0개로 끝났다.
- evaluator-only 복구를 다섯 차례 시도했지만 usable vote를 얻지 못해 중단했고, scored judge와 Gate 2는 실행하지 않았다.
- pilot과 실제 사용 감사는 후보 선정과 유지비용 판단의 보조 근거로만 사용했다. 어느 것도 topology 일반 법칙이나 독립적인 효용 증명으로 취급하지 않았다.

## 한계와 설계 교훈

- current 이름 그대로의 production skill과 no-skill을 paired 비교하지 않았다.
- 작은 fixture 표본이므로 실제 사용자 분포나 UI 과업 전체로 일반화할 수 없다.
- blind vote가 없어 Gate 1 전체는 완결되지 않았다.
- non-regression 조기 종료 조건을 먼저 확인했어야 했다. 이미 제품 후보의 pass 가능성이 없어진 뒤 evaluator 복구를 반복한 것은 설계·우선순위 실패였다.

## 제품 적용과 전환

- Project Legibility의 source lock, generated bundle, catalog, routing fixture와 notices에서 두 UI 스킬을 제거했다.
- 명시 호출 `$project-legibility:design-user-interfaces`와 `$project-legibility:ui-design-rigor`에는 직접 successor가 없다. UI 과업은 일반 요청으로 기술한다.
- 두 canonical skill repository와 기존 Project Legibility release는 변경하지 않았다.
- 게시 여부와 plugin version, 한영 `CHANGELOG`, tag, publisher pin은 별도 release task가 소유한다.

## 저장소 검증

- `python3 scripts/sync_skills.py check --offline`: 통과
- `python3 scripts/validate_bundle.py`: 통과 (`9 sources`, `10 skills`)
- `python3 -m unittest discover -s tests -v`: 통과
