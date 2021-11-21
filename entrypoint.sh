#! /bin/bash
python travel_site/manage.py makemigrations --no-input

python travel_site/manage.py migrate --no-input

cd travel_site/
exec gunicorn core.wsgi:application -b 0.0.0.0:8000 --reload