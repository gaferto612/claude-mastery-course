"""
03 - Multi-turn conversations
Claude is stateless — you maintain history. This is a tiny CLI chatbot.
"""

from anthropic import Anthropic

client = Anthropic()

SYSTEM_PROMPT = """You are a friendly Python tutor. Keep answers short
(under 120 words) unless the student explicitly asks for depth. Use
small code examples whenever they help."""

history = []


def chat(user_msg: str) -> str:
    history.append({"role": "user", "content": user_msg})
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=history,
    )
    reply = resp.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply


if __name__ == "__main__":
    print("Tiny Python tutor. Type 'quit' to exit.\n")
    while True:
        user = input("You: ").strip()
        if user.lower() in {"quit", "exit", "q"}:
            break
        if not user:
            continue
        print(f"\nClaude: {chat(user)}\n")
