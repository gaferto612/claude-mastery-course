# 📊 The Visual Reference

> All the key diagrams from the course in one place. Bookmark this page.

---

## 🗺️ Course flow

```mermaid
flowchart LR
    A[👋 Introduction] --> B[🚀 Getting Started]
    B --> C[💡 Prompting]
    C --> D[🛠️ Features]
    D --> E[💻 Claude Code]
    D --> F[⚙️ API]
    E --> G[🧪 Advanced]
    F --> G
    G --> H[🏗️ Projects]
    H --> I[📚 Resources]

    style A fill:#FFF1E6,stroke:#D97757,color:#1a1a1a
    style C fill:#FFE5D1,stroke:#D97757,color:#1a1a1a
    style F fill:#FFD9BC,stroke:#D97757,color:#1a1a1a
    style I fill:#FFB67E,stroke:#D97757,color:#1a1a1a
```

---

## 🧠 The three Claude surfaces

```mermaid
flowchart LR
    User((👤 You)) --> CA[💬 Claude.ai]
    User --> CC[💻 Claude Code]
    User --> API[⚙️ Claude API]

    CA --> Model{🧠 Claude}
    CC --> Model
    API --> Model

    style Model fill:#1a1a1a,stroke:#D97757,color:#fff
```

---

## 💎 The model family

```
                          INTELLIGENCE
                              ▲
                       💎 Opus│
                              │
                              │  ⚡ Sonnet
                              │
                              │            🚀 Haiku
                              └──────────────────────────►
                                                  SPEED & COST


   Opus    →  Hardest tasks: complex reasoning, agentic coding
   Sonnet  →  Daily driver: 90% of production work
   Haiku   →  High volume: classification, simple Q&A
```

---

## 🎯 The 6 ingredients of a great prompt

```mermaid
flowchart TD
    Prompt[🎯 Great Prompt] --> Role[🎭 ROLE]
    Prompt --> Context[📋 CONTEXT]
    Prompt --> Task[🎯 TASK]
    Prompt --> Constraints[📐 CONSTRAINTS]
    Prompt --> Format[📦 FORMAT]
    Prompt --> Examples[🌟 EXAMPLES]

    style Prompt fill:#1a1a1a,stroke:#D97757,color:#fff
    style Role fill:#FFF1E6,stroke:#D97757,color:#1a1a1a
    style Context fill:#FFE5D1,stroke:#D97757,color:#1a1a1a
    style Task fill:#FFD9BC,stroke:#D97757,color:#1a1a1a
    style Constraints fill:#FFCEA8,stroke:#D97757,color:#1a1a1a
    style Format fill:#FFC293,stroke:#D97757,color:#1a1a1a
    style Examples fill:#FFB67E,stroke:#D97757,color:#1a1a1a
```

---

## 🛠️ Diagnosing a bad prompt

```mermaid
flowchart TD
    A[I'm getting bad output] --> B{Task<br/>ambiguous?}
    B -->|Yes| C[Add: 'Ask 3<br/>questions first']
    B -->|No| D{Wrong tone<br/>or format?}
    D -->|Yes| E[Add an EXAMPLE<br/>or FORMAT spec]
    D -->|No| F{Complex<br/>multi-step?}
    F -->|Yes| G[Break into<br/>a CHAIN]
    F -->|No| H{Reasoning<br/>shallow?}
    H -->|Yes| I[Add 'think<br/>step-by-step']
    H -->|No| J{Details<br/>missing?}
    J -->|Yes| K[Add ROLE +<br/>CONTEXT +<br/>CONSTRAINTS]
    J -->|No| L[Try a bigger<br/>model]

    style C fill:#D97757,stroke:#1a1a1a,color:#fff
    style E fill:#D97757,stroke:#1a1a1a,color:#fff
    style G fill:#D97757,stroke:#1a1a1a,color:#fff
    style I fill:#D97757,stroke:#1a1a1a,color:#fff
    style K fill:#D97757,stroke:#1a1a1a,color:#fff
    style L fill:#D97757,stroke:#1a1a1a,color:#fff
```

---

## 📁 The Claude.ai feature universe

```mermaid
mindmap
  root((Claude.ai))
    Workspace
      Projects
      Custom Instructions
      Style Presets
    Inputs
      File Uploads
      Images
      PDFs
    Outputs
      Artifacts
      Code Execution
    Live data
      Web Search
      Research Mode
    Memory
      Cross-chat
      Past chat search
    Connectors
      Google Workspace
      GitHub
      Slack
      Notion
      40+ more
    Skills
      PowerPoint
      Excel
      Word
      Custom Skills
```

---

## 🔄 Claude Code's core loop

```mermaid
flowchart TD
    A[👤 You describe goal] --> B[🧠 Claude plans]
    B --> C{Read or edit?}
    C -->|Read| D[📖 Read files]
    C -->|Edit| E[📝 Propose edit]
    E --> F{👤 Approve?}
    F -->|Yes| G[✏️ Apply]
    F -->|No| H[💬 Push back]
    H --> B
    D --> I[💬 Report]
    G --> J{Done?}
    J -->|No| B
    J -->|Yes| K[✅ Finished]

    style F fill:#FFD9BC,stroke:#D97757,color:#1a1a1a
    style K fill:#D97757,stroke:#1a1a1a,color:#fff
```

---

## 🤖 The agent loop (API)

```mermaid
flowchart TD
    Start([🎯 Goal]) --> Plan[🧠 Plan]
    Plan --> D{Tool needed?}
    D -->|Yes| Tool[🔧 Call tool]
    Tool --> Obs[👀 Result]
    Obs --> Done{Done?}
    D -->|No| Answer[💬 Answer]
    Done -->|No| Plan
    Done -->|Yes| Answer
    Answer --> End([✅])

    style End fill:#D97757,stroke:#1a1a1a,color:#fff
```

---

## 🔌 Tool use sequence

```mermaid
sequenceDiagram
    participant U as 👤 User
    participant C as 🧠 Claude
    participant Y as 💻 Your Code

    U->>C: "Should I bring a jacket?"
    C->>Y: tool_use: get_weather("Paris")
    Y->>Y: Calls weather API
    Y->>C: tool_result: {temp: 14, drizzle}
    C->>U: "Yes — 14°C, drizzly. Light jacket."
```

---

## 🌐 MCP architecture

```mermaid
flowchart TD
    Claude[🧠 Claude] -.MCP.-> S1[📧 Mail]
    Claude -.MCP.-> S2[🐙 GitHub]
    Claude -.MCP.-> S3[🗄️ Database]
    Claude -.MCP.-> S4[📓 Notion]

    style Claude fill:#1a1a1a,stroke:#D97757,color:#fff
```

---

## 💰 The cost-saving router pattern

```mermaid
flowchart LR
    User([👤 Query]) --> Router[⚡ Router<br/>cheap + fast]
    Router -->|Easy 90%| Haiku[🚀 Haiku]
    Router -->|Hard 10%| Opus[💎 Opus]
    Haiku --> Reply([💬 Answer])
    Opus --> Reply

    style Router fill:#FFE5D1,stroke:#D97757,color:#1a1a1a
    style Reply fill:#D97757,stroke:#1a1a1a,color:#fff
```

---

## 🚀 Production checklist flow

```mermaid
flowchart TD
    Build[🏗️ Built something] --> Sec[🔒 Secrets in vault]
    Sec --> Rate[⏱️ Rate limit]
    Rate --> Cost[💰 Cost caps]
    Cost --> Retry[🔁 Retries with backoff]
    Retry --> Log[📝 Logging + PII redaction]
    Log --> Eval[🧪 Eval set]
    Eval --> Fall[🛡️ Fallback model]
    Fall --> Cache[💾 Prompt caching]
    Cache --> Ship[🚀 Ship!]

    style Ship fill:#D97757,stroke:#1a1a1a,color:#fff
```

---

## 📚 The four projects (Module 8)

```mermaid
flowchart TD
    Course[📚 Module 8] --> P1[1️⃣ CLI Chatbot]
    Course --> P2[2️⃣ Doc Q&A]
    Course --> P3[3️⃣ Research Agent]
    Course --> P4[4️⃣ Code Reviewer]

    P1 --> S1[Streaming<br/>Multi-turn<br/>System prompts]
    P2 --> S2[RAG<br/>Caching<br/>File parsing]
    P3 --> S3[Tool use<br/>Planning<br/>Web fetch]
    P4 --> S4[Structured outputs<br/>git integration<br/>JSON schema]

    style Course fill:#1a1a1a,stroke:#D97757,color:#fff
```

---

> 👉 Want this interactively? Open [`hub.html`](../hub.html) in your browser.
