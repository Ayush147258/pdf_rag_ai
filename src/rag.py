import os
import logging
import shutil

from src.loader import load_and_split_pdf
from src.vector_db import create_vector_db, load_vector_db
from src.llm import get_llm
from src.config import (
    DATA_DIR,
    DB_DIR,
    TOP_K,
    SCORE_THRESHOLD,
    GEMINI_MODEL,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
)

chat_history = []


# -------------------------
# Index single PDF
# -------------------------
def index_pdf(file_name):

    logging.info(f"Indexing {file_name}")

    file_path = os.path.join(DATA_DIR, file_name)

    chunks = load_and_split_pdf(file_path)

    logging.info(f"Chunks created: {len(chunks)}")

    db = create_vector_db(chunks)

    logging.info("Index stored")

    return db


# -------------------------
# Ask question
# -------------------------
def ask_question(question):

    global chat_history

    logging.info(f"Question: {question}")

    db = load_vector_db()

    if db is None:
        return "No PDF indexed. Please index a PDF first."

    results = db.similarity_search_with_score(question, k=TOP_K)

    logging.info(f"Results retrieved: {len(results)}")

    docs = []

    for doc, score in results:
        if score < SCORE_THRESHOLD:
            docs.append(doc)

    logging.info(f"Docs after filter: {len(docs)}")

    if not docs:
        logging.info("No relevant docs found")
        return "No relevant information found in indexed PDFs."

    context = "\n\n".join([d.page_content for d in docs])

    sources = []

    for d in docs:
        src = d.metadata.get("file_name", "")
        page = d.metadata.get("page", "")
        chunk = d.metadata.get("chunk_id", "")

        sources.append(f"{src} page {page} chunk {chunk}")

    history_text = "\n".join(chat_history)

    llm = get_llm()

    prompt = f"""
You are a RAG assistant.

Answer only from context.
If not found, say: Not found in documents.

Context:
{context}

Conversation:
{history_text}

Question:
{question}

Answer:
"""

    logging.info("Sending prompt to Gemini")

    response = llm.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    answer = response.text

    logging.info("Answer generated")

    chat_history.append(f"Q: {question}")
    chat_history.append(f"A: {answer}")

    source_text = "\n".join(set(sources))

    final = f"{answer}\n\nSources:\n{source_text}"

    return final


# -------------------------
# Reset chat
# -------------------------
def reset_history():

    global chat_history

    chat_history = []

    return "History cleared"


# -------------------------
# List PDFs
# -------------------------
def list_pdfs():

    if not os.path.exists(DATA_DIR):
        return "No PDF folder found."

    files = os.listdir(DATA_DIR)

    if not files:
        return "No PDFs indexed."

    return "\n".join(files)


# -------------------------
# Clear index
# -------------------------
def clear_index():

    if not os.path.exists(DB_DIR):
        return "No index to clear."

    shutil.rmtree(DB_DIR)

    return "Index cleared."


# -------------------------
# Index all PDFs
# -------------------------
def index_all_pdfs():

    if not os.path.exists(DATA_DIR):
        return "PDF folder not found."

    files = os.listdir(DATA_DIR)

    if not files:
        return "No PDFs to index."

    for f in files:

        file_path = os.path.join(DATA_DIR, f)

        chunks = load_and_split_pdf(file_path)

        create_vector_db(chunks)

    return "All PDFs indexed."