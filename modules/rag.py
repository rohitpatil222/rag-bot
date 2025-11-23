from modules.vectorstore import search_similar_chunks
from modules.generator import generate_answer

def answer_query(query: str) -> str:
    """
    1. Search relevant chunks from SQLite vector DB
    2. Send as context to LLM generator
    3. Return final answer
    """

    # 1. Search most relevant chunks
    results = search_similar_chunks(query, top_k=3)

    # If nothing found, respond safely
    if not results:
        return "I couldn’t find anything related in the documents."

    # Clean & convert results into context text
    context_text = "\n\n".join([r[1] for r in results])  # r[1] = chunk text

    # 2. Generate final answer
    answer = generate_answer(query, context_text)

    return answer
