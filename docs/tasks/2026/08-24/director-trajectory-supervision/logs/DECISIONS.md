**2026-08-24**
- worker drift는 별도 상시 supervisor가 아니라 기존 Director가 필요할 때 호출하는 독립 trajectory reviewer로 다룬다.
- 시간 간격만으로 review를 반복하지 않고, 반복·범위 확장·acceptance frontier 정체 같은 사건 신호에서만 제한된 읽기 전용 review를 사용한다.
- review는 구현 정합성이나 새 검증 범위를 결정하지 않고 진행 경로의 비례성·직접성만 평가하며, 최종 scheduling 책임은 Director에 남는다.
- 정상 진행에서는 침묵하고 개입이 유용할 때만 기존 owner에게 좁은 steering 또는 재계획·결정 요청을 전달한다.

**2026-08-24**
- 이번 변경은 Director의 기존 명시 호출과 여러 작업 지휘 역할 안에서 worker drift를 줄이는 실행 guardrail이다.
- Project Legibility 0.9.3 patch release로 게시한다.
- 새 skill·trigger·자동 참여·외부 권한을 만들지 않고 현재 역할의 사건 기반 감독 품질만 호환 가능하게 보강하기 때문이다.
- 제품 계약에는 내부 trajectory review 역할을 명시하되 routing fixture와 invocation policy는 유지한다.
