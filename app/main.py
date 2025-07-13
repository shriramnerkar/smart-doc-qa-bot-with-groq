# app/main.py
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from app.qa_bot import generate_answer

app = FastAPI()

@app.post("/ask")
async def ask(file: UploadFile = File(...), question: str = Form(...)):
    if file.filename.endswith(".pdf"):
        content = await file.read()
        answer = generate_answer(file=content, user_question=question)
        return JSONResponse(content={"answer": answer})
    return JSONResponse(status_code=400, content={"error": "Only PDFs are supported"})
