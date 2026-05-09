# 📚 The Prompt Cookbook

A working library of prompts you can copy, paste, and adapt. Organized by use case.

> Tip: each prompt has bracketed `[placeholders]` you'll need to fill in. Don't skip them — they're where the leverage is.

---

## ✍️ Writing

### 1. The "blank page killer"
```
I need to write [type of doc] about [topic]. Before drafting, do this:
1. Brainstorm 5 angles I could take, each with a 1-sentence pitch.
2. Recommend the best one and explain why in 2 sentences.
3. Wait for me to confirm before writing anything.
```

### 2. Edit my draft
```
You are a sharp editor. Read my draft below. Don't rewrite it — instead:
1. List the 3 weakest sentences with specific rewrites
2. Flag any place I'm being vague or hedging
3. Suggest one structural change that would improve flow

<draft>
[paste]
</draft>
```

### 3. Match my voice
```
Here are 3 things I've written:

<sample_1>[paste]</sample_1>
<sample_2>[paste]</sample_2>
<sample_3>[paste]</sample_3>

Now write a [thing] in the same voice on the topic of [subject].
Keep it [length].
```

### 4. Tighten this
```
Cut this by 30% without losing meaning. Don't change my voice or
add new ideas. Show only the tightened version.

[paste]
```

---

## 💼 Work & productivity

### 5. Meeting prep
```
I have a [type] meeting with [who] about [topic]. The desired outcome
is [outcome]. Help me prep:
- 3 questions I should be ready to answer
- 3 questions I should ask
- The one risk I'm probably underweighting
```

### 6. Decompose a project
```
I want to [project goal]. Break it into the 5–7 smallest concrete
next actions, each starting with a verb and finishable in under 90
minutes. Order them by dependency. Flag the one I should start today.
```

### 7. Decision matrix
```
I'm choosing between [Option A] and [Option B] for [context].

Build a decision matrix:
- Rows: 5 criteria that actually matter for me
- Columns: the two options
- Score each 1-5 with a brief reason

Then tell me your pick and the one thing that would flip your answer.
```

### 8. Draft a tough email
```
I need to send [recipient] an email saying [hard message]. Context:
[your context — relationship, history, stakes].

Write three versions, each labeled with its strategy:
- "Direct and warm"
- "Hold the line"
- "Soft landing"

Each under 150 words. After, recommend which fits and why.
```

---

## 🧠 Learning & thinking

### 9. The Feynman explainer
```
Explain [concept] to me as if I'm smart but new to the field.
- Start with a 1-sentence summary
- Use one concrete real-world analogy
- Tell me one common misconception
- End with a question that tests if I really understood

After I answer, tell me what I got right or wrong.
```

### 10. Steelman the opposite
```
I believe [position]. Steelman the strongest opposing view in
3 paragraphs — make it the best version, not a strawman. Then
note where my view is most vulnerable.
```

### 11. Help me debug my thinking
```
Here's how I'm thinking about [problem]:

<my_reasoning>
[paste]
</my_reasoning>

Find the 2-3 most consequential flaws in my reasoning. Be direct.
For each: name the flaw, explain it, and suggest the better frame.
```

### 12. Spaced-repetition flashcards
```
I'm learning [topic]. Below are my notes. Generate 15 flashcards
in Anki-importable format (Q? Tab A.).
- Mix recall, reasoning, and "explain in your own words" cards
- Skip trivia; focus on what actually matters

<notes>
[paste]
</notes>
```

---

## 💻 Coding

### 13. Code review on a function
```
Review this function as a senior engineer would. Focus on:
1. Correctness (any bugs?)
2. Security/safety
3. Performance
4. Readability

Don't rewrite it. Give a numbered list of concerns ranked by severity.

```python
[paste]
```
```

### 14. Explain code I didn't write
```
Walk me through this code section by section. Assume I know the
language but not this codebase. After the walk-through, tell me:
- The 2 most non-obvious things
- Anything that smells wrong or risky

[paste]
```

### 15. Test cases I'd miss
```
Here's a function. Generate a test suite that catches the bugs
I'd miss. Specifically include:
- 2 obvious tests
- 3 edge cases (empty, max, off-by-one, unicode, etc.)
- 2 "evil input" tests

[paste]
```

### 16. Refactor with intent
```
Refactor this code so [specific goal: e.g. "the auth logic is reusable",
"the function is under 30 lines", "side effects are isolated"].

Don't just tidy it. Make the intended structure visible.
Show before/after diff style with a 1-line note on each change.

[paste]
```

### 17. Translate between languages
```
Translate this [source language] code to idiomatic [target language].
Don't do a literal port — use the target language's natural patterns.
Note any place the translation isn't 1:1 and why.

[paste]
```

---

## 📊 Analysis

### 18. Data summary
```
Here's a CSV/dataset. Without inventing anything beyond what's in it:
1. State its shape (rows, columns, types)
2. List 3 surprising things
3. List 3 things you'd want to verify before trusting any conclusion
4. Suggest the single most useful chart to make

[paste data]
```

### 19. Document Q&A with citations
```
Below is a document. Answer my question using ONLY information from it.
For every claim, cite the section/paragraph. If the document doesn't
answer, say "Not in the document."

<document>
[paste]
</document>

Question: [your question]
```

### 20. Compare and contrast
```
Compare [A] and [B] across these dimensions:
- [dimension 1]
- [dimension 2]
- [dimension 3]

Format: a markdown table. Then below the table, give a 3-sentence
"which to pick when" guide.
```

---

## 🎯 Negotiation & people

### 21. Salary negotiation prep
```
I have a job offer for [role] at [company] for [amount]. I want to
negotiate up to [target]. Help me:
1. Draft my email response (warm, confident, not desperate)
2. Anticipate 3 objections they might raise + my responses
3. Tell me the one thing I should NOT say
```

### 22. Disagree with my boss
```
I disagree with [decision] from my manager. Help me push back without
damaging the relationship. Draft a Slack message under 200 words that:
- Acknowledges their reasoning genuinely
- States my disagreement specifically
- Proposes a concrete alternative or a way to test
- Leaves room for them to save face if they change their mind
```

---

## 🚀 Creativity

### 23. Brainstorm without converging
```
Brainstorm [number] ideas for [topic]. Rules:
- No filtering — include weird, bad, and obvious ones
- Each is one sentence
- Group them into 3-4 categories at the end
- Mark your 3 personal favorites with ⭐
```

### 24. The "yes, and" exercise
```
I have an idea: [paste idea]. Don't critique it. Instead, build on it
with 5 "yes, and..." extensions that take it in surprising directions.
Then tell me which of the 5 has the most potential and why.
```

---

## 🧰 Meta / using Claude better

### 25. Have Claude improve my prompt
```
I want to use this prompt:

<prompt>
[paste your prompt]
</prompt>

It's not getting great results. Critique it as a prompt engineer
and rewrite it. Specifically:
- What's missing (role? context? format? examples?)
- What's confusing or contradictory
- The improved version

Then explain your top 3 changes.
```

### 26. The "think harder" boost
```
[Your original prompt]

Before you answer, think through this carefully step by step.
Consider at least 3 approaches and pick the best one.
Then give your final answer in a clearly labeled section.
```

### 27. Force structured output
```
[Task]

Return your answer as JSON matching exactly this schema:
{
  "[field_1]": "[type / description]",
  "[field_2]": "[type / description]",
  ...
}

NO prose, NO markdown, NO ```json fences. JSON only.
```

### 28. Force Claude to ask first
```
Before answering, ask me 3 clarifying questions whose answers
would most change your approach. Don't start the actual task
until I respond.

Task: [your task]
```

### 29. The "rate yourself"
```
[After Claude gives an answer:]

Rate your answer on:
- Specificity (was it generic or tailored?)
- Honesty (did you hedge unnecessarily?)
- Usefulness (could I act on it?)

Then give a v2 that scores higher on the weakest dimension.
```

### 30. The vault prompt
```
You are my long-term thinking partner on [topic]. Here's everything
relevant about me/this project:

<background>
[paste — role, goals, constraints, what's been tried, what hasn't worked]
</background>

For now: just confirm you've absorbed this. From the next message on,
treat all this as shared context. I'll ask follow-ups freely.
```

---

## How to use this cookbook

1. **Bookmark this file.** You'll come back.
2. **Copy → adapt → save your version.** Make it yours.
3. **Add to it.** When a prompt of yours works really well, write it down.
4. **PRs welcome.** Got a great prompt that should be here? See [CONTRIBUTING.md](../CONTRIBUTING.md).
