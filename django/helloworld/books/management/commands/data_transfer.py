from django.core.management import BaseCommand
from django.db import connections

from argparse import ArgumentParser


class Command(BaseCommand):
    help = 'Transfer data from one database to another'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('source', type=str, help='Alias for source database as it is scripted in settings.py')
        parser.add_argument('target', type=str, help='Alias for target database as it is scripted in settings.py')

    def handle(self, *args, **options):
        source = options['source']
        target = options['target']

        if {source, target} <= set(connections):
            connections[source].connect()
            source = connections[source].connection
            connections[target].connect()
            target = connections[target].connection
            source.backup(target)
            print('Data was transferred successfully')
        else:
            raise KeyError('wrong alias')

