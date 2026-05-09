"""
02 - Streaming responses
Stream tokens as they're generated — better UX for chat apps.
"""

from anthropic import Anthropic

client = Anthropic()

print("Claude: ", end="", flush=True)

with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Write a vivid 200-word story about a lighthouse keeper who befriends a whale."}
    ],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

print()  # final newline
