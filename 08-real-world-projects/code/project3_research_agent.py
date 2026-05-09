"""
Project 3 — A tool-using research agent.

This uses placeholder web tools. To make it real, swap in:
- Tavily Search API (https://tavily.com)
- SerpAPI / Brave Search / Anthropic web_search server tool
- requests + BeautifulSoup + readability for fetch_page

Run:
    python project3_research_agent.py "your research question"
"""

import json
import sys
from anthropic import Anthropic

client = Anthropic()

tools = [
    {
        "name": "web_search",
        "description": "Search the web. Returns a list of {title, snippet, url}.",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    },
    {
        "name": "fetch_page",
        "description": "Fetch the readable text of a URL.",
        "input_schema": {
            "type": "object",
            "properties": {"url": {"type": "string"}},
            "required": ["url"],
        },
    },
]


# --- Replace these stubs with real implementations ---
def web_search(query: str):
    return [
        {"title": f"Result A for '{query}'", "snippet": "Example snippet A", "url": f"https://example.com/a/{query.replace(' ', '-')}"},
        {"title": f"Result B for '{query}'", "snippet": "Example snippet B", "url": f"https://example.com/b/{query.replace(' ', '-')}"},
    ]


def fetch_page(url: str):
    return f"[Pretend body of {url}. In a real implementation, fetch and clean.]"


TOOL_FUNCS = {"web_search": web_search, "fetch_page": fetch_page}


def research(question: str, max_steps: int = 15) -> str:
    messages = [{"role": "user", "content": (
        f"Research the following question and write a 400-word report with citations.\n\n"
        f"QUESTION: {question}\n\n"
        f"Process: (1) search, (2) fetch the most promising 2-3 pages, "
        f"(3) synthesize. Cite each claim like [1], [2] and list sources at the end."
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
            print(f"  step {step+1}: {tu.name}({tu.input})", file=sys.stderr)
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

    return "Hit step limit without finishing."


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python project3_research_agent.py "your question"')
        sys.exit(1)
    print(research(" ".join(sys.argv[1:])))
