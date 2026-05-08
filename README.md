---
title: Rag Langchain Llama
emoji: 🔥
colorFrom: purple
colorTo: green
sdk: gradio
sdk_version: 6.14.0
python_version: '3.10'
app_file: app.py
pinned: false
short_description: RAG system using LangChain and Llama
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# 🤖 RAG LangChain Llama

A Retrieval-Augmented Generation (RAG) application built using LangChain, Gradio, and Llama models.  
The system allows users to ask questions about Generative AI research papers stored in PDF format.

## Features

- PDF document retrieval
- LangChain RAG pipeline
- Hugging Face deployment
- Gradio interactive UI
- Llama-based text generation

## Tech Stack

- Python
- LangChain
- Transformers
- Gradio
- Hugging Face Spaces

## Demo

https://huggingface.co/spaces/ThuHoangAnh/rag-langchain-llama

## Installation

```bash
pip install -r requirements.txt
python app.py
```

## Project Structure

```text
src/
 ├── base/
 ├── rag/
 ├── app.py
```

## Example Questions

- What is the main idea of Attention Is All You Need?
- Explain the difference between BERT and GPT.
- What are the innovations introduced in DeepSeek-V3?