# Module 08 — Real-World Projects

> **Goal:** Build four end-to-end projects that show how everything in this course comes together.

⏱️ **~2-3 hours** &nbsp;&nbsp;&nbsp; 📊 **4 architecture diagrams** &nbsp;&nbsp;&nbsp; 💻 **4 standalone scripts**

Each project is small enough to finish in an afternoon but realistic enough to extend into something you'd actually use.

---

## 🚀 The four projects — at a glance

| # | Project | Skills covered |
|---|---|---|
| 1️⃣ | **CLI Chatbot with Personality** | 🛠️ Streaming · multi-turn · system prompts |
| 2️⃣ | **Document Q&A (Mini RAG)** | 🛠️ RAG basics · file parsing · prompt caching |
| 3️⃣ | **Research Agent** | 🛠️ Tool use · multi-step planning · web fetch |
| 4️⃣ | **Code Reviewer Bot** | 🛠️ Structured outputs · git integration · JSON schema |

---

## Project 1 — A CLI Chatbot with Personality

A terminal chatbot that remembers context within a session and has a configurable personality. You can swap "shakespeare," "pirate," or "no-nonsense engineer" by changing one variable.

### Code: `project1_chatbot.py`

```python
"""
A streaming CLI chatbot with personality presets.
Run: python project1_chatbot.py [persona]
Personas: shakespeare | pirate | engineer | (default friendly)
"""

import sys
from anthropic import Anthropic

PERSONAS = {
    "shakespeare": "Thou art a witty assistant who speaketh in early modern English. Use 'thee', 'thou', 'forsooth'. Keep answers under 100 words.",
    "pirate":      "You're a swashbuckling pirate AI. Use 'arrr', nautical metaphors, and pirate slang. Be helpful but in character.",
    "engineer":    "You are a senior staff engineer. Direct, terse, pragmatic. Skip pleasantries. Code blocks only when needed.",
    "default":     "You are a warm, helpful assistant. Keep answers conversational and clear.",
}

client = Anthropic()
persona_key = sys.argv[1] if len(sys.argv) > 1 else "default"
system_prompt = PERSONAS.get(persona_key, PERSONAS["default"])

history = []
print(f"Chatting as: {persona_key}. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"quit", "exit", "q"}:
        break
    if not user_input:
        continue

    history.append({"role": "user", "content": user_input})

    print("Claude: ", end="", flush=True)
    full_text = ""

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system_prompt,
        messages=history,
    ) as stream:
        for chunk in stream.text_stream:
            print(chunk, end="", flush=True)
            full_text += chunk

    print("\n")
    history.append({"role": "assistant", "content": full_text})
```

**Try it:**
```bash
python project1_chatbot.py pirate
You: Help me write a polite email to my landlord
```

**Extend it:**
- Save conversation history to a JSON file so sessions persist
- Add a `/persona <name>` command to switch mid-conversation
- Add token counting and cost tracking with `/cost`

---

## Project 2 — Document Q&A (Mini RAG)

Drop a folder of `.txt`/`.md`/`.pdf` files in, then ask questions. The simplest possible RAG with prompt caching to keep costs low.

### Architecture

```
📁 ./docs (PDFs, MDs, TXTs)  ──▶  📤 Extract  ──▶  💾 Cached corpus
                                                          │
                                                          ▼
👤 User question  ──────────────────────────▶  ⚙️ Claude API  ──▶  💬 Answer
                                                                     (with citations)
```

### Code: `project2_doc_qa.py`

```python
"""
Tiny doc Q&A. Drop files into ./docs/ then ask questions.
Run: python project2_doc_qa.py "What is our refund policy?"
"""

import sys
import base64
from pathlib import Path
from anthropic import Anthropic

client = Anthropic()
DOCS_DIR = Path("docs")


def load_corpus() -> str:
    """Read every text file in ./docs/ and concatenate."""
    parts = []
    for path in sorted(DOCS_DIR.glob("*")):
        if path.suffix.lower() in {".txt", ".md"}:
            parts.append(f"\n\n=== {path.name} ===\n{path.read_text()}")
    return "".join(parts)


def collect_pdfs() -> list:
    """Return PDF doc blocks for the API."""
    blocks = []
    for path in sorted(DOCS_DIR.glob("*.pdf")):
        blocks.append({
            "type": "document",
            "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": base64.standard_b64encode(path.read_bytes()).decode(),
            },
        })
    return blocks


def ask(question: str) -> str:
    text_corpus = load_corpus()
    pdf_blocks = collect_pdfs()

    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": "You answer questions strictly from the documents provided. If the answer isn't in them, say so. Cite filenames when you can.",
            },
            {
                "type": "text",
                "text": f"DOCUMENT CORPUS:{text_corpus}",
                "cache_control": {"type": "ephemeral"},
            },
        ],
        messages=[{
            "role": "user",
            "content": [
                *pdf_blocks,
                {"type": "text", "text": question},
            ],
        }],
    )
    return resp.content[0].text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python project2_doc_qa.py "your question"')
        sys.exit(1)
    print(ask(sys.argv[1]))
```

**Extend it:**
- For huge corpora, add a real vector DB (Chroma, LanceDB) and retrieve only the top-K relevant chunks
- Add streaming for snappier UX
- Build a small Streamlit/Flask UI

---

## Project 3 — Research Agent

Give it a question, it searches the web, fetches pages, and writes a sourced report.

### Code: `project3_research_agent.py`

```python
"""
A simple research agent. Uses a fake web tool — swap in a real
search/fetch API (Brave, Serper, Tavily, or Anthropic's web_search).
"""

import json
from anthropic import Anthropic

client = Anthropic()

# --- Tools ---
tools = [
    {
        "name": "web_search",
        "description": "Search the web. Returns a list of results with title, snippet, and url.",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    },
    {
        "name": "fetch_page",
        "description": "Fetch the readable text content of a URL.",
        "input_schema": {
            "type": "object",
            "properties": {"url": {"type": "string"}},
            "required": ["url"],
        },
    },
]

# Replace these with real implementations (Tavily, SerpAPI, requests + readability, etc.)
def web_search(query: str):
    return [
        {"title": f"Fake result for {query}", "snippet": "Pretend snippet", "url": f"https://example.com/{query.replace(' ', '-')}"}
    ]

def fetch_page(url: str):
    return f"Pretend page content for {url}"

TOOL_FUNCS = {"web_search": web_search, "fetch_page": fetch_page}


def research(question: str, max_steps: int = 15) -> str:
    messages = [{"role": "user", "content": (
        f"Research the following question and write a 400-word report with citations.\n\n"
        f"QUESTION: {question}\n\n"
        f"Process: search, then fetch the most promising 2-3 pages, then synthesize. "
        f"Cite each claim like [1], [2] and list sources at the end."
    )}]

    for step in range(max_steps):
        resp = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2048,
            tools=tools,
            messages=messages,
        )

        if resp.stop_reason == "tool_use":
            tu = next(b for b in resp.content if b.type == "tool_use")
            print(f"  step {step+1}: {tu.name}({tu.input})")
            result = TOOL_FUNCS[tu.name](**tu.input)
            messages.append({"role": "assistant", "content": resp.content})
            messages.append({
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": tu.id,
                    "content": json.dumps(result),
                }],
            })
            continue

        return next(b.text for b in resp.content if b.type == "text")

    return "Research stopped at iteration cap."


if __name__ == "__main__":
    print(research("What are the main differences between Claude Opus and Sonnet?"))
```

**Extend it:**
- Plug in a real search API (Tavily is the easiest)
- Add a "fact-check" pass at the end that verifies claims against sources
- Cache fetched pages to avoid duplicate fetches

---

## Project 4 — Code Reviewer Bot

Reads a git diff, returns structured review comments. Plug into a CI step or git hook.

### Code: `project4_code_review.py`

```python
"""
Code review bot. Reads a diff (from stdin or git) and returns
structured review comments as JSON.

Usage:
    git diff main...HEAD | python project4_code_review.py
"""

import json
import subprocess
import sys
from anthropic import Anthropic

client = Anthropic()


REVIEW_SYSTEM = """You are a senior staff engineer doing a code review.
You produce concise, useful feedback — never nitpicks, never compliments.

Return ONLY a JSON array of review items, each shaped like:
{
  "file": "path/to/file.py",
  "line": 42,
  "severity": "critical" | "major" | "minor",
  "category": "bug" | "security" | "performance" | "design" | "style",
  "comment": "What's wrong and how to fix it (1-2 sentences)."
}

Skip the array entirely if the diff is fine. NO prose, NO markdown, JSON only."""


def get_diff() -> str:
    if not sys.stdin.isatty():
        return sys.stdin.read()
    # Fallback: diff against main
    return subprocess.check_output(["git", "diff", "main...HEAD"]).decode()


def review(diff: str) -> list:
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=REVIEW_SYSTEM,
        messages=[{"role": "user", "content": f"DIFF:\n```diff\n{diff}\n```"}],
    )
    text = resp.content[0].text.strip()
    # Be tolerant if Claude wraps in code fences
    if text.startswith("```"):
        text = text.split("```")[1].split("```")[0]
        if text.startswith("json"):
            text = text[4:]
    return json.loads(text)


def render(items: list):
    if not items:
        print("✅ No issues found.")
        return
    print(f"Found {len(items)} issue(s):\n")
    for item in items:
        emoji = {"critical": "🚨", "major": "⚠️ ", "minor": "💡"}.get(item["severity"], "•")
        print(f"{emoji}  {item['file']}:{item['line']} [{item['category']}]")
        print(f"   {item['comment']}\n")


if __name__ == "__main__":
    diff = get_diff()
    if not diff.strip():
        print("No diff to review.")
        sys.exit(0)
    render(review(diff))
```

**Extend it:**
- Post comments back to a GitHub PR via the GitHub API
- Add a config file with project-specific rules ("we always use snake_case," "no print statements in committed code")
- Use **strict tool use** to guarantee JSON output instead of post-processing

---

## 🎓 What you've now built

By finishing this module you've covered:

- ✅ Multi-turn conversation with personas
- ✅ Document grounding with caching
- ✅ Tool-using agents
- ✅ Structured outputs for automation

Pick one project, **make it yours** — different topic, different tools, real data — and put it in your portfolio.

> 👉 **Next up:** [Module 09 — Resources](../09-resources/) — cheat sheets, links, glossary.

---

| ← Previous | 🏠 Home | Next → |
|---|---|---|
| [Module 07 — Advanced Techniques](../07-advanced-techniques/) | [Course README](../README.md) | [Module 09 — Resources](../09-resources/) |
