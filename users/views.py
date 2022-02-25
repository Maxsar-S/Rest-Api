# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from users.models import User, Biography
from users.serializer import UserModelSerializer, BiographySerializer, UserModelBaseSerializer


class UsersViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet,
                   mixins.CreateModelMixin):
    queryset = User.objects.all()
    ordering = ['pk']

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelBaseSerializer
        return UserModelSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer
