#!/usr/bin/env bash

# Comandos para preparar o Django
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

# Inicia o servidor Gunicorn (obrigatório para produção)
gunicorn setup.wsgi:application --bind 0.0.0.0:$PORT