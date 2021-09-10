from rest_framework.relations import HyperlinkedRelatedField, StringRelatedField
from rest_framework.serializers import ModelSerializer

from users.serializer import UserModelSerializer
from mainapp.models import Article, Post


class PostSerializer(ModelSerializer):
    author = UserModelSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class ArticleSerializer(ModelSerializer):
    author = StringRelatedField()

    class Meta:
        model = Article
        fields = '__all__'


class ArticleGetSerializer(ArticleSerializer):
    author = HyperlinkedRelatedField(view_name='author-detail',
                                      read_only=True,)
