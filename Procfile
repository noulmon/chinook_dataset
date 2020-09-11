web: gunicorn chinook_datasets.wsgi:application
release: python manage.py collectstatic --noinput && python manage.py load_database
