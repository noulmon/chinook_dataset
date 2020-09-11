web: gunicorn chinook_dataset.wsgi:application
release: python manage.py collectstatic --noinput && python manage.py load_database
