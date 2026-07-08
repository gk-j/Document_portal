Document Portal — AI Document Analysis, Chat & Comparison Platform

Document Portal is an AI-powered web application for analyzing, comparing, and chatting with documents using Retrieval-Augmented Generation (RAG). It allows users to upload PDFs, extract structured insights, compare two documents, and ask natural-language questions over uploaded files.

The project is built with FastAPI, LangChain, FAISS, and multiple LLM/embedding provider options including Groq, OpenAI, Gemini, Claude, Hugging Face, and Ollama. The backend exposes APIs for document analysis, document comparison, RAG indexing, and conversational document search.

Key Features

* Document Analysis
    Upload a PDF and extract structured metadata, summaries, and key insights using an LLM-powered analysis pipeline.
* Document Comparison
    Upload two documents and generate a structured comparison showing key differences, similarities, and summary-level insights.
* Chat with Documents
    Build a FAISS vector index from uploaded documents and ask questions using a conversational RAG pipeline.
* Session-Based Retrieval
    Supports session-specific FAISS indexes, allowing each document upload/chat session to stay isolated.
* Flexible Model Support
    Designed to work with multiple LLM and embedding providers such as Groq, OpenAI, Gemini, Claude, Hugging Face, and Ollama.
* FastAPI Backend
    Includes REST endpoints for analysis, comparison, indexing, querying, and health checks.

Tech Stack

* Backend: FastAPI, Python
* AI/LLM Framework: LangChain, LCEL
* Vector Database: FAISS
* Document Processing: PyMuPDF, pypdf, docx2txt
* LLM Providers: Groq, OpenAI, Gemini, Claude, Hugging Face, Ollama
* Infrastructure: Docker, Uvicorn
* Testing & Utilities: Pytest, dotenv, structured logging

API Overview

* POST /analyze — Upload and analyze a document
* POST /compare — Compare two uploaded documents
* POST /chat/index — Build a FAISS index for document chat
* POST /chat/query — Ask questions against indexed documents
* GET /health — Check API status

Why I Built This

I built this project to understand how real-world document intelligence systems work beyond basic LLM prompts. The goal was to design a backend that can ingest files, extract document text, create embeddings, store them in a vector database, and use RAG to return more grounded answers from uploaded documents.

This project helped me learn how to structure an AI application with separate modules for ingestion, analysis, comparison, retrieval, prompting, logging, and API routing.



## Conda environment setup
    ```
    conda create -p venv python==3.12 -y

    conda activate ./venv/

    ```

## Project setup

    ```
    git clone https://github.com/gk-j/Document_portal

    cd Document_portal

    code .

    # Create a new Conda environment with Python 3.10
    conda create -p <env_name> python=3.10 -y

    # Activate the environment (use full path to the environment)
    conda activate <path_of_the_env>

    # Install dependencies from requirements.txt
    pip install -r requirements.txt
    ```

## project requirements
1.LLM_Model 
        groq(free)
        openai(paid)
        gemini(paid)
        claude(paid)
        huggingface(free)
        ollama(local setup)

2.embedding model ##openai,huggingface,gemini

3.vector database ##inmemory,ondisk,cloudbased
