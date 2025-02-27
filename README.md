1. Create and use migrations:
 ``` 
  python manage.py makemigrations  
  python manage.py migrate
```
3. Setup ur SMTP in setting.py

4. Start celery
```
  celery -A email_service worker --loglevel=info
  celery -A email_service beat --loglevel=info
```

6. Start Django
```
  python manage.py runserver
```

8. Create superuser if needed:
```
  python manage.py createsuperuser
```
