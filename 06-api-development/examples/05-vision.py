"""
05 - Vision: send Claude an image
Claude can describe images, transcribe text, analyze charts, and more.

Usage:
    python 05-vision.py path/to/image.png
"""

import base64
import sys
from pathlib import Path
from anthropic import Anthropic

client = Anthropic()


def media_type_for(path: Path) -> str:
    return {
        ".png":  "image/png",
        ".jpg":  "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif":  "image/gif",
        ".webp": "image/webp",
    }[path.suffix.lower()]


def analyze(path: Path, question: str) -> str:
    img_b64 = base64.standard_b64encode(path.read_bytes()).decode()

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
                        "media_type": media_type_for(path),
                        "data": img_b64,
                    },
                },
                {"type": "text", "text": question},
            ],
        }],
    )
    return resp.content[0].text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 05-vision.py <image_path> [question]")
        sys.exit(1)

    image_path = Path(sys.argv[1])
    question = sys.argv[2] if len(sys.argv) > 2 else "Describe this image in detail. What's the most interesting thing about it?"

    print(analyze(image_path, question))
