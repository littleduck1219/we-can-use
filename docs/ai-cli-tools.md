# AI CLI·에디터 도구

Claude Code 외의 AI 코딩 CLI 에이전트, AI 에디터·IDE와 각 도구의 확장·룰 생태계 모음.

## CLI 에이전트

<table>
<tr><th width="340">링크</th><th>설명</th></tr>
<tr><td><a href="https://github.com/openai/codex">OpenAI Codex CLI</a></td><td>OpenAI의 오픈소스(Apache-2.0) 터미널 코딩 에이전트로, 샌드박스 실행과 안전성에 중점을 둔 CLI 도구</td></tr>
<tr><td><a href="https://github.com/github/copilot-cli">GitHub Copilot CLI</a></td><td>Copilot 코딩 에이전트를 터미널로 가져온 GitHub 공식 CLI로, 2026년 2월 정식 출시(GA)됨</td></tr>
<tr><td><a href="https://antigravity.google/docs/cli/overview">Antigravity CLI</a></td><td>2026년 6월 Gemini CLI를 대체한 Google의 Go 기반 터미널 에이전트(`agy`)로, 멀티 에이전트 백그라운드 워크플로 지원</td></tr>
<tr><td><a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a></td><td>Google의 오픈소스 터미널 AI 에이전트(레거시)로, 유료 API 키·Code Assist Standard/Enterprise 사용자용으로는 계속 동작</td></tr>
<tr><td><a href="https://aider.chat">Aider</a></td><td>커뮤니티가 주도하는 오픈소스 터미널 페어 프로그래밍 도구로, git 통합과 다양한 LLM 지원이 강점</td></tr>
<tr><td><a href="https://github.com/sst/opencode">OpenCode</a></td><td>2026년 기준 최대 규모(약 16만 스타)의 오픈소스 CLI 코딩 에이전트로, 세련된 TUI와 폭넓은 모델 프로바이더 지원</td></tr>
<tr><td><a href="https://ampcode.com">Amp</a></td><td>Sourcegraph가 만든 에이전틱 코딩 도구로, CLI와 VS Code 계열 에디터에서 동작하며 스레드 공유 기능 제공</td></tr>
<tr><td><a href="https://github.com/charmbracelet/crush">Crush</a></td><td>Charm이 만든 글래머러스한 TUI 기반 터미널 코딩 에이전트로, OpenAI·Anthropic·Google 등 멀티 프로바이더 지원</td></tr>
<tr><td><a href="https://github.com/block/goose">Goose</a></td><td>Block(Square)이 개발한 오픈소스 로컬 AI 에이전트로, 확장 가능한 아키텍처로 코딩 작업을 자동화</td></tr>
<tr><td><a href="https://github.com/QwenLM/qwen-code">Qwen Code</a></td><td>Alibaba Qwen 팀의 CLI 코딩 에이전트로, Qwen-Coder 모델에 최적화된 터미널 워크플로 제공</td></tr>
</table>

## AI 에디터·IDE

<table>
<tr><th width="340">링크</th><th>설명</th></tr>
<tr><td><a href="https://cursor.com">Cursor</a></td><td>VS Code 포크 기반의 대표적인 AI 네이티브 코드 에디터로, 에이전트 모드·규칙(.cursorrules)·MCP 지원</td></tr>
<tr><td><a href="https://windsurf.com">Windsurf</a></td><td>Cognition(Devin 개발사)이 인수한 AI IDE로, Cascade 에이전트와 제로 데이터 보존 등 프라이버시 중심 설계</td></tr>
<tr><td><a href="https://zed.dev">Zed</a></td><td>Rust로 작성된 초고속 협업 에디터로, 내장 AI 에이전트 패널과 외부 에이전트(ACP) 연동 지원</td></tr>
<tr><td><a href="https://github.com/cline/cline">Cline</a></td><td>VS Code에서 동작하는 오픈소스 자율 코딩 에이전트 확장으로, 계획/실행 모드와 브라우저 조작 지원</td></tr>
<tr><td><a href="https://github.com/RooCodeInc/Roo-Code">Roo Code</a></td><td>Cline에서 포크된 VS Code AI 에이전트로, 커스텀 모드(Modes) 시스템과 멀티 에이전트 워크플로가 특징</td></tr>
<tr><td><a href="https://kilocode.ai">Kilo Code</a></td><td>Cline·Roo Code의 장점을 결합한 오픈소스 VS Code AI 에이전트 확장</td></tr>
<tr><td><a href="https://continue.dev">Continue</a></td><td>VS Code·JetBrains용 오픈소스 AI 코딩 어시스턴트로, 커스텀 모델·규칙 기반의 확장성 제공</td></tr>
</table>

## 도구별 확장·룰 생태계

<table>
<tr><th width="340">링크</th><th>설명</th></tr>
<tr><td><a href="https://cursor.directory">cursor.directory</a></td><td>Cursor용 규칙(rules)과 MCP 서버를 모아둔 최대 규모의 커뮤니티 디렉터리</td></tr>
<tr><td><a href="https://github.com/PatrickJS/awesome-cursorrules">Awesome CursorRules</a></td><td>프레임워크·언어별 .cursorrules 설정 파일을 모은 4만 스타 규모의 큐레이션 저장소</td></tr>
<tr><td><a href="https://github.com/github/awesome-copilot">Awesome Copilot</a></td><td>GitHub 공식 커뮤니티 저장소로, Copilot용 instructions·에이전트·스킬·프롬프트 모음</td></tr>
<tr><td><a href="https://geminicli.com/extensions/">Gemini CLI Extensions Gallery</a></td><td>Google 공식·서드파티 Gemini CLI 확장 1,300여 개를 GitHub 스타 순으로 탐색할 수 있는 공식 갤러리</td></tr>
<tr><td><a href="https://github.com/Piebald-AI/awesome-gemini-cli">Awesome Gemini CLI</a></td><td>Gemini CLI용 도구·확장·리소스를 모은 큐레이션 리스트</td></tr>
<tr><td><a href="https://github.com/cline/prompts">Cline Prompts (Community)</a></td><td>Cline 확장의 프롬프트 라이브러리에서 바로 적용 가능한 커뮤니티 규칙(.clinerules)·워크플로 모음</td></tr>
<tr><td><a href="https://zed.dev/extensions">Zed Extensions</a></td><td>Zed 에디터의 공식 확장 마켓플레이스로, 언어 지원·테마·AI 연동 확장 제공</td></tr>
</table>
