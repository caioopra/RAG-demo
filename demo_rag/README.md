# Demo RAG - Onboarding Bot

Sistema de perguntas e respostas usando RAG (Retrieval-Augmented Generation) com LangChain e Google Gemini.

O bot responde perguntas de desenvolvedores com base em um documento interno da empresa (`guia_engenharia.md`).

## Como funciona

1. Carrega o documento interno
2. Quebra o texto em chunks
3. Gera embeddings e indexa no ChromaDB
4. Busca os chunks mais relevantes por similaridade
5. Injeta o contexto no prompt e envia ao LLM

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Crie um arquivo `.env` com sua chave da API do Google:

```
GOOGLE_API_KEY=your_google_api_key_here
```

## Executar

```bash
python demo_rag.py
```
