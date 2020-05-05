#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn pixies.wsgi:application --bind 0.0.0.0:$PORT --log-file -
