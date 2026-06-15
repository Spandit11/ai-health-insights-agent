# 🏗️ AI Health Insights Agent Architecture

## Overview

AI Health Insights Agent is an Agentic AI healthcare platform that combines:

* LangGraph Multi-Agent Workflow
* Golden Validation Engine
* Retrieval-Augmented Generation (RAG)
* Streamlit User Interface
* FAISS Vector Database

The platform analyzes uploaded health reports, validates extracted medical metrics against trusted reference ranges, generates health insights, and allows users to interact with their reports through a RAG-powered chat interface.

---

# 🎯 Architecture Goals

The system was designed to:

* Reduce AI hallucinations
* Introduce deterministic medical validation
* Demonstrate Agentic AI design patterns
* Showcase LangGraph workflow orchestration
* Support explainable AI outputs
* Enable document-based conversational AI

---

# 🏥 High-Level Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
PDF Upload
 │
 ▼
PDF Text Extraction
 │
 ├──────────────────────────┐
 │                          │
 ▼                          ▼
LangGraph Workflow      RAG Pipeline
 │                          │
 ▼                          ▼
Metric Extraction       Text Chunking
 │                          │
 ▼                          ▼
Golden Validation       Embeddings
 │                          │
 ▼                          ▼
Analysis Agent          FAISS Vector Store
 │                          │
 ▼                          ▼
Risk Agent              Retriever
 │                          │
 ▼                          ▼
Recommendation Agent    Chat Agent
 │                          │
 ▼                          ▼
Summary Agent           User Answers
 │
 ▼
Health Insights
```

---

# 🤖 LangGraph Multi-Agent Workflow

The health analysis engine is implemented using LangGraph.

Workflow:

```text
START
 │
 ▼
Metric Extraction Agent
 │
 ▼
Validation Agent
 │
 ▼
Analysis Agent
 │
 ▼
Risk Assessment Agent
 │
 ▼
Recommendation Agent
 │
 ▼
Summary Agent
 │
 ▼
END
```

---

# 📊 Agent Responsibilities

## 1. Metric Extraction Agent

### Input

Raw health report text

### Output

```json
{
  "hba1c": 5.9,
  "ldl": 165,
  "fasting_glucose": 108
}
```

### Responsibility

Extract medical metrics from health reports.

---

## 2. Validation Agent

### Input

Extracted metrics

### Output

```json
{
  "hba1c": {
    "value": 5.9,
    "status": "Pre-Diabetic"
  }
}
```

### Responsibility

Validate extracted values against trusted reference ranges.

---

## 3. Analysis Agent

### Input

Validated metrics

### Output

Health findings and observations.

### Responsibility

Interpret validated medical results.

---

## 4. Risk Assessment Agent

### Input

Validated metrics and analysis findings

### Output

Potential health risks.

### Responsibility

Identify possible risk factors.

---

## 5. Recommendation Agent

### Input

Risk assessment

### Output

Lifestyle and health recommendations.

### Responsibility

Generate actionable suggestions.

---

## 6. Summary Agent

### Input

Analysis, risks, and recommendations

### Output

Executive summary.

### Responsibility

Produce concise health insights.

---

# 🧠 Golden Validation Engine

The Golden Validation Engine reduces hallucinations by moving medical classification logic out of the LLM.

Example:

```text
HbA1c = 5.9
```

Instead of allowing the LLM to decide the status:

```text
5.9 → Pre-Diabetic
```

is determined using trusted rules stored in:

```text
data/health_reference.json
```

Example:

```json
{
  "hba1c": {
    "normal_max": 5.6,
    "prediabetic_max": 6.4
  }
}
```

Benefits:

* Deterministic results
* Explainable outputs
* Reduced hallucinations
* Easier auditing

---

# 💬 RAG Chat Architecture

The platform also supports conversational querying.

Workflow:

```text
Health Report
 │
 ▼
Chunking
 │
 ▼
Embeddings
 │
 ▼
FAISS Index
 │
 ▼
Retriever
 │
 ▼
Chat Agent
 │
 ▼
Answer + Source Chunks
```

---

# 🛠️ Technology Stack

## Frontend

* Streamlit

## AI Framework

* LangGraph
* LangChain

## Vector Database

* FAISS

## Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

## LLM

* OpenAI / Azure OpenAI

## Language

* Python

---

# 🔒 Design Principles

The project follows:

* Agentic AI Design
* Separation of Responsibilities
* Retrieval-Augmented Generation
* Deterministic Validation
* Explainable AI
* Modular Architecture
* Enterprise Workflow Orchestration

---

# 🚀 Future Architecture Direction

Planned enhancements include:

* Human-in-the-Loop Validation
* MCP Tool Integration
* Multi-Agent Collaboration
* Long-Term Memory
* Azure AI Foundry Integration
* Azure AI Search
* Cosmos DB Persistence
* Containerized Deployment
* Personalized Health Coach Agent

Refer to:

FUTURE_ENHANCEMENTS.md

for detailed roadmap.
