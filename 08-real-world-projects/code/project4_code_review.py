"""
Project 4 — Code review bot.

Reads a git diff and returns structured review comments.

Setup:
    pip install anthropic

Run:
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

Skip the array entirely (return []) if the diff is fine. NO prose, NO markdown — JSON only."""


def get_diff() -> str:
    if not sys.stdin.isatty():
        return sys.stdin.read()
    try:
        return subprocess.check_output(["git", "diff", "main...HEAD"]).decode()
    except subprocess.CalledProcessError:
        return ""


def review(diff: str) -> list:
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=REVIEW_SYSTEM,
        messages=[{"role": "user", "content": f"DIFF:\n```diff\n{diff}\n```"}],
    )
    text = resp.content[0].text.strip()

    # Tolerate code-fenced output
    if text.startswith("```"):
        text = text.strip("`").strip()
        if text.startswith("json"):
            text = text[4:].strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print("Couldn't parse JSON; raw response was:\n" + text, file=sys.stderr)
        return []


def render(items: list):
    if not items:
        print("✅ No issues found.")
        return
    print(f"Found {len(items)} issue(s):\n")
    for item in items:
        emoji = {"critical": "🚨", "major": "⚠️ ", "minor": "💡"}.get(item.get("severity"), "•")
        print(f"{emoji}  {item.get('file', '?')}:{item.get('line', '?')} [{item.get('category', '?')}]")
        print(f"   {item.get('comment', '')}\n")


if __name__ == "__main__":
    diff = get_diff()
    if not diff.strip():
        print("No diff to review. Pipe one in: `git diff main...HEAD | python project4_code_review.py`")
        sys.exit(0)
    render(review(diff))
