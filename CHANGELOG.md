# Changelog

Project Legibility의 사용자에게 보이는 주요 변경을 기록합니다.

## [Unreleased]

## [0.13.0] - 2026-09-04

### Changed

- `purpose-first-design`을 canonical repository와 설치 identity로 완성해 정본 스킬과 Project Legibility bundle의 소유·식별 경로를 일치시켰습니다.
- `purpose-first-design` 자동 참여 범위를 새 기능의 초기 방향, 기존 구현 재사용, 임시 구현 및 그 밖의 결과에 중대한 영향을 주는 열린 제품·구현 계획 선택까지 넓혔습니다. 의미가 정해진 작업과 구체적인 전문 문제는 제외하며, 잠긴 의미와 안전·운영 경계는 보존합니다.

## [0.12.0] - 2026-09-04

### Changed

- 포함된 `purpose-fit-design`을 `purpose-first-design`으로 교체했습니다. 새 스킬은 제품 의미나 구현 계획의 방향이 실질적으로 열려 있을 때 목적, 확정된 결정과 경계, 권한, 근거와 관찰 가능한 성공에서 가장 작은 충분한 방향을 정합니다. 완료 전에는 답변이 새로 만든 불필요한 범위·약속·가정·열린 결정을 줄이되 확정 의미와 필수 안전·운영 복잡성을 보존합니다. 기존 명시 호출은 `$purpose-first-design`으로 바꿔야 합니다.

## [0.11.1] - 2026-08-28

### Changed

- 포함된 `structure-first`에서 책임 주체, 흐름, 완료 조건, 검증에 관한 핵심 판단을 짧은 실행 계약으로 전면 배치했습니다. 공개 입출력, 책임 경계, 비동기·상태 수명주기, 표현 형식, 전환과 경계 검증의 세부 규칙은 적용 조건이 맞을 때만 한 단계 아래의 세부 문서에서 읽습니다. 기존 제품 역할과 자동 선택 조건은 유지합니다.

## [0.11.0] - 2026-08-27

### Changed

- Project Legibility bundle에서 `design-user-interfaces`와 `ui-design-rigor`를 제거했습니다. 두 스킬의 명시 호출에는 직접 successor가 없으며, UI 작업은 일반 요청으로 전달합니다.
- 포함된 `project-context`가 폐기할 실험·브라우저 검증 코드와 실행 산출물은 저장소 밖 격리 위치에서 다루고, 보존할 코드와 증거는 정식 owner에 두도록 계약을 정리했습니다. 휴리스틱 문서 누적 검사기 `check_gardening.py`는 제거하고 정형 구조 검증은 runtime-shape checker에 남겼습니다.
- 포함된 `codex-token-discipline`의 사용량 감사 도구를 token total, cache rate, child share와 tool-output volume 같은 직접 관찰 신호에 집중하도록 단순화했습니다.

### Fixed

- 사용량 감사 도구가 fork된 child rollout에 복제된 ancestor 기록을 child 사용량과 도구 출력에 다시 더하던 중복 집계를 수정했습니다.

## [0.10.0] - 2026-08-26

### Changed

- 포함된 `tighten-docs`를 의미가 정해진 사람이 작성하는 문서의 기본 품질 패스로 확장했습니다. 다른 코드·제품·운영 작업에 딸린 문서 변경과 일상적인 본문 수정·리뷰에도 초안부터 최종 검토까지 참여하며, 제거된 판단이 부정·비교·경고·예외·방어적 근거로 남았는지 반사실로 검사해 현재 정본에서 삭제합니다.
- 포함된 `codex-project-director`가 자신이 만들었거나 명시적으로 인계받은 작업만 제어하고, 작업 식별자와 교체 세대, 다음 사건, 실제 효과 상태를 대조하도록 작업 생명주기를 강화했습니다. 보고나 종료 표시만으로 완료하지 않고 모든 현재 작업과 이전 세대 작업을 안전하게 회수해 소유권을 해제하고 정본 완료 조건을 입증한 뒤 완료합니다.

## [0.9.3] - 2026-08-24

### Changed

- 포함된 `codex-project-director`가 반복 조사·검증, packet 밖 범위 확장이나 acceptance frontier 정체 같은 drift 신호에서만 독립적인 읽기 전용 trajectory review를 사용하도록 보강했습니다. 시간 경과나 정상 진척만으로는 개입하지 않고, reviewer는 구현·테스트·새 요구사항을 맡지 않은 채 `CONTINUE`, `STEER`, `STOP_AND_REPLAN`, `ESCALATE` 중 하나를 자문 증거로 반환합니다. `CONTINUE`에는 침묵하며, 중단·재계획도 기존 담당자의 안전한 중단과 effect state 인계 전에는 재배정하지 않습니다.

## [0.9.2] - 2026-08-24

### Changed

- 포함된 `codex-project-director`가 구현·디버깅·진단·테스트·검증을 직접 수행하지 않고, 기존 산출물·권위 있는 상태·담당자 증거에 대한 범위가 정해진 읽기 전용 조정과 인수 확인만 하도록 실행 소유권을 강화했습니다. 현재 Goal에 필요하고 독립적으로 실행 가능한 lane은 WIP 한도까지 매 scheduling pass에서 병렬 dispatch하며, focus 변경만으로 다른 eligible lane을 중단하지 않습니다.

## [0.9.1] - 2026-08-24

### Fixed

- 제거된 `semantic-boundary-design`을 forbidden skill로 고정하던 검증을 제거했습니다. 현재 제품 구성에서는 제외된 상태를 유지하지만, 향후 근거와 판단에 따른 재도입 가능성까지 validator가 금지하지 않습니다.

## [0.9.0] - 2026-08-24

### Changed

- 고유 효용이 입증되지 않고 `structure-first`와 선택·책임이 겹치던 `semantic-boundary-design`을 제품 구성에서 제거했습니다. 확정된 동일 도메인 의미가 여러 표현에서 달라질 실질적 위험이 있을 때 해석 owner, 허용된 projection·호환 번역과 최초 재해석 경계의 대표 검증을 유지하는 최소 원칙은 `structure-first`의 기존 ownership·verification 계약에 흡수했습니다. 안전한 증거가 없거나 현재 증거가 충돌하면 해당 경계를 미해결로 유지하며, 다른 스킬 이름에 의존하던 라우팅 문구도 자기완결적인 입력 경계로 교체했습니다.

## [0.8.2] - 2026-08-14

### Changed

- 특정 canonical source의 공개 full SHA만 갱신하고 나머지 pin을 보존하는 원격 조립 경로를 추가했습니다. 릴리스는 검토·commit된 입력을 한 `publish` 명령으로 Project Legibility main CI, 같은 SHA의 immutable tag·GitHub Release, publisher catalog pin·CI까지 게시하며, 중단 뒤 같은 명령이 공개된 외부 상태에서 이어갑니다. Candidate branch, 별도 상태 파일과 배포 뒤 작업 기록 대기는 공개 경로에 두지 않습니다.

## [0.8.1] - 2026-08-14

### Changed

- 포함된 `codex-project-director`가 모든 구현과 제품 또는 시스템 변경을 디렉터와 구분되는 사용자 가시 작업자에게 두고, 지속적인 조사·디버깅·테스트도 그 작업자에게 남기도록 실행 소유권을 명확히 했습니다. role, model, tool 또는 작업자 준비 실패를 포함해 dispatch가 거절되거나 불가능해져도 권한이나 소유권은 바뀌지 않으며 디렉터는 실행을 인수하지 않습니다. 관련 capability 또는 준비 조건이 바뀌기 전에는 같은 경로를 재시도하지 않고, 맞는 기존 작업자나 실질적으로 다른 승인 경로를 사용하며, 그렇지 않으면 필요한 준비 사건 또는 결정을 재개 조건으로 기록합니다.

## [0.8.0] - 2026-08-11

### Changed

- 포함된 `tighten-docs`가 의미가 정해진 현재 정본 문서를 만들거나 크게 고치거나 마무리할 때 초안부터 참여하도록 선택 경계를 넓혔습니다. 미해결 제품·정책·설계·구현 의미, 작업 기록, 생성물과 단순 기계 수정은 맡지 않습니다.

## [0.7.3] - 2026-08-11

### Changed

- 포함된 `codex-project-director`가 단순히 안전하고 유용한 일이 남았다는 이유로 범위를 이어가지 않고, 현재 사용자가 승인한 Goal에 필요한 작업이 남아 있을 때만 계속하도록 교정했습니다.

## [0.7.2] - 2026-08-10

### Changed

- 포함된 `project-context`가 재개 전에 목표·현재 상태·재개 지점을 맞추고, 완료된 선택 작업의 인접 다음 일을 새 지시로 승격하지 않고 후보로 유지하도록 교정했습니다. 사용자나 승인된 정식 계획이 선택한 다음 일은 계속 이어갑니다.

## [0.7.1] - 2026-08-03

### Changed

- 포함된 `structure-first`가 국소 작업 중 다른 owner의 증거가 드러나면 가장 작은 관련 단위만 다시 열고, 경계를 소유한 안전한 증거 없이 국소 테스트만으로 작업을 닫지 않도록 보강했습니다. Production이나 전체 end-to-end 검증을 자동 요구하지는 않습니다.

## [0.7.0] - 2026-07-31

### Changed

- 포함된 `codex-project-director`를 `$codex-project-director` 명시 호출로 제한하고, 활성 lane 하나와 가장 가치 높은 다음 행동을 기본으로 삼아 빈 용량을 채우기 위한 작업 확장을 막았습니다.
- 포함된 `codex-token-discipline`이 root와 child의 총비용을 함께 줄이도록 바꾸고, 예측하기 어려운 출력의 실행 전 예산·증거 재사용·단일 agent 기본값을 추가했습니다. 명확한 초과 비용 위험에서는 자동 참여하되 일반 작업은 건너뜁니다.

## [0.6.9] - 2026-07-29

### Changed

- 포함된 `project-context`와 migration 계약을 재개에 필요한 현재 상태·정본 소유권·감사 가능한 이력에 집중하도록 압축하고, 불확실한 legacy 문서를 성급히 reference로 승격하거나 이동하지 않도록 경계를 유지했습니다.
- 포함된 `ui-design-rigor`를 화면 목적과 제품 구조를 보존하는 국소 개선, 실제 근거 수준, 영향 비례 보고에 집중하도록 압축해 보편 checklist와 인접 재설계로의 확장을 줄였습니다.

## [0.6.8] - 2026-07-29

### Changed

- 포함된 `codex-project-director`가 사용자나 정본에 없는 완료 조건을 만들지 않고, 이미 승인된 구현·출시·배포·readback과 독립적으로 실행 가능한 lane을 불필요한 재승인이나 중간 정지 없이 이어가도록 교정했습니다.
- 반복 실패는 실제 stage·class 증거를 먼저 확보하고, 검증 범위는 acceptance claim과 변경 위험에 맞추도록 줄였습니다. 세션 컨텍스트는 비정본 작업 메모리로 취급하며 승인된 정본 인계, stale-context 재도출과 in-flight 변경 소유권을 보존합니다.

## [0.6.7] - 2026-07-28

### Changed

- 포함된 `project-context`가 여러 작업·담당·단계의 구현이나 승인 판정을 바꾸는 공유 해석에 정본 담당자 하나를 두고, task brief와 인계가 그 경로를 재사용하도록 보강했습니다. 재사용 가능한 공유 계약은 `docs/reference/**`와 migration의 `REFERENCE` 분류가 맡습니다.
- 포함된 `codex-project-director`가 필수 완료 관문과 지향 비교 목표를 구분하고, 작업 흐름의 독립적인 승인 결과를 병렬화 조건에 포함하도록 보강했습니다. 리뷰어의 직접 관찰은 완료 주장 반증에 사용하고 원인·수정안은 변경 담당자의 검증 가설로 분류하며, 반복 품질 판본은 현재 승인 기준선과 정본 비교 경로에 따라 판정합니다.

## [0.6.6] - 2026-07-28

### Changed

- 포함된 `codex-project-director`를 권한·사건 기반 감독·검증과 복구의 세 축으로 줄여, 적극적인 감독과 기존 승인 작업 복구를 유지하면서 반복 절차를 제거했습니다.
- 새 저장소·서비스·API를 설계 조언이나 완료 필요성만으로 변경하지 않고, 결과·대상·행동 범위·담당자와 실제 사용자 권한을 확인하도록 보강했습니다. cross-repo 변경은 정본 관계와 기존 연결을 먼저 확인합니다.

## [0.6.5] - 2026-07-28

### Changed

- 포함된 `codex-project-director`가 승인 기록의 결과·영역·효과·담당자가 유지되는 국소 수정과 수정된 판본의 대표 검증을 기존 권한의 연속으로 처리하고, `retry0`은 같은 판본·가정·입력의 무변경 반복만 금지하도록 교정했습니다.
- 작업자의 종료·다음 결정 문구를 그대로 승인 요청으로 올리지 않고 실제 권한 변화를 재분류하며, 사용자에게 묻기 전에 변경된 승인 필드를 밝히도록 보강했습니다. 기존 실행 전 검토와 정확히 한 번 효과는 유지합니다.

## [0.6.4] - 2026-07-27

### Changed

- 포함된 `codex-project-director`가 변경 권한을 사용자 승인 결과·영역·효과·담당자에 고정하고, 새 발견은 현재 담당자에게 남긴 채 승인 밖 변경 제안만 결정 대상으로 올리도록 보강했습니다.
- 감독은 승인된 작업의 다음 사건과 실행 증거를 기준으로 복구하며, 사용자 승인 경로의 직접 증거와 실제 실행 효과로 완료와 실패를 판단하도록 정리했습니다.

## [0.6.3] - 2026-07-27

### Changed

- 포함된 `codex-project-director`가 작업을 나누기 전에 제품 결과를 충분히 해석하고, 별도 작업은 독립적으로 깊어질 수 있는 큰 전문 책임에만 사용하며, 국소 문제와 전문 의견에 방향을 넘기지 않고 실제 제품 완료로 수렴하도록 보강했습니다.
- 안정적인 제품 기준은 기존 제품 정본 또는 `docs/director-charter.md`에, 계속 변하는 현재 행동과 대기는 `docs/director-state.md`에 유지하도록 두 기록 면의 책임을 구분했습니다.

## [0.6.2] - 2026-07-26

### Changed

- 포함된 `codex-project-director`가 지속적인 조사·구현·디버깅을 사용자 가시 작업 세션에 맡기고, 디렉터 내부 에이전트를 제한된 지원·결정·독립 반증으로 한정하도록 보강했습니다. 다른 작업 세션의 자체 위임은 유지합니다.

## [0.6.1] - 2026-07-25

### Changed

- 포함된 `codex-project-director`가 결함 증거와 제안 해법을 분리하고 기존 결정 상향 경계를 적용하며, 사용자 승인 계약값을 정확히 인계하고 교정과 충돌하는 영향 작업만 확인 후 재개하도록 보강했습니다.

## [0.6.0] - 2026-07-25

### Added

- 사용자가 디렉터로 지정한 세션에서 여러 Codex 작업을 하나의 검증된 결과까지 조정하는 `codex-project-director`를 추가했습니다.
- 기존 제품 화면의 읽기 전용 검토, 구조 보존형 개선과 방향이 정해진 구성 요소 구현을 맡는 `ui-design-rigor`를 추가했습니다.

## [0.5.1] - 2026-07-24

### Changed

- bundled `source-owner-audit`가 소스 소유권 근거와 쓰기 권한을 분리하고, owner 확인만으로 실행 범위를 사용자 승인 밖으로 넓히지 않도록 보강했습니다.

## [0.5.0] - 2026-07-23

### Changed

- `purpose-fit-design`은 새 기능, 기존 구현 재사용과 임시 구현의 초기 방향을 목적·제약·근거와 성공 조건에 맞춰 판단하는 간결한 스킬로 정리했습니다.
- `structure-first`는 기능 구현·버그 수정·리팩터링 전반에서 현재 구조 유지, 국소 변경과 구조 개선 중 문제에 맞는 결과를 선택하도록 조정했습니다.
- 위험 징후와 경험칙을 조사 단서로 삼고, 공개 플러그인 설명과 스킬 선택 검증 사례를 새 호출 모델에 맞췄습니다.

## [0.4.1] - 2026-07-18

### Changed

- bundled `structure-first`가 증상이나 결과가 나타난 위치가 아니라 바꾸려는 동작이나 규칙의 실제 책임을 기준으로 가장 작은 current unit을 고르도록 보강했습니다.

## [0.4.0] - 2026-07-16

### Added

- 제품 약속, 스킬 구성 역할과 호출 모델의 정본인 제품 계약을 추가했습니다.

### Changed

- 공개 README와 plugin 설명을 에이전트 변경이 쌓여도 코드 구조, 판단 기준과 작업 맥락을 함께 강화하는 제품 방향으로 다시 구성했습니다.
- 일반적인 기능 변경, 버그 수정, 리팩터링과 작업 재개 요청에서 canonical trigger에 맞는 스킬이 선택되도록 사용 예시와 starter prompt를 갱신했습니다.
- Core practices, 조건부 Gateway, Specialists와 Optional helpers의 제품 역할을 구분하고 개별 스킬의 의미와 trigger는 각 canonical 저장소가 소유하도록 경계를 명시했습니다.
- bundled `purpose-fit-design`이 사용자 정정의 국소·관계·광범위 도달 범위를 구분하고, 영향받지 않은 목적·제약·확인된 owner 경계를 보존하도록 보강했습니다.

## [0.3.2] - 2026-07-15

### Changed

- 공개 README가 긴 저장소 작업에서 얻는 결과, 대표 사용 장면과 plugin 구성을 먼저 보여주도록 정리했습니다.
- bundled `tighten-docs`가 대상의 역할과 독자 결과를 긍정형 최종 문장으로 직접 쓰고, 실제 금지·한계·안전 경계가 있을 때 부정과 대비를 사용하도록 보강했습니다.

## [0.3.1] - 2026-07-15

### Changed

- 운영 화면이 공용 primitive를 page template로 복제하지 않고 핵심 판단과 다음 행동, 위계를 실질적으로 바꾸는 위험·lifecycle 구분에서 구조를 정하도록 bundled `design-user-interfaces`를 보강했습니다.
- 최소 구현 경계가 서로 다른 도메인 의미와 판단 소유자를 보존하고, 문서 정본 소유권이 그 자체로 runtime UX composition을 규정하지 않도록 bundled `structure-first`와 `tighten-docs`를 보강했습니다.

## [0.3.0] - 2026-07-13

### Added

- 새 화면과 큰 재설계에서 사용자 과업, 실제 콘텐츠, 정보 구조, 관련 상태와 렌더 검증을 함께 다루는 `design-user-interfaces`를 추가했습니다.

## [0.2.5] - 2026-07-13

### Changed

- 공개 README와 목록 설명이 확인된 사용자 상황·결과·다음 행동을 먼저 제시하도록 bundled `tighten-docs`를 갱신했습니다.

## [0.2.4] - 2026-07-13

### Changed

- bundled `tighten-docs`가 독립적인 문서 경계, 정본 소유, 조합 라우팅을 구분하도록 갱신했습니다.

## [0.2.3] - 2026-07-13

### Changed

- 공개 문서에서 변경 내역과 각 스킬의 원본 설명으로 바로 이동할 수 있게 경로를 정리했습니다.
- 리팩터링 예제가 기존 동작을 보존하도록 교정하고, 실행되지 않은 테스트를 검증 완료로 표현하지 않도록 고쳤습니다.
- 스킬 유지보수, 편집 승인과 토큰 감사 안내를 실제 실행 범위와 권한 경계에 맞게 다듬었습니다.
- 생성 배포본을 최신 원본 스킬 커밋으로 갱신했습니다.

### Removed

- 현재 운영에 필요하지 않은 GitHub issue와 pull request 양식을 제거했습니다.

## [0.2.2] - 2026-07-12

### Changed

- 플러그인과 canonical 스킬 설명을 내부 구조보다 사용자가 얻는 결과가 먼저 보이도록 다시 썼습니다.
- bundle과 marketplace가 개별 스킬 목적을 재서술하지 않고 canonical 저장소로 안내하도록 설명 소유권을 정리했습니다.
- 개선 제안과 버그 양식에서 maintainer용 용어와 판단 항목을 제거했습니다.

## [0.2.1] - 2026-07-11

### Changed

- README와 plugin 카드에서 현재 스킬·저장소 개수를 중복해 적지 않도록 정리했습니다.
- Architecture, contribution guide와 GitHub 양식의 표현을 더 짧고 명확하게 다듬었습니다.

## [0.2.0] - 2026-07-11

### Changed

- 공개 설치 좌표를 publisher marketplace의 `project-legibility@perhapsspy`로 변경했습니다.
- Plugin 카드 설명과 starter prompt를 구체적인 사용 문장으로 다시 썼습니다.
- Project Legibility release와 publisher catalog의 검증·공개 절차를 분리했습니다.

### Removed

- 제품 저장소가 직접 소유하던 단일 plugin marketplace를 제거했습니다.

## [0.1.0] - 2026-07-11

### Added

- 독립적으로 관리되는 canonical 저장소의 스킬을 하나의 skills-only Codex plugin으로 배포했습니다.
- `project-context`와 `structure-first`를 중심으로 작업 재개와 코드 변경 흐름을 다루도록 구성했습니다.
- full commit SHA를 기록하는 `sources.lock.json`과 self-contained generated skill snapshot을 추가했습니다.
- local, remote와 offline source/snapshot 검증을 위한 sync workflow를 추가했습니다.
- 세 가지 project-level starter prompt와 marketplace metadata를 추가했습니다.
- 한국어·영어 README, architecture와 contribution guide를 추가했습니다.

### Scope

- v0.1에는 MCP server, app, hook, lifecycle automation과 umbrella skill이 없습니다.

[Unreleased]: https://github.com/perhapsspy/project-legibility/compare/v0.12.0...HEAD
[0.12.0]: https://github.com/perhapsspy/project-legibility/compare/v0.11.1...v0.12.0
[0.11.1]: https://github.com/perhapsspy/project-legibility/compare/v0.11.0...v0.11.1
[0.11.0]: https://github.com/perhapsspy/project-legibility/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/perhapsspy/project-legibility/compare/v0.9.3...v0.10.0
[0.9.3]: https://github.com/perhapsspy/project-legibility/compare/v0.9.2...v0.9.3
[0.8.0]: https://github.com/perhapsspy/project-legibility/compare/v0.7.3...v0.8.0
[0.7.0]: https://github.com/perhapsspy/project-legibility/compare/v0.6.9...v0.7.0
[0.6.9]: https://github.com/perhapsspy/project-legibility/compare/v0.6.8...v0.6.9
[0.6.8]: https://github.com/perhapsspy/project-legibility/compare/v0.6.7...v0.6.8
[0.6.7]: https://github.com/perhapsspy/project-legibility/compare/v0.6.6...v0.6.7
[0.6.6]: https://github.com/perhapsspy/project-legibility/compare/v0.6.5...v0.6.6
[0.6.5]: https://github.com/perhapsspy/project-legibility/compare/v0.6.4...v0.6.5
[0.6.4]: https://github.com/perhapsspy/project-legibility/compare/v0.6.3...v0.6.4
[0.6.3]: https://github.com/perhapsspy/project-legibility/compare/v0.6.2...v0.6.3
[0.6.2]: https://github.com/perhapsspy/project-legibility/compare/v0.6.1...v0.6.2
[0.6.1]: https://github.com/perhapsspy/project-legibility/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/perhapsspy/project-legibility/compare/v0.5.1...v0.6.0
[0.5.1]: https://github.com/perhapsspy/project-legibility/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/perhapsspy/project-legibility/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/perhapsspy/project-legibility/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/perhapsspy/project-legibility/compare/v0.3.2...v0.4.0
[0.3.2]: https://github.com/perhapsspy/project-legibility/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/perhapsspy/project-legibility/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.3.0
[0.2.5]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.5
[0.2.4]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.4
[0.2.3]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.3
[0.2.2]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.2
[0.2.1]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.1
[0.2.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.0
[0.1.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.1.0
