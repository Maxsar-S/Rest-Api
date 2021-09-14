from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient

from .models import User
from .views import UsersViewSet


class TestUserViewSet(TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     super().setUpClass()

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

    def test_get_list_guest(self):
        # 1 APIRequestFactory
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UsersViewSet.as_view({'get': 'list'})
        response = view(request)
        # print(dir(response))
        # response.render()
        # print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_auth(self):
        # print(self.user, self.user.email)
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        force_authenticate(request, user=self.user)
        view = UsersViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        # 2
        factory = APIRequestFactory()
        request = factory.post(
            '/api/users/',
            self.user_data,
            # format='json'
        )
        view = UsersViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        # 3.1
        factory = APIRequestFactory()
        request = factory.post(
            '/api/users/',
            self.user_data,
            format='json'
        )
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = UsersViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user(self):
        # 3.2
        factory = APIRequestFactory()
        request = factory.post(
            '/api/users/',
            self.user_data,
            format='json'
        )
        force_authenticate(request, user=self.superuser)
        view = UsersViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail_guest(self):
        # 4. APIClient
        user = User.objects.create(**self.user_data)
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detail_user(self):
        # 4. APIClient
        user = User.objects.create(**self.user_data)
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        # 6.
        user = User.objects.create(**self.user_data)
        client = APIClient()
        client.login(username='django', password='geekbrains')
        response = client.put(f'/api/users/{user.id}/',
                              self.user_data_upd)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.first_name, self.user_data_upd['first_name'])
        self.assertEqual(user.last_name, self.user_data_upd['last_name'])
        self.assertEqual(user.birthday_year, self.user_data_upd['birthday_year'])
        client.logout()
