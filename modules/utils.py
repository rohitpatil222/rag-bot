def build_prompt(query, chunks):
    context = "\n\n".join([c['text'] for c in chunks])
    prompt = f"""
You are a helpful assistant. Use the context below to answer the question.

Context:
{context}

Question: {query}
Answer:
"""
    return prompt
