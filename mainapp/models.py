from django.db import models

# Create your models here.


from django.db import models

from users.models import User


class Article(models.Model):
    name = models.CharField(max_length=32, unique=True)
    authors = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=32, unique=True)
    author = models.ForeignKey(User, models.PROTECT)
    article = models.ForeignKey(Article, models.PROTECT, max_length=32)
    text = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
