# 결정 기록

**2026-07-11**
- 기존 저장소가 제품, marketplace와 plugin 식별자를 모두 project-legibility로 소유해 두 번째 플러그인부터 배포자 namespace가 제품명에 묶인다.
- Project Legibility 저장소는 제품 bundle과 release만 소유하고, 새 perhapsspy/codex-plugins 저장소가 marketplace perhapsspy를 소유한다.
- 제품별 source와 release를 독립적으로 유지하면서 marketplace를 한 번만 등록해 앞으로의 플러그인을 설치할 수 있다.
- 기존 project-legibility marketplace는 main에서 제거하고 설치 좌표를 project-legibility@perhapsspy로 완전히 교체한다.
