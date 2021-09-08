from django_filters import rest_framework as filters

from mainapp.models import Post, Article
from mainapp.serializer import PostSerializer, ArticleSerializer


class PostFilter(filters.FilterSet):
    article = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Post
        fields = ['article']


class ArticleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Article
        fields = ['name']
