/**
 * 09 - Tool use in TypeScript
 *
 * Same idea as 04-tool-use.py — Claude calls a weather function
 * when (and only when) the user asks something weather-related.
 */

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const tools: Anthropic.Tool[] = [
  {
    name: "get_weather",
    description: "Get the current weather for a city. Use this when the user asks about weather, what to wear, or whether to go outside.",
    input_schema: {
      type: "object",
      properties: {
        city: { type: "string", description: "Name of the city, e.g. 'Paris'" },
        unit: { type: "string", enum: ["c", "f"] },
      },
      required: ["city"],
    },
  },
];

function getWeather(city: string, unit: "c" | "f" = "c") {
  const fakeDb: Record<string, { temp: number; conditions: string }> = {
    Paris: { temp: 14, conditions: "drizzly" },
    Tokyo: { temp: 22, conditions: "clear" },
    "New York": { temp: 8, conditions: "windy" },
  };
  const data = fakeDb[city] ?? { temp: 20, conditions: "unknown" };
  return { city, unit, ...data };
}

async function agent(userMessage: string): Promise<string> {
  const messages: Anthropic.MessageParam[] = [
    { role: "user", content: userMessage },
  ];

  while (true) {
    const resp = await client.messages.create({
      model: "claude-sonnet-4-6",
      max_tokens: 1024,
      tools,
      messages,
    });

    if (resp.stop_reason === "tool_use") {
      const toolUse = resp.content.find((b) => b.type === "tool_use") as Anthropic.ToolUseBlock;
      console.log(`  [tool] calling ${toolUse.name} with`, toolUse.input);
      const result = getWeather((toolUse.input as any).city, (toolUse.input as any).unit);
      console.log(`  [tool] result:`, result);

      messages.push({ role: "assistant", content: resp.content });
      messages.push({
        role: "user",
        content: [
          {
            type: "tool_result",
            tool_use_id: toolUse.id,
            content: JSON.stringify(result),
          },
        ],
      });
      continue;
    }

    const textBlock = resp.content.find((b) => b.type === "text") as Anthropic.TextBlock;
    return textBlock.text;
  }
}

for (const q of [
  "What's the capital of France?",
  "Should I bring a jacket to Paris today?",
  "Compare the weather in Tokyo and New York for me.",
]) {
  console.log(`\nUser: ${q}`);
  console.log(`Claude: ${await agent(q)}`);
}
