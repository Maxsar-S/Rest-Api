from django_filters import rest_framework as filters

from mainapp.models import Post


class PostFilter(filters.FilterSet):
    article = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Post
        fields = ['article']
