# app/llm_groq.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def ask_llm(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "mixtral-8x7b-32768",  # Or llama3-8b-8192, etc.
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }
    res = requests.post(GROQ_API_URL, headers=headers, json=body)
    res.raise_for_status()
    return res.json()["choices"][0]["message"]["content"]
