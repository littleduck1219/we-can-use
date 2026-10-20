# MCP (Model Context Protocol)

[English](mcp.md) | **한국어**

MCP 서버, 이를 인덱싱하는 디렉토리·레지스트리, 그리고 큐레이션 리스트 모음.

**섹션:** [공식](#공식) · [디렉토리 & 레지스트리](#디렉토리--레지스트리) · [큐레이션 리스트](#큐레이션-리스트) · [주요 서버](#주요-mcp-서버) · [검색 & 웹](#검색--웹) · [디자인 & 프런트엔드](#디자인--프런트엔드) · [DB & 백엔드](#데이터베이스--백엔드) · [커뮤니케이션 & 생산성](#커뮤니케이션--생산성) · [DevOps](#개발-인프라--devops) · [기타](#기타-주요-서버)

## 공식

- **[Model Context Protocol](https://modelcontextprotocol.io)** — 공식 문서: 프로토콜 명세, 아키텍처, 시작 가이드.
- **[MCP Reference Servers](https://github.com/modelcontextprotocol/servers)** — Filesystem, Fetch, Memory 등 공식 레퍼런스 서버 저장소.
- **[Official MCP Registry](https://registry.modelcontextprotocol.io)** — Anthropic·GitHub·Microsoft 등이 공동 운영하는 공식 레지스트리 (REST API).
- **[MCP Registry (GitHub)](https://github.com/modelcontextprotocol/registry)** — 공식 레지스트리의 오픈소스 저장소.
- **[MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)** — 서버·클라이언트 제작용 공식 TypeScript SDK.
- **[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)** — 서버·클라이언트 제작용 공식 Python SDK.

## 디렉토리 & 레지스트리

- **[Smithery](https://smithery.ai)** — CLI 설치·호스팅으로 7,000+ MCP 서버 제공.
- **[PulseMCP](https://www.pulsemcp.com)** — 매일 갱신되는 18,000+ 서버 수작업 큐레이션 디렉토리.
- **[Glama MCP Servers](https://glama.ai/mcp/servers)** — 품질·보안 지표와 함께 30,000+ 서버 인덱싱.
- **[mcp.so](https://mcp.so)** — 20,000+ 서버의 커뮤니티 마켓플레이스.
- **[MCP Market](https://mcpmarket.com)** — 카테고리별로 탐색하는 서버 마켓플레이스.
- **[Docker MCP Catalog](https://hub.docker.com/mcp)** — 컨테이너화된 MCP 서버의 Docker 공식 카탈로그.
- **[mcpservers.org](https://mcpservers.org/)** — Claude·Codex·Cursor 등에서 쓰는 9,800+ 공식·커뮤니티 서버.
- **[Composio Toolkits](https://composio.dev/toolkits/)** — MCP 또는 API로 쓰는 1,000+ SaaS 연동.
- **[MCP Awesome](https://mcp-awesome.com/)** — 튜토리얼과 함께 품질 검증된 1,200+ 서버.
- **[Awesome MCP Tools](https://awesome-mcp.tools/)** — awesome-mcp-servers 저장소를 6시간마다 재수집하는 라이브 디렉토리.
- **[Cline MCP Marketplace](https://cline.bot/mcp-marketplace)** — Cline 에이전트용 원클릭 MCP 서버 설치.
- **[ModelScope MCP](https://modelscope.cn/mcp)** — 알리바바 ModelScope가 운영하는 중국 최대 MCP 마켓플레이스.

## 큐레이션 리스트

- **[Awesome MCP Servers (punkpeye)](https://github.com/punkpeye/awesome-mcp-servers)** — 가장 널리 알려진 MCP 서버 큐레이션 리스트 (다국어 README).
- **[Awesome MCP Servers (wong2)](https://github.com/wong2/awesome-mcp-servers)** — 공식·커뮤니티 서버를 다루는 또 하나의 인기 리스트.
- **[Awesome MCP Clients](https://github.com/punkpeye/awesome-mcp-clients)** — MCP를 지원하는 클라이언트 앱 리스트.
- **[Awesome MCP DevTools](https://github.com/punkpeye/awesome-mcp-devtools)** — MCP 개발용 SDK·라이브러리·테스트 도구 리스트.

## 주요 MCP 서버

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)** — GitHub 공식: 저장소·이슈·PR 관리.
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** — Microsoft 공식: Playwright 기반 브라우저 자동화.
- **[Context7](https://github.com/upstash/context7)** — 최신 라이브러리 문서·코드 예제를 LLM에 주입 (Upstash).
- **[Filesystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** — 공식 레퍼런스: 로컬 파일 읽기·쓰기·검색.
- **[Notion MCP Server](https://github.com/makenotion/notion-mcp-server)** — Notion 공식: Notion API 연동.
- **[Supabase MCP](https://github.com/supabase/mcp)** — 공식: AI로 Supabase 프로젝트·DB 제어.
- **[Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp)** — 인덱스 튜닝·성능 분석을 갖춘 PostgreSQL 서버.
- **[Firecrawl MCP Server](https://github.com/firecrawl/firecrawl-mcp-server)** — Firecrawl 공식: 웹 스크래핑·크롤링.
- **[Browserbase MCP Server](https://github.com/browserbase/mcp-server-browserbase)** — 클라우드 헤드리스 브라우저 자동화.
- **[Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare)** — 공식: Workers, KV, R2 등 Cloudflare 리소스 관리.
- **[AWS MCP Servers](https://github.com/awslabs/mcp)** — AWS 서비스를 아우르는 AWS Labs 공식 서버 모음.
- **[MCP Atlassian](https://github.com/sooperset/mcp-atlassian)** — Jira·Confluence 연동 인기 커뮤니티 서버.
- **[Blender MCP](https://github.com/ahujasid/blender-mcp)** — Claude로 Blender 3D 모델링 제어.

## 검색 & 웹

- **[Brave Search MCP](https://github.com/brave/brave-search-mcp-server)** — 공식: 웹·이미지·뉴스·비디오 검색과 AI 요약.
- **[Exa MCP](https://github.com/exa-labs/exa-mcp-server)** — AI 에이전트용 시맨틱 검색 엔진 Exa의 공식 서버.
- **[Tavily MCP](https://github.com/tavily-ai/tavily-mcp)** — LLM 최적화 검색 API: 실시간 검색·추출·크롤링.
- **[Perplexity MCP](https://github.com/ppl-ai/modelcontextprotocol)** — Perplexity Sonar API 기반 실시간 웹 리서치.

## 디자인 & 프런트엔드

- **[Figma Dev Mode MCP](https://developers.figma.com/docs/figma-mcp-server/)** — 공식: 디자인 토큰·컴포넌트·레이아웃을 코드 생성에 주입.
- **[Framelink Figma MCP](https://github.com/GLips/Figma-Context-MCP)** — Figma 레이아웃 데이터를 AI 코딩 도구에 제공하는 인기 커뮤니티 서버.
- **[shadcn MCP](https://ui.shadcn.com/docs/registry/mcp)** — 공식: shadcn/ui 레지스트리 컴포넌트 검색·설치.
- **[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)** — Google 공식: 실행 중인 브라우저 디버깅·프로파일링·자동화.
- **[Magic MCP (21st.dev)](https://github.com/21st-dev/magic-mcp)** — 자연어 설명으로 모던 UI 컴포넌트 생성.

## 데이터베이스 & 백엔드

- **[MongoDB MCP](https://github.com/mongodb-js/mongodb-mcp-server)** — 공식: MongoDB·Atlas 클러스터 쿼리·관리.
- **[Redis MCP](https://github.com/redis/mcp-redis)** — 공식: 자연어로 Redis 데이터 검색·저장·관리.
- **[Neon MCP](https://github.com/neondatabase/mcp-server-neon)** — 서버리스 Postgres의 프로젝트·브랜치·쿼리 관리.
- **[Prisma MCP](https://github.com/prisma/mcp)** — 공식: Prisma Postgres DB 생성·백업·마이그레이션.
- **[Convex MCP](https://docs.convex.dev/ai/convex-mcp-server)** — 공식: Convex 테이블·함수·배포를 에이전트가 조회·실행.
- **[ClickHouse MCP](https://github.com/ClickHouse/mcp-clickhouse)** — 공식: ClickHouse 분석 DB에 SQL 쿼리 실행.
- **[Qdrant MCP](https://github.com/qdrant/mcp-server-qdrant)** — 공식: Qdrant를 에이전트의 시맨틱 메모리 레이어로 활용.
- **[Chroma MCP](https://github.com/chroma-core/chroma-mcp)** — 공식: Chroma에서 벡터·전문 검색과 문서 저장.

## 커뮤니케이션 & 생산성

- **[Slack MCP Server](https://github.com/korotovsky/slack-mcp-server)** — 가장 인기 있는 Slack 서버: DM, 스레드, 히스토리, 메시지 전송.
- **[Linear MCP](https://linear.app/docs/mcp)** — Linear 이슈·프로젝트용 공식 원격 서버.
- **[Sentry MCP](https://github.com/getsentry/sentry-mcp)** — 공식: Sentry 에러 조회와 AI 근본 원인 분석 (Seer).
- **[Stripe Agent Toolkit](https://github.com/stripe/agent-toolkit)** — 공식: 에이전트에서 결제·인보이스·고객 관리.
- **[Zapier MCP](https://zapier.com/mcp)** — 단일 MCP 엔드포인트로 8,000+ 앱 연동.

## 개발 인프라 & DevOps

- **[Kubernetes MCP](https://github.com/containers/kubernetes-mcp-server)** — kubectl 없이 Kubernetes/OpenShift를 다루는 네이티브 Go 서버.
- **[Terraform MCP](https://github.com/hashicorp/terraform-mcp-server)** — HashiCorp 공식: Terraform 레지스트리 데이터로 IaC 작성 지원.
- **[Grafana MCP](https://github.com/grafana/mcp-grafana)** — 공식: 대시보드·데이터소스 조회와 Prometheus/Loki 쿼리.
- **[Azure MCP](https://github.com/Azure/azure-mcp)** — Microsoft 공식: Azure 리소스 관리와 주요 서비스 운영.
- **[Vercel MCP](https://vercel.com/docs/mcp/vercel-mcp)** — 공식: Vercel 프로젝트·배포·로그 관리.
- **[SandBase Harness MCP](https://github.com/sandbaseai/sandbase-harness)** — 영속 세션, 샌드박스 실행, 아티팩트, 감사 로그와 리플레이를 제공하는 로컬 우선·셀프호스팅 에이전트 런타임 브리지. 격리는 선택한 백엔드와 배포 구성에 따라 달라집니다.

## 기타 주요 서버

- **[Serena](https://github.com/oraios/serena)** — LSP 기반 심볼 수준 코드 검색·편집으로 코딩 에이전트를 강화.
- **[ElevenLabs MCP](https://github.com/elevenlabs/elevenlabs-mcp)** — 공식: TTS, 보이스 클로닝, 전사 등 오디오 AI 연결.
- **[MarkItDown MCP](https://github.com/microsoft/markitdown)** — Microsoft: PDF·오피스 문서를 LLM 친화적 Markdown으로 변환.

---

**함께 보기:** [전체 카탈로그 (3,700+ 저장소)](../catalog/mcp-servers.md) · [지금 뜨는 MCP·인프라](trending.ko.md#mcp--에이전트-인프라) · [에이전트 프레임워크](agent-frameworks.ko.md)
