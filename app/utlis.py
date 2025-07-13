# app/utils.py
from PyPDF2 import PdfReader

def extract_text_from_pdf(file) -> str:
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text
