import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"   # change to "phi3" if needed


def generate_answer(query: str, context: str) -> str:
    """
    Uses local Ollama LLM to generate an answer based on context.
    """

    prompt = f"""
You are a helpful assistant. Answer the question ONLY using the context.

Context:
{context}

Question: {query}

Answer:
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        data = response.json()
        return data.get("response", "No answer generated.")

    except Exception as e:
        return f"LLM error: {str(e)}"
