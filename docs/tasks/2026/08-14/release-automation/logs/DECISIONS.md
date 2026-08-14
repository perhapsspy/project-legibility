**2026-08-14**
- 0.8.1은 원격 CI보다 local route 선택과 검증·catalog handoff·사후 기록에 더 많은 시간을 썼고, 이전 prose-only 개선이 같은 실패를 막지 못했다.
- 릴리스 정본을 exact canonical SHA에서 한 번 만든 Project Legibility candidate와 그 SHA를 고정한 catalog candidate로 정의하고, exact-SHA CI를 병렬 통과한 commit만 main·tag·catalog로 승격한다.
- ChatGPT Pro 자문과 로컬 workflow 분석 모두 중복 local/main/tag 검증보다 build-once·single observer·resume 가능한 promotion이 수동 지연과 재실행을 함께 제거한다고 판단했다.
- scoped remote update, release-candidates CI, journaled start/resume/status/abort와 짧은 runbook이 실행 계약을 소유하며 post-release task commit은 완료 gate에서 제외한다.

**2026-08-14**
- 독립 단순성 감사에서 실제 지연은 수동 준비 5분 17초와 사후 기록 87초였고, hosted workflow 약 46초는 주 병목이 아니었음이 확인됐다.
- release-candidates ref, 두 저장소 candidate 병렬화, journal 기반 start·resume·status·abort, 동일 SHA CI 재사용을 제거하고 준비된 release commit을 외부 공개 상태로 재개하는 publish 한 명령으로 축소한다.
- candidate 체계는 약 8~19초를 줄이는 대신 약 800줄의 orchestration과 경합·재개 상태를 추가해, 해결하려던 사람 대기보다 운영 복잡성과 배포 위험을 더 크게 만들었다.
- scoped remote source update와 세 불변 gate—canonical source provenance, tag 전 Project Legibility main CI, catalog pin 후 catalog CI—만 유지한다. 같은 publish 명령의 재실행이 remote main·tag·Release·catalog pin을 읽어 이어가며 별도 journal은 두지 않는다.
