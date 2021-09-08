from django.core.management.base import BaseCommand

from mainapp.models import Post

class Command(BaseCommand):
    help = 'Create users for testing'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        Post.objects.all().delete()
        count = options['count']
        for i in range(count):
            post = Post.objects.create(name=f'fname{i}',
                                       author=f'fauthor{i}',
                                       article=f'farticle{i}',
                                       text=f'text{i}',
                                       )
            print(f'post {post} created')
