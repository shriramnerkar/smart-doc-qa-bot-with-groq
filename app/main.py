from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.qa_bot import generate_answer

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask(file: UploadFile = File(...), question: str = Form(...)):
    if file.filename.endswith(".pdf"):
        content = await file.read()
        answer = generate_answer(file=content, user_question=question)
        return JSONResponse(content={"answer": answer})
    return JSONResponse(status_code=400, content={"error": "Only PDFs are supported"})
