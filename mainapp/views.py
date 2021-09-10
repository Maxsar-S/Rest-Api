from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from mainapp.filters import PostFilter
from mainapp.models import Article, Post
from mainapp.pagination import LimitOffsetPaginationByTwenty, LimitOffsetPaginationByTen
from mainapp.serializer import ArticleSerializer, ArticleGetSerializer, PostSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    pagination_class = LimitOffsetPaginationByTen
    serializer_class = ArticleSerializer

    # def get_serializer_class(self):
    #     # if self.request.method in ['GET']:
    #     #     return ArticleGetSerializer
    #     return ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPaginationByTwenty
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


