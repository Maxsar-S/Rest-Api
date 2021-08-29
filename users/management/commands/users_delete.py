from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Delete users'

    def hadle(self, *args, **options):
        User.objects.all().delete()