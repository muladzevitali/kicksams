from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command for initializing data to user app: user"""
    help = 'Initialize default data: admin_user'

    def handle(self, *args, **options):
        call_command('loaddata', 'media/initial_data/locations/countries.json')
        call_command('loaddata', 'media/initial_data/locations/city_names.json')
        call_command('loaddata', 'media/initial_data/locations/cities.json')
