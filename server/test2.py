import uuid
from langchain.llms.openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores.chroma import Chroma
# May need to install ChromaDB:
# pip install chromadb
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter

# Chroma
import chromadb
from chromadb.utils import embedding_functions


from dotenv import load_dotenv
load_dotenv()

llm = "gpt-3.5-turbo"


# embeddings = OpenAIEmbeddings()

def load_pdf(pdf):
    # print(pdf)
    # print(PyPDFLoader(pdf))
    return PyPDFLoader(pdf).load()


def r_text_splitter(loadPDF):
    chunk_size = 250,
    chunk_overlap = 20

    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=0,
        separators=["\n\n", "\n", "\. ", " ", ""]
    )
    # return r_splitter.split_text(loadPDF)
    return r_splitter.split_documents(loadPDF)


def ch_text_splitter(loadPDF):
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0
    )
    return text_splitter.split_documents(loadPDF)


file = "CISC-1115-Syllabus.txt"
file2 = "cisc-1115-course_description.txt"

loader = UnstructuredFileLoader(file)
# print("loader: ", loader)
doc = loader.load()
texts = r_text_splitter(doc)
print(doc)
print("--------")
print(texts)

print(type(texts))

length = len(texts)
ids = []
for i in range(length):

    ids.append(str(i))
# print(ids)
# Vectorstores
# persist_directory = '/chroma_db/'
# collection_name = file
# embedding = OpenAIEmbeddings()
# vectordb = Chroma.from_documents(texts, embedding=embedding)
# vectordb.persist()


# embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# client = chromadb.PersistentClient(path=persist_directory)
# collection = client.get_or_create_collection(name=collection_name)
# # print(len(texts))
# collection.add(documents=[texts], ids=ids)
