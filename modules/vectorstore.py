import sqlite3
import numpy as np
from modules.embedding import embed_text

DB_PATH = "db/embeddings.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS embeddings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chunk TEXT NOT NULL,
            vector BLOB NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_chunk(chunk: str):
    vector = embed_text(chunk)
    vector_blob = vector.tobytes()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO embeddings (chunk, vector) VALUES (?, ?)",
        (chunk, vector_blob)
    )

    conn.commit()
    conn.close()


def search_similar_chunks(query: str, top_k: int = 3):
    query_vector = embed_text(query)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT chunk, vector FROM embeddings")
    rows = cursor.fetchall()
    conn.close()

    scored = []
    for chunk_text, vector_blob in rows:
        db_vector = np.frombuffer(vector_blob, dtype=np.float32)
        score = np.dot(query_vector, db_vector)   # cosine-like
        scored.append((score, chunk_text))

    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:top_k]
