from django.contrib import admin

# Register your models here.
from user.models import SocialAccount

admin.site.register(SocialAccount)
