\# 📄 PDF RAG AI



> A Retrieval-Augmented Generation (RAG) system for querying PDF documents — powered by LangChain, ChromaDB, and Google Gemini.

## UI Preview
![UI](ui.png)
![UI](ui2.png)



\## 🧠 What is This?



\*\*PDF RAG AI\*\* is a locally-runnable, command-line RAG pipeline that lets you \*\*chat with your PDF documents\*\*. Upload one or multiple PDFs, and ask natural language questions — the system retrieves the most relevant chunks and generates accurate, source-cited answers using Google Gemini.



Built as a learning project to explore \*\*RAG architecture\*\*, \*\*vector databases\*\*, and \*\*LLM integration\*\* without needing a GPU or cloud infrastructure.



\---



\## ✨ Features



| Feature | Description |

|---|---|

| 📚 Multi-PDF Indexing | Index and query multiple PDFs in a single session |

| 🔍 Semantic Search | Vector similarity search via ChromaDB |

| 🤖 Gemini 2.5 Flash | Fast, accurate LLM responses |

| 🧩 Sentence Transformers | Local embeddings — no API cost |

| 💬 Chat Memory | Context-aware follow-up questions |

| 📌 Source Tracking | Every answer cites its PDF and page number |

| ⚙️ Config-Based Settings | Centralized configuration via `config.py` |

| 🪵 Logging System | Structured logs for debugging and monitoring |

| 🖥️ CLI Interface | Simple numbered-menu interface |



\---



\## 🏗️ Architecture



```

┌─────────────┐    ┌─────────────┐    ┌──────────────┐    ┌────────────┐

│   PDF File  │───▶│   Loader    │───▶│   Chunking   │───▶│ Embeddings │

└─────────────┘    └─────────────┘    └──────────────┘    └─────┬──────┘

&#x20;                                                                 │

&#x20;                                                                 ▼

┌─────────────┐    ┌─────────────┐    ┌──────────────┐    ┌────────────┐

│  Answer +   │◀───│    Gemini   │◀───│   Retriever  │◀───│  ChromaDB  │

│   Sources   │    │     LLM     │    │              │    │            │

└─────────────┘    └─────────────┘    └──────────────┘    └────────────┘

&#x20;                                           ▲

&#x20;                                    User Question

```



\---



\## 📁 Project Structure



```

pdf\_rag\_ai/

├── app.py          # Entry point — CLI menu and orchestration

├── config.py       # Centralized settings and constants

├── loader.py       # PDF loading and text chunking

├── vector\_db.py    # ChromaDB indexing and retrieval

├── llm.py          # Gemini LLM integration and prompt logic

├── requirements.txt

├── .env            # API key (not committed)

├── data/           # Place your PDF files here

└── README.md

```



\---



\## ⚡ Quick Start



\### 1. Clone the Repository



```bash

git clone https://github.com/your-username/pdf-rag-ai.git

cd pdf-rag-ai

```



\### 2. Create a Virtual Environment



```bash

py -3.11 -m venv env

env\\Scripts\\activate        # Windows

\# source env/bin/activate   # macOS / Linux

```



\### 3. Install Dependencies



```bash

pip install -r requirements.txt

```



\### 4. Configure Your API Key



Create a `.env` file in the project root:



```env

GEMINI\_API\_KEY=your\_api\_key\_here

```



> Get your free Gemini API key from \[Google AI Studio](https://aistudio.google.com/app/apikey).



\### 5. Run the App



```bash

python app.py

```



\---



\## 🖥️ CLI Commands



```

========== PDF RAG AI ==========

1 → Index a PDF

2 → Ask a question

3 → Reset chat memory

4 → Show indexed PDFs

5 → Clear vector database

6 → Batch index all PDFs in /data

7 → Exit

=================================

```



\---



\## 🛠️ Tech Stack



\- \*\*Python 3.11\*\*

\- \*\*\[LangChain](https://www.langchain.com/)\*\* — RAG pipeline orchestration

\- \*\*\[ChromaDB](https://www.trychroma.com/)\*\* — Local vector database

\- \*\*\[Sentence Transformers](https://www.sbert.net/)\*\* — Local text embeddings

\- \*\*\[Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/)\*\* — Answer generation

\- \*\*python-dotenv\*\* — Environment variable management



\---



\## 📦 Requirements



```

langchain

langchain-community

langchain-google-genai

chromadb

sentence-transformers

pypdf

python-dotenv

```



> Install all at once: `pip install -r requirements.txt`



\---



\## 🗺️ Roadmap



\- \[ ] 🌐 Web UI with Gradio or Streamlit

\- \[ ] ⚡ FAISS support for faster retrieval

\- \[ ] 🦙 Ollama integration for fully offline LLM

\- \[ ] 🔀 Hybrid search (keyword + semantic)

\- \[ ] 🤖 Agent integration for multi-step reasoning

\- \[ ] 🐳 Docker support



\---



\## 🤝 Contributing



Contributions, issues, and feature requests are welcome!



1\. Fork the repository

2\. Create a new branch (`git checkout -b feature/your-feature`)

3\. Commit your changes (`git commit -m 'Add some feature'`)

4\. Push to the branch (`git push origin feature/your-feature`)

5\. Open a Pull Request



\---



\## 📚 Learning Resources



This project was built to understand:

\- How RAG pipelines work end-to-end

\- Vector embeddings and similarity search

\- LangChain chains and memory

\- Integrating LLMs with external data











\---



<p align="center">Made with ❤️ for learning RAG architecture</p>

