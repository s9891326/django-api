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
    type = models.CharField(max_length=7, choices=StoreType.choices)
    phone_number_regex = RegexValidator(regex=r"^\d{4}\-\d{3}\-\d{3}$",
                                        message="Phone number must be entered in the format: '0912-345-678'")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=12)
    description = models.TextField(blank=True, default="")
    local = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='stores', default="")
    create_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    class MenuType(models.TextChoices):
        RecommendProduct = 'Recommend_product', _('推薦商品')
        PopularSelect = 'Popular_select', _('人氣精選')
        Meal = 'Meal', _('套餐')
        Rice = 'Rice', _('飯類')
        Noodles = 'Noodles', _('麵類')
        SideDish = 'Side_dishes', _('小菜類')

    store = models.ForeignKey('Store', related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=50, choices=MenuType.choices, default=MenuType.RecommendProduct)
    price = models.IntegerField()
    description = models.TextField(blank=True, default="")
    picture = models.ImageField(upload_to='menus', blank=True)

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
    description = models.TextField(blank=True, default="")
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store.name}_{self.create_by.username}"
