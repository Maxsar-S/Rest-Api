import json

from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from mainapp.models import Article


class TestArticleViewSet(APITestCase):
    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(
            'ALex', 'alex@mail.com', 'ALex'
        )
        self.user = get_user_model().objects.create_user(
            'user_1', 'user_1@gb.local', 'geekbrains'
        )
        self.user_data = {'last_name': 'Test_2',
                          'first_name': 'Tester_2',
                          'email': 'test_1@test.test'}
        self.user_data_upd = {'last_name': 'Test_2',
                              'first_name': 'Tester_2',
                              'email': 'test_2@test.test'}

    def test_get_list(self):
        # 8
        self.client.login(username='ALex', password='ALex')
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        # 9. Надо добавить выбор сериализатора во View, чтобы создать автора
        author = User.objects.create(**self.user_data)
        article = Article.objects.create(name='Статья_1', author=author)
        self.client.force_login(user=self.superuser)
        response = self.client.put(f'/api/articles/{article.id}/',
                                   {'name': 'Статья_2',
                                    'author': article.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        article = Article.objects.get(id=article.id)
        self.assertEqual(article.name, 'Статья_2')

    def test_edit_mixer(self):
        # 11
        article = mixer.blend(Article)
        self.client.force_login(user=self.superuser)
        response = self.client.put(f'/api/articles/{article.id}/',
                                   {'name': 'Руслан и Людмила',
                                    'author': article.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        article = Article.objects.get(id=article.id)
        self.assertEqual(article.name, 'Руслан и Людмила')

    def test_get_detail(self):
        # 12
        article = mixer.blend(Article, name='Алые паруса')
        self.client.force_login(user=self.user)
        response = self.client.get(f'/api/articles/{article.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_article = json.loads(response.content)
        self.assertEqual(response_article['name'], 'Алые паруса')

    def test_get_detail_author(self):
        # 13
        article = mixer.blend(Article, author__last_name='Tester_2')
        self.client.force_login(user=self.superuser)
        response = self.client.get(f'/api/articles/{article.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_article = json.loads(response.content)
        self.assertEqual(response_article['author']['last_name'], 'Tester_2')
