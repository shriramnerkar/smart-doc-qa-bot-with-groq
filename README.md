### File: README.md
# 📄 Smart Document QA Bot (Docker + FastAPI + Streamlit)

Upload any PDF, ask questions, and get answers directly from your documents using Retrieval-Augmented Generation (RAG).

## 🔧 Tech Stack
- FastAPI + Streamlit
- LangChain + OpenAI GPT-3.5
- FAISS (Vector Store)
- Dockerized app

## 🚀 How to Run Locally
```bash
git clone <repo-url>
cd smart-doc-qa-bot
docker build -t smart-doc-qa .
docker run -p 8501:8501 -p 8000:8000 smart-doc-qa
```

Visit: `http://localhost:8501`

## 📦 API Endpoints
- `POST /upload`: Upload PDF
- `POST /ask`: Ask a question (form param: question)
