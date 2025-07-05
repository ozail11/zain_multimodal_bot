from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import OpenAI
import os

def get_response_from_knowledge(question, vectorstore_path="faiss_index"):
    if not os.path.exists(vectorstore_path):
        return "قاعدة المعرفة غير جاهزة."

    embeddings = HuggingFaceEmbeddings()
    db = FAISS.load_local(vectorstore_path, embeddings)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(temperature=0), retriever=db.as_retriever())
    return qa.run(question)
