from rest_framework import serializers


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


data = {'name': 'Грин', 'birthday_year': 1880}
serializer = UserSerializer(data=data)
print(serializer.is_valid())

data = {'name': 'Грин', 'birthday_year': -10}
serializer = UserSerializer(data=data)
print(serializer.is_valid())

print(serializer.errors)

data = {'name': 'Пушкин', 'birthday_year': 1699}
serializer = UserSerializer(data=data)
print(serializer.is_valid())

print(serializer.errors)
