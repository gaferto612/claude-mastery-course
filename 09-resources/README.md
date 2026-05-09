# Module 09 — Resources, Cheat Sheets & Glossary

The closing reference module. Bookmark this one.

🎨 **Looking for visuals?** → [**Visual Reference**](./visual-reference.md) — every diagram from the course in one page
🖥️ **Want it interactive?** → Open [`../hub.html`](../hub.html) in your browser

---

## 9.1 Official Anthropic Resources

| What | URL |
|---|---|
| Claude.ai | https://claude.ai |
| Claude API docs | https://docs.claude.com/en/api/overview |
| Models overview | https://docs.claude.com/en/docs/about-claude/models/overview |
| Pricing | https://www.anthropic.com/pricing |
| Console & API keys | https://console.anthropic.com |
| Workbench (prompt testing) | https://console.anthropic.com/workbench |
| Claude Code docs | https://docs.claude.com/en/docs/claude-code/overview |
| Claude Code on npm | https://www.npmjs.com/package/@anthropic-ai/claude-code |
| Anthropic Cookbook (notebooks) | https://github.com/anthropics/anthropic-cookbook |
| Help Center | https://support.claude.com |
| Anthropic news / launches | https://www.anthropic.com/news |
| MCP (Model Context Protocol) | https://modelcontextprotocol.io |
| Status page | https://status.anthropic.com |

---

## 9.2 The Prompt Engineering Cheat Sheet

```
🎭 ROLE         "You are a [specific] who has done [thing] for [time]."
📋 CONTEXT      "I'm building/writing/deciding about [situation]."
🎯 TASK         "Do exactly: [verb] + [object] + [success criterion]."
📐 CONSTRAINTS  "Length / tone / what to avoid / what must include."
📦 FORMAT       "Output as: markdown table / JSON / 5 bullets / etc."
🌟 EXAMPLE      "Match the tone of: [paste]."
```

### Power moves
- **XML tags** for structured input: `<context>...</context>`, `<draft>...</draft>`
- **Step-by-step thinking** for hard problems
- **Few-shot examples** (3 input/output pairs) for classification
- **"Ask me 3 questions first"** for ambiguous tasks
- **"What would you change to make this 50% better?"** for iteration

---

## 9.3 The API Cheat Sheet

```python
from anthropic import Anthropic

client = Anthropic()

# --- BASIC CALL ---
resp = client.messages.create(
    model="claude-sonnet-4-6",   # or claude-opus-4-7, claude-haiku-4-5
    max_tokens=1024,
    system="You are a concise assistant.",
    messages=[{"role": "user", "content": "Hello"}],
    temperature=0.7,             # 0 = deterministic, 1 = creative
)
print(resp.content[0].text)

# --- STREAMING ---
with client.messages.stream(model=..., max_tokens=..., messages=...) as s:
    for chunk in s.text_stream:
        print(chunk, end="")

# --- VISION ---
{"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": b64}}

# --- PDF ---
{"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": b64}}

# --- TOOL USE ---
client.messages.create(..., tools=[{"name": "...", "description": "...", "input_schema": {...}}])
# stop_reason will be "tool_use"; loop until "end_turn"

# --- PROMPT CACHING ---
system=[
    {"type": "text", "text": "...", "cache_control": {"type": "ephemeral"}},
]
```

---

## 9.4 Choosing a Model — Quick Decision Tree

```
Is the task simple/repetitive? ──Yes──► Haiku
       │
       No
       │
Is it a hard reasoning/coding task ──Yes──► Opus (or Opus + extended thinking)
or a long-horizon agent?
       │
       No
       │
       └──► Sonnet (the default for most production work)
```

---

## 9.5 Glossary

- **Token** — A chunk of text the model processes (roughly ¾ of a word).
- **Context window** — How much text the model can hold at once. Modern Claude: up to 1M tokens.
- **System prompt** — A persistent instruction that sets Claude's role/rules.
- **Temperature** — Randomness control. Low = consistent, high = creative.
- **Streaming** — Returning the response token-by-token as it's generated.
- **Tool use / function calling** — Claude calling your code via a defined interface.
- **Agent** — Claude in a loop, using tools to make progress on a goal.
- **MCP (Model Context Protocol)** — Open standard for connecting AI to tools/data.
- **Artifact** — A live document, code file, or app rendered in Claude.ai.
- **Project** — A persistent workspace with shared instructions and files.
- **Prompt caching** — Reusing pre-computed input to cut cost & latency.
- **Extended thinking** — A mode where Claude reasons explicitly before answering.
- **Hallucination** — When the model makes something up that sounds plausible but isn't true.
- **RAG** — Retrieval-Augmented Generation. Fetch relevant docs, then answer.
- **Constitutional AI** — Anthropic's training method using AI-generated feedback against a set of principles.
- **RLHF** — Reinforcement Learning from Human Feedback.

---

## 9.6 FAQ

**Q: Will Claude train on my data?**
A: For Claude.ai consumer plans, you control this in Settings — opt out of training is supported. For API and enterprise plans, your data is **not used to train models** by default. Always read the current terms.

**Q: Is the API the same as Claude.ai?**
A: No. The API is raw access to the model. Claude.ai is a polished product *built on top* of the API with extra features (Projects, Artifacts, search, memory). Pricing is also separate.

**Q: How do I report a bad response?**
A: Thumbs-down in Claude.ai sends feedback to Anthropic. For specific safety issues, see [anthropic.com/safety](https://www.anthropic.com/safety).

**Q: How do I keep up with new features?**
A: [anthropic.com/news](https://www.anthropic.com/news) and the [release notes](https://docs.claude.com/en/release-notes/overview).

**Q: Can I run Claude locally / offline?**
A: No. Claude is closed-source and runs on Anthropic's infrastructure. For self-hosting, look at open models like Llama, Mistral, or Qwen.

**Q: What's the difference between Claude and ChatGPT?**
A: Different companies (Anthropic vs. OpenAI), different training approaches (Constitutional AI vs. RLHF heavier), different strengths (Claude often praised for writing/coding/long context; GPT for ecosystem integration). Try both — they're complementary.

---

## 9.7 Recommended Learning Path After This Course

1. **Build something that solves a real problem for *you*** — even a tiny one. The biggest gains come from real use, not more reading.
2. **Read the [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)** — concrete examples for tool use, RAG, evals.
3. **Join the [Anthropic Discord](https://www.anthropic.com/discord)** — real engineers, real questions, no marketing fluff.
4. **Follow the [release notes](https://docs.claude.com/en/release-notes/overview)** — this space moves fast.
5. **Keep a personal prompt library.** Your best prompts are an asset. Save them.

---

## 9.8 Contributing & Feedback

Found a bug, have a better example, or want to add a project? PRs welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## 🎉 You finished the course

If you've actually built the projects in Module 08, **you're now in the top few percent of Claude users**. Most people stop at "type a question, copy the answer." You've moved from a user to a builder.

Now go ship something.

> ⭐ If this course helped, please star the repo so other people can find it.

---

| ← Previous | 🏠 Home | Next → |
|---|---|---|
| [Module 08 — Real-World Projects](../08-real-world-projects/) | [Course README](../README.md) | _End of course_ |
