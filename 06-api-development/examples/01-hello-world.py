"""
01 - Hello, Claude!
Your very first call to the Claude API.

Setup:
    pip install anthropic
    export ANTHROPIC_API_KEY="sk-ant-..."

Run:
    python 01-hello-world.py
"""

from anthropic import Anthropic

client = Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "In 3 short bullets, what is the Anthropic Claude API?",
        }
    ],
)

print(message.content[0].text)
print("\n--- Usage ---")
print(f"Input tokens:  {message.usage.input_tokens}")
print(f"Output tokens: {message.usage.output_tokens}")
