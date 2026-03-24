import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data", "pdfs")

DB_DIR = os.path.join(BASE_DIR, "vector_db")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")
# Retrieval settings
TOP_K = 5
SCORE_THRESHOLD = 1.5

# Chunk settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# Model
GEMINI_MODEL = "gemini-2.5-flash"
# Logging
LOG_LEVEL = "INFO"