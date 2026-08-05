# AI CLI 도구 & 에디터

[English](ai-cli-tools.md) | **한국어**

Claude Code 외의 AI 코딩 CLI 에이전트, AI 에디터·IDE, 그리고 각 도구의 확장·규칙 생태계 모음.

**섹션:** [CLI 에이전트](#cli-에이전트) · [AI 에디터 & IDE](#ai-에디터--ide) · [병렬 에이전트 매니저](#병렬-에이전트-매니저) · [도구별 확장 & 규칙 생태계](#도구별-확장--규칙-생태계)

## CLI 에이전트

- **[OpenAI Codex CLI](https://github.com/openai/codex)** — OpenAI의 오픈소스 터미널 코딩 에이전트. 샌드박스 실행과 안전성 중심.
- **[GitHub Copilot CLI](https://github.com/github/copilot-cli)** — Copilot 코딩 에이전트를 터미널로 가져온 GitHub 공식 CLI (2026년 2월 GA).
- **[Antigravity CLI](https://antigravity.google/docs/cli/overview)** — Gemini CLI를 대체한 Google의 Go 기반 터미널 에이전트(`agy`). 멀티 에이전트 백그라운드 워크플로 지원.
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** — Google의 오픈소스 터미널 AI 에이전트 (레거시). 유료 API 키와 Code Assist에서 여전히 사용 가능.
- **[Aider](https://aider.chat)** — 커뮤니티 오픈소스 터미널 페어 프로그래밍 도구. git 통합과 폭넓은 LLM 지원.
- **[OpenCode](https://github.com/sst/opencode)** (160k★) — 최대 규모 오픈소스 CLI 코딩 에이전트. 세련된 TUI와 폭넓은 프로바이더 지원.
- **[Amp](https://ampcode.com)** — Sourcegraph의 에이전트 코딩 도구. CLI와 VS Code 계열 에디터에서 동작, 스레드 공유.
- **[Crush](https://github.com/charmbracelet/crush)** — Charm의 화려한 TUI 코딩 에이전트. OpenAI, Anthropic, Google 등 지원.
- **[Goose](https://github.com/block/goose)** — Block(Square)의 오픈소스 로컬 AI 에이전트. 확장 가능한 아키텍처.
- **[Qwen Code](https://github.com/QwenLM/qwen-code)** — 알리바바 Qwen 팀의 CLI 코딩 에이전트. Qwen-Coder 모델에 최적화.
- **[grok-build](https://github.com/xai-org/grok-build)** (24k★) — SpaceXAI의 코딩 에이전트 하네스·TUI: 풀스크린, 마우스 인터랙션, 확장 가능.

## AI 에디터 & IDE

- **[Cursor](https://cursor.com)** — VS Code 포크 기반 대표 AI 네이티브 에디터: 에이전트 모드, 규칙(.cursorrules), MCP 지원.
- **[Windsurf](https://windsurf.com)** — Cognition(Devin 제작사)이 인수한 AI IDE. Cascade 에이전트와 제로 데이터 보존 설계.
- **[Zed](https://zed.dev)** — Rust로 작성된 초고속 협업 에디터. 내장 에이전트 패널과 외부 에이전트(ACP) 연동.
- **[Cline](https://github.com/cline/cline)** — VS Code용 오픈소스 자율 코딩 에이전트: plan/act 모드, 브라우저 자동화.
- **[Roo Code](https://github.com/RooCodeInc/Roo-Code)** — Cline에서 포크된 VS Code 에이전트. 커스텀 Modes와 멀티 에이전트 워크플로.
- **[Kilo Code](https://kilocode.ai)** — Cline과 Roo Code의 장점을 결합한 오픈소스 VS Code 에이전트.
- **[Continue](https://continue.dev)** — VS Code·JetBrains용 오픈소스 AI 어시스턴트. 커스텀 모델·규칙으로 확장.

## 병렬 에이전트 매니저

여러 코딩 에이전트를 각자 격리된 작업공간에서 나란히 돌리는 도구.

- **[Orca](https://github.com/stablyai/orca)** (38k★) — git worktree에서 에이전트 함대를 병렬로 돌리는 에이전트 개발 환경(ADE). Claude Code, Codex, Cursor CLI 등 30+ CLI 에이전트를 데스크톱·모바일·VPS에서 지원.
- **[Vibe Kanban](https://github.com/BloopAI/vibe-kanban)** (28k★) — 칸반 보드로 코딩 에이전트를 오케스트레이션: 태스크 계획, 병렬 실행, 시각적 리뷰. 커뮤니티 유지보수, Apache-2.0.
- **[Conductor](https://conductor.build)** — Claude Code/Codex/Cursor 에이전트를 격리 작업공간에서 병렬 실행하는 무료 맥 앱. Linear 연동.
- **[claude-squad](https://github.com/smtg-ai/claude-squad)** — 여러 AI 에이전트(Claude Code, Codex 등)를 격리 작업공간에서 병렬 관리하는 TUI.
- **[AionUi](https://github.com/iOfficeAI/AionUi)** (31k★) — OpenClaw, Claude Code, Codex, Gemini CLI 등 20+ CLI 에이전트용 무료 로컬 오픈소스 24/7 협업 GUI.
- **[multica](https://github.com/multica-ai/multica)** (44k★) — 코딩 에이전트를 실제 팀원처럼 다루는 오픈소스 관리형 에이전트 플랫폼: 태스크 할당·진행 추적.
- **[Symphony](https://github.com/openai/symphony)** (26k★) — 프로젝트 작업을 격리된 자율 구현 런으로 바꾸는 OpenAI 도구: 감독 대신 관리.

## 도구별 확장 & 규칙 생태계

- **[cursor.directory](https://cursor.directory)** — Cursor 규칙·MCP 서버의 최대 커뮤니티 디렉토리.
- **[Awesome CursorRules](https://github.com/PatrickJS/awesome-cursorrules)** (40k★) — 프레임워크·언어별 .cursorrules 설정 파일 모음.
- **[Awesome Copilot](https://github.com/github/awesome-copilot)** — Copilot 지침·에이전트·스킬·프롬프트의 GitHub 공식 커뮤니티 저장소.
- **[Gemini CLI Extensions Gallery](https://geminicli.com/extensions/)** — 1,300+ 공식·서드파티 Gemini CLI 확장 갤러리.
- **[Awesome Gemini CLI](https://github.com/Piebald-AI/awesome-gemini-cli)** — Gemini CLI 도구·확장·리소스 큐레이션.
- **[Cline Prompts](https://github.com/cline/prompts)** — Cline 프롬프트 라이브러리용 커뮤니티 규칙(.clinerules)과 워크플로.
- **[Zed Extensions](https://zed.dev/extensions)** — Zed 공식 마켓플레이스: 언어 지원, 테마, AI 연동.

---

**함께 보기:** [스킬 & 플러그인](skills-plugins.ko.md) · [지금 뜨는 코딩 에이전트](trending.ko.md#ai-코딩-에이전트--cli) · [에이전트 프레임워크](agent-frameworks.ko.md)
