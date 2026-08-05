# 에이전트 프레임워크 & SDK

[English](agent-frameworks.md) | **한국어**

AI 앱·에이전트를 만들기 위한 SDK, 프레임워크, 프로토콜, 관측·평가 도구, 메모리/RAG 인프라 모음.

**섹션:** [에이전트 SDK](#에이전트-sdk) · [프레임워크](#프레임워크) · [프로토콜 & 표준](#프로토콜--표준) · [관측 & 평가](#관측--평가) · [메모리 & RAG](#메모리--rag) · [LLM 인프라](#llm-인프라)

## 에이전트 SDK

- **[Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)** — Claude Code와 같은 에이전트 루프 위에 만든 Anthropic 공식 SDK (Python/TS).
- **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)** — 에이전트·핸드오프·가드레일 프리미티브를 갖춘 경량 SDK.
- **[Google ADK](https://adk.dev/)** — 다국어를 지원하는 Google 오픈소스 Agent Development Kit.
- **[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)** — AutoGen과 Semantic Kernel을 잇는 .NET/Python 멀티 에이전트 프레임워크.
- **[Vercel AI SDK](https://ai-sdk.dev/)** — 여러 LLM 프로바이더를 통합 API로 쓰는 TypeScript AI 툴킷.

## 프레임워크

- **[LangChain](https://github.com/langchain-ai/langchain)** — LLM 앱·에이전트 구축에 가장 널리 쓰이는 프레임워크.
- **[LangGraph](https://github.com/langchain-ai/langgraph)** — 장시간 실행되는 상태 유지 에이전트용 저수준 오케스트레이션.
- **[LlamaIndex](https://www.llamaindex.ai/)** — 문서 파싱·인덱싱 중심의 데이터 연결·에이전트 프레임워크.
- **[CrewAI](https://www.crewai.com/)** — 역할 기반 멀티 에이전트 "크루"를 구성하는 프레임워크·엔터프라이즈 플랫폼.
- **[AG2](https://ag2.ai/)** — AutoGen에서 포크된 오픈소스 멀티 에이전트 오케스트레이션 프레임워크.
- **[Mastra](https://mastra.ai/)** — 워크플로와 관측성을 내장한 TypeScript 에이전트 프레임워크.
- **[Pydantic AI](https://pydantic.dev/docs/ai/overview/)** — Pydantic 팀의 타입 안전성 중심 Python 에이전트 프레임워크.
- **[smolagents](https://github.com/huggingface/smolagents)** — 에이전트가 코드를 작성해 행동하는 Hugging Face의 미니멀 라이브러리.
- **[DSPy](https://dspy.ai/)** — 프롬프트 대신 시그니처·모듈·옵티마이저로 LLM을 "프로그래밍".
- **[Haystack](https://haystack.deepset.ai/)** — 프로덕션급 RAG·에이전트 파이프라인용 deepset의 오케스트레이션 프레임워크.

## 프로토콜 & 표준

- **[A2A Protocol](https://a2a-protocol.org/)** — 에이전트 간 통신·협업을 표준화하는 Agent2Agent 개방 프로토콜.
- **[AGENTS.md](https://agents.md/)** — AI 코딩 에이전트에 프로젝트 컨텍스트를 주는 개방형 파일 표준.
- **[Agent Client Protocol](https://agentclientprotocol.com/)** — 에디터/IDE와 코딩 에이전트 간 통신 표준 (Zed 주도).

## 관측 & 평가

- **[LangSmith](https://www.langchain.com/langsmith)** — 에이전트 트레이싱·평가·배포를 아우르는 LangChain의 플랫폼.
- **[Langfuse](https://langfuse.com/docs)** — 관측·프롬프트 관리·평가를 갖춘 오픈소스 LLM 엔지니어링 플랫폼.
- **[Braintrust](https://www.braintrust.dev/)** — 트레이스 검사와 품질 테스트로 AI 제품을 평가·개선.
- **[W&B Weave](https://wandb.ai/site/weave/)** — 프로덕션 에이전트를 관측·개선하는 Weights & Biases 도구.
- **[Arize Phoenix](https://github.com/Arize-ai/phoenix)** — 트레이싱·평가·실험 추적을 지원하는 오픈소스 AI 관측 플랫폼.
- **[promptfoo](https://www.promptfoo.dev/)** — LLM 앱 평가·레드팀 테스트를 자동화하는 오픈소스 도구.
- **[OpenAI Evals](https://github.com/openai/evals)** — LLM 시스템 평가용 OpenAI 프레임워크·벤치마크 레지스트리.
- **[DeepEval](https://github.com/confident-ai/deepeval)** — Pytest처럼 동작하는 오픈소스 LLM 평가 프레임워크.
- **[Ragas](https://github.com/explodinggradients/ragas)** — RAG·LLM 앱용 객관적 평가 지표와 테스트 데이터 생성 툴킷.

## 메모리 & RAG

- **[Pinecone](https://www.pinecone.io/)** — 수십억 벡터로 확장되는 완전 관리형 벡터 DB.
- **[Qdrant](https://qdrant.tech/)** — 하이브리드 검색·필터링에 강한 고성능 오픈소스 벡터 검색 엔진.
- **[Chroma](https://www.trychroma.com/)** — 벡터·전문·메타데이터 검색을 갖춘 오픈소스 AI 검색 인프라.
- **[Weaviate](https://weaviate.io/)** — 벡터 검색·RAG·에이전트 메모리를 결합한 오픈소스 AI DB.
- **[pgvector](https://github.com/pgvector/pgvector)** — PostgreSQL에서 벡터 유사도 검색을 하는 오픈소스 확장.
- **[Mem0](https://mem0.ai/)** — 세션을 넘어 사용자를 기억하는 AI 에이전트용 메모리 레이어.
- **[MemPalace](https://github.com/MemPalace/mempalace)** (58k★) — 벤치마크 검증이 가장 잘 된 무료 오픈소스 AI 메모리 시스템.
- **[OpenViking](https://github.com/volcengine/OpenViking)** (28k★) — 에이전트 메모리·지식 RAG·스킬을 통합하는 자기 진화 컨텍스트 DB (Volcengine).
- **[agentmemory](https://github.com/rohitg00/agentmemory)** (27k★) — 실전 벤치마크 기반 AI 코딩 에이전트용 영속 메모리.
- **[beads](https://github.com/gastownhall/beads)** (26k★) — 코딩 에이전트를 위한 메모리 업그레이드.

## LLM 인프라

- **[LiteLLM](https://github.com/BerriAI/litellm)** — 단일 OpenAI 형식 인터페이스로 100+ LLM 프로바이더를 호출하는 오픈소스 AI 게이트웨이.
- **[OmniRoute](https://github.com/diegosouzapw/OmniRoute)** (40k★) — 무료 MIT AI 게이트웨이: 단일 엔드포인트로 290+ 프로바이더, 500+ 모델.
- **[headroom](https://github.com/headroomlabs-ai/headroom)** (65k★) — 도구 출력·로그·파일·RAG 청크를 LLM에 닿기 전에 압축: 토큰 20%+ 절감.

---

**함께 보기:** [MCP 서버](mcp.ko.md) · [로컬 LLM 런타임](app-builders-local-llm.ko.md#로컬-llm-런타임) · [벤치마크 & 리더보드](directories.ko.md#벤치마크--리더보드)
