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

# Chroma
import chromadb
from chromadb.utils import embedding_functions


# from dotenv import load_dotenv
# load_dotenv()

llm = "gpt-3.5-turbo"


# embeddings = OpenAIEmbeddings()

def load_pdf(pdf):
    # print(pdf)
    # print(PyPDFLoader(pdf))
    return PyPDFLoader(pdf).load()

# Use ch_splitter for now.


def r_text_splitter(loadPDF):
    chunk_size = 250,
    chunk_overlap = 20

    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
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


file = "CISC-1115-Syllabus.pdf"
file2 = "cisc-1115-course_description.txt"

pdf = load_pdf(file)
# print(len(pdf))
# print("-------")
document = ch_text_splitter(pdf)
print(document)
print(len(document))


# Vectorstores
persist_directory = '/chroma_db/'
collection_name = file
embeddings = embedding_functions.DefaultEmbeddingFunction()
embeddings2 = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# print(collection_name)
client = chromadb.PersistentClient(path=persist_directory)
collection = client.get_or_create_collection(
    name=collection_name, embedding_function=embeddings
)

# Create a list of unique ids for each document based on the content
# ids = [str(uuid.uuid5(uuid.NAMESPACE_DNS, doc.page_content))
#        for doc in document]
# unique_ids = list(set(ids))
# print(unique_ids)

# Ensure that only docs that correspond to unique ids are kept and that only one of the duplicate ids is kept
# seen_ids = set()
# unique_docs = [doc for doc, id in zip(
#     document, ids) if id not in seen_ids and (seen_ids.add(id) or True)]
# my_model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
# embedding_model = SentenceTransformerEmbeddings(model_name=my_model_name)
# default_ef = embedding_functions.DefaultEmbeddingFunction()
# Add the unique documents to your database
# db = Chroma.from_documents(unique_docs, embeddings, ids=unique_ids, persist_directory=persist_directory)

# for doc in document:
#     ids = str(uuid.uuid5(uuid.NAMESPACE_DNS, doc.page_content))
#     # print (doc)
#     # print(ids)
#     print(type(doc))
#     collection.add(documents=doc, ids=ids)
collection.add(documents=document, ids=["id1", "id2"])



print(collection)

# vectordb = Chroma(persist_directory=persist_directory,
#   embedding_function=embeddings, collection_name="test")
# vectordb = Chroma.from_documents(document, embeddings, persist_directory=persist_directory)
# vectordb = Chroma.from_texts(document, embeddings2)
# print(vectordb._collection.count())
# retriever = vectordb.as_retriever(
#     search_type="similarity", search_kwargs={"k": 1})
# result = db.similarity_search(query, k=2)
# qa = RetrievalQA.from_chain_type(
#     llm=OpenAI(temperture=0), chain_type="map reduce", retriever=retriever, return_source_documents=True)

# query = """
# How many assignments?
# """
# result = qa({"query": query})
# print(result)
