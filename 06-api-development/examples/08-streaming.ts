/**
 * 08 - Streaming in TypeScript
 *
 * Setup:
 *   npm install @anthropic-ai/sdk
 *   export ANTHROPIC_API_KEY="sk-ant-..."
 *
 * Run:
 *   npx tsx 08-streaming.ts
 */

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const stream = await client.messages.stream({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: "Write a vivid 200-word story about a lighthouse keeper who befriends a whale.",
    },
  ],
});

process.stdout.write("Claude: ");

for await (const event of stream) {
  if (event.type === "content_block_delta" && event.delta.type === "text_delta") {
    process.stdout.write(event.delta.text);
  }
}

process.stdout.write("\n");

const final = await stream.finalMessage();
console.log(`\n--- Usage ---`);
console.log(`Input tokens:  ${final.usage.input_tokens}`);
console.log(`Output tokens: ${final.usage.output_tokens}`);
