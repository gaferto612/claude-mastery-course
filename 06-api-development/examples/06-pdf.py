"""
06 - PDF support
Send a PDF directly to Claude — no parsing layer needed.

Usage:
    python 06-pdf.py path/to/document.pdf
"""

import base64
import sys
from pathlib import Path
from anthropic import Anthropic

client = Anthropic()


def summarize_pdf(path: Path) -> str:
    pdf_b64 = base64.standard_b64encode(path.read_bytes()).decode()

    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_b64,
                    },
                },
                {
                    "type": "text",
                    "text": (
                        "Read this document and produce:\n"
                        "1. A 3-sentence executive summary\n"
                        "2. The 5 most important points (bullets)\n"
                        "3. Anything that stands out as risky, surprising, or worth flagging"
                    ),
                },
            ],
        }],
    )
    return resp.content[0].text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 06-pdf.py <pdf_path>")
        sys.exit(1)
    print(summarize_pdf(Path(sys.argv[1])))
