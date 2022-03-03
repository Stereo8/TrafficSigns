@echo off

call .venv/Scripts/activate.bat

cd django-projekat

if %1 == "-h" (
  call "python manage.py runserver 0.0.0.0:8000"
) else (
  call "python manage.py runserver"
)

