# Aula: Introdução a RAG (Retrieval-Augmented Generation)

Repositório com os materiais da aula demonstrativa sobre RAG (Retrieval-Augmented Generation), apresentada como parte da avaliação no SENAI.

## O que é RAG?

RAG é uma técnica que permite que um LLM responda perguntas com base em **dados privados**, buscando informações relevantes em uma base de dados e injetando esse contexto no prompt antes de gerar a resposta.

## Estrutura

```
├── demo_rag/                         # Demo: bot de onboarding com RAG
│   ├── demo_rag.py                   # Pipeline RAG completo
│   ├── guia_engenharia.md            # Documento interno simulado
│   ├── requirements.txt              # Dependências
│   └── .env.example                  # Template da chave de API
│
└── embedding/                        # Visualização de embeddings
    ├── embedding_3d.py               # Script que gera o gráfico 3D
    └── embeddings_3d_interativo.png  # Imagem gerada
```

## Como Rodar

```bash
cd demo_rag
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Edite com sua GOOGLE_API_KEY
python demo_rag.py
```

## Tecnologias

- **LangChain** — orquestração do pipeline RAG
- **ChromaDB** — banco de dados vetorial
- **Google Gemini** — LLM e modelo de embeddings
- **Matplotlib** — visualização 3D dos embeddings
