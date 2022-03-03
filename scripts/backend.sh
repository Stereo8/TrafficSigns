#! /bin/bash

source .venv/bin/activate

cd django-projekat

if [ $1 = "-h" ]
then
  python manage.py runserver 0.0.0.0:8000
else
  python manage.py runserver
fi