from django.contrib import admin

from orders.models import Event, Order, Pay


# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ("store",)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("event", "create_at", "create_by")


class PayAdmin(admin.ModelAdmin):
    list_display = ("order", "pay_way", "is_pay")


admin.site.register(Event, EventAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Pay, PayAdmin)
