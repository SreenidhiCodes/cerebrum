# CEREBRUM
A Minimal, Explainable Memory Architecture for Conversational AI

“Stores only what matters. Recalls only when needed.”

# Problem Statement

Most conversational AI systems suffer from one of two extremes:

1. Forget everything (no context retention)

2. Remember everything (memory overload, hallucinations)

Additionally:

-No distinction between user preferences and task context

-No transparency in why something was recalled

-No structured audit mechanism

Goal:
Design a minimal, transparent, scalable memory system that supports 500–1000+ evolving conversation turns.

# System Architecture
Core Components
| Component                   | Responsibility                                            |
| --------------------------- | --------------------------------------------------------- |
| `memoryclassifier.py`       | Classifies input (Permanent / Temporary / Forget / Audit) |
| `permanentmemorymanager.py` | Manages long-term memory (P)                              |
| `memorymanager.py`          | Manages temporary session memory (T)                      |
| `retriever.py`              | Controls recall priority                                  |
| `main.py`                   | Orchestrates memory decisions                             |
| `app.py`                    | FastAPI interface layer                                   |




# Memory Design
# 1. Permanent Memory (P)

Stores long-term user identity signals.

Examples:

Language preference

Response style

Example format:
{
  "memory_id": "P1",
  "key": "language",
  "value": "Telugu",
  "origin_turn": 1,
  "last_used_turn": 59
}


# 2. Temporary Memory (T)

Stores active task/session context.

Examples:

Hackathon discussion

PPT planning

Architecture design

Lifecycle:

Start → Update → Recall → End


Example:

{
  "memory_id": "T1",
  "content": [
    "Start hackathon discussion",
    "Decide architecture"
  ],
  "origin_turn": 2,
  "last_used_turn": 15
}


# Memory Extraction Format

Rule-based classifier determines:
| Input Pattern         | Action             |
| --------------------- | ------------------ |
| “I prefer…”           | Store as Permanent |
| “Start project…”      | Start Temporary    |
| “end / stop”          | End Temporary      |
| “what did you store?” | Audit mode         |
| Other                 | No storage         |

No black-box ML. Fully deterministic.

# Persistence Strategy

JSON-based storage

Separate stores for:

-Permanent

-Temporary

-Turn-based tracking

-Memory IDs auto-increment (P1, T1…)

Designed for:

-500–1000+ turn conversations

-Easy migration to SQL/NoSQL

# Retrieval & Injection Policy
Priority Order

<Active Temporary Memory (T)

<Permanent Memory (P)

<Minimal Recall Output (Default)

Instead of dumping JSON:

Turn 59 → P1 recalled | T1 recalled


# Audit Mode (On Explicit Request)

Only when user asks:

“What did you store?”

“How is it stored?”

Full structured JSON is shown.

This ensures:

Clean UX

Transparency

Explainability

# Evaluation Methodology
Metrics Evaluated

Memory Precision (correct classification)

Recall Transparency

Session Continuity

Explainability

Scalability

Test Scenario

Simulated:

59-turn evolving conversation

Session switch

Temporary memory expiration

Audit request

Multi-topic continuation


# Latency

Measured locally (FastAPI):
| Operation          | Avg Latency |
| ------------------ | ----------- |
| Classification     | < 5ms       |
| Memory write       | < 3ms       |
| Retrieval          | < 5ms       |
| Full request cycle | ~15–25ms    |


# API (FastAPI)
Start Server
uvicorn app:app --reload

Swagger Docs
http://127.0.0.1:8000/docs

# POST /chat

Request:

{
  "message": "I prefer Telugu"
}


Response:

{
  "turn": 1,
  "event": "permanent_memory_stored",
  "memory_id": "P1"
}

# GET /health
{
  "status": "Cerebrum API running successfully"
}


# CPI (CLI Processing Interface)

Run:

python rundemo.py


# Project Structure
cerebrum/
│
├── model/
│   ├── main.py
│   ├── memoryclassifier.py
│   ├── memorymanager.py
│   ├── permanentmemorymanager.py
│   └── retriever.py
│
├── memorystore/
│   ├── permanent.json
│   ├── temporary.json
│   └── session.json
│
├── app.py
├── rundemo.py
└── README.md


# Key Strengths

✔ Fully Explainable
✔ No hallucinated memory
✔ Minimal storage
✔ Clear ID-based recall
✔ Modular architecture
✔ Production-ready API
✔ Hackathon-friendly

# Limitations

Rule-based classification (not semantic)

JSON persistence (not distributed)

Single-session focus

# Future Work

Vector-based semantic memory

Database backend

Multi-user support

Memory relevance scoring

Embedding-based topic continuity

Privacy-aware deletion policies

# Conclusion

CEREBRUM does not try to remember everything.

It remembers:

What defines the user.

What defines the task.

And nothing more.

Minimal.
Transparent.
Explainable.
Scalable.
