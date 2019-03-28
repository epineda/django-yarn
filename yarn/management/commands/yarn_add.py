from django.core.management.base import BaseCommand
from yarn.finders import yarn_add


class Command(BaseCommand):
    help = 'Run yarn add'

    def handle(self, *args, **options):
        yarn_add()
