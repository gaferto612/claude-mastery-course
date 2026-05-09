"""
07 - Prompt caching
Cache long, static context (system prompt, knowledge base, big document)
so subsequent calls within ~5 minutes pay ~10% the normal input price.
"""

from anthropic import Anthropic

client = Anthropic()

# Pretend this is a long product manual (must be > ~1024 tokens to be cacheable).
PRODUCT_MANUAL = """
[ Imagine 50 pages of detailed product documentation here.
  This block is what we want to cache so repeated questions
  don't re-bill us for the same input tokens. ]
""" * 50  # padded so it's actually large enough


def ask(question: str):
    return client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system=[
            {
                "type": "text",
                "text": "You are a customer support agent for AcmeCorp. Answer using only the manual below.",
            },
            {
                "type": "text",
                "text": PRODUCT_MANUAL,
                "cache_control": {"type": "ephemeral"},  # ← cache this block
            },
        ],
        messages=[{"role": "user", "content": question}],
    )


if __name__ == "__main__":
    print("First call (writes the cache):")
    r1 = ask("How do I reset my AcmeCorp 3000 device?")
    print(r1.content[0].text)
    print(f"  cache_creation_input_tokens: {getattr(r1.usage, 'cache_creation_input_tokens', 0)}")
    print(f"  cache_read_input_tokens:     {getattr(r1.usage, 'cache_read_input_tokens', 0)}")

    print("\nSecond call (reads the cache — much cheaper):")
    r2 = ask("What's the warranty period?")
    print(r2.content[0].text)
    print(f"  cache_creation_input_tokens: {getattr(r2.usage, 'cache_creation_input_tokens', 0)}")
    print(f"  cache_read_input_tokens:     {getattr(r2.usage, 'cache_read_input_tokens', 0)}")
