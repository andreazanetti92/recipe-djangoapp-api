"""
Django command to wait for DB to be available
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait the DB"""

    def handle(self, *args, **options):
        """Entrypoint for Django command"""
        self.stdout.write('waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 secs...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Available!'))