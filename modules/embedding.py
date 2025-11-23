from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str):
    embedding = model.encode([text])[0]
    return np.array(embedding, dtype="float32")
