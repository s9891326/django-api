import json

from django.contrib.auth.models import User
from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from user.tasks import add
# Create your tests here.
from utils.status_message import StatusMessage


class RedisTest(TestCase):
    def setUp(self) -> None:
        self.key = "redis-key"
        self.value = "redis-value"

    def test_redis_get_and_set(self):
        print("test_redis_get_and_set")
        cache.set(self.key, self.value)
        self.assertEqual(cache.get(self.key), self.value)

    def test_redis_del(self):
        print("test_redis_del")
        cache.set(self.key, self.value, timeout=60)
        print(f"cache get: {cache.get(self.key)}")
        cache.delete(self.key)
        print(f"cache get: {cache.get(self.key)}")
        self.assertIsNone(cache.get(self.key))

# class CeleryTest(TestCase):
#     def setUp(self) -> None:
#         self.x = 1
#         self.y = 3
#         self.z = 4
#
#     def test_add_task(self):
#         result = add.delay(self.x, self.y)
#         print(result)


class UserTest(APITestCase):
    """
    Test User all action
    """

    # urlpatterns = [
    #     #     path('')
    #     # ]

    def setUp(self):
        self.user1 = User.objects.create_user(
            email='test1@test.com',
            username='test',
            password='test',
        )

        self.admin = User.objects.create_superuser(
            email='admin@test.com',
            username='admin',
            password='admin',
        )

    def test_login(self):
        """
        Test if a user can login and get a JWT response token
        :return:
        """
        url = reverse("token_login")
        data = {
            'email': 'admin@test.com',
            'username': 'admin',
            'password': 'admin'
        }
        response = self.client.post(url, data)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['status'], status.HTTP_200_OK)
        self.assertEqual(response_data['msg'], StatusMessage.HTTP_200_OK.value)
        self.assertTrue('access' in response_data["results"])

    def test_user_register(self):
        """
        Test if a user can register
        :return:
        """
        url = reverse('register')
        data = {
            'email': 'test2@test.com',
            'username': 'test2',
            'password': 'test',
        }
        response = self.client.post(url, data)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data['status'], status.HTTP_201_CREATED)
        self.assertEqual(response_data['msg'], StatusMessage.HTTP_201_CREATED_REGISTER.value)

