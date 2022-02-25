from rest_framework.serializers import ModelSerializer

from users.serializer import UserModelSerializer
from mainapp.models import Article, Post


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleGetSerializer(ArticleSerializer):
    # author = HyperlinkedRelatedField(view_name='user-detail',
    #                                   read_only=True,)
    author = UserModelSerializer()


class PostSerializer(ModelSerializer):
    # author = UserModelSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class PostGetSerializer(PostSerializer):
    author = UserModelSerializer()
    article = ArticleSerializer()
