"""
04 - Tool use (function calling)
Give Claude a tool, let it decide when to call it, and feed the result back.

This example: Claude can look up the weather. It will only call the tool
when the user actually asks something weather-related.
"""

import json
from anthropic import Anthropic

client = Anthropic()

# 1. Define your tool(s)
tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a city. Use this when the user asks about weather, what to wear, or whether to go outside.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "Name of the city, e.g. 'Paris'"},
                "unit": {"type": "string", "enum": ["c", "f"], "default": "c"},
            },
            "required": ["city"],
        },
    }
]


# 2. Implement the actual tool
def get_weather(city: str, unit: str = "c") -> dict:
    """Pretend weather API. Replace with a real call."""
    fake_db = {
        "Paris": {"temp": 14, "conditions": "drizzly"},
        "Tokyo": {"temp": 22, "conditions": "clear"},
        "New York": {"temp": 8, "conditions": "windy"},
    }
    data = fake_db.get(city, {"temp": 20, "conditions": "unknown"})
    return {"city": city, "unit": unit, **data}


# 3. The agent loop
def agent(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]

    while True:
        resp = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=tools,
            messages=messages,
        )

        # If Claude wants a tool call, fulfill it
        if resp.stop_reason == "tool_use":
            tool_use_block = next(b for b in resp.content if b.type == "tool_use")
            print(f"  [tool] calling {tool_use_block.name} with {tool_use_block.input}")
            result = get_weather(**tool_use_block.input)
            print(f"  [tool] result: {result}")

            messages.append({"role": "assistant", "content": resp.content})
            messages.append({
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": tool_use_block.id,
                    "content": json.dumps(result),
                }],
            })
            continue

        # Otherwise we have the final answer
        return next(b.text for b in resp.content if b.type == "text")


if __name__ == "__main__":
    for question in [
        "What's the capital of France?",                      # no tool needed
        "Should I bring a jacket to Paris today?",            # weather tool
        "Compare the weather in Tokyo and New York for me.",  # tool called twice
    ]:
        print(f"\nUser: {question}")
        print(f"Claude: {agent(question)}")
