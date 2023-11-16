from langchain.llms.openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores.chroma import Chroma
# May need to install ChromaDB:
# pip install chromadb
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA



from dotenv import load_dotenv
load_dotenv()

llm = "gpt-3.5-turbo"
persist_directory = '/chroma_db/'

embeddings = OpenAIEmbeddings()
collection_name = "doc_embeddings"
vectordb = Chroma(persist_directory=persist_directory,
                  embedding_function=embeddings, collection_name=collection_name)

# print(vectordb._collection.count())


def load_pdf(pdf):
    return PyPDFLoader(pdf).load()


def r_text_splitter(loadedPDF):
    chunk_size = 200,
    chunck_overlap = 0

    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size,
        chunck_overlap,
        separators=["\n\n", "\n", "\. ", " ", ""]
    )
    return r_splitter.split_text(loadedPDF)


def doc_assist(file, query):
    texts = r_text_splitter(load_pdf(file))
    # Vectorstores
    db = Chroma.from_documents(texts, embeddings)
    retriever = db.as_retriever(
        search_type="similarity", search_kwargs={"k": 2})
    # result = db.similarity_search(query, k=2)
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(temperture=0), chain_type="map reduce", retriever=retriever, return_source_documents=True)
    
    return qa({"query": query})