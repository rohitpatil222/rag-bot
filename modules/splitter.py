import os

DATA_DIR = "data/docs"

def load_document_chunks():
    """
    Loads .txt or .md documents from /data/docs
    Returns list of chunks [(text)].
    """

    chunks = []
    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)

        if file.endswith(".txt") or file.endswith(".md"):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            # Simple fixed-size chunking
            size = 400
            for i in range(0, len(text), size):
                chunk = text[i:i + size].strip()
                if chunk:
                    chunks.append(chunk)

    return chunks
