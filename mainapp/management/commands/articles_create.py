from django.core.management.base import BaseCommand

from mainapp.models import Article


class Command(BaseCommand):
    help = 'Create users for testing'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        Article.objects.all().delete()
        count = options['count']
        for i in range(count):
            article = Article.objects.create(name=f'fname{i}',
                                             authors=f'fauthors{i}',
                                             )
            print(f'Article {Article} created')
