from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from django.db import models


# Create your models here.
class Store(models.Model):
    class StoreType(models.TextChoices):
        Japan = 'Japan', _('日式料理')
        Western = 'Western', _('西式料理')
        Taiwan = 'Taiwan', _('台式料理')

    name = models.CharField(max_length=30)
    store_type = models.CharField(max_length=7, choices=StoreType.choices)
    phone_number_regex = RegexValidator(regex=r"^\d{4}\-\d{3}\-\d{3}$",
                                        message="Phone number must be entered in the format: '0912-345-678'")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=12)
    notes = models.TextField(blank=True, default="")
    local = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    store = models.ForeignKey('Store', related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    class CommentScore(models.IntegerChoices):
        first = 1,  _('一顆星')
        two = 2, _('二顆星')
        three = 3, _('三顆星')
        four = 4, _('四顆星')
        five = 5, _('五顆星')

    store = models.ForeignKey('Store', related_name='comment_items', on_delete=models.CASCADE)
    score = models.IntegerField(default=CommentScore.three, choices=CommentScore.choices)
    notes = models.TextField(blank=True, default="")
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store.name}_{self.create_by.username}"
