# 이력 선택 문장 수정과 독립 사례 비교

2026-10-21, 제안한 영·한 문장 교체를 적용하고 A2 선행 경로와 독립 사례 한 쌍을 확인했다. **독립 사례에서는 수정 전후 모두 같은 결함을 발견·재현했다. 이번 비교에서 문장 교체의 추가 발견 효과는 입증되지 않았다.**

A2는 빈 상태에서 분리된 시작 상태까지 실제 관련 함수로 도달했다. 다만 기존 반례 후반부의 “ignored 응답 뒤 이전 accepted 패킷의 메타데이터가 다시 보임”은 외부 생산자의 지원 이력으로 입증되지 않았다. 이 두 결과를 구분한다.

## 스킬 반영

정본 `structure-first`의 `references/verification.md`와 한국어 pair에서 이력 선택 문장만 교체했다. 다른 표현은 유지하면서 한 표현만 갱신·초기화·누락시키는 실행 조건에서 이력을 도출하고, 그 관계가 소비 판단을 정당화하는지 확인하도록 했다.

- 수정 전: `5be8eafbb18747a19dcd3efc7927abbd5c0ed605`
- 수정 후: `4ecfc9f7e9f2025d9693862307da79fec1fd87a9`

정본 main에 push하고 원격 SHA를 확인했다. 정본 스킬 유효성 검사 후 `sync_skills.py update --source structure-first=<수정 후 commit>`으로 로컬 생성 bundle·lock·notices를 동기화했다. offline 검사·bundle 검증·저장소 unittest 57개가 통과했다. 미릴리스 변경이며 plugin version·tag·publisher pin·설치 cache는 이번 범위에 포함하지 않았다.

## A2 선행 경로

역사적 runtime 전체와 policy 파일을 원래 독립 리뷰의 실행 출력에서 복원해 기록된 해시와 대조했다. runtime SHA-256은 `6c84fe4a40e2e7bdf89fa569cabe0cc6a901b7e9151362412ac5430f4d22c877`, policy는 `7cf56a64b83e1642b7b4b0137efb039b735b06401620cf96da745133a4c5b75c`다.

컴파일용 harness는 원문의 `observeNTP` 함수와 record 선언을 기계적으로 추출하고 원문 policy를 그대로 사용했다. 추출한 함수 본문도 원문과 일치했다. host 상태 구조체는 기존 지원 snapshot에서 가져왔다. host 상태와 시간 관측을 fixture 경계로 두고, **record·policy 모두 영값에서 시작**했다. policy가 발행한 NTP inspect를 adapter에 통과시켜 완료 결과를 다시 Evaluate에 전달했다. 내부 baseline·accepted ID·fresh flag를 직접 설정하지 않았다.

| 시점 | 입력 | runtime 이력 | policy 현재 ID | baseline / fresh |
|---|---|---|---|---|
| 10초 | 정상 A, count=7 | A | A | A / false |
| 310초 | 정상 B, count=8 | B | B | A / true |
| 610초 | ignored C, count=9 | B | 없음 | A / true |
| 910초 | 메타데이터 조회 실패 | B | 없음 | A / false |

단일 daemon·boot, active unit, poll 2048초와 보존된 자동 NTP 복구 비허용 의도를 사용했다. 앞선 시계 관측은 Ahead로 두어 Agent clock 변경 없이 fallback에 머무르게 했다. 이 경로로 **생산자는 B를 기억하지만 policy의 현재 관측에는 ID가 없고 기준은 A인 상태**, 이어 확인 증거가 초기화되는 상태를 만들었다.

최종 `TestA2ReachablePrefix`의 세 사례가 통과했다. 첫 사례는 위 선행 경로에서 종료한다. 대조에서는 610초에도 B를 보이게 해 실패 시 baseline=B가 되고 이후 같은 B만으로 복귀하지 않음을 확인했다. 정상 대조에서는 실패 뒤 실제 새 D(count=10)를 공급하고 정상 시간 확인을 이어 `ntp_restored`가 됐다. 이는 실제 관련 함수의 합성 경로이며 전체 resident·실제 D-Bus·현장 실행은 아니다.

### 기존 반례 후반부에 대한 정정

초기 합성 실행에서는 ignored C 뒤 예전 B의 상태를 다시 주입하면 오복귀했다. 그러나 이 주입을 실제 daemon이 낼 수 있는 관측으로 취급해서는 안 된다. 확인한 [systemd v249 수신 처리](https://github.com/systemd/systemd/blob/v249/src/timesync/timesyncd-manager.c#L600)는 수신 시 packet count를 증가시키고 응답·목적 시각·ignored(spike) 값을 저장한다. [D-Bus 속성](https://github.com/systemd/systemd/blob/v249/src/timesync/timesyncd-bus.c#L146)은 그 현재 값을 내보낸다. 이 코드에서 C 이후 새 수신 없이 옛 B tuple이 복원된다는 근거를 확보하지 못했다.

따라서 **A2 시작 상태의 Go 경로 도달성은 확인했지만, 기존 오복귀 witness 전체의 외부 계약 도달성은 미확인**이다. 최종 선행 테스트는 옛 B를 되돌려 주는 후반부를 제거했다. v249는 외부 생산자 제약을 확인한 정본 사례이며, 실제 배포 버전이나 모든 지원 버전을 검증한 결과는 아니다. 과거 A2 미보고 점수는 잠근 합성 입력 기준의 기록으로 유지하되, 실제 지원 결함을 놓쳤다는 판정으로 확대하지 않는다. A1의 별도 재현 결과와도 구분한다.

## 독립 사례와 고정 조건

문구 설계에 쓰지 않은 기존 공개 사례인 Go `singleflight`를 선택했다. [2019년 이슈 #31420](https://github.com/golang/go/issues/31420)과 [upstream 수정](https://github.com/golang/sync/commit/56d357773e8497dfd526f0727e187720d1093757)이 선택 근거다. NTP 사례의 이름이나 도메인을 바꿔 만든 입력이 아니다.

소스는 수정 직전 `golang/sync` commit `e225da77a7e68af35c70ccbf71af2b83e6acac3c`의 `singleflight.go` 원문이다. 파일 SHA-256은 `8853de5a62b9ee4550dbbe1034bf935ea4819d79d70c33b0af0a743e4089261d`다. LICENSE를 보존하고 동일한 Go 1.25.0 module wrapper를 붙였다. 실제 실행 도구는 Go 1.27.2 darwin/arm64였다.

API 주석을 옮긴 계약과 동일 소스, 각 버전의 스킬 7개 파일을 제공했다. 전체 입력은 각각 11개이며 영·한 이력 선택 문장이 있는 두 파일만 달랐다. 원본 테스트·이슈 설명·수정본·평가자 witness는 worker 입력에서 제외했다. `Do`·`DoChan`·`Forget`의 정상 반환 계약을 검토하도록 했고 결함 개수·위치·이력·정답은 주지 않았다. panic·Goexit는 계약 밖으로 명시했다.

후보 문구와 평가 기준을 먼저 고정하고 버전을 중립 case 경로에 무작위 배치했다. worker는 각각 새 `gpt-6.1-sol/high`, `fork_turns=none`이며 요청문은 자기 경로 외에 동일했다. 한도는 각각 8분·exec 명령 25회, 실행은 각 한 번뿐이다. A2 선행 상태를 확인한 뒤 dispatch했다. 두 결과와 입력 해시를 고정한 뒤 매핑을 열어 채점했으며 후속 힌트·재위임·다른 사례 추가는 없었다.

평가자 사전 witness는 이전 실행 A → Forget → 대체 실행 B → A 완료 → B 진행 중 C 호출의 결과를 검사했다. 수정 전 소스에서는 C가 별도로 실행돼 실패했고, 공식 수정본에서는 같은 witness와 일반 중복 억제·합법적인 Forget 대조가 모두 통과했다. 이 자료는 worker에게 제공하지 않았다.

## 비교 결과

| 평가 | 수정 전 5be8eaf | 수정 후 4ecfc9f |
|---|---|---|
| 기존 독립 결함 발견 | 1/1, 직접 재현 | 1/1, 직접 재현 |
| 코드의 갱신·삭제 조건에서 이력 구성 | 수행 확인 | 수행 확인 |
| 공개 API로 이력 도달 | 확인 | 확인 |
| 일반 합류·정상 완료·Forget 허용 동작 | 대조 확인 | 대조 확인 |
| 추가 확정 결함 / 확인한 오탐 | 없음 / 없음 | 없음 / 없음 |
| 실행 명령 / 종료까지 | 12회 / 약 276초 | 13회 / 약 264초 |

양쪽 모두 기존 호출의 완료가 새 호출의 map 등록을 삭제하는 경로를 찾아, B가 여전히 실행 중인데 C가 별도 실행되는 것을 재현했다. mutex 직렬화와 현재 호출의 식별을 구분했고, Forget이 허용한 A/B 중첩을 결함으로 오인하지 않았다. A/B 진입 API 네 조합을 양쪽 모두 실행했으며, 수정 후 worker는 C의 Do 진입도 추가했다. 이 추가 subcase를 독립 결함 발견 점수로 세지 않는다.

worker 소스 복사본은 입력과 일치했다. 메인이 두 테스트 묶음을 `go test -race ./singleflight -v -count=1`로 재실행했다. 수정 전은 결함 재현 4개 subcase 실패·정상 test 2개 통과, 수정 후는 재현 5개 사례 실패·정상 3개 사례 통과였다. 실패는 기대한 잘못된 결과·별도 실행의 관측이며 timeout이나 race 진단 때문이 아니었다. 양쪽 race 보고는 없었고 전체 race 부재로 확대하지 않는다.

실행 기록에서 모델·effort·지정 참조 읽기·한도 준수를 확인했다. 기록된 명령에는 상대 case·평가자·기존 세션·메모리·upstream 조회 신호가 없었다. 이는 지시와 기록의 검사이며 OS 접근 격리는 아니다. 세션은 수정 전 `01a15d40-6964-7ab0-9fd0-aad334e49076`, 수정 후 `01a15d40-99cd-7ce2-8866-6cad0198b407`다.

**기존 문구에서도 같은 행동과 결함 발견이 나타났으므로 이번 교체의 추가 효용은 미입증**이다. 한 공개 사례·한 쌍뿐이며 모델의 사전 친숙도는 통제하지 못했다. 일반 발견률·문구의 인과 효과·작은 실행 시간 차이에 의미를 부여하지 않는다. 결과를 보고 문구나 사례를 다시 고르지 않고 종료했다. 검토한 임시 입력·테스트·원시 출력은 정리하며 실행 근거는 원래 Codex 세션에 보존한다.
