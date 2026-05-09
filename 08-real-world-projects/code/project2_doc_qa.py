"""
Project 2 — Tiny document Q&A with prompt caching.

Drop .txt, .md, or .pdf files into ./docs/ then ask questions.

Setup:
    pip install anthropic
    mkdir docs && put your files in there

Run:
    python project2_doc_qa.py "What is our refund policy?"
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
    if not DOCS_DIR.exists():
        return ""
    for path in sorted(DOCS_DIR.glob("*")):
        if path.suffix.lower() in {".txt", ".md"}:
            parts.append(f"\n\n=== {path.name} ===\n{path.read_text()}")
    return "".join(parts)


def collect_pdfs() -> list:
    """Return PDF document blocks for the API."""
    blocks = []
    if not DOCS_DIR.exists():
        return blocks
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

    if not text_corpus and not pdf_blocks:
        return "No documents found in ./docs/. Add some .txt, .md, or .pdf files first."

    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": "You answer questions strictly from the documents provided. If the answer isn't in them, say so clearly. Cite filenames when you can.",
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
