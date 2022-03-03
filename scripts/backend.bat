@echo off

cd django-projekat

call .venv/Scripts/activate.bat
if %1 == -h (call python manage.py runserver 0.0.0.0:8000) else (call python manage.py runserver)