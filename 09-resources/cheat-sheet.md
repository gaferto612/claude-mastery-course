# 🧾 The One-Page Cheat Sheet

Print this. Tape it next to your monitor.

---

## The 6 ingredients of a great prompt

| | |
|---|---|
| 🎭 **Role** | Who Claude is |
| 📋 **Context** | What's the situation |
| 🎯 **Task** | The exact ask |
| 📐 **Constraints** | Length / tone / what to avoid |
| 📦 **Format** | The shape of the output |
| 🌟 **Example** | A reference of "good" |

---

## The 5 power moves

1. **Ask Claude to ask you 3 questions first** for ambiguous tasks.
2. **Use XML tags** for structured input: `<context>`, `<draft>`, `<task>`.
3. **Show, don't tell** — paste an example of the tone/format you want.
4. **Iterate, don't restart** — *"shorten paragraph 2"*, not *"do it again."*
5. **Push back** — *"What would you change to make this 50% better?"*

---

## Which model

```
Hard reasoning / coding / agents ──► Opus
Daily production work ───────────► Sonnet (default)
High volume / latency-sensitive ──► Haiku
```

---

## API one-liner

```python
client.messages.create(
    model="claude-sonnet-4-6", max_tokens=1024,
    system="...", messages=[{"role": "user", "content": "..."}]
)
```

---

## Cost-saving knobs

- ✂️ **Smaller model** when possible
- 💾 **Prompt caching** for static system context
- 📦 **Batch API** for non-urgent jobs (50% off)
- 🧹 **Trim prompts** — every token costs

---

## When to use which surface

| | Use |
|---|---|
| Thinking, writing, exploration | **Claude.ai** |
| Multi-file code work | **Claude Code** |
| Building products | **API** |

---

## Red flags to fix in your prompts

- ⚠️ One-line prompts ("write me X")
- ⚠️ Vague feedback ("make it better")
- ⚠️ Stuffing 10 tasks in one message
- ⚠️ Repeating context every chat (use a Project)
- ⚠️ Accepting the first answer
