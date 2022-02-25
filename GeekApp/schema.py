import graphene
from graphene import Schema, ObjectType, String, List, Field
from graphene_django import DjangoObjectType

from mainapp.models import Article, Post
from users.models import User


class UserDjangoType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ArticleDjangoType(DjangoObjectType):
    class Meta:
        model = Article
        fields = '__all__'


class PostDjangoType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'


class Query(ObjectType):
    all_users = List(UserDjangoType)
    user_by_id = Field(UserDjangoType,
                       pk=int(required=True))
    all_posts = List(PostDjangoType)
    all_articles = graphene.List(ArticleDjangoType)
    article_by_name = graphene.List(ArticleDjangoType,
                                    name=String())

    def resolve_all_articles(root, info):
        return Article.objects.all()

    def resolve_article_by_name(root, info, name):
        return Article.objects.filter(name__contains=name)

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user_by_id(root, info, pk):
        return User.objects.filter(pk=pk).first()

    def resolve_all_posts(root, info):
        return Post.objects.all()


class UserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(UserDjangoType)

    @classmethod
    def mutate(cls, root, info, email, id):
        user = User.objects.get(pk=id)
        user.email = email
        user.save()
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()


schema = Schema(query=Query, mutation=Mutation)
