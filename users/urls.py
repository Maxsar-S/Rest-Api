from django.urls import path, include
from rest_framework.routers import DefaultRouter
import users.views as users

router = DefaultRouter()
router.register('users', users.UsersViewSet)
urlpatterns = [
    path('view/set/', include(router.urls)),
]
