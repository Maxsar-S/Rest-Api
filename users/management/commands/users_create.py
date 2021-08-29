from django.core.management.base import BaseCommand

from users.models import User

class Command(BaseCommand):
    help = 'Create users for testing'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        count = options['count']
        for i in range(count):
            user = User.objects.create(first_name=f'fname{i}',
                                       last_name=f'lname{i}',
                                       username=f'uname{i}',
                                       email=f'email{i}',
                                       )
            print(f'user {user} created')
