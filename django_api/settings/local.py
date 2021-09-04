from .base import *

SECRET_KEY = "django-insecure-ul&i%n^6hr+0e7%jlab%ao#pbcousb9t@il*8a&koc+r&6^!"
DEBUG = True
# TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'django',
    #     'USER': 'eddy',
    #     'PASSWORD': 'eddy',
    #     'HOST': 'localhost',
    #     # POST官方推薦的是字串。
    #     'POST': '3306',
    # }
}

# 最重要的設定，設定訊息broker,格式為：db://user:password@host:port/dbname
# 如果redis安裝在本機，使用localhost
# 如果docker部署的redis，使用redis://redis:6379
# CELERY_BROKER_URL = "redis://192.168.223.127:6379/0"


# ============ #
# django-redis #
# ============ #
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://192.168.223.127:6379/0",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
