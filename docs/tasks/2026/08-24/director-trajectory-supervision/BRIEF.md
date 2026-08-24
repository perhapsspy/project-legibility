# 디렉터 작업 궤적 감독

## 목표

- `codex-project-director`가 작업 결과뿐 아니라 worker의 진행 경로가 현재 Goal에 계속 비례하고 직접적인지도 감독하게 한다.
- 상시 polling이나 구현 review 관료제를 만들지 않고, drift 신호에서만 독립적인 읽기 전용 trajectory review를 사용한다.

## 범위

- `codex-project-director` 정본의 한영 스킬 계약과 필요한 검증을 갱신한다.
- Project Legibility 제품 계약, source lock, generated bundle, 한영 changelog와 patch release 경계를 갱신한다.
- publisher marketplace는 push된 Project Legibility release commit만 고정한다.

## 현재 사실

- 현재 디렉터는 사건 기반 scheduler와 독립 반증을 지원하지만 worker의 진행 방식에 대한 별도 drift 감지는 명시하지 않는다.
- trajectory reviewer는 구현 정합성 reviewer가 아니라 원래 packet, acceptance frontier와 최근 진행을 바탕으로 경로의 비례성·직접성만 판단해야 한다.
- `CONTINUE`는 무개입, `STEER`는 결과·우선순위 교정, `STOP_AND_REPLAN`은 반복·범위 확장·교착의 재계획, `ESCALATE`는 governing 결정을 요구한다.

## 현재 상태

- 제품 수준 역할 변경을 `docs/PRODUCT.md`와 `docs/PRODUCT.en.md`에 먼저 반영했다.
- Director 정본 `d8325758441953f436adbef7ab736ba685f0c30d`을 공개 `main`에 게시하고 source lock·generated bundle·출처 고지에 동기화했다.
- Project Legibility 0.9.3 manifest와 한영 changelog를 준비했으며 offline source check, 기본·release-tag bundle 검증과 52개 단위 검사가 통과했다.

## 다음 행동

- Project Legibility release commit을 만들고 `v0.9.3` release와 publisher catalog pin·CI까지 게시한다.

## 작업 경계

- `<codex-project-director-root>/skills/codex-project-director/`
- `docs/PRODUCT*.md`
- `plugins/project-legibility/`
- `CHANGELOG*.md`
- `docs/tasks/2026/08-24/director-trajectory-supervision/`
- `<codex-plugins-root>`의 Project Legibility source pin
