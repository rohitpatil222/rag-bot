import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = os.getenv("DB_PATH", "db/embeddings.db")
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
TOP_K = int(os.getenv("TOP_K", "3"))
