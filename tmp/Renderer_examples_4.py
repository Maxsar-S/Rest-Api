from rest_framework import serializers

from python_models import Article, User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()


class BiographySerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1024)
    user = UserSerializer()


class ArticleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    authors = UserSerializer(many=True)


class PostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    author = UserSerializer()

user1 = User('Грин', 1880)
serializer = UserSerializer(user1)
print(serializer.data)

user2 = User('Пушкин', 1799)
article = Article('Некоторая книга', [user1, user2])

serializer = ArticleSerializer(article)
print(serializer.data)
