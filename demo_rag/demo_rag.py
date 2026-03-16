from dotenv import load_dotenv

# Importando as ferramentas do LangChain
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


def main():
    print("Iniciando o sistema de Onboarding Bot (RAG)...\n")

    # =====================================================================
    # FASE 1: INGESTÃO DE DADOS (O Preparo)
    # =====================================================================

    # 1. Carregando o documento privado da empresa
    print("[1/4] Carregando documento interno...")
    loader = TextLoader("guia_engenharia.md", encoding="utf-8")
    documento = loader.load()

    # 2. Quebrando o texto em pedaços (Chunking)
    # Motivo: LLMs têm limite de contexto e queremos apenas as partes relevantes
    print("[2/4] Quebrando o documento em Chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,  # Tamanho de caracteres por bloco
        chunk_overlap=50,  # Sobreposição para não perder o sentido das frases
    )
    chunks = text_splitter.split_documents(documento)

    # 3. Criando os Embeddings e salvando no Banco de Dados Vetorial (ChromaDB)
    print("[3/4] Gerando Embeddings e indexando no Banco Vetorial...")
    # Aqui a "Mágica Matemática" acontece: Texto vira Vetor
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001"),
    )

    # =====================================================================
    # FASE 2: RECUPERAÇÃO E GERAÇÃO (Tempo de Execução)
    # =====================================================================

    # Pergunta de um Dev Júnior entrando na empresa:
    pergunta_usuario = (
        "Qual branch devo usar para subir algo em produção? Posso usar a master?"
    )
    print(f"\n[Usuário Pergunta]: {pergunta_usuario}\n")

    # 4. Buscando por similaridade no banco
    print("[4/4] Buscando no banco (Cosine Similarity) e acionando o LLM...\n")
    retriever = vector_db.as_retriever(
        search_kwargs={"k": 2}
    )  # Traz os 2 pedaços mais parecidos
    documentos_recuperados = retriever.invoke(pergunta_usuario)

    # Pegando apenas o texto dos pedaços encontrados para montar o contexto
    contexto_injetado = "\n".join([doc.page_content for doc in documentos_recuperados])

    # 5. Criando o Prompt e Injetando o Contexto
    template = """Você é um assistente sênior de engenharia de software da TechCorp.
    Responda à pergunta do desenvolvedor de forma direta, baseando-se APENAS no contexto abaixo.
    Se a resposta não estiver no contexto, diga que não sabe.

    Contexto da Empresa:
    {contexto}

    Pergunta do Desenvolvedor: {pergunta}
    
    Resposta:"""

    prompt = PromptTemplate.from_template(template)

    # Exibindo o prompt completo que será enviado ao modelo
    prompt_formatado = prompt.format(
        contexto=contexto_injetado, pergunta=pergunta_usuario
    )
    print("=================== PROMPT ENVIADO ===================")
    print(prompt_formatado)
    print("=======================================================\n")

    # 6. Enviando para o LLM gerar a resposta final
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", temperature=0)

    # Montando a chamada: Formata o prompt -> Passa pro LLM
    chain = prompt | llm

    resposta_final = chain.invoke({
        "contexto": contexto_injetado,
        "pergunta": pergunta_usuario,
    })

    print("=====================================================")
    print(f"🤖 [Bot Responde]:\n{resposta_final.content}")
    print("=====================================================")


if __name__ == "__main__":
    main()
