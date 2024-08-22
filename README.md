# book_me: Appiontment Booking System
Full-stack appointment booking system designed to manage client appointments and scheduling. This application features user authentication, appointment scheduling, and automated email notifications. This app will not work without proper configuration not detailed below.

## Technologies used
-**Backend:** Python (Flask)

-**Frontend:** HTML, CSS, JavaScript

-**Database:** SQLite (easily replacable)

-**Email Notifications:** Flask-Mail

-**Frameworks:** Django, Gunicorn, Nginx

## Dependencies
To install required dependencies use

`pip install -r requirements.txt`

## Activating virtual environment

`python3 -m venv env`

`source env/bin/activate`

## Setting up database

`python manage.py migrate`

## Managing gunicorn 

`gunicorn -c config/gunicorn/dev.py` run quietly

`lsof -i :8000` view gunicorn pid

## Useful links

[Setup](https://realpython.com/django-nginx-gunicorn/)

[Django documentation](https://docs.djangoproject.com/en/5.1/)
