@echo off
REM Activate virtual environment and run both FastAPI and Streamlit

echo 🔄 Activating virtual environment...
call .venv\Scripts\activate

echo 🚀 Starting FastAPI backend on port 8000...
start cmd /k "uvicorn app.api:app --host 0.0.0.0 --port 8000"

echo 🌐 Launching Streamlit frontend on port 8501...
streamlit run main.py

pause
