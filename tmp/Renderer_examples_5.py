from rest_framework import serializers
from django.core.management.base import BaseCommand
from mainapp.models import  Post, Article
from users.models import User, Biography


class Command(BaseCommand):

    def handle(self, *args, **options):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = '__all__'

        class BiographySerializer(serializers.ModelSerializer):
            class Meta:
                model = Biography
                fields = ['text', 'user']

        class PostSerializer(serializers.ModelSerializer):
            author = UserSerializer()

            class Meta:
                model = Post
                exclude = ['name']

        class ArticleSerializer(serializers.ModelSerializer):
            authors = serializers.StringRelatedField(many=True)

            class Meta:
                model = Article
                fields = '__all__'

        user1 = User.objects.create(name='Грин', birthday_year=1880)
        serializer = UserSerializer(user1)
        print(serializer.data)  # {'id': 17, 'name': 'Грин', 'birthday_year': 1880}

        biography = Biography.objects.create(text='Некоторая биография', author=user1)
        serializer = BiographySerializer(biography)
        print(serializer.data)  # {'text': 'Некоторая биография', 'author': 17}

        post = Post.objects.create(name='Некоторый пост', author=user1)
        serializer = PostSerializer(post)
        print(serializer.data)  # {'id': 8, 'author': OrderedDict([('id', 17), ('name', 'Грин'), ('birthday_year', 1880)])}

        user2 = User.objects.create(name='Пушкин', birthday_year=1799)
        article = Article.objects.create(name='Некоторая статья')
        article.authors.add(user1)
        article.authors.add(user2)
        article.save()
        serializer = ArticleSerializer(article)
        print(serializer.data)  #
