# 작업 기록

**2026-10-20**
- 정본 main 3403d274771ea26eb9e1fcfed181c034d29f54f6의 원격 readback 뒤 sync_skills.py update --source로 해당 source만 갱신했다. 새 스킬 경로·lock·notice와 제품 계약·README 한영 pair·catalog·선택/비선택 사례를 맞췄다. 생성 bundle을 직접 편집하지 않았다.
- Offline sync check, bundle validator, 단위 테스트 50개와 diff 공백 검사를 통과했다. 다른 source pin 유지와 정본·bundle 세 파일의 바이트 동일성을 확인했다. 정본은 push했고 bundle 통합은 로컬 main에 보존한다. Plugin release와 설치본 갱신은 후속 범위다.
- GitHub repository ID를 유지한 rename과 새 origin·설치 URL을 확인하고 정본 42157089eea8e488e8c0d739e9120637b3bbfcff를 고정해 재조립했다. 새 경로의 source 일치 검사, offline 검사, bundle validator와 단위 테스트 50개가 통과했으며 다른 7개 source는 유지했다. Codex 앱 등록은 이전 경로로 남아 있고 UI 도구의 명시적 접근 거부로 변경하지 못했다.
