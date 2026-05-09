# 📊 The Visual Reference

> All the key visuals from the course in one place. Bookmark this page.

---

## 🗺️ Course flow

| | | | | |
|---|---|---|---|---|
| 👋 **01** Intro | → | 🚀 **02** Getting Started | → | 💡 **03** Prompting |
| | | | | ↓ |
| 🏗️ **08** Projects | ← | 🧪 **07** Advanced | ← | 🛠️ **04** Features |
| ↓ | | ↑ | | ↓ |
| 📚 **09** Resources | | ⚙️ **06** API | ← | 💻 **05** Claude Code |

---

## 🧠 The three Claude surfaces

```
👤 You
   │
   ├──▶ 💬 Claude.ai      (chat — web, mobile, desktop)  ─┐
   ├──▶ 💻 Claude Code    (terminal coding agent)        ─┼──▶ 🧠 Claude
   └──▶ ⚙️ Claude API     (build your own apps)          ─┘
```

---

## 💎 The model family

```
                          INTELLIGENCE
                              ▲
                       💎 Opus│
                              │
                              │  ⚡ Sonnet
                              │
                              │            🚀 Haiku
                              └──────────────────────────►
                                                  SPEED & COST
```

| | 💎 **Opus** | ⚡ **Sonnet** | 🚀 **Haiku** |
|---|---|---|---|
| Best for | Hardest tasks | Daily driver | High volume |
| Examples | Complex reasoning, agentic coding | 90% of production work | Classification, simple Q&A |

---

## 🎯 The 6 ingredients of a great prompt

```
                          🎯 Great Prompt
                                │
        ┌───────────┬───────────┼───────────┬───────────┐
        ▼           ▼           ▼           ▼           ▼
   🎭 ROLE     📋 CONTEXT    🎯 TASK    📐 CONSTRAINTS  📦 FORMAT  🌟 EXAMPLES
```

---

## 🛠️ Diagnosing a bad prompt

🚨 **Bad output? Walk down this list — first match wins.**

| If… | Then… |
|---|---|
| ❓ Task is **ambiguous** | Add: *"Ask me 3 clarifying questions first"* |
| 🎨 Wrong **tone or format** | Add: an **example** or a **format spec** |
| 🧩 Complex **multi-step** task | Break into a **chain** of smaller prompts |
| 🧠 Reasoning is **shallow** | Add: *"Think step-by-step before answering"* |
| 📋 Details are **missing** | Add: **role + context + constraints** |
| 🤷 Still bad? | Try a **different model** (Sonnet → Opus) |

---

## 📁 The Claude.ai feature universe

| Area | What's in it |
|---|---|
| 🏗️ **Workspace** | Projects · Custom Instructions · Style Presets |
| 📥 **Inputs** | File Uploads · Images · PDFs · Spreadsheets |
| 📤 **Outputs** | Artifacts · Code Execution · File Creation |
| 🌐 **Live data** | Web Search · Research Mode |
| 🧠 **Memory** | Cross-chat memory · Past chat search |
| 🔌 **Connectors** | Google Workspace · GitHub · Slack · Notion · 40+ more |
| 🎒 **Skills** | PowerPoint · Excel · Word · Custom Skills |

---

## 🔄 Claude Code's core loop

```
   👤 You describe a goal
            │
            ▼
   🧠 Claude plans  ◀──────────────┐
            │                      │
            ▼                      │
      Read-only or edit?           │
       │            │              │
       ▼            ▼              │
  📖 Read       📝 Propose         │
   files         edit              │
       │            │              │
       │            ▼              │
       │     👤 You approve?       │
       │      │           │        │
       │     yes          no ──▶ 💬 push back ──┘
       │      ▼
       │   ✏️ Apply
       │      │
       ▼      ▼
   💬 Report  ── Done? ──▶ ✅ Finished
                  │
                  no ──▶ (back to plan)
```

---

## 🤖 The agent loop (API)

```
🎯 Goal
   │
   ▼
🧠 Plan  ◀──────────────┐
   │                    │
   ▼                    │
  Tool needed?          │
   │           │        │
   yes         no       │
   ▼           ▼        │
🔧 Call tool   │        │
   │           │        │
   ▼           │        │
👀 Result      │        │
   │           │        │
   ▼           ▼        │
  Done?                 │
   │       │            │
   no  ────┘ (loop)     │
   │                    │
   yes                  │
   ▼                    │
💬 Answer ──▶ ✅ Done    │
```

---

## 🔌 Tool use sequence

```
1.  👤 User       ──▶  🧠 Claude     "Should I bring a jacket?"
2.  🧠 Claude     ──▶  💻 Your code   tool_use: get_weather("Paris")
3.  💻 Your code  ──▶  💻 Your code   calls weather API
4.  💻 Your code  ──▶  🧠 Claude      tool_result: {temp: 14, drizzle}
5.  🧠 Claude     ──▶  👤 User        "Yes — 14°C, drizzly. Light jacket."
```

---

## 🌐 MCP architecture

> 🧠 **Claude** &nbsp; ──MCP──▶ &nbsp; 📧 Mail · 🐙 GitHub · 🗄️ Database · 📓 Notion · ➕ any other MCP server

Each server exposes **tools** (actions Claude can take), **resources** (data Claude can read), and **prompts** (templates).

---

## 💰 The cost-saving router pattern

```
                                              ┌──▶ 🚀 Haiku   (easy 90%)   ──▶ 💬 Answer
👤 User query  ──▶  ⚡ Router (cheap/fast) ──┤
                                              └──▶ 💎 Opus    (hard 10%)   ──▶ 💬 Answer
```

---

## 🚀 Production checklist

Walk top to bottom before shipping any Claude-powered app:

| # | Step | What to check |
|---|---|---|
| 1 | 🔒 Secrets in vault | No keys in code, repo, or logs |
| 2 | ⏱️ Rate-limit endpoint | Don't expose raw API to users |
| 3 | 💰 Cost caps + alerting | Anomaly alerts on token spend |
| 4 | 🔁 Retries with backoff | Handle 429s and 5xxs gracefully |
| 5 | 📝 Logging + PII redaction | Audit trail, but no leaks |
| 6 | 🧪 Eval set | Regression tests on every prompt change |
| 7 | 🛡️ Fallback model | Survive model outages |
| 8 | 💾 Prompt caching | Static context > 1024 tokens? Cache it |
| 9 | 🚀 **Ship it!** | |

---

## 📚 The four projects (Module 8)

| # | Project | Skills |
|---|---|---|
| 1️⃣ | 💬 **CLI Chatbot** | Streaming · multi-turn · system prompts |
| 2️⃣ | 📄 **Doc Q&A** | RAG · caching · file parsing |
| 3️⃣ | 🔍 **Research Agent** | Tool use · planning · web fetch |
| 4️⃣ | 🤖 **Code Reviewer** | Structured outputs · git integration · JSON schema |

---

> 👉 Want this interactively? Open [`hub.html`](../hub.html) in your browser.
