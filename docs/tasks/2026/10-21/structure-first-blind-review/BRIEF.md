# Structure First 리뷰 행동 개선

목표는 새 리뷰 에이전트가 수정 스킬과 원래 코드·계약을 받아, 부모의 추가 호출이나 재검토 지시 없이 세 결함을 발견하고 해당 관계를 재현하는 것이다. 사용자는 실패 보고에서 멈추지 말고 피드백 → Pro 상담 → 스킬 개선 → 같은 조건의 실험을 계속하도록 요청했다.

후보26의 첫 실행과 같은 고정본의 새 확인이 모두 세 결함과 원래 판단·전달 관계를 재현했다. 각각 642.938초·exec26회, 639.522초·exec29회이며 중간 개입은 각각0회다. 두 실행 모두 목표 기준과 이전 강화 기준을 통과해 채택했다. 발견과 실제 실행 범위는 [최종 자율 확인](working/AUTONOMOUS-RESULTS.md)에 구분했다.

Pro26 제안으로 초기 조사와 후반 질문 선택 절을 교체했다. 결과를 허용하는 값의 실제 생산 근거와 소비자가 전제하는 의미를 비교해, 기존 미결 목록에 없던 질문도 만든다. 보존 오류의 독립 수명과 소비 대조는 같은 조사 안에 유지한다. 새로운 단계·전수 목록·정답 힌트는 넣지 않았다. 정확한 연구 전후 문구는 [변경 설명](working/CHANGE-EXPLANATION.md), 실패와 제안의 근거는 [개선 루프](working/IMPROVEMENT-LOOP.md)가 소유한다.

조건은 복원 소스 95파일, 전체 계약 48줄, 후보별 고정 스킬, 같은 일반 TASK, 새 Sol high/fork none, 전체 720초·exec 40회다. 정답·개수·위치·이전 결과·부모 맥락을 주지 않고 한 번만 위임한다. 메인은 종료 전 시간·호출 등 metadata만 관측하고, 종료 후 입력·구현·산출물을 동결해 발견과 실제 검증 범위를 따로 판정한다. 첫 목표 통과 뒤 같은 고정본으로 새 확인 한 번을 수행하며 모든 실패를 보존한다.

후보17 전에 고정한 목표 기준은 세 결함의 명시적 발견, 논쟁 중인 원래 판단·전달 경로 실행, 지원 전제와 검증 범위 구분이다. 이전 강화 기준은 B의 raw Date → 수동 보정 실행도 요구한다. 두 기준을 나란히 보고하고 과거 실패를 새 기준으로 성공으로 바꾸지 않는다. A2는 전체 외부 이력의 도달성 미검증으로 제외했다. C는 유효한 저장 owner 오류 → 공개 reader의 관계가 필요하며 coordinator 오류 생성 전체 E2E를 추가로 요구하지 않는다. 서로 다른 시험의 증거를 합쳐 같은 관계 재현으로 세지 않는다.

코드는 복원본이다. 주요 코어는 당시 기록과 byte 단위로 맞췄지만 지원 파일은 후속 보존 snapshot에서 가져왔으므로 당시 전체 checkout의 완전한 복제를 주장하지 않는다. 안전한 로컬 fixture에서 확인했고 Linux/systemd·실제 TLS·NTP 수신·시계 변경·현장 binary는 미검증이다. 알려진 사례로 조정한 국소 수용이며 일반 발견률이나 특정 문구의 인과효과를 입증하지 않는다.

정본 `e77bee1a09ce2328536d3f2e426732bb249ec43c`를 포함한 [Project Legibility 0.17.2](https://github.com/perhapsspy/project-legibility/releases/tag/v0.17.2)를 게시했다. 릴리스 commit은 `81629dff031b4cec511be2d9a9b647694f016b6d`, publisher commit은 `cd77f999d5bb288025e029e2453bf1c74d726334`다. main CI·같은 SHA의 tag/Release·양쪽 marketplace pin/CI·원격 manifest를 확인했다. Bundle/lock과 저장소 57개·catalog 17개 테스트도 통과했다.

| 적용 대상 | 실제 확인 결과 |
|---|---|
| Mac Codex | 공식 marketplace upgrade/add로 0.17.2 설치·활성화. 게시본 41파일 byte 일치, 기존 plugin 설정 15항목 보존, 새 app-server의 forceReload 발견에서 9스킬 모두 0.17.2/enabled. |
| Claude Code 공개 설치 | 임시 격리 CLI 2.1.304에서 공개 marketplace 등록·0.17.2 설치·9스킬 inventory 확인. Mac의 전역 Claude 설치나 모델 행동 동등성 검증은 아니다. |
| dot cloud Codex | 현재 도구·브라우저·SSH 설정에 지원 실행 경로가 없어 미반영. Mac 실행을 dot 적용으로 세지 않는다. |
| Windows | 사용자가 별도로 싱크하겠다고 답했으므로 사용자 수동 반영 대상이다. |

Windows의 플러그인 갱신은 공식 CLI `codex plugin marketplace upgrade perhapsspy`와 `codex plugin add project-legibility@perhapsspy`를 순서대로 실행하고, 각 단계 실패 시 중단한다. `codex plugin list --marketplace perhapsspy --json`에서 0.17.2·installed/enabled를 확인한다.

새 실행의 발견 확인은 설치된 스킬의 등록·활성 증거다. 실행 중인 이 대화에 이미 전달된 지침을 다시 로딩했거나 실제 Mac GUI를 확인했다는 주장은 하지 않는다. Mac 화면 잠금으로 native UI 확인은 수행하지 않았다. 이전 자율 실험과 이번 설치 확인의 역할을 구분한다.

실험·설치 검증의 소유 임시 자료는 결과 보존 뒤 정리하며, 기존 보존 소스·native 기록·상담 증거 이미지는 유지한다. 게시·적용 상세 근거는 logs/WORKLOG.md가 소유한다.

이전 단계의 근거는 해당 owner에 보존한다.

- [기존 방식과 제안 방식 비교](working/REVIEW-METHOD-COMPARISON.md), [접근 재검토](working/APPROACH-REVIEW.md): 이번 자율 개선 전의 비교와 원인 가설.
- [평가 정정과 복원](working/FOLLOWUP-PROPOSAL.md): A2 제외와 기존 기준.
- [구·신 버전 비교](working/COMPARISON.md), [지정 진단](working/EVIDENCE-DIAGNOSTIC.md), [독립 비교](working/TRANSFER-COMPARISON.md), [복원 반복](working/RESTORED-REPEAT.md), [선행 리뷰](working/RESULTS.md): 각 단계의 발견과 실행 범위.
