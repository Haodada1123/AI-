@echo off
chcp 65001 >nul
set PYTHONUNBUFFERED=1
"D:\quark-download\实习\.venv\Scripts\python.exe" manage.py runserver
pause
