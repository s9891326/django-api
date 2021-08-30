from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class SocialAccount(models.Model):
    provider = models.CharField(max_length=200, default="google")  # 若未來新增其他的登入方式 FB...
    unique_id = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, related_name='social', on_delete=models.CASCADE)


class TestModel(models.Model):
    test_name = models.CharField(max_length=100)
