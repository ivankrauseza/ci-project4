# ci-project4 - Lavoro Booking System
Lavaro ('Work' in Italian) is a company that provides shared office space, but also sells consumer pods to the general public for remote working. Customers can book a workspace, Staff members can manage bookings, Superusers can manage everything.

## Features
- Guest: Book a demonstration
- Customer: Sign up to become a member
- Admin: Manage Platform


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
- FONTAWESOME: icons flashing on reload

## Resources
- Favicon (https://favicon.io/)
- https://jqueryui.com/datepicker/
- FALSE: https://timepicker.co/
- Google Fonts (Roboto)
- Logo Icon https://www.freepik.com/free-vector/lion-fire-gradient-mascot-illustration-logo-design_54089107.htm#query=flame%20head&position=18&from_view=search&track=ais&uuid=17e479dc-1bd0-4830-8e21-a8fb72937208
- Meeting image : https://www.freepik.com/free-vector/social-distancing-meeting-illustration-theme_8256854.htm#query=meeting%20room&position=0&from_view=search&track=ais&uuid=57a3fe96-1158-4868-8372-122d8170d273
- LinkedIn Learning: https://www.linkedin.com/learning/django-forms/
- GoogleAuth: https://pylessons.com/django-google-oauth
- https://www.toptal.com/designers/htmlarrows/symbols/