from rest_framework import serializers
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        class UserSerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            birthday_year = serializers.IntegerField()

        data = {'name': 'Грин', 'birthday_year': 1880}
        serializer = UserSerializer(data=data)
        print(serializer.is_valid())  # True

        data = {'name': 'Грин', 'birthday_year': 'abc'}
        serializer = UserSerializer(data=data)
        print(serializer.is_valid())  # False

        print(serializer.errors)  # {'birthday_year': [ErrorDetail(string='A valid integer is required.', code='invalid')]}

        serializer.is_valid(raise_exception=True)
