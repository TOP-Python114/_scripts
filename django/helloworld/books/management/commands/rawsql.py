from django.core.management import BaseCommand
from django.db import connections

from argparse import ArgumentParser
from pathlib import Path
from sys import path


BASE_DIR = Path(path[0])


class Command(BaseCommand):
    help = 'Raw SQL script execution'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('script_name', type=str, help='SQL script relative path from the project directory')
        parser.add_argument('-d', '--database', type=str, help='Database alias as it scripted in settings.py to reference required connected engine')

    def handle(self, *args, **options):
        if options['database']:
            db_alias = options['database']
        else:
            db_alias = 'default'

        script = (BASE_DIR / options['script_name']).read_text(encoding='utf-8')

        with connections[db_alias].cursor() as cursor:
            for query in set(script.split(';')) - {''}:
                # print(f'\n{query.strip()}')
                res = cursor.execute(query.strip())
                connections[db_alias].commit()
                print(*res.fetchall(), sep='\n')

