# Code Examples — Module 06

Working code for everything in [Module 06 — Building with the Claude API](../README.md).

## Setup

```bash
# Python
pip install anthropic

# TypeScript
npm install @anthropic-ai/sdk
npm install -D tsx typescript

# Both: set your API key
export ANTHROPIC_API_KEY="sk-ant-..."
```

## Files

| File | Topic |
|---|---|
| `01-hello-world.py` | First API call |
| `02-streaming.py` | Stream tokens as they generate |
| `03-multi-turn.py` | Tiny CLI chatbot with history |
| `04-tool-use.py` | Function calling / agent loop |
| `05-vision.py` | Send Claude an image |
| `06-pdf.py` | Send Claude a PDF |
| `07-prompt-caching.py` | Cut costs ~90% on repeated context |
| `08-streaming.ts` | Streaming in TypeScript |
| `09-tool-use.ts` | Tool use in TypeScript |

Run any Python file with `python <file>`. Run TypeScript files with `npx tsx <file>`.
