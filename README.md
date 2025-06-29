# 🌐 Multi-Lingual Chatbot with Vector Search

## Features
- Uses `paraphrase-multilingual-MiniLM` for sentence embeddings.
- Vector search with FAISS.
- Answer generation via GPT-3.5 / GPT-4.

## Run locally
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
uvicorn app.main:app --reload

