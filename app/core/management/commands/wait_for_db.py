"""
Django command to wait for DB to be available
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait the DB"""

    def handle(self, *args, **options):
        pass