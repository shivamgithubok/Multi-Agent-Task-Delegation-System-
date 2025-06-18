import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

load_dotenv()

def load_and_split_docs(directory:str):
    docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            loader= TextLoader(os.apth.join(directory,filename))
            loaded_docs = loader.load()
            docs.extend(splitter.split_documents(loaded_docs))
    return docs

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))

def create_vector_db(docs):
    return Chroma.from_documents(docs, embedding=embeddings, persist_directory="./chromadb")

def get_retrieval_qa(vectorstore):
    retriever = vectorstore.as_retriever()
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain

# Initialize everything
docs = load_and_split_docs("data/docs")
vectordb = create_vector_db(docs)
qa_chain = get_retrieval_qa(vectordb)

# 5. Final callable agent
class KnowledgeRetrieverAgent:
    def retrieve_answer(self, user_query: str) -> str:
        result = qa_chain.run(user_query)
        return result.strip()