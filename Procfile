web: gunicorn ContactList.wsgi --workers 1 --threads 4 --worker-class gthread --bind 0.0.0.0:$PORT --timeout 120 --access-logfile -
release: python manage.py migrate && python manage.py create_superuser
