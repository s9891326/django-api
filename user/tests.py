from django.core.cache import cache
from django.test import TestCase

from user.tasks import add
# Create your tests here.


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

