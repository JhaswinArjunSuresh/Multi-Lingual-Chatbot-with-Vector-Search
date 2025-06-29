from fastapi import FastAPI
from pydantic import BaseModel
from .knowledge import KnowledgeBase
from .chatbot import generate_answer

app = FastAPI()
kb = KnowledgeBase()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    results = kb.search(query.question)
    answer = generate_answer(query.question, results)
    return {"question": query.question, "results": results, "answer": answer}

@app.get("/health")
def health():
    return {"status": "ok"}

