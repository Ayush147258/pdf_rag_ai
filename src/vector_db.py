import os
from langchain_chroma import Chroma
from src.embed import get_embedding_model
from src.config import DB_DIR


def create_vector_db(chunks):

    embedding = get_embedding_model()

    if os.path.exists(DB_DIR):

        db = Chroma(
            persist_directory=DB_DIR,
            embedding_function=embedding,
        )

        db.add_documents(chunks)

    else:

        db = Chroma.from_documents(
            chunks,
            embedding,
            persist_directory=DB_DIR,
        )

    db.persist()

    return db


def load_vector_db():

    if not os.path.exists(DB_DIR):
        return None

    embedding = get_embedding_model()

    db = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embedding,
    )

    return db