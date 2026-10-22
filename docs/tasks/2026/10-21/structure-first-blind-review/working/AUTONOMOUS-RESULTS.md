# 스킬만 준 자율 리뷰의 최종 확인

후보26의 첫 실행과 문구를 바꾸지 않은 새 확인 실행이 모두 세 결함을 발견하고 해당 원래 판단·전달 관계를 재현했다. 부모는 각 에이전트에 최초 일반 요청 한 번만 보냈다. 중간 호출·힌트·재검토 지시는 없었다. 정본 `e77bee1a09ce2328536d3f2e426732bb249ec43c`를 main에 push하고 원격 SHA를 다시 확인했다.

## 같은 조건과 실제 비용

두 실행은 새 `gpt-6.1-sol/high`, `fork_turns=none`, 전체 720초·exec 40회다. 입력은 같은 복원 소스 95파일, 전체 계약 48줄, 고정 스킬 11파일, 일반 TASK다. 두 입력 manifest의 모든 상대 경로와 hash가 같았다. TASK SHA256은 `956a927915f2a46ec45af4d248b3ffb223338d0ea39b66cc26b731dbce41ca07`이다. 정답·개수·결함 위치·이전 결과·부모 대화를 주지 않았다.

| 실행 | 시간 | exec | 후반 지침 최초 읽기 | 부모 후속 | 발견/관계 실행 | 판정 |
|---|---:|---:|---|---:|---|---|
| 첫 실행 | 642.938초 | 26 | 324.110초·18회째 | 0 | 3/3, 아래 범위 | 목표·이전 강화 기준 PASS |
| 같은 고정본 새 확인 | 639.522초 | 29 | 294.944초·17회째 | 0 | 3/3, 아래 범위 | 목표·이전 강화 기준 PASS |

Native 실행 ID는 각각 `01a16354-f0b0-7542-99f6-7491e0916e01`, `01a16360-4490-7dc1-a8b4-dd18ac55ff9b`다. 입력·원래 구현·동결 산출물 불변, 720초 이후 exec 0회, 제한 자료 경로 신호 없음, 웹·브라우저·자식 위임 없음, 지정 모델·effort를 확인했다. 이는 실제 도구 호출과 경로 감사이며 OS 수준 sandbox를 증명하는 것은 아니다.

확인 보고서는 전환을45%라고 썼지만 실제 후반 읽기는17/40회, 약42.5%로 한 호출 빨랐다. 정확한45% 전환 준수는 입증하지 않는다. 자율 전환·추가 조사·통합은 수행됐으며, 판정은 사전 고정한 세 관계·원래720초/40회·부모후속0 기준이다.

## 발견과 실제 실행 범위

| 결함 | 첫 실행 | 같은 고정본 새 확인 |
|---|---|---|
| A1: 복구 이전 NTP 응답을 뒤늦게 알아 새 수신으로 오인 | typed host packet metadata → 원래 observeNTP → Evaluate. A 검사600초·B 수신630초·복구660초·정상660/960초를 고정하고 B를645초에 미리 검사하는 이력만 바꿨다. 늦은 첫 발견은 fresh/ntp_restored, 미리 안 대조는 fallback이었다. | 같은 원래 변환/정책 경로. A 검사1초·B 수신100초·복구200초·늦은 검사201초·정상201/501초와 미리 안 대조. 원천 수신 사건은 고정했고 파생 fresh/baseline/state를 주입하지 않았다. |
| B: 수동 보정의 전체 불확실성 안전 구간 누락 | 관측 호출마다 새 응답 객체의 IMF Date/RTT0을 원래 header parser로 해석했다. 같은 Date여도 parser를 두 번 실행했으며, 파생 관측 하나를 재생한 것이 아니다. 5.5±1초에서 원래 manual setter1회, automatic0회. | 서로 다른 순차 HTTP200·Date·RTT1초를 원래 response parser에 넣어6±2초를 만들었다. 원래 manual setter1회, automatic0회. |
| C: 관리 정보 읽기 실패가 유효한 저장 owner 오류·횟수·기한을 숨김 | 실제 coordinator 정상 시작 뒤 management를 손상시켜 원래 writer가 오류/count1/비영 retry≈160초를 저장했다. 같은 기록·소유·boot에서 management만 정상 복원해 public reader의 ok/nilhealth와 retrying/같은 count·deadline을 비교했다. | owner 오류/count3/retry42분과 같은 boot·유효 marker/hash·reference를 가진 표시용 저장 seed를 사용했다. 정상 paused management는 retrying/health, management JSON만 손상시키면 ok/nilhealth. 오류 생산과 seed 전체의 생성 이력은 실행하지 않았다. |

C의 생성 과정은 쟁점이 아니므로 지원 seed를 허용한다는 기존 기준을 적용했다. 두 번째 실행이 원래 오류 writer까지 실행했다고 합치지 않는다. 각 실행은 자기 기록을 같은 reader로 비교했으며 서로 다른 실행의 producer/consumer를 이어 붙여 재현으로 세지 않았다.

B의 공개 dispatcher는 두 실행 모두 소스 추적이며 직접 실행은 timeSyncRun부터다. A1의 실제 systemctl/busctl packet 생산·파싱은 해당 이력 시험에 포함하지 않았다. 별도 D-Bus 실패→unit 사실 보존 시험을 A의 전체 raw-host 경로 실행으로 합치지 않는다. 두 실행 모두 source facts와 실행되는 핵심 해석·판단을 구분했다.

## 자기 절차 수행과 검증

초기 질문에 관측 생산 근거와 소비 의미의 차이가 생겼고, 수신 사건을 고정한 지식 이력 대조로 판별했다. 후반에는 기존 발견의 확장 외에도 D-Bus metadata 실패 시 별도로 검증된 unit 정보 보존이라는 다른 관계를 선택해 실행하고 정상으로 판정했다. 첫 실행은 policy까지, 확인 실행은 host reader→observeNTP까지다. 단순 단계 이름이나 발견 개수로 절차 수행을 대신하지 않았다.

첫 실행의 새 시험7개가 든410줄 파일, 확인 실행의 새 시험6개가 든205줄 파일을 메인이 전체 읽었다. 첫 실행은 focused 전체 package와 race 검사, 확인 실행은 전체 Go 검사를 마쳤다. 메인의 독립 `go test ./... -count=1`도 양쪽 모두 통과했다. Characterization assertion의 PASS는 결함이 예상대로 재현됐다는 뜻이다. 초기 cwd/Date 형식/backoff·pending fixture 전제 실패는 각 보고와 실행 기록에 보존했고, 수정 후 실제 실행본만 인정했다.

## 채택·반영과 한계

정본 한·영8파일을 commit/push한 뒤 정식 sync 도구로 bundle과 lock을 맞췄다. Skill frontmatter·상대 링크·whitespace 검사, bundle offline check, bundle validator, repo unittest57개가 통과했다. 게시 SHA·최종 검사 결과·임시 자료 정리는 [BRIEF](../BRIEF.md)에 있다. 자율 검증 뒤 승인된0.17.2배포·적용상태는 [BRIEF](../BRIEF.md)가 소유한다.

코드는 복원본이며 주요 코어는 당시 기록과 byte 단위로 맞췄지만 지원 파일은 후속 보존 snapshot이다. 당시 전체 checkout의 완전한 복제나 현재 제품 결함 여부를 주장하지 않는다. 실제 TLS·NTP 수신·clock syscall·Linux systemd/netlink·현장 binary·배포·장기 재시작 전체는 미검증이다. Seed의 모든 필드 결합이나 원래 생산 이력까지 검증한 것은 아니다.

후보9~25의 실패, 후보20의 capacity 중단, 후보21의 첫 목표 PASS 후 같은본 확인 실패를 [개선 루프](IMPROVEMENT-LOOP.md)에 보존했다. 실패 후보의 성과를 합쳐 성공으로 만들지 않았다. 알려진 복원 사례를 보며 문구를 조정한 개발 결과이므로 일반 발견률·항상 성공·특정 한 문장의 인과효과는 입증하지 않는다. 정확한 연구 전후 문구는 [변경 설명](CHANGE-EXPLANATION.md)에 있다.
