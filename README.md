1. Create and use migrations:
  python manage.py makemigrations
  python manage.py migrate

2. Setup ur SMTP in setting.py

3. Start celery
  celery -A email_service worker --loglevel=info  
  celery -A email_service beat --loglevel=info

4. Start Django
  python manage.py runserver

5. Create superuser if needed:
  python manage.py createsuperuser
