"""GeekApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from mainapp.views import ArticleViewSet, PostViewSet
from users.views import UsersViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="GeekApp",
        default_version='0.1',
        description="Documentation to GeekApp project",
        contact=openapi.Contact(email="alekseibarannikov@gb.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('articles', ArticleViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('views/', include('mainapp.urls')),
    path('api/', include(router.urls)),
    re_path(r'^api/(?P<version>\d\.\d)/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    # path('users/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
