# app/qa_bot.py
from .utils import extract_text_from_pdf
from .llm_groq import ask_llm

def generate_answer(file, user_question: str):
    pdf_text = extract_text_from_pdf(file)
    prompt = f"""You are an expert assistant. Based on the following document:
---
{pdf_text}
---
Answer the question: {user_question}
"""
    return ask_llm(prompt)
