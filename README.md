# ci-project4 - Lavoro Booking System
CI Project 4

## Initial Setup
- django-admin startproject lavoro
- python manage.py startapp booking
- touch .env
- touch .gitignore (add env to gitignore)

## Admin
- python manage.py makemigrations / python manage.py makemigrations --dry-run
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver (test admin)
