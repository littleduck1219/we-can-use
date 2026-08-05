# Agent Frameworks & SDKs

**English** | [한국어](agent-frameworks.ko.md)

SDKs, frameworks, protocols, observability and eval tools, and memory/RAG infrastructure for building AI apps and agents.

**Sections:** [Agent SDKs](#agent-sdks) · [Frameworks](#frameworks) · [Protocols & Standards](#protocols--standards) · [Observability & Evals](#observability--evals) · [Memory & RAG](#memory--rag) · [LLM Infrastructure](#llm-infrastructure)

## Agent SDKs

- **[Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)** — Anthropic's official SDK (Python/TS) built on the same agent loop as Claude Code.
- **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)** — Lightweight SDK with agent, handoff, and guardrail primitives.
- **[Google ADK](https://adk.dev/)** — Google's open-source Agent Development Kit with multi-language support.
- **[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)** — .NET/Python multi-agent framework, successor to AutoGen and Semantic Kernel.
- **[Vercel AI SDK](https://ai-sdk.dev/)** — TypeScript AI toolkit with a unified API across LLM providers.

## Frameworks

- **[LangChain](https://github.com/langchain-ai/langchain)** — The most widely used framework for building LLM apps and agents.
- **[LangGraph](https://github.com/langchain-ai/langgraph)** — Low-level orchestration for long-running, stateful agents.
- **[LlamaIndex](https://www.llamaindex.ai/)** — Data connectivity and agent framework focused on document parsing and indexing.
- **[CrewAI](https://www.crewai.com/)** — Role-based multi-agent "crews" framework and enterprise platform.
- **[AG2](https://ag2.ai/)** — Open-source multi-agent orchestration framework forked from AutoGen.
- **[Mastra](https://mastra.ai/)** — TypeScript agent framework with built-in workflows and observability.
- **[Pydantic AI](https://pydantic.dev/docs/ai/overview/)** — Type-safety-focused Python agent framework from the Pydantic team.
- **[smolagents](https://github.com/huggingface/smolagents)** — Hugging Face's minimal agent library where agents act by writing code.
- **[DSPy](https://dspy.ai/)** — "Program" LLMs with signatures, modules, and optimizers instead of prompts.
- **[Haystack](https://haystack.deepset.ai/)** — deepset's orchestration framework for production RAG and agent pipelines.

## Protocols & Standards

- **[A2A Protocol](https://a2a-protocol.org/)** — Agent2Agent open protocol standardizing agent-to-agent communication.
- **[AGENTS.md](https://agents.md/)** — Open file format standard for giving AI coding agents project context.
- **[Agent Client Protocol](https://agentclientprotocol.com/)** — Standardizes communication between editors/IDEs and coding agents (led by Zed).

## Observability & Evals

- **[LangSmith](https://www.langchain.com/langsmith)** — LangChain's platform for agent tracing, evaluation, and deployment.
- **[Langfuse](https://langfuse.com/docs)** — Open-source LLM engineering platform: observability, prompt management, evals.
- **[Braintrust](https://www.braintrust.dev/)** — Evaluate and improve AI products through trace inspection and quality testing.
- **[W&B Weave](https://wandb.ai/site/weave/)** — Weights & Biases tool for observing and improving production agents.
- **[Arize Phoenix](https://github.com/Arize-ai/phoenix)** — Open-source AI observability: tracing, evals, experiment tracking.
- **[promptfoo](https://www.promptfoo.dev/)** — Open-source automation for evals and red-team testing of LLM apps.
- **[OpenAI Evals](https://github.com/openai/evals)** — OpenAI's framework and benchmark registry for evaluating LLM systems.
- **[DeepEval](https://github.com/confident-ai/deepeval)** — Open-source LLM evaluation framework that works like Pytest.
- **[Ragas](https://github.com/explodinggradients/ragas)** — Objective evaluation metrics and test data generation for RAG apps.

## Memory & RAG

- **[Pinecone](https://www.pinecone.io/)** — Fully managed vector database scaling to billions of vectors.
- **[Qdrant](https://qdrant.tech/)** — High-performance open-source vector search engine; strong hybrid search.
- **[Chroma](https://www.trychroma.com/)** — Open-source AI search infra: vector, full-text, and metadata search.
- **[Weaviate](https://weaviate.io/)** — Open-source AI database combining vector search, RAG, and agent memory.
- **[pgvector](https://github.com/pgvector/pgvector)** — Vector similarity search extension for PostgreSQL.
- **[Mem0](https://mem0.ai/)** — Memory layer for AI agents that remembers users across sessions.

## LLM Infrastructure

- **[LiteLLM](https://github.com/BerriAI/litellm)** — Open-source AI gateway calling 100+ LLM providers through one OpenAI-format interface.

---

**See also:** [MCP servers](mcp.md) · [Local LLM runtimes](app-builders-local-llm.md#local-llm-runtimes) · [Benchmarks & leaderboards](directories.md#benchmarks--leaderboards)
