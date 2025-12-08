#  Mini RAG Chatbot (Python + SQLite + Ollama + Telegram Bot)

A fully local, offline-capable **Retrieval-Augmented Generation (RAG) chatbot** built using:

- **Python**
- **Your custom documents**
- **SentenceTransformer embeddings**
- **SQLite as a vector database**
- **Ollama (local LLMs like Phi-3 / Llama3)**
- **Telegram Bot API**

This project allows users to query internal documents like:

```
/ask What is the leave policy?
```

The bot retrieves relevant context **from your own documents**, sends it to a **local LLM**, and returns the final answer.

---

#  1. What This Project Does

This RAG system:

### ✔ Loads your text documents  
### ✔ Splits them into chunks  
### ✔ Converts chunks into embeddings  
### ✔ Stores them inside SQLite  
### ✔ Retrieves relevant chunks for any question  
### ✔ Sends context + question to a local LLM (Ollama)  
### ✔ Returns an accurate response via Telegram  

Everything runs **locally**, **securely**, with **no cloud dependency**.

---

#  2. System Architecture

```
                      ┌──────────────────────────┐
                      │      User (Telegram)      │
                      └──────────────┬───────────┘
                                     │ /ask query
                                     ▼
                         ┌──────────────────────┐
                         │      app.py          │
                         │ Telegram Bot Handler │
                         └─────────┬────────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │       rag.py         │
                        │  RAG Orchestration   │
                        └─────────┬────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
┌────────────────┐      ┌─────────────────────┐     ┌───────────────────┐
│ splitter.py    │      │ vectorstore.py      │     │ generator.py       │
│ Load documents │      │ SQLite Similarity   │     │ Ollama LLM Answer │
│ Chunk into txt │      │ Search (Top-K=1)    │     │ (phi3 / llama3)   │
└────────────────┘      └─────────────────────┘     └───────────────────┘
                                       │
                                       ▼
                             ┌──────────────────┐
                             │   embeddings.db  │
                             │ SQLite Vector DB │
                             └──────────────────┘
```

---

#  3. Folder Structure

```
rag-bot/
│
├── app.py                     # Telegram bot entrypoint
├── config.py                  # BOT_TOKEN, model config
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
│
├── data/
│   └── docs/                  # Your documents (.txt / .md)
│
├── db/
│   └── embeddings.db          # SQLite vector DB (auto-created)
│
├── modules/
│   ├── embedding.py           # SentenceTransformer embeddings
│   ├── splitter.py            # Load + chunk documents
│   ├── vectorstore.py         # SQLite similarity search
│   ├── generator.py           # Ollama model generation
│   └── rag.py                 # Complete RAG pipeline
│
├── scripts/
│   └── ingest.py              # Build vector DB from documents
│
└── logs/
    └── bot.log                # Runtime logs
```

---

#  4. Installation

## Step 1 — Create Virtual Environment

```
python -m venv venv
.env\Scriptsctivate
```

## Step 2 — Install Dependencies

```
pip install -r requirements.txt
```

---

#  5. Configure Telegram Bot

Edit `config.py`:

```python
BOT_TOKEN = "your_telegram_bot_token"
```

Create your bot via **@BotFather** → Get a token → Paste it here.

---

#  6. Install Ollama + LLM Models

Install Ollama:  
https://ollama.com/download

Then pull a fast model:

```
ollama pull phi3
```

Or even faster:

```
ollama pull qwen2.5:0.5b
```

Models are **100% free** and run locally.

---

#  7. Add Your Documents

Place your `.txt` or `.md` files inside:

```
data/docs/
```

Example:

```
policies.txt
attendance.md
leave-rules.txt
```

The bot uses ONLY these files to answer questions.

---

#  8. Run Ingestion

This converts documents → chunks → embeddings → SQLite.

```
python -m scripts.ingest
```

Output:

```
 Loaded <X> chunks
 Ingestion complete.
```

A new file appears:

```
db/embeddings.db
```

---

#  9. Run the Telegram Bot

```
python app.py
```

Output:

```
Bot is running...
```

Open Telegram → message your bot:

```
/ask What is the leave policy?
```

---

#  10. How RAG Works Internally

### 1️ Load & chunk all documents  
`splitter.py` splits files into 300–500 character chunks.

### 2️ Embed chunks  
`embedding.py` uses:  
`all-MiniLM-L6-v2` (fast + accurate)

### 3️ Store vectors in SQLite  
Each chunk and its vector go into `embeddings.db`

### 4️ Receive user query  
Telegram → `/ask <question>`

### 5️ Embed query  
Find the closest chunk using dot-product similarity.

### 6️ Send to Ollama  
`generator.py` generates answer:

- model = `"phi3"`  
- `num_predict = 120` (fast)
- `num_ctx = 1024`

### 7️ Return final reply to user

---

#  11. Performance Optimization

This project uses optimizations:

- **Phi3** (fastest model on CPU)
- **Top-K = 1** chunk retrieval
- **Token limit = 120**
- **Small prompt context**

---

#  12. Test Commands

```
/ask What is the leave policy?
/ask Summarize the company rules.
/ask What is the code of conduct?
/ask Give me bullet points of the policies.
/ask What happens if someone shares confidential info?
```

---

#  13. Technologies Used

| Component | Technology |
|----------|------------|
| Embeddings | SentenceTransformer MiniLM |
| Vector DB | SQLite |
| Similarity | Dot-product search |
| LLM | Ollama (phi3 / llama3 / qwen) |
| Bot | python-telegram-bot |
| Language | Python |
| Architecture | Modular RAG |

---

#  14. Future Enhancements

- PDF ingestion  
- Multi-file ingestion  
- Streaming responses  
- Gradio or FastAPI UI  
- Replace SQLite with FAISS or Chroma  

---
