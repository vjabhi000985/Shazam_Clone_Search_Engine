# 🎵 Shazam Clone : Audio Transcription & Subtitle Search

## Overview

This project focuses on building **AI-powered search systems**, **audio-to-text conversion**, and **interactive search applications**. It integrates **search engine technologies, vector embeddings, speech-to-text models, and subtitle processing** to enable efficient information retrieval and media analysis.

## Deployment URL :

[Shazam Clone Search Engine](https://0789dd5d92321ee4c6.gradio.live/)

- Note - URL is available for 72 hours only.

## Objective

Develop an advanced search engine algorithm that efficiently retrieves subtitles based on user queries, leveraging natural language processing (NLP) and machine learning to enhance search relevance and accuracy.

- Keyword-based vs. Semantic Search Engines
- Keyword-Based Search Engine: Relies on exact keyword matches between user queries and indexed documents.
- Semantic Search Engine: Understands the meaning and context of queries and documents beyond keyword matching.

## Core Logic

The search engine compares user queries against subtitle documents through these key steps:

### 1. Preprocessing the Data

- Extract and clean subtitle data (remove timestamps, punctuation, etc.).

- Subset the dataset if compute resources are limited (e.g., use 30% of the data).

### 2. Generating Text Vectors

- Convert subtitle text into vector embeddings using different techniques:

- BOW (Bag of Words) / TF-IDF → For keyword-based search.

- BERT-based SentenceTransformers → For semantic search.

### 3. Implementing a Document Chunker

- Break down large subtitles into smaller chunks to preserve context.

- Use overlapping windows to prevent information loss.

### 4. Storing Embeddings in ChromaDB

- Store vector representations of subtitle chunks in ChromaDB for efficient retrieval.

### 5. Retrieving Documents Based on User Query

- Convert user audio query to text (using AssemblyAI or other ASR models).
- Vectorize the text query and compute cosine similarity between query and subtitle embeddings.
- Rank and return the most relevant subtitle segments.

## Notebooks & Descriptions

### 1. Audio_2_Text.ipynb

- Converts **audio files into text** using **speech recognition models** using **AssemblyAI**.
- Useful for **transcription services, podcasts, and accessibility applications**.

### 2. Chroma_db_Embeddings_V2.ipynb

- Uses **ChromaDB** to create and manage **vector embeddings**.
- Enables **efficient similarity search, semantic retrieval, and document indexing**.
- Applied in **question-answering systems, AI-powered search engines, and NLP tasks**.

### 3. Gradio_Search_Engine_Demo.ipynb

- Implements a **search engine demo** using **Gradio**, allowing users to test queries interactively.
- Supports **keyword-based search, vector search (semantic search), or hybrid models**.
- Likely integrates with **ChromaDB embeddings** for **intelligent retrieval**.

### 4. Search_Engine_Extracting_Data.ipynb

- Focuses on **data extraction, scraping, and indexing** for a search engine.
- Handles **text preprocessing, tokenization, and document structuring**.
- Useful for **web crawlers, automated indexing, and structured data retrieval**.

### 5. Shazam_Clone_Search_Engine.ipynb

- Builds a **music recognition system** similar to **Shazam**.
- Enables **identification of audio, speeches, or sound patterns from audio samples**.

### 6. Subtitles_Chunking.ipynb

- Processes **subtitle files** by **splitting them into smaller text segments**.
- Helps in **automatic subtitle generation, video search indexing, and multilingual translation**.
- Includes **time-stamping, sentence segmentation, and embedding generation** for efficient retrieval.

### 7. Testing_Search_Mechanism.ipynb

- Evaluates the effectiveness of different **search algorithms**.
- Tests **ranking models, BM25, TF-IDF, and vector-based retrieval methods**.

## Libraries Used :

- gradio
- assemblyai
- pydub
- python-dotenv
- chromadb
- sentence-transformers

## Applications

- **Multimodal Search Engines**: Combining **text, audio, and embeddings** for **intelligent retrieval**.
- **Audio & Music Recognition**: Implementing a **Shazam-like** system for **identifying songs and sound patterns**.
- **Semantic Search & NLP**: Using **vector embeddings for AI-driven document retrieval**.
- **Interactive Demos & UI**: Leveraging **Gradio** for easy-to-use **search engine interfaces**.
- **Video & Subtitle Processing**: Extracting and structuring **subtitles for indexing and accessibility**.

## Summary

This project integrates **cutting-edge AI search technologies**, **text/audio processing**, and **interactive search tools**. With **vector databases, NLP models, and search ranking algorithms**, it offers **advanced media analysis, transcription, and retrieval capabilities**. 🚀

---

### Want to Contribute?

Feel free to **open issues, suggest improvements, or contribute** to enhance this project!

Let me know if you need modifications! 😊
