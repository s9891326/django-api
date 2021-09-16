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
        America = 'America', _('美式料理')
        China = 'China', _('中式料理')

    name = models.CharField(verbose_name="店家", max_length=30)
    type = models.CharField(verbose_name="店家類型", max_length=10, choices=StoreType.choices, default=StoreType.Taiwan)
    phone_number_regex = RegexValidator(regex=r"^\d{4}\-\d{3}\-\d{3}$",
                                        message="Phone number must be entered in the format: '0912-345-678'")
    phone_number = models.CharField(verbose_name="聯絡電話", validators=[phone_number_regex], max_length=12)
    description = models.TextField(verbose_name="簡介", blank=True, default="")
    local = models.CharField(verbose_name="地點", max_length=50)
    picture = models.ImageField(verbose_name="店家圖片", upload_to='stores', default="")
    create_at = models.DateTimeField(verbose_name="創建時間", auto_now_add=True)
    create_by = models.ForeignKey(User, verbose_name="創建者", on_delete=models.CASCADE)

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
        Dessert = 'Dessert', _('點心')

    store = models.ForeignKey('Store', related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="菜單名稱", max_length=20)
    type = models.CharField(verbose_name="菜單類型", max_length=50, choices=MenuType.choices,
                            default=MenuType.RecommendProduct)
    price = models.IntegerField(verbose_name="菜單價格")
    description = models.TextField(verbose_name="菜單內容物說明", blank=True, default="")
    picture = models.ImageField(verbose_name="菜單圖片", upload_to='menus', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    class CommentScore(models.IntegerChoices):
        First = 1,  _('一顆星')
        Two = 2, _('二顆星')
        Three = 3, _('三顆星')
        Four = 4, _('四顆星')
        Five = 5, _('五顆星')

    store = models.ForeignKey('Store', related_name='comment_items', on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name="評價分數", choices=CommentScore.choices, default=CommentScore.Three)
    description = models.TextField(verbose_name="評價內容", blank=True, default="")
    create_by = models.ForeignKey(User, verbose_name="評價者", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store.name}_{self.create_by.username}"
