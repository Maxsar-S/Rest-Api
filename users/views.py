from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from users.models import User, Biography
from users.serializer import UserModelSerializer, BiographySerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer