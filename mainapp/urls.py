from django.urls import path, include
from rest_framework.routers import DefaultRouter

import mainapp.views as mainapp

router = DefaultRouter()
router.register('articles', mainapp.ArticleViewSet)
router.register('posts', mainapp.PostViewSet)

urlpatterns = [
    path('view/set/', include(router.urls)),
]
