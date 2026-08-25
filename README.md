# 🎓 MAKAUT Study Helper (RAG System)

An intelligent, context-aware study assistant built specifically for MAKAUT (Maulana Abul Kalam Azad University of Technology) students. This project leverages a **Retrieval-Augmented Generation (RAG)** architecture to extract knowledge from study materials (PDFs), index them in a vector database, and provide accurate, syllabus-aligned answers to student queries.

---

## 🚀 Features

PDF Knowledge Extraction: Uses `pdfplumber` for highly accurate text extraction from complex university notes, syllabus copies, and textbooks.
Vector Database: Powered by ChromaDB for fast and efficient storage and retrieval of document embeddings.
Open-Source Embeddings: Utilizes Hugging Face embeddings (`sentence-transformers`) for high-quality, local vectorization of text chunks.
Ultra-Fast LLM Inference: Powered by ChatGroq using the `llama-3.1-8b-instant` model, ensuring lightning-fast and highly accurate conversational responses.

---

 🛠️ Tech Stack

Language:Python 3.8+
Framework:LangChain
Text Extraction:`pdfplumber`
Vector Database:ChromaDB (`chromadb`)
Embeddings:Hugging Face (`langchain-huggingface`, `sentence-transformers`)
LLM Model:ChatGroq (`llama-3.1-8b-instant` via `langchain-groq`)

---

 📂 Project Structure

While your specific file names may vary, the architecture follows this modular structure:

```text
├── data/                   # Directory to drop your MAKAUT PDF study materials
├── extract.py              # Uses pdfplumber to parse and clean text from PDFs
├── embedding.py            # Handles chunking and Hugging Face vectorization
├── database.py             # Manages the ChromaDB instance (insertion/storage)
├── retriever.py            # Performs semantic similarity search against ChromaDB
├── llm_model.py            # The main RAG pipeline combining retriever + ChatGroq (Llama 3)
├── main.py                 # The main entry point/UI to ask questions
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (Groq API Key)
