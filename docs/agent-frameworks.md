# Agent Frameworks & SDKs

A collection of SDKs, frameworks, protocols, observability and eval tools, and memory/RAG infrastructure for building AI apps and agents.

## Agent SDKs

<table width="100%">
<tr><th width="340">Link</th><th>Description</th></tr>
<tr><td><a href="https://code.claude.com/docs/en/agent-sdk/overview">Claude Agent SDK</a></td><td>Anthropic's official agent SDK (Python/TypeScript) built on the same agent loop, tools, and context management as Claude Code</td></tr>
<tr><td><a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK</a></td><td>OpenAI's lightweight SDK for building agent apps with agent, handoff, and guardrail primitives</td></tr>
<tr><td><a href="https://adk.dev/">Google ADK</a></td><td>Google's open-source Agent Development Kit with multi-language support</td></tr>
<tr><td><a href="https://github.com/microsoft/agent-framework">Microsoft Agent Framework</a></td><td>Microsoft's .NET/Python multi-agent framework, successor to AutoGen and Semantic Kernel</td></tr>
<tr><td><a href="https://ai-sdk.dev/">Vercel AI SDK</a></td><td>TypeScript AI toolkit with a unified API across multiple LLM providers</td></tr>
</table>

## Frameworks

<table width="100%">
<tr><th width="340">Link</th><th>Description</th></tr>
<tr><td><a href="https://github.com/langchain-ai/langchain">LangChain</a></td><td>The most widely used framework for building LLM apps and agents</td></tr>
<tr><td><a href="https://github.com/langchain-ai/langgraph">LangGraph</a></td><td>Low-level orchestration framework for long-running, stateful agents</td></tr>
<tr><td><a href="https://www.llamaindex.ai/">LlamaIndex</a></td><td>Data connectivity and agent framework focused on document parsing and indexing (includes LlamaParse)</td></tr>
<tr><td><a href="https://www.crewai.com/">CrewAI</a></td><td>Framework and enterprise platform for composing role-based multi-agent "crews"</td></tr>
<tr><td><a href="https://ag2.ai/">AG2</a></td><td>Open-source multi-agent orchestration framework forked from AutoGen</td></tr>
<tr><td><a href="https://mastra.ai/">Mastra</a></td><td>TypeScript agent framework with built-in workflows and observability</td></tr>
<tr><td><a href="https://pydantic.dev/docs/ai/overview/">Pydantic AI</a></td><td>Type-safety-focused Python agent framework from the Pydantic team</td></tr>
<tr><td><a href="https://github.com/huggingface/smolagents">smolagents</a></td><td>Hugging Face's minimal agent library where agents act by writing code</td></tr>
<tr><td><a href="https://dspy.ai/">DSPy</a></td><td>Framework for "programming" LLMs with signatures, modules, and optimizers instead of prompts</td></tr>
<tr><td><a href="https://haystack.deepset.ai/">Haystack</a></td><td>deepset's open-source orchestration framework for production-grade RAG and agent pipelines</td></tr>
</table>

## Protocols & Standards

<table width="100%">
<tr><th width="340">Link</th><th>Description</th></tr>
<tr><td><a href="https://a2a-protocol.org/">A2A Protocol</a></td><td>Agent2Agent open protocol standardizing communication and collaboration between agents</td></tr>
<tr><td><a href="https://agents.md/">AGENTS.md</a></td><td>Open file format standard for giving AI coding agents project context</td></tr>
<tr><td><a href="https://agentclientprotocol.com/">Agent Client Protocol</a></td><td>Protocol standardizing communication between editors/IDEs and coding agents (led by Zed)</td></tr>
</table>

## Observability & Evals

<table width="100%">
<tr><th width="340">Link</th><th>Description</th></tr>
<tr><td><a href="https://www.langchain.com/langsmith">LangSmith</a></td><td>LangChain's observability platform covering agent tracing, evaluation, and deployment</td></tr>
<tr><td><a href="https://langfuse.com/docs">Langfuse</a></td><td>Open-source LLM engineering platform with observability, prompt management, and evals</td></tr>
<tr><td><a href="https://www.braintrust.dev/">Braintrust</a></td><td>Platform for evaluating and improving AI products through trace inspection and quality testing</td></tr>
<tr><td><a href="https://wandb.ai/site/weave/">W&B Weave</a></td><td>Weights & Biases tool for observing and continuously improving production agents</td></tr>
<tr><td><a href="https://github.com/Arize-ai/phoenix">Arize Phoenix</a></td><td>Open-source AI observability platform supporting tracing, evals, and experiment tracking</td></tr>
<tr><td><a href="https://www.promptfoo.dev/">promptfoo</a></td><td>Open-source tool for automating evals and red-team testing of LLM apps</td></tr>
<tr><td><a href="https://github.com/openai/evals">OpenAI Evals</a></td><td>OpenAI's framework and benchmark registry for evaluating LLM systems</td></tr>
<tr><td><a href="https://github.com/confident-ai/deepeval">DeepEval</a></td><td>Open-source LLM evaluation framework that works like Pytest</td></tr>
<tr><td><a href="https://github.com/explodinggradients/ragas">Ragas</a></td><td>Toolkit of objective evaluation metrics and test data generation for RAG and LLM apps</td></tr>
</table>

## Memory & RAG

<table width="100%">
<tr><th width="340">Link</th><th>Description</th></tr>
<tr><td><a href="https://www.pinecone.io/">Pinecone</a></td><td>Fully managed vector database scaling to billions of vectors</td></tr>
<tr><td><a href="https://qdrant.tech/">Qdrant</a></td><td>High-performance open-source vector search engine strong at hybrid search and filtering</td></tr>
<tr><td><a href="https://www.trychroma.com/">Chroma</a></td><td>Open-source AI search infrastructure with vector, full-text, and metadata search</td></tr>
<tr><td><a href="https://weaviate.io/">Weaviate</a></td><td>Open-source AI database combining vector search, RAG, and agent memory</td></tr>
<tr><td><a href="https://github.com/pgvector/pgvector">pgvector</a></td><td>Open-source extension for vector similarity search in PostgreSQL</td></tr>
<tr><td><a href="https://mem0.ai/">Mem0</a></td><td>Memory layer for AI agents that remembers user interactions across sessions</td></tr>
</table>

## LLM Infrastructure

<table width="100%">
<tr><th width="340">Link</th><th>Description</th></tr>
<tr><td><a href="https://github.com/BerriAI/litellm">LiteLLM</a></td><td>Open-source AI gateway that calls 100+ LLM providers through a single OpenAI-format interface</td></tr>
</table>
