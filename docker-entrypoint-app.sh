#!/bin/bash

# Apply database migrations
#python manage.py makemigrations
#python manage.py migrate

# Collect static files
#python manage.py collectstatic --noinput

#export DJANGO_SETTINGS_MODULE=core.settings

# Start server
python manage.py runserver 0.0.0.0:${WEB_PORT}
