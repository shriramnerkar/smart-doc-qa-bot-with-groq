import io
from app.utils import extract_text_from_pdf
from app.llm_groq import ask_llm

def generate_answer(file_bytes: bytes, user_question: str):
    file_stream = io.BytesIO(file_bytes)
    pdf_text = extract_text_from_pdf(file_stream)

    prompt = f"""You are an expert assistant. Based on the following document:
---
{pdf_text}
---
Answer the question: {user_question}
"""
    return ask_llm(prompt)
