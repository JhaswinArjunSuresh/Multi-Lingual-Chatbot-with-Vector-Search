from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class KnowledgeBase:
    def __init__(self):
        self.model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        with open("data/knowledge.txt", "r") as f:
            self.texts = [line.strip() for line in f if line.strip()]
        
        self.embeddings = self.model.encode(self.texts, convert_to_numpy=True)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def search(self, query, top_k=3):
        query_vec = self.model.encode([query], convert_to_numpy=True)
        D, I = self.index.search(query_vec, top_k)
        results = [{"text": self.texts[i], "distance": float(d)} for i, d in zip(I[0], D[0])]
        return results

