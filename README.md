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

## Authentication
- pip install django-allauth
- configure settings.py and urls.py as per allauth documentation
- settings.py > import os
- settings.py > ALLOWED_HOSTS = ['localhost']
- settings.py > SITE_ID = 1
- settings.py > EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
- ADMIN > /admin/account/emailaddress/ (verify admin email address)