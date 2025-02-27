from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_chroma import Chroma
import chromadb
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter


# Application Title
#      Ask About Me: AI-powered Personal Assistant


def create_db():
    load_dotenv()

    # Load documents - Resume.docx, About project - .txt
    # loader_proj = TextLoader("./Docs/project_info.txt")
    loader_resume = TextLoader("./Docs/my_resume_paragraph_based.txt")

    docs_resume = loader_resume.load()
    # docs_proj = loader_proj.load()

    # create chunks
    chunks_resume = []
    txt_splitter = CharacterTextSplitter(separator="\n\n", is_separator_regex=False)
    for i, doc in enumerate(docs_resume):
        print("Resume doc no: ", i+1)
        chunks = txt_splitter.split_text(doc.page_content)
        chunks_resume += chunks

    for i, chunk in enumerate(chunks_resume):
        print(f"Chunk no: {i+1} : {chunk}")


    # define model
    # llm_gemini = GoogleGenerativeAI(model="gemini-pro")
    # llm_openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    #
    # # define vector database - chroma db
    # client_chroma = chromadb.PersistentClient()
    # chroma_db_resume = Chroma(
    #     client=client_chroma,
    #     collection_name="my_resume",
    #     embedding_function=llm_openai_embeddings
    # )
    #
    # chroma_db_resume.add_texts(chunks_resume)
    #
    # print("Done")