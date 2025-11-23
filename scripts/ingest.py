from modules.splitter import load_document_chunks
from modules.vectorstore import create_table, insert_chunk

def run_ingestion():
    print("📥 Starting ingestion...")

    create_table()
    chunks = load_document_chunks()

    for chunk in chunks:
        insert_chunk(chunk)

    print("✅ Ingestion complete.")


if __name__ == "__main__":
    run_ingestion()
