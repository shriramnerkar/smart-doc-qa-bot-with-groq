@echo off
REM Activate your virtual environment (if any)
REM call venv\Scripts\activate

echo Starting Smart Document QA Bot...
set FLASK_APP=app/main.py
set FLASK_ENV=development
flask run

pause
