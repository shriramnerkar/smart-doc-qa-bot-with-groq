@echo off
echo Starting Smart Document QA Bot...
set FLASK_APP=main.py
set FLASK_ENV=development
flask run
pause
