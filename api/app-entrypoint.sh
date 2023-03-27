#!/bin/bash

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput --clear

echo "Starting app in DEBUG=$DEBUG"
gunicorn --access-logfile - --workers 3 -b 0.0.0.0:8001 config.wsgi