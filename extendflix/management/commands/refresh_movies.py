from django.core.management.base import BaseCommand, CommandError
from extendflix.views import update_movies


class Command(BaseCommand):
    help = 'Reloads the movies from the API'

    def handle(self, *args, **options):
        return update_movies()
