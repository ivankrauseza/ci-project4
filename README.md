# ci-project4 - Lavoro Booking System
Customers can book a workspace, Staff members can manage bookings, Superusers can manage everything.

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
- pip install django-allauth (add to installed apps)
- pip install django-crispy-forms (add to installed apps)
- configure settings.py and urls.py as per allauth documentation
- settings.py > import os
- settings.py > ALLOWED_HOSTS = ['localhost']
- settings.py > SITE_ID = 1
- settings.py > EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
- settings.py > CRISPY_TEMPLATE_PACK = 'uni_form'
- ADMIN > /admin/account/emailaddress/ (verify admin email address)

## Form Submissions
- settings.py > MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

## Templates

### Default Templates
- base.html
- index.html (temporary for testing)

### AllAuth Templates
- Copy default AllAuth templates to templates/account (extend base.html)
- settings.py > TEMPLATES > 'DIRS': [os.path.join(BASE_DIR, 'templates')],

## Libraries
- Bootstrap (5.3.2)
- jQuery (3.7.1)
- FontAwesome (4)

## Static files
- css
- js
- images
- favicon

## Bugs
- FIXED: CSS: background images not showing (path to static file needed to change)
- CALENDAR: User can manually edit calender field (prevent picking past date, only future)

## Resources
- Favicon (https://favicon.io/)
- https://jqueryui.com/datepicker/
- FALSE: https://timepicker.co/