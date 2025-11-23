# RAG Bot (Mini-RAG) 
This repository is a ready-to-run skeleton for the Mini-RAG Telegram/Discord bot described in your assignment.

## What is included
- `app.py` – bot entrypoint (Telegram example)
- `modules/` – the core RAG pipeline modules (splitter, embedding, vectorstore, generator, utils)
- `scripts/ingest.py` – ingest docs -> chunks -> embed -> sqlite
- `db/` – placeholder for the SQLite DB
- `data/docs/` – put your 3-5 markdown/text docs here

## Original Assignment File
The original assignment you uploaded is included at this path on the server (we keep the original file):
`/mnt/data/DataScience_Assignment.docx`

## Running locally (basic)
1. Create a Python venv, install requirements: `pip install -r requirements.txt`
2. Fill `data/docs/` with your `.md` or `.txt` files.
3. Set environment variable: `export BOT_TOKEN=your_telegram_bot_token`
4. Run ingestion: `python scripts/ingest.py`
5. Run the bot: `python app.py`

## Notes
- This skeleton uses SQLite for simplicity. Replace with FAISS or other stores if needed.
- For LLM generation, the template uses `ollama` by default if available; otherwise update `modules/generator.py` to call OpenAI/HF APIs.
