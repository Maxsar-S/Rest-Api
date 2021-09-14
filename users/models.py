from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        ordering = ['id']


class Biography(models.Model):
    text = models.TextField()
    user = models.OneToOneField(User,
                                  on_delete=models.CASCADE,
                                  primary_key=True)
