# 스킬 & 플러그인

[English](skills-plugins.md) | **한국어**

스킬, 플러그인, 서브에이전트, 훅, 그리고 이것들을 배포하는 마켓플레이스 모음. 스킬(SKILL.md)은 개방형 [Agent Skills](https://agentskills.io) 표준을 따르므로 Claude Code뿐 아니라 Codex, Gemini CLI 등 지원하는 어떤 도구에서도 쓸 수 있습니다. Claude Code 전용 항목(훅, 상태 줄 등)은 설명에 표시했습니다.

**섹션:** [공식](#공식) · [스킬](#스킬) · [플러그인 & 마켓플레이스](#플러그인--마켓플레이스) · [서브에이전트](#서브에이전트) · [훅 & 기타](#훅--기타) · [보조 도구](#보조-도구) · [에디터 연동](#에디터-연동) · [설정 & 프레임워크](#설정--프레임워크) · [가이드 & 모음](#가이드--모음)

## 공식

- **[claude-code](https://github.com/anthropics/claude-code)** — Claude Code 공식 저장소. 공식 plugin-dev 플러그인 포함.
- **[skills](https://github.com/anthropics/skills)** — Anthropic 공식 Agent Skills 저장소: 문서 편집, 아트, MCP 서버 제작 등 예제 스킬.
- **[claude-plugins-community](https://github.com/anthropics/claude-plugins-community)** — Anthropic이 관리하는 커뮤니티 플러그인 마켓플레이스 카탈로그.
- **[공식 문서: Skills](https://code.claude.com/docs/en/skills)** — 스킬 작성·관리·공유.
- **[공식 문서: Plugins](https://code.claude.com/docs/en/plugins)** — 플러그인 제작과 마켓플레이스 배포.
- **[공식 문서: Subagents](https://code.claude.com/docs/en/sub-agents)** — 커스텀 서브에이전트 정의와 컨텍스트 관리.
- **[공식 문서: Hooks](https://code.claude.com/docs/en/hooks)** — 훅 이벤트, 설정, JSON 입출력 형식.
- **[공식 문서: MCP](https://code.claude.com/docs/en/mcp)** — MCP 서버로 외부 도구 연결.
- **[Agent Skills](https://agentskills.io)** — 개방형 Agent Skills 명세 사이트.

## 스킬

- **[awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)** — 직접 선별한 Claude 스킬·리소스·도구 큐레이션 리스트.
- **[superpowers](https://github.com/obra/superpowers)** — TDD, 브레인스토밍, 디버깅 등 조합 가능한 스킬 기반 에이전트 개발 방법론 플러그인.
- **[superpowers-marketplace](https://github.com/obra/superpowers-marketplace)** — Superpowers 계열 플러그인을 배포하는 마켓플레이스.
- **[claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** — 공식·커뮤니티 Claude 스킬 모음.

## 플러그인 & 마켓플레이스

- **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** — 슬래시 명령, 서브에이전트, MCP, 훅을 아우르는 플러그인 리스트.
- **[awesome-claude-plugins](https://github.com/composio-community/awesome-claude-plugins)** — 플러그인 시스템으로 Claude Code를 확장하는 플러그인 큐레이션.
- **[claude-code-templates](https://github.com/davila7/claude-code-templates)** — 에이전트·명령·훅·MCP 등 400+ 컴포넌트를 설치하는 CLI (aitmpl.com).
- **[AITmpl](https://www.aitmpl.com/plugins/)** — claude-code-templates의 웹 브라우저. 플러그인·마켓플레이스 디렉토리.
- **[SkillsMP](https://skillsmp.com/)** — GitHub의 Claude/Codex 스킬을 AI 검색으로 찾는 대형 스킬 마켓플레이스.
- **[Claude Marketplaces](https://claudemarketplaces.com/)** — 플러그인·스킬·MCP 서버 마켓플레이스들의 디렉토리.
- **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** — 471개 플러그인, 3,000+ 스킬의 오픈소스 마켓플레이스 (tonsofskills.com).
- **[Subagents.sh](https://subagents.sh/)** — 다운로드 순으로 정렬된 서브에이전트 탐색·설치 디렉토리.
- **[SkillsClaude](https://skillsclaude.org/skills)** — 카테고리·신뢰 등급·태그로 거르는 7,200+ Claude 스킬 디렉토리.
- **[Claude Skills Hub](https://claudeskills.info/)** — 42,000+ SKILL.md 파일을 인덱싱한 서드파티 마켓플레이스.
- **[Agent Skill Club](https://www.agentskill.club/)** — 카테고리별 3,600+ 오픈소스 Claude 스킬 무료 라이브러리.
- **[Claude Plugins](https://claude-plugins.dev/)** — 다운로드 수와 설치 명령을 제공하는 커뮤니티 플러그인 마켓플레이스.
- **[Awesome Claude](https://awesomeclaude.ai/)** — Claude 도구·스킬·연동·학습 리소스 종합 디렉토리.

## 서브에이전트

- **[agents](https://github.com/wshobson/agents)** (38k★) — 200+ 에이전트와 175개 스킬의 프로덕션급 멀티 하네스 마켓플레이스.
- **[awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)** — 개발 전 영역을 다루는 100+ 전문 서브에이전트.
- **[claude-code-sub-agents](https://github.com/lst97/claude-code-sub-agents)** — 풀스택 개발에 특화된 서브에이전트 모음.

## 훅 & 기타

- **[claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery)** — 훅으로 Claude Code 동작을 제어하는 실습 예제 저장소.
- **[awesome-claude-code-hooks](https://github.com/ithiria894/awesome-claude-code-hooks)** — 비용 추적, 보안 검사, 파일 정리 등 이벤트 기반 훅 모음.
- **[claude-code-hooks](https://github.com/karanb192/claude-code-hooks)** — 안전·비용·관측 훅 모음. 명령 한 줄로 설치되는 마켓플레이스 겸용.
- **[awesome-claude-code (hesreallyhim)](https://github.com/hesreallyhim/awesome-claude-code)** — 스킬·훅·에이전트·플러그인을 아우르는 대표 awesome 리스트.
- **[awesome-claude-code (jqueryscript)](https://github.com/jqueryscript/awesome-claude-code)** — IDE 연동, 프레임워크 등 개발 도구 중심 리소스 리스트.
- **[awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit)** — 135개 에이전트, 176개 플러그인, 20개 훅을 모은 툴킷.

## 보조 도구

- **[ccusage](https://github.com/ryoppippi/ccusage)** — 로컬 JSONL로 Claude Code 토큰 사용량·비용을 분석하는 인기 CLI.
- **[Claude Code Usage Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor)** — 실시간 사용량 추적, 한도 예측, 알림.
- **[ccstatusline](https://github.com/sirmalloc/ccstatusline)** — powerline 지원과 테마를 갖춘 커스터마이징 상태 줄.
- **[claude-powerline](https://github.com/Owloops/claude-powerline)** — 실시간 사용량과 git 정보를 보여주는 Vim powerline 스타일 상태 줄.
- **[CCometixLine](https://github.com/Haleclipse/CCometixLine)** — 모델·git·컨텍스트 윈도 정보를 표시하는 Rust 상태 줄.
- **[opcode](https://github.com/winfunc/opcode)** (22k★) — 커스텀 에이전트 생성과 세션 관리를 지원하는 데스크톱 GUI (구 Claudia).
- **[claude-squad](https://github.com/smtg-ai/claude-squad)** — 여러 AI 에이전트(Claude Code, Codex 등)를 격리 작업공간에서 병렬 관리하는 TUI.
- **[Claude Code UI](https://github.com/siteboon/claudecodeui)** — 모바일·웹에서 Claude Code 세션을 원격 관리하는 웹 GUI.
- **[claude-code-webui](https://github.com/sugyan/claude-code-webui)** — 스트리밍 채팅을 지원하는 경량 Claude CLI 웹 인터페이스.
- **[claude-code-router](https://github.com/musistudio/claude-code-router)** (26k★) — Claude Code 요청을 로컬 모델 등 다른 모델로 라우팅.
- **[claude-code-otel](https://github.com/ColeMurray/claude-code-otel)** — OpenTelemetry·Prometheus·Grafana 기반 사용량·비용 관측 스택.
- **[claude_telemetry](https://github.com/TechNickAI/claude_telemetry)** — 도구 호출·토큰·비용을 Logfire, Sentry, Datadog 등으로 보내는 OTel 래퍼.
- **[ccdashboard](https://github.com/NikiforovAll/ccdashboard)** — Claude Code 텔레메트리용 Grafana/Aspire 대시보드 관리 CLI.

## 에디터 연동

- **[claudecode.nvim](https://github.com/coder/claudecode.nvim)** — WebSocket MCP 프로토콜을 완전 구현한 Coder의 Neovim IDE 확장.
- **[claude-code.nvim](https://github.com/greggh/claude-code.nvim)** — 터미널 토글과 수정 파일 자동 리로드를 지원하는 Neovim 연동.
- **[claude-code-ide.el](https://github.com/manzaltu/claude-code-ide.el)** — MCP 기반 양방향 브리지로 Emacs 기능을 연결하는 IDE 연동.
- **[claude-code.el](https://github.com/stevemolitor/claude-code.el)** — Emacs에서 Claude Code CLI를 쓰는 인터페이스 패키지.

## 설정 & 프레임워크

- **[SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)** — 전문 명령·인지 페르소나·개발 방법론을 더하는 설정 프레임워크.
- **[my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)** — CLAUDE.md 메모리 뱅크 시스템을 포함한 스타터 템플릿.
- **[cc-sessions](https://github.com/GWUDCAP/cc-sessions)** — 계획 승인 전까지 코드 수정을 차단하는 워크플로 강제 확장.
- **[ruflo](https://github.com/ruvnet/ruflo)** (59k★) — 멀티 에이전트 스웜 오케스트레이션 메타 하네스 (구 claude-flow).
- **[Claude Task Master](https://github.com/eyaltoledano/claude-task-master)** (27k★) — PRD를 실행 가능한 개발 태스크로 자동 분해하는 AI 태스크 관리.
- **[Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin)** (21k★) — Every의 계획-구현-리뷰-학습 루프 공식 플러그인: 37 스킬, 51 에이전트.

## 가이드 & 모음

- **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** — 설치부터 명령·워크플로·에이전트·스킬까지 다루는 입문~고급 가이드.
- **[claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide)** — 에이전트 팀 워크플로 등 실전 패턴을 정리한 종합 가이드.
- **[awesome-claude-agents](https://github.com/vijaythecoder/awesome-claude-agents)** — 기술 스택을 자동 감지해 전문 서브에이전트 팀을 구성하는 오케스트레이션 모음.
- **[claude-code-subagents](https://github.com/0xfurai/claude-code-subagents)** — 프로그래밍 도메인·프레임워크별 100+ 서브에이전트.
- **[ClaudeLog](https://claudelog.com/)** — Claude Code 동작 원리·설정·생태계 도구를 깊이 다루는 커뮤니티 지식 베이스.

---

**함께 보기:** [전체 카탈로그 (10,000+ 저장소)](../catalog/skills-plugins.md) · [크로스 툴 스킬 레지스트리](directories.ko.md#스킬--에이전트-레지스트리-크로스-툴) · [지금 뜨는 플러그인·스킬](trending.ko.md#플러그인--스킬)
