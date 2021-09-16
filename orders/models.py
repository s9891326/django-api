from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Event(models.Model):
    store = models.ForeignKey("stores.Store", related_name="orders", on_delete=models.CASCADE)

    class Meta:
        get_latest_by = "pk"

    def __str__(self):
        return str(self.store)

class Order(models.Model):
    class MealStatus(models.TextChoices):
        Wait = 'wait', _('等待店家回應')
        Accepted = 'accepted', _('店家接受')
        Processing = 'processing', _('處理中')
        Delivery = 'delivery', _('配送中')
        Finish = 'finish', _('完成')

    event = models.ForeignKey(Event, related_name="orders", on_delete=models.CASCADE)
    meal_time = models.DateTimeField(verbose_name="取餐時間")
    meal_local = models.CharField(verbose_name="取餐地點", max_length=50)
    meal_status = models.CharField(verbose_name="餐點狀態", max_length=20, choices=MealStatus.choices,
                                   default=MealStatus.Wait)
    create_at = models.DateField(verbose_name="創建時間", auto_now_add=True)
    create_by = models.ForeignKey(User, verbose_name="創建者", on_delete=models.CASCADE)

    class Meta:
        # 限制每個使用者同一天只能在一個餐點中點一次餐點
        unique_together = ("event", "create_at", "create_by")

    def __str__(self):
        return f"{self.create_by.username}_{self.event.store.name}"

    def get_uuid(self):
        print(self.create_at)
        print(self.id)

class Pay(models.Model):
    class PayWay(models.TextChoices):
        Cash = "cash", _("現金")
        CreditCard = "credit_card", _("信用卡")

    order = models.ForeignKey('Order', verbose_name="付款訂單", related_name="pay", on_delete=models.CASCADE)
    pay_way = models.CharField(verbose_name="付款方式", max_length=20, choices=PayWay.choices, default=PayWay.CreditCard)
    is_pay = models.BooleanField(verbose_name="付款是否成功", default=False)

    def __str__(self):
        return f"{self.order}"
