from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import CHUNK_SIZE, CHUNK_OVERLAP

def load_and_split_pdf(file_path):

    loader = PyPDFLoader(file_path)
    documents = loader.load()
    for d in documents:
        d.metadata["file_name"] = file_path

    splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(documents)

    for i, c in enumerate(chunks):
        c.metadata["chunk_id"] = i

    return chunks