import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from werkzeug.utils import secure_filename

# Load and split PDF into text chunks
def load_and_split_pdf(filepath, chunk_size=1000, chunk_overlap=200):
    try:
        loader = PyPDFLoader(filepath)
        documents = loader.load()
        splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        chunks = splitter.split_documents(documents)
        return chunks
    except Exception as e:
        print(f"[ERROR] Failed to load PDF: {e}")
        return []

# Save uploaded file securely
def save_uploaded_file(file_obj, upload_dir):
    filename = secure_filename(file_obj.filename)
    filepath = os.path.join(upload_dir, filename)
    file_obj.save(filepath)
    return filepath

# Optional: Clean text (remove extra spaces/newlines)
def clean_text(text):
    return ' '.join(text.split())
