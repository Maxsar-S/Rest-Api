from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Create superuser'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username = options['username']
        user = User.objects.create_superuser(
            first_name=f'f_name_{username}',
            last_name=f'l_name_{username}',
            username=f'superuser_name_{username}',
            email=f'superuser_email{username}@gmail.com',
            password="GeekApp"
            )

        print(f'{user} was created')