# Module 07 — Advanced Techniques

> **Goal:** Push past basic chat and basic API. Extended thinking, agents, MCP, computer use, evaluation, and the patterns the pros use.

⏱️ **~30 minutes** &nbsp;&nbsp;&nbsp; 📊 **5 diagrams** &nbsp;&nbsp;&nbsp; 🎯 **Modules 03 + 06 recommended first**

---

## 7.1 Extended Thinking

Modern Claude models (Opus 4.7, Sonnet 4.6, etc.) can do **extended thinking** — taking extra time to reason through a hard problem before answering. You see the thinking, then the answer.

### When to use it

- Complex math, logic, or proof-style problems
- Multi-step planning where the wrong first step costs a lot
- Code with subtle invariants
- Decisions where you want to *see the reasoning*

### Enabling it (API)

```python
resp = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=8192,
    thinking={"type": "enabled", "budget_tokens": 4096},
    messages=[{"role": "user", "content": "Plan a 3-day Tokyo itinerary optimized for foodies who hate crowds. Reason carefully."}],
)
```

The `budget_tokens` is roughly how much "thinking" Claude can do. More budget → deeper reasoning, slower, more expensive.

The response will contain both `thinking` blocks and `text` blocks. Render the text to users; keep the thinking for debugging or display it as collapsible "show reasoning" UI.

### A note on effort levels

For Opus 4.7, Sonnet 4.6, and Opus 4.6, you can also tune an **effort** parameter — letting Claude decide adaptively how much to think on each step. Lower effort is faster/cheaper; higher effort handles harder problems.

---

## 7.2 Building Agents

An **agent** is Claude in a loop, using tools to make progress on a goal.

```
🎯 Receive goal
       │
       ▼
🧠 Plan next action  ◀──────────────┐
       │                            │
       ▼                            │
   Need a tool?                     │
    │         │                     │
   yes        no (have answer)      │
    ▼         │                     │
🔧 Call tool  │                     │
    │         │                     │
    ▼         │                     │
👀 Observe    │                     │
    │         │                     │
    ▼         ▼                     │
   Goal achieved?                   │
    │            │                  │
    no ──────────┘ (loop)           │
    │                               │
    yes                             │
    ▼                               │
💬 Give answer  ──▶  ✅ Done         │
```

### Levels of agentic-ness

| Level | Description | Example |
|---|---|---|
| 0 | Single shot, no tools | "Summarize this." |
| 1 | One tool call | "What's the weather?" → calls weather API → answers |
| 2 | Multi-step with one tool | "Research these 5 companies" → searches each, summarizes |
| 3 | Multi-step, multi-tool | "Book me a flight under $500 and add it to my calendar" |
| 4 | Long-horizon | "Refactor this codebase to use TypeScript" (hours of work) |

### Designing agents that don't go off the rails

1. **Define stop conditions clearly.** "When you've answered the original question" or "after 10 tool calls" or "when the user confirms."
2. **Limit tool surface.** Each extra tool roughly halves reliability. Give Claude only what it needs.
3. **Use planning prompts.** Ask Claude to plan first, then execute. Catch bad plans early.
4. **Save state.** For long tasks, persist progress so a crash doesn't restart from zero.
5. **Stream and log everything.** You'll need it when something weird happens (and it will).
6. **Set budget caps.** Both `max_tokens` and a hard limit on iterations.

A simple agent loop pattern:

```python
def run_agent(goal: str, tools, max_iterations=20):
    messages = [{"role": "user", "content": goal}]

    for i in range(max_iterations):
        resp = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2048,
            tools=tools,
            messages=messages,
        )

        if resp.stop_reason == "end_turn":
            return next(b.text for b in resp.content if b.type == "text")

        if resp.stop_reason == "tool_use":
            tool_use = next(b for b in resp.content if b.type == "tool_use")
            result = execute_tool(tool_use.name, tool_use.input)

            messages.append({"role": "assistant", "content": resp.content})
            messages.append({
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": str(result),
                }],
            })

    return "Hit iteration limit without finishing."
```

---

## 7.3 MCP — Model Context Protocol (Deep Dive)

**MCP** is an open standard (originated by Anthropic, now adopted broadly) for connecting AI models to tools and data sources. Think of it as **USB for AI**: instead of every AI vendor and every tool building bespoke integrations, they all speak MCP.

### Architecture

```
                                  📧 Mail MCP server      ──▶  Tools · Resources · Prompts
                                  🐙 GitHub MCP server    ──▶  Tools · Resources · Prompts
🧠 Claude  ──MCP protocol──▶
                                  🗄️ Your DB MCP server   ──▶  Tools · Resources · Prompts
                                  📓 Notion MCP server    ──▶  Tools · Resources · Prompts
```

### Use cases

- **Public servers** — pre-built MCP servers for Gmail, Calendar, GitHub, Slack, Linear, Notion, etc.
- **Local servers** — run an MCP server on your machine that exposes a local DB, your Obsidian vault, your design files
- **Custom servers** — write one for your company's internal tools (deploy systems, customer DBs, etc.)

### Building a tiny MCP server (concept)

An MCP server exposes:

- **Tools** — actions Claude can take ("send email," "create issue")
- **Resources** — data Claude can read ("inbox.txt," "schema.sql")
- **Prompts** — pre-baked prompt templates users can invoke

The official MCP SDKs (Python, TypeScript) make writing one ~30 lines of code. See [modelcontextprotocol.io](https://modelcontextprotocol.io) for the spec and SDKs.

---

## 7.4 Computer Use

The **computer use** tool gives Claude a screen, keyboard, and mouse. It can:

- Take screenshots
- Move the cursor
- Click and type
- Read text from the screen

Use cases: web automation that doesn't have a clean API, legacy enterprise software, QA testing, accessibility tooling.

### Caveats

- It's **slower and pricier** than API-based tools — only use it when there's no API alternative
- **Sandbox it.** Run in a VM or container, not on your real desktop
- It's still an emerging capability — expect retries and weird failures
- Human review on consequential actions is essential

---

## 7.5 Evaluation — How Do You Know It Works?

When you change a prompt, how do you know things actually got better and not silently worse?

You build a **small eval set** and run it on every change.

### Minimum viable evaluation

```python
# eval_set.json
test_cases = [
    {"input": "I want a refund for order 12345", "expected_intent": "refund"},
    {"input": "When does my package arrive?",     "expected_intent": "shipping"},
    {"input": "How do I change my password?",    "expected_intent": "account"},
    # ... 20-50 of these
]

correct = 0
for case in test_cases:
    pred = classify(case["input"])  # your prompt + Claude
    if pred == case["expected_intent"]:
        correct += 1

print(f"Accuracy: {correct}/{len(test_cases)} = {correct/len(test_cases):.0%}")
```

### Levels of eval rigor

1. **Vibes** — "looks fine to me" (most people stop here, unfortunately)
2. **Spot-check set** — a handful of inputs you re-run by eye
3. **Automated metric** — exact match, regex, or rules
4. **LLM-as-judge** — use Claude itself to grade outputs against a rubric
5. **Human review** — the gold standard, but slow and expensive

For most production work, **levels 3 + 4 combined** are plenty.

### Anthropic's Workbench

The [Console Workbench](https://console.anthropic.com/workbench) lets you A/B prompts, save versions, and run them against test inputs. Use it instead of bouncing between scripts.

---

## 7.6 Reducing Hallucinations

Claude hallucinates less than it used to, but not zero. Defenses:

1. **Ground in retrieved context.** Don't ask "what's the policy?" — paste the policy and ask.
2. **Tell it to admit uncertainty.** *"If you don't know, say so. Don't guess."*
3. **Ask for citations.** *"For each claim, cite the source line from the document above."*
4. **Constrain the output schema.** Structured outputs (JSON schema) catch many drift errors.
5. **Verify with code.** For factual claims, do a search or DB lookup *after* Claude proposes — confirm before showing the user.
6. **Lower temperature** for factual tasks (0–0.3).

---

## 7.7 Structured Outputs

For anything that downstream code will parse, force structure.

```python
resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are an extraction engine. Return ONLY JSON matching the schema. No prose.",
    messages=[{
        "role": "user",
        "content": f"""Extract from the email below into this schema:
{{
  "from": string,
  "subject": string,
  "intent": "billing" | "support" | "sales" | "other",
  "urgency": 1 | 2 | 3 | 4 | 5,
  "needs_human": boolean
}}

EMAIL:
{email_text}"""
    }],
)

import json
data = json.loads(resp.content[0].text)
```

Or use the API's **strict tool use** feature, which guarantees the output matches your JSON schema (or raises an error).

---

## 7.8 Cost & Latency Optimization

The four levers:

1. **Pick the right model.** Don't use Opus where Haiku would do.
2. **Shorten prompts.** Every token costs money. Trim sample data, system prompts, scrollback.
3. **Cache static context.** Module 06.10 — easy 80%+ reduction on chatbots.
4. **Batch when you can.** 50% off for non-urgent jobs.

A common architecture — the **router pattern**:

```
                                              ┌──▶ 🚀 Haiku   (easy 90%)   ──▶ 💬 Answer
👤 User query  ──▶  ⚡ Router (cheap/fast) ──┤
                                              └──▶ 💎 Opus    (hard 10%)   ──▶ 💬 Answer
```

A **router prompt** (cheap, fast) decides which lane each query takes.

---

## 7.9 Safety Patterns for Production

If your app uses Claude on user-generated input, you should think about:

- **Prompt injection.** Users will try to override your system prompt. Defense: keep secrets out of the system prompt; treat user input as untrusted; never let user input control tool calls without validation.
- **Jailbreaks.** People will try to make Claude do harmful things. Anthropic's training handles most of this, but for sensitive applications, layer your own checks.
- **PII leakage.** Don't log raw conversations to public systems. Redact before storing.
- **Output filtering.** For some apps, run a second pass classifier on Claude's output before showing it to users.

---

## 7.10 The Anthropic Cookbook

Anthropic publishes a [Cookbook](https://github.com/anthropics/anthropic-cookbook) — Jupyter notebooks covering tool use, embeddings, RAG, evaluations, and more, with runnable code. Highly recommended next stop.

---

## ✅ Module 7 Checkpoint

You should now understand:

- Extended thinking and when it helps
- The agent loop pattern
- MCP as a standard for tool/data integration
- When computer use fits (and when it doesn't)
- How to evaluate prompts properly
- Production safety considerations

> 👉 **Next up:** [Module 08 — Real-World Projects](../08-real-world-projects/) — four full projects with code.

---

| ← Previous | 🏠 Home | Next → |
|---|---|---|
| [Module 06 — API Development](../06-api-development/) | [Course README](../README.md) | [Module 08 — Real-World Projects](../08-real-world-projects/) |
