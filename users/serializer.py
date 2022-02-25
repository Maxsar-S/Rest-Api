from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from users.models import User, Biography


class UserModelBaseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UserModelSerializer(UserModelBaseSerializer):
    class Meta(UserModelBaseSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class BiographySerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'user']
