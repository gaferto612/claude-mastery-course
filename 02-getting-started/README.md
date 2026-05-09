# Module 02 — Getting Started with Claude

> **Goal:** Get an account, understand the plans, install the apps, and have your first real conversation.

⏱️ **~15 minutes** &nbsp;&nbsp;&nbsp; 📊 **2 diagrams** &nbsp;&nbsp;&nbsp; 🎯 **Free account is enough**

---

## 2.0 Your journey in this module

```
📝 Sign up   ──▶   💎 Pick plan   ──▶   📱 Install apps   ──▶   ⚙️ Tune settings   ──▶   💬 First chat
```

---

## 2.1 Creating Your Claude Account

1. Go to **[claude.ai](https://claude.ai)**
2. Sign up with email, Google, or Apple
3. Verify your email and you're in

That's it. You can start chatting on the **Free** tier with no credit card.

---

## 2.2 Free vs. Pro vs. Max vs. Team — Which One Do You Need?

> **Quick map:** 🆓 Free  ·  💎 Pro  ·  ⚡ Max  ·  👥 Team  ·  🏢 Enterprise — going from casual to large-org. Detailed comparison below 👇

| Plan | Best for | What you get |
|---|---|---|
| **Free** | Casual users | Daily message limits, web/mobile, basic features |
| **Pro** | Power users | ~5x more usage, bigger models, Projects, larger files, web search |
| **Max** | Heavy users | Significantly higher limits than Pro, priority access |
| **Team** | Small businesses | Pro features + central billing + admin + collaboration |
| **Enterprise** | Larger orgs | SSO, SCIM, advanced security, custom data retention |

> 📌 Pricing and limits change. Always check the current page at [anthropic.com/pricing](https://www.anthropic.com/pricing) and [support.claude.com](https://support.claude.com).

**My honest take:**
- Start **Free** for a few days to see if it clicks
- Upgrade to **Pro** the moment message limits start interrupting your work
- **Max** only if you're consistently hitting Pro's ceiling

---

## 2.3 Installing the Apps

Claude has three places to live:

### Web
Just visit [claude.ai](https://claude.ai) in any modern browser. No install needed.

### Mobile
- **iOS:** [App Store — Claude](https://apps.apple.com/app/claude/id6473753684)
- **Android:** [Google Play — Claude](https://play.google.com/store/apps/details?id=com.anthropic.claude)

The mobile app supports voice input, photo uploads from your camera, and shares the same conversations as the web.

### Desktop
A native macOS and Windows desktop app is available — search "Claude desktop" or grab it from claude.ai. The desktop app supports **keyboard shortcuts, system-wide hotkeys, and screenshot uploads** that make it noticeably faster than browser tabs.

---

## 2.4 The Claude.ai Interface — A Tour

When you open Claude.ai, here's what you're looking at:

```
┌──────────────────────────────────────────────────────────┐
│  [☰]                                          [Settings] │  ← Sidebar toggle, profile
│                                                          │
│  + New chat                                              │
│  📁 Projects                                             │  ← Persistent workspaces
│  🕒 Recents                                              │  ← Conversation history
│  ⭐ Starred                                              │
│                                                          │
│  ────────────────────────────────────────────────────    │
│                                                          │
│              Hello! How can I help you today?           │
│                                                          │
│  [Type a message...]              [📎] [🌐] [🔬] [⏎]    │  ← Attach, search, research
└──────────────────────────────────────────────────────────┘
```

Key elements:

- **The composer** — where you type. You can attach files, toggle web search, or kick off a Research task.
- **Model picker** — switch between Sonnet, Opus, etc., usually near the top of the chat.
- **Style picker** — choose tones like *Concise*, *Explanatory*, *Formal*, or set a custom style.
- **Settings** — manage memory, profile info, integrations, data export.

---

## 2.5 Your First Real Conversation

Open a new chat and try this. Don't just paste it — read it, then send it. Watch what Claude does.

```
I'm a [your role, e.g. "marketing manager at a B2B SaaS company"].
I have a 30-minute presentation tomorrow on [your topic, e.g. "our Q3
pipeline strategy"]. Help me prepare.

Start by asking me 3-5 sharp questions to understand the audience,
the key message, and what success looks like. After I answer,
draft an outline.
```

**Why this prompt works** (we'll cover this fully in Module 03):

- ✅ **Role** — Claude knows who you are
- ✅ **Context** — what's the situation
- ✅ **Specific task** — clear deliverable
- ✅ **Process** — how to do it (ask first, then draft)

Compare that to: *"help me with my presentation"* — which gives Claude no signal at all.

---

## 2.6 Quick Settings Worth Knowing

Open **Settings** and look at:

- **Profile** — give Claude a short bio about you. It'll personalize replies (e.g. your role, your writing style preferences, projects you're working on).
- **Memory** — toggle whether Claude can remember information across chats. Useful for long-running work; disable if you want each chat to be a clean slate.
- **Connectors / Integrations** — connect Google Drive, Gmail, Calendar, GitHub, Slack, and more. Claude can then read your real data when relevant.
- **Data controls** — manage chat history, training opt-outs (your choice), and exports.

---

## 2.7 Five Habits of Effective Claude Users

After you've used Claude for a week, the people who get the most out of it tend to share these habits:

1. **Tell Claude who you are and what you're doing.** Context compounds.
2. **Use Projects** for anything you'll work on more than once.
3. **Iterate, don't redo.** If a reply is 70% right, ask Claude to revise the 30% — don't start over.
4. **Treat Claude like a smart colleague,** not a search engine. Ask follow-ups. Push back. Disagree.
5. **Save your best prompts.** Build a personal library of patterns that work for you.

---

## ✅ Module 2 Checkpoint

You should now have:

- ✅ A working Claude.ai account
- ✅ Mobile and/or desktop app installed (optional but recommended)
- ✅ Profile filled in with a short bio
- ✅ Had at least one real conversation using the structured prompt above

> 👉 **Next up:** [Module 03 — Prompt Engineering](../03-prompting/) — where the real leverage is.

---

| ← Previous | 🏠 Home | Next → |
|---|---|---|
| [Module 01 — Introduction](../01-introduction/) | [Course README](../README.md) | [Module 03 — Prompt Engineering](../03-prompting/) |
