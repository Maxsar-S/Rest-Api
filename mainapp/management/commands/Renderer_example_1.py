import io

from django.core.management.base import BaseCommand
from rest_framework import serializers

from .python_models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        class UserSerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            birthday_year = serializers.IntegerField()

            def create(self, validated_data):
                return User(**validated_data)

        user = User('Пушкин', 1799)
        serializer = UserSerializer(user)


        from rest_framework.renderers import JSONRenderer

        renderer = JSONRenderer()
        json_bytes = renderer.render(serializer.data)
        print(json_bytes)
        print(type(json_bytes))

        from rest_framework.parsers import JSONParser

        stream = io.BytesIO(json_bytes)
        parser = JSONParser()
        data = parser.parse(stream)
        print(data)
        print(type(data))

