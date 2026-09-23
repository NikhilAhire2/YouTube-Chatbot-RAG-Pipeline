# Multilingual YouTube Chatbot – RAG Pipeline

A **multilingual YouTube chatbot** built using a Retrieval-Augmented Generation (RAG) pipeline. The system retrieves relevant information from YouTube video transcripts and generates contextual answers using an LLM.

## 🚀 Tech Stack

- **Python**
- **LangChain**
- **Gemini Embedding-001**
- **FAISS**
- **YouTube Transcript API**
- **LLM / Gemini**

## 🏗️ Architecture

```text
YouTube Video
      ↓
YouTube Transcript API
      ↓
Transcript Extraction
      ↓
Text Chunking
      ↓
Gemini Embedding-001
      ↓
FAISS Vector Database
      ↓
Semantic Search / Retrieval
      ↓
Relevant Transcript Chunks
      ↓
RAG Pipeline
      ↓
LLM
      ↓
Contextual Answer
```

## ✨ Features

- 🎥 Automated YouTube transcript ingestion using the **YouTube Transcript API**
- 🔍 Semantic search using **Gemini Embedding-001**
- ⚡ Efficient vector search using **FAISS**
- 🧠 Retrieval-Augmented Generation (**RAG**) for contextual responses
- 🌐 Multilingual chatbot support
- 🔗 Modular pipeline design using **LangChain**
- 📚 Retrieves relevant transcript chunks before generating answers

## 🔄 RAG Pipeline

### 1. Transcript Ingestion

The **YouTube Transcript API** is used to automatically extract transcripts from YouTube videos.

### 2. Text Processing

The transcript is divided into smaller chunks so that relevant portions can be retrieved efficiently.

### 3. Embedding Generation

Each transcript chunk is converted into a semantic vector using **Gemini Embedding-001**.

### 4. Vector Storage

The generated embeddings are stored in a **FAISS vector database**.

### 5. Retrieval

When a user asks a question, the query is converted into an embedding and compared against stored transcript embeddings.

The most relevant transcript chunks are retrieved.

### 6. Generation

The retrieved chunks are provided as context to the LLM, which generates a contextual answer.

```text
User Question
      ↓
Query Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Transcript Chunks
      ↓
Context + Question
      ↓
LLM
      ↓
Answer
```

## 🌐 Multilingual Support

The chatbot supports multilingual interaction, allowing users to interact with the YouTube video content in different languages and improving accessibility for a wider audience.

## 📁 Project Structure

```text
multilingual-youtube-chatbot/
│
├── app/
│   ├── ingestion/
│   ├── embeddings/
│   ├── retrieval/
│   ├── rag/
│   └── chatbot/
│
├── data/
│   └── transcripts/
│
├── vectorstore/
│   └── faiss/
│
├── notebooks/
│
├── requirements.txt
├── .env
└── README.md
```

## 🎯 Key Highlights

- Built a **multilingual YouTube chatbot** using a RAG architecture.
- Implemented automated transcript ingestion using the **YouTube Transcript API**.
- Used **Gemini Embedding-001** for high-quality semantic embeddings.
- Used **FAISS** for efficient similarity search and retrieval.
- Designed a modular **LangChain-based RAG pipeline**.
- Generated contextual answers using retrieved transcript information.
- Added multilingual support to improve **YouTube video accessibility**.
