from rest_framework import serializers
from python_models import User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        return instance


data = {'name': 'Пушкин', 'birthday_year': 1799}
serializer = UserSerializer(data=data)
serializer.is_valid()
author = serializer.save()
print(vars(author), type(author), id(author))


data = {'name': 'Александр'}
serializer = UserSerializer(author, data=data, partial=True)  # patch
serializer.is_valid()
user = serializer.save()
print(vars(user), type(user), id(user))

