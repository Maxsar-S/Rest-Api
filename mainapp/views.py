from rest_framework import status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from mainapp.filters import ArticleFilter, PostFilter
from mainapp.models import Article, Post
from mainapp.pagination import LimitOffsetPaginationByTwenty, LimitOffsetPaginationByTen
from mainapp.serializer import ArticleSerializer, PostSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = LimitOffsetPaginationByTen
    filterset_class = ArticleFilter


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPaginationByTwenty
    filterset_class = PostFilter


    def destroy(self, request, *args, **kwargs):
        Post.objects.filter(pk=kwargs['pk']).update(is_active=False)
        return Response(status=status.HTTP_204_NO_CONTENT)
