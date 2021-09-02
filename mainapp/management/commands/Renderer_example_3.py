from django.core.management.base import BaseCommand
from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField

from users.models import User, Biography
from mainapp.models import Article, Post


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
                fields = '__all__'

        class ArticleSerializer(serializers.ModelSerializer):
            # authors = serializers.StringRelatedField(many=True)
            authors = HyperlinkedRelatedField(view_name='user-detail',
                                              read_only=True,
                                              many=True)



            class Meta:
                model = Article
                fields = '__all__'

        user1 = User.objects.create(first_name='Михаил',
                                        last_name='Лермонтов',
                                        birthday_year=1814)


        user2 = User.objects.create(first_name='Александр',
                                        last_name='Пушкин',
                                        birthday_year=1799)
        article = Article.objects.create(name='Некоторая книга')
        article.author.add(user1)
        article.author.add(user2)
        article.save()
        serializer = ArticleSerializer(article)
        print(serializer.data)
