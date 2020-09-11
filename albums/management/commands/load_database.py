# from hasura_datasets.settings import ON_HEROKU
import os

import psycopg2
import urllib.parse as urlparse
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            if settings.ON_HEROKU:
                url = urlparse.urlparse(os.environ['DATABASE_URL'])
                database = url.path[1:]
                user = url.username
                password = url.password
                host = url.hostname
            else:
                host="localhost"
                database="hasura_datasets"
                user="postgres"
                password="root"
            # establishing the database connection
            
            connection = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password,
            )

            connection.autocommit = True

            # reading chinook dataset sql file
            sql_file = open(os.path.join('chinook_postgres.sql'), 'r', encoding="utf8")
            with connection.cursor() as cursor:
                # inserting data into the database
                cursor.execute(sql_file.read())
                print('Successfully added database!')
        except Exception as e:
            print(e)
