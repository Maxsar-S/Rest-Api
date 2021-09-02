import io

from django.core.management.base import BaseCommand
from rest_framework import serializers

from .python_models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        class UserSerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            birthday_year = serializers.IntegerField()

            def validate_birthday_year(self, value):
                if value < 0:
                    raise serializers.ValidationError('Год рождения не может быть отрицательным')
                return value

            def validate(self, attrs):
                if attrs['name'] == 'Пушкин' and attrs['birthday_year'] != 1799:
                    raise serializers.ValidationError('Неверный год рождения Пушкина')
                return attrs



        data = {'name': 'Пушкин', 'birthday_year': 1699}
        serializer = UserSerializer(data=data)
        print(serializer.is_valid())

        print(serializer.errors)
