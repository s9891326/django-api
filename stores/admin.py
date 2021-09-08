from django.contrib import admin
from django.db.models import Avg

from stores.models import Store, Menu, Comment
# Register your models here.


class MenuInline(admin.StackedInline):
    model = Menu
    extra = 1

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "get_score")
    inlines = (MenuInline, CommentInline)

    def get_score(self, obj):
        return obj.comment_items.all().aggregate(avg=Avg("score"))["avg"]
    get_score.short_description = "avg_score"
    # get_score.admin_order_field = "score"

class MenuAdmin(admin.ModelAdmin):
    list_display = ("store", "name", "price",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("store", )

admin.site.register(Store, StoreAdmin)
# admin.site.register(Store)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Comment, CommentAdmin)

