from django.db import models

# Create your models here.


from django.db import models

from users.models import User


class Article(models.Model):
    name = models.CharField(max_length=32)
    # authors = models.ManyToManyField(User)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
