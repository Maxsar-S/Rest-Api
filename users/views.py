
from django.shortcuts import render

# Create your views here.
from rest_framework import status, mixins, viewsets

from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.models import User, Biography
from users.serializer import UserModelSerializer, BiographySerializer


class UsersViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer
