"""
Project 1 — A streaming CLI chatbot with personality presets.

Setup:
    pip install anthropic
    export ANTHROPIC_API_KEY="sk-ant-..."

Run:
    python project1_chatbot.py [persona]

Personas: shakespeare | pirate | engineer | (default friendly)
"""

import sys
from anthropic import Anthropic

PERSONAS = {
    "shakespeare": "Thou art a witty assistant who speaketh in early modern English. Use 'thee', 'thou', 'forsooth'. Keep answers under 100 words.",
    "pirate":      "You're a swashbuckling pirate AI. Use 'arrr', nautical metaphors, and pirate slang. Be helpful but in character.",
    "engineer":    "You are a senior staff engineer. Direct, terse, pragmatic. Skip pleasantries. Code blocks only when needed.",
    "default":     "You are a warm, helpful assistant. Keep answers conversational and clear.",
}

client = Anthropic()
persona_key = sys.argv[1] if len(sys.argv) > 1 else "default"
system_prompt = PERSONAS.get(persona_key, PERSONAS["default"])

history = []
print(f"Chatting as: {persona_key}. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"quit", "exit", "q"}:
        break
    if not user_input:
        continue

    history.append({"role": "user", "content": user_input})

    print("Claude: ", end="", flush=True)
    full_text = ""

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system_prompt,
        messages=history,
    ) as stream:
        for chunk in stream.text_stream:
            print(chunk, end="", flush=True)
            full_text += chunk

    print("\n")
    history.append({"role": "assistant", "content": full_text})
