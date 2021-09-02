from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from users.models import User, Biography


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class BiographySerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'user']