from django.core.signals import request_finished
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from user.models import TestModel


# decorators 連接信號
@receiver(request_finished, dispatch_uid="my_unique_identifier")
def my_callback(sender, **kwargs):
    print("request finished")


# 普通繫結方式
def my_signal_handler(sender, **kwargs):
    print("Request finished!================================")
request_finished.connect(my_signal_handler, dispatch_uid="my_signal_handler")


# 針對model 的signal
# 接收特定發送者的信號
@receiver(pre_save, sender=TestModel, dispatch_uid="testModel_pre_save")
def my_pre_save(sender, **kwargs):
    print("pre_save")


@receiver(post_save, sender=TestModel, dispatch_uid="testModel_post_save")
def my_post_save(sender, **kwargs):
    print("post_save")


# 防止重複信號
# request_finished.connect(my_callback, dispatch_uid="my_unique_identifier")

