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

#Chroma
import chromadb



from dotenv import load_dotenv
load_dotenv()

llm = "gpt-3.5-turbo"
persist_directory = '/chroma_db/'

embeddings = OpenAIEmbeddings()
# embeddings2 = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

def load_pdf(pdf):
    # print(pdf)
    print(PyPDFLoader(pdf))
    return PyPDFLoader(pdf).load()

# Not working. Use ch_splitter intead.
def r_text_splitter(loadedPDF):
    chunk_size = 250,
    chunk_overlap = 20

    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
        separators=["\n\n", "\n", "\. ", " ", ""]
    )
    return r_splitter.split_text(loadedPDF)

def ch_text_splitter(loadPDF):
    text_splitter = CharacterTextSplitter(
        chunk_size = 200,
        chunk_overlap = 0
    )
    return text_splitter.split_documents(loadPDF)



file = "CISC-1115-Syllabus.pdf"
file2 = "course.pdf"

pdf = load_pdf(file)
print(pdf)
# loader = PyPDFLoader(file)
# print(loader)
# documents = loader.load()
# print(documents)
# documents = r_text_splitter(load_pdf(file2))
# print(documents)

document = ch_text_splitter(pdf)
print(document)


# Vectorstores
collection_name = '${file}_embeddings'
vectordb = Chroma(persist_directory=persist_directory,
                  embedding_function=embeddings, collection_name="test")

vectordb = Chroma.from_documents(document, embeddings)
# vectordb = Chroma.from_texts(document, embeddings2)
print(vectordb._collection.count())
# retriever = vectordb.as_retriever(
#     search_type="similarity", search_kwargs={"k": 1})
# # result = db.similarity_search(query, k=2)
# qa = RetrievalQA.from_chain_type(
#     llm=OpenAI(temperture=0), chain_type="map reduce", retriever=retriever, return_source_documents=True)

# query = """
# How many assignments?
# """
# result = qa({"query": query})
# print(result)