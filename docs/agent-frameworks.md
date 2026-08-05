# 에이전트 프레임워크·SDK

AI 앱·에이전트를 직접 만들 때 쓰는 SDK, 프레임워크, 프로토콜, 관측·평가 도구, 메모리·RAG 인프라 모음.

## 에이전트 SDK

<table width="100%">
<tr><th width="340">링크</th><th>설명</th></tr>
<tr><td><a href="https://code.claude.com/docs/en/agent-sdk/overview">Claude Agent SDK</a></td><td>Claude Code의 에이전트 루프·도구·컨텍스트 관리를 그대로 쓰는 Anthropic 공식 에이전트 SDK (Python/TypeScript)</td></tr>
<tr><td><a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK</a></td><td>에이전트·핸드오프·가드레일 프리미티브로 에이전트 앱을 만드는 OpenAI의 경량 SDK</td></tr>
<tr><td><a href="https://adk.dev/">Google ADK</a></td><td>멀티 언어를 지원하는 Google의 오픈소스 에이전트 개발 킷(Agent Development Kit)</td></tr>
<tr><td><a href="https://github.com/microsoft/agent-framework">Microsoft Agent Framework</a></td><td>AutoGen·Semantic Kernel을 잇는 Microsoft의 .NET/Python 멀티 에이전트 프레임워크</td></tr>
<tr><td><a href="https://ai-sdk.dev/">Vercel AI SDK</a></td><td>여러 LLM 프로바이더를 통합 API로 다루는 TypeScript AI 툴킷</td></tr>
</table>

## 프레임워크

<table width="100%">
<tr><th width="340">링크</th><th>설명</th></tr>
<tr><td><a href="https://github.com/langchain-ai/langchain">LangChain</a></td><td>가장 널리 쓰이는 LLM 앱·에이전트 구축 프레임워크</td></tr>
<tr><td><a href="https://github.com/langchain-ai/langgraph">LangGraph</a></td><td>장시간 실행되는 상태 기반(stateful) 에이전트를 위한 저수준 오케스트레이션 프레임워크</td></tr>
<tr><td><a href="https://www.llamaindex.ai/">LlamaIndex</a></td><td>문서 파싱·인덱싱 중심의 데이터 연결 및 에이전트 프레임워크(LlamaParse 포함)</td></tr>
<tr><td><a href="https://www.crewai.com/">CrewAI</a></td><td>역할 기반 멀티 에이전트 "크루"를 구성하는 프레임워크 겸 엔터프라이즈 플랫폼</td></tr>
<tr><td><a href="https://ag2.ai/">AG2</a></td><td>AutoGen에서 갈라져 나온 오픈소스 멀티 에이전트 오케스트레이션 프레임워크</td></tr>
<tr><td><a href="https://mastra.ai/">Mastra</a></td><td>워크플로·관측성이 내장된 TypeScript 에이전트 프레임워크</td></tr>
<tr><td><a href="https://pydantic.dev/docs/ai/overview/">Pydantic AI</a></td><td>Pydantic 팀이 만든 타입 안전성 중심의 Python 에이전트 프레임워크</td></tr>
<tr><td><a href="https://github.com/huggingface/smolagents">smolagents</a></td><td>에이전트가 코드를 작성해 행동하는 Hugging Face의 미니멀 에이전트 라이브러리</td></tr>
<tr><td><a href="https://dspy.ai/">DSPy</a></td><td>프롬프트 대신 시그니처·모듈·옵티마이저로 LLM을 "프로그래밍"하는 프레임워크</td></tr>
<tr><td><a href="https://haystack.deepset.ai/">Haystack</a></td><td>프로덕션급 RAG·에이전트 파이프라인을 위한 deepset의 오픈소스 오케스트레이션 프레임워크</td></tr>
</table>

## 프로토콜·표준

<table width="100%">
<tr><th width="340">링크</th><th>설명</th></tr>
<tr><td><a href="https://a2a-protocol.org/">A2A Protocol</a></td><td>에이전트 간 통신·협업을 표준화하는 Agent2Agent 오픈 프로토콜</td></tr>
<tr><td><a href="https://agents.md/">AGENTS.md</a></td><td>AI 코딩 에이전트에게 프로젝트 컨텍스트를 제공하는 오픈 파일 포맷 표준</td></tr>
<tr><td><a href="https://agentclientprotocol.com/">Agent Client Protocol</a></td><td>에디터·IDE와 코딩 에이전트 간 통신을 표준화하는 프로토콜(Zed 주도)</td></tr>
</table>

## 관측·평가

<table width="100%">
<tr><th width="340">링크</th><th>설명</th></tr>
<tr><td><a href="https://www.langchain.com/langsmith">LangSmith</a></td><td>에이전트 트레이싱·평가·배포를 아우르는 LangChain의 관측성 플랫폼</td></tr>
<tr><td><a href="https://langfuse.com/docs">Langfuse</a></td><td>관측성·프롬프트 관리·평가를 제공하는 오픈소스 LLM 엔지니어링 플랫폼</td></tr>
<tr><td><a href="https://www.braintrust.dev/">Braintrust</a></td><td>트레이스 검사와 품질 테스트로 AI 제품을 평가·개선하는 플랫폼</td></tr>
<tr><td><a href="https://wandb.ai/site/weave/">W&B Weave</a></td><td>프로덕션 에이전트의 관측과 지속적 개선을 위한 Weights & Biases 도구</td></tr>
<tr><td><a href="https://github.com/Arize-ai/phoenix">Arize Phoenix</a></td><td>트레이싱·평가·실험 추적을 지원하는 오픈소스 AI 관측성 플랫폼</td></tr>
<tr><td><a href="https://www.promptfoo.dev/">promptfoo</a></td><td>LLM 앱의 평가와 레드팀 테스트를 자동화하는 오픈소스 도구</td></tr>
<tr><td><a href="https://github.com/openai/evals">OpenAI Evals</a></td><td>LLM 시스템 평가를 위한 OpenAI의 프레임워크 및 벤치마크 레지스트리</td></tr>
<tr><td><a href="https://github.com/confident-ai/deepeval">DeepEval</a></td><td>Pytest처럼 쓰는 오픈소스 LLM 평가 프레임워크</td></tr>
<tr><td><a href="https://github.com/explodinggradients/ragas">Ragas</a></td><td>RAG·LLM 앱을 위한 객관적 평가 지표와 테스트 데이터 생성 툴킷</td></tr>
</table>

## 메모리·RAG

<table width="100%">
<tr><th width="340">링크</th><th>설명</th></tr>
<tr><td><a href="https://www.pinecone.io/">Pinecone</a></td><td>수십억 벡터 규모를 지원하는 완전관리형 벡터 데이터베이스</td></tr>
<tr><td><a href="https://qdrant.tech/">Qdrant</a></td><td>하이브리드 검색·필터링에 강한 고성능 오픈소스 벡터 검색 엔진</td></tr>
<tr><td><a href="https://www.trychroma.com/">Chroma</a></td><td>벡터·전문·메타데이터 검색을 제공하는 오픈소스 AI 검색 인프라</td></tr>
<tr><td><a href="https://weaviate.io/">Weaviate</a></td><td>벡터 검색·RAG·에이전트 메모리를 하나로 제공하는 오픈소스 AI 데이터베이스</td></tr>
<tr><td><a href="https://github.com/pgvector/pgvector">pgvector</a></td><td>PostgreSQL에서 벡터 유사도 검색을 지원하는 오픈소스 확장</td></tr>
<tr><td><a href="https://mem0.ai/">Mem0</a></td><td>세션을 넘어 사용자 상호작용을 기억하는 AI 에이전트용 메모리 레이어</td></tr>
</table>

## LLM 인프라

<table width="100%">
<tr><th width="340">링크</th><th>설명</th></tr>
<tr><td><a href="https://github.com/BerriAI/litellm">LiteLLM</a></td><td>100개 이상 LLM 프로바이더를 OpenAI 포맷 단일 인터페이스로 호출하는 오픈소스 AI 게이트웨이</td></tr>
</table>
