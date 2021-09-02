from rest_framework.viewsets import ModelViewSet

from mainapp.models import Article, Post
from mainapp.serializer import ArticleSerializer, PostSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
