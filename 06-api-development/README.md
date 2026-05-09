<div align="center">

# ⚙️ Module 06 — Building with the Claude API

[![Module](https://img.shields.io/badge/06-API-4DABF7?style=for-the-badge&labelColor=2a1f1a)](#)
[![Time](https://img.shields.io/badge/⏱️_45_min-FF7A4D?style=for-the-badge&labelColor=2a1f1a)](#)
[![Level](https://img.shields.io/badge/🛠️_Developer-FF6B9D?style=for-the-badge&labelColor=2a1f1a)](#)
[![Examples](https://img.shields.io/badge/💻_9_examples-6BCF7F?style=for-the-badge&labelColor=2a1f1a)](./examples/)
[![Key](https://img.shields.io/badge/🔑_API_key-FFD23F?style=for-the-badge&labelColor=2a1f1a)](https://console.anthropic.com)

***Goal:** make your first API call, then build with streaming, system prompts, tool use, and vision. Python + TypeScript.*

</div>

---

## 6.0 What you'll be able to build

```
👤 Your code  ──HTTPS──▶  ⚙️ Claude API  ──▶  🧠 Models
                                                  │
                                                  ├──▶  💬 Chat
                                                  ├──▶  🌊 Streaming
                                                  ├──▶  🛠️ Tool use
                                                  ├──▶  👁️ Vision
                                                  ├──▶  📄 PDFs
                                                  └──▶  💾 Cached prompts
```

---

## 6.1 Getting an API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign in (same account as Claude.ai is fine)
3. Click **API Keys → Create Key**
4. Add billing — API access is **separate** from your Claude.ai subscription. You pay per token.
5. **Copy the key once** — it won't be shown again. Store it somewhere safe.

```bash
# Add to your shell profile (.zshrc, .bashrc)
export ANTHROPIC_API_KEY="sk-ant-..."
```

> [!WARNING]
> **Never commit API keys to git.** Use `.env` files or a secret manager. There are bots that scan public repos within minutes.

---

## 6.2 Pricing — The 30-Second Version

The API charges per **token** (~¾ of a word). Pricing varies by model:

```
                    INPUT (per million tokens)        OUTPUT (per million tokens)
                    ──────────────────────────        ─────────────────────────────
  💎 Opus          ████████████████████  $$$           ████████████████████████  $$$$
  ⚡ Sonnet        ████████  $$                        ████████████  $$
  🚀 Haiku         ██  $                               ███  $

   (illustrative — check pricing page for current rates)
```

- **Input tokens** (what you send) and **Output tokens** (what Claude generates) — output is more expensive
- **Prompt caching** — cache repeated context for ~90% input cost reduction
- **Batch API** — non-urgent jobs at 50% off

> 📌 Prices change. Always check [docs.claude.com/en/docs/about-claude/pricing](https://docs.claude.com/en/docs/about-claude/pricing) before estimating costs.

---

## 6.3 Your First API Call

### Python

```bash
pip install anthropic
```

```python
# hello_claude.py
from anthropic import Anthropic

client = Anthropic()  # reads ANTHROPIC_API_KEY from env

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "In 3 bullets, what is the Anthropic Claude API?"}
    ],
)

print(message.content[0].text)
```

Run it:

```bash
python hello_claude.py
```

### TypeScript / Node

```bash
npm install @anthropic-ai/sdk
```

```typescript
// hello-claude.ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic(); // reads ANTHROPIC_API_KEY from env

const message = await client.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "In 3 bullets, what is the Anthropic Claude API?" },
  ],
});

console.log(message.content[0].type === "text" ? message.content[0].text : "");
```

That's it — you've used the API.

---

## 6.4 Anatomy of a Messages Request

```python
client.messages.create(
    model="claude-sonnet-4-6",          # which model
    max_tokens=1024,                    # cap on response length
    system="You are a witty haiku-only assistant.",  # system prompt
    messages=[                          # conversation history
        {"role": "user",      "content": "Tell me about the ocean."},
        {"role": "assistant", "content": "Vast salt cathedral / ..."},
        {"role": "user",      "content": "Now about mountains."},
    ],
    temperature=0.7,                    # 0 = deterministic, 1 = creative
)
```

Key concepts:

- **`system`** — the persistent instruction (think of it as Claude's "role")
- **`messages`** — the conversation. Alternates `user` and `assistant`. **You** maintain history; the API is stateless.
- **`max_tokens`** — required. Hard cap on output length.
- **`temperature`** — randomness. Use `0` for extraction/classification, `0.7+` for creative writing.

---

## 6.5 Streaming Responses

For chat UIs, you don't want to wait for the full response. Stream it.

### Python (streaming)

```python
with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write a 200-word story about a lonely lighthouse."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### TypeScript (streaming)

```typescript
const stream = await client.messages.stream({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Write a 200-word story about a lonely lighthouse." }],
});

for await (const event of stream) {
  if (event.type === "content_block_delta" && event.delta.type === "text_delta") {
    process.stdout.write(event.delta.text);
  }
}
```

---

## 6.6 Multi-Turn Conversations

Claude is **stateless** — you must keep and resend the conversation history yourself.

```python
history = []

def chat(user_message: str) -> str:
    history.append({"role": "user", "content": user_message})
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are a helpful coding tutor.",
        messages=history,
    )
    reply = resp.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply

print(chat("What's a Python decorator?"))
print(chat("Show me a simple example."))
print(chat("Now apply that to a function that logs how long it takes to run."))
```

For long conversations, you'll eventually hit the **context window** limit. Strategies:

- Summarize older turns and replace them
- Keep only the last N exchanges
- Use a vector store for old context, retrieve relevant chunks
- Use **prompt caching** (see 6.10) to keep static context cheap

---

## 6.7 Tool Use (Function Calling)

Tools let Claude call your code. The flow:

```
1.  👤 User       ──▶  🧠 Claude     "Should I bring a jacket to Paris?"
2.  🧠 Claude     ──▶  🧠 Claude      decides: needs weather
3.  🧠 Claude     ──▶  💻 Your code   tool_use: get_weather(city="Paris")
4.  💻 Your code  ──▶  💻 Your code   calls real weather API
5.  💻 Your code  ──▶  🧠 Claude      tool_result: {temp: 14, drizzle}
6.  🧠 Claude     ──▶  👤 User        "Yes — 14°C and drizzly. Bring a light jacket."
```

1. You define a tool's **name, description, and input schema**
2. Claude decides whether to call it and with what args
3. Your code runs the tool
4. You send the result back to Claude
5. Claude uses it to answer the user

```python
import json
from anthropic import Anthropic

client = Anthropic()

tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"},
                "unit": {"type": "string", "enum": ["c", "f"], "default": "c"},
            },
            "required": ["city"],
        },
    }
]

def get_weather(city: str, unit: str = "c") -> dict:
    # In reality, call a weather API. We'll fake it.
    return {"city": city, "temp": 22, "unit": unit, "conditions": "sunny"}

messages = [{"role": "user", "content": "Should I bring a jacket to Paris today?"}]

while True:
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

    if resp.stop_reason == "tool_use":
        # Claude wants to call a tool
        tool_use = next(b for b in resp.content if b.type == "tool_use")
        result = get_weather(**tool_use.input)

        messages.append({"role": "assistant", "content": resp.content})
        messages.append({
            "role": "user",
            "content": [{
                "type": "tool_result",
                "tool_use_id": tool_use.id,
                "content": json.dumps(result),
            }],
        })
        continue  # let Claude see the result and respond

    # Final answer
    print(next(b.text for b in resp.content if b.type == "text"))
    break
```

This pattern is the foundation of every "agent" — Claude in a loop, calling tools until the task is done.

---

## 6.8 Vision — Sending Images

Claude can see images. Send them as base64 or a URL.

```python
import base64

with open("chart.png", "rb") as f:
    img_b64 = base64.standard_b64encode(f.read()).decode()

resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": img_b64,
                },
            },
            {"type": "text", "text": "What's the most surprising thing in this chart?"},
        ],
    }],
)
print(resp.content[0].text)
```

Use cases: chart analysis, OCR, accessibility (alt text generation), receipt parsing, screenshot debugging.

---

## 6.9 PDF Support

Recent Claude models can read PDFs natively — no parsing layer needed.

```python
import base64

with open("contract.pdf", "rb") as f:
    pdf_b64 = base64.standard_b64encode(f.read()).decode()

resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    messages=[{
        "role": "user",
        "content": [
            {"type": "document", "source": {
                "type": "base64", "media_type": "application/pdf", "data": pdf_b64,
            }},
            {"type": "text", "text": "List every party's obligations as a markdown table."},
        ],
    }],
)
print(resp.content[0].text)
```

---

## 6.10 Prompt Caching — Big Cost Savings

If you keep sending the same long context (a system prompt, a knowledge base), **cache it**. Cached input tokens cost ~10% of normal pricing.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   FIRST CALL (writes cache)                                  │
│   ┌───────────────────────────────────────┐                  │
│   │ System: "You're support for Acme..."  │  $$ premium      │
│   │ Knowledge: [50 pages of docs]   ──┐   │  to write cache  │
│   │ User: "How do I reset?"           │   │                  │
│   └───────────────────────────────────│───┘                  │
│                                       │                      │
│                                       ▼ stored ~5 min        │
│   SUBSEQUENT CALLS (read cache)                              │
│   ┌───────────────────────────────────────┐                  │
│   │ System: same                          │  ✅ ~10% cost    │
│   │ Knowledge: same  ─────────────────┐   │                  │
│   │ User: "What's warranty?"          │   │                  │
│   └───────────────────────────────────│───┘                  │
│                                       │                      │
│                                       └─► uses cached ✨     │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

```python
resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "You are a customer support agent for AcmeCorp...",
            "cache_control": {"type": "ephemeral"},  # cache this block
        },
        {
            "type": "text",
            "text": LONG_KNOWLEDGE_BASE,
            "cache_control": {"type": "ephemeral"},
        },
    ],
    messages=[{"role": "user", "content": "How do I reset my password?"}],
)
```

First call writes the cache (small premium). Every subsequent call within ~5 minutes pays the discounted rate. For chatbots and RAG, this can cut costs by 80%+.

---

## 6.11 Batch API — 50% Off for Async Work

For jobs you don't need answered immediately (overnight summarization, batch classification), use the **Batch API**:

- Submit a file of requests
- Wait up to 24 hours
- Pay 50% less

Great for: dataset labeling, bulk content generation, periodic reports.

---

## 6.12 Production Checklist

Before you ship anything API-powered, walk this checklist top to bottom:

| # | Step | Why |
|:---:|---|---|
| 1 | 🔒 **Secrets in vault** | No keys in code, repo, or logs |
| 2 | ⏱️ **Rate-limit endpoint** | Don't expose raw API to users |
| 3 | 💰 **Cost caps + alerts** | Anomaly alerts on token spend |
| 4 | 🔁 **Retries with backoff** | Handle 429s and 5xxs gracefully |
| 5 | 📝 **Logging + PII redaction** | Audit trail without leaks |
| 6 | 🧪 **Eval set** | Regression tests on every prompt change |
| 7 | 🛡️ **Fallback model** | Survive model outages |
| 8 | 💾 **Prompt caching** | If static context > 1024 tokens, cache it |
| 9 | 🚀 **Ship it!** | |

Detailed checklist:

- [ ] **Secrets** in env vars or a vault, never in code
- [ ] **Rate limiting** on your endpoint (don't expose raw API to users)
- [ ] **Cost caps** — monitor spend, alert on anomalies
- [ ] **Retries with backoff** for 429s and 5xxs (the SDK does this for you, mostly)
- [ ] **Logging** of prompts and responses (with PII redaction)
- [ ] **Evals** — a small test set you re-run on every prompt change
- [ ] **Fallback** to a smaller model if the big one is unavailable
- [ ] **Prompt caching** if you have static context > 1024 tokens

---

## 6.13 The Code Examples Folder

Working examples for everything in this module live in [`examples/`](./examples/):

- `01-hello-world.py`
- `02-streaming.py`
- `03-multi-turn.py`
- `04-tool-use.py`
- `05-vision.py`
- `06-pdf.py`
- `07-prompt-caching.py`
- `08-streaming.ts`
- `09-tool-use.ts`

---

## ✅ Module 6 Checkpoint

You should now be able to:

- Make a basic Messages API call in Python or TypeScript
- Stream responses
- Maintain multi-turn conversations
- Define and handle tool calls
- Send images and PDFs
- Use prompt caching to control costs

> 👉 **Next up:** [Module 07 — Advanced Techniques](../07-advanced-techniques/) — extended thinking, agents, MCP, and computer use.

---

## 📚 Further reading

- [Claude API docs](https://docs.claude.com/en/api/overview)
- [Anthropic SDKs](https://docs.claude.com/en/api/client-sdks)
- [The Anthropic Cookbook (notebooks)](https://github.com/anthropics/anthropic-cookbook)

---

| ← Previous | 🏠 Home | Next → |
|---|---|---|
| [Module 05 — Claude Code](../05-claude-code/) | [Course README](../README.md) | [Module 07 — Advanced Techniques](../07-advanced-techniques/) |
