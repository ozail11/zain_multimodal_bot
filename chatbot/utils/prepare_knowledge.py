from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from chatbot.models import KnowledgeItem

def build_vectorstore(vectorstore_path="faiss_index"):
    items = KnowledgeItem.objects.all()
    documents = []

    for item in items:
        doc = Document(
            page_content=item.answer,
            metadata={"question": item.question}
        )
        documents.append(doc)

    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(documents, embeddings)
    db.save_local(vectorstore_path)

    print(f"Vectorstore saved locally at: {vectorstore_path}")
