from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

def load_and_prepare_doc(filepath):
    from langchain.document_loaders import PyPDFLoader
    loader = PyPDFLoader(filepath)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    return chunks

def get_qa_chain(chunks):
    # Embedding for vector store
    embeddings = OpenAIEmbeddings()

    # Create vector index from document chunks
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # 👇 Here's where GPT-3.5 Turbo is used
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # Create a RetrievalQA chain using GPT-3.5 + vector retriever
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa_chain
