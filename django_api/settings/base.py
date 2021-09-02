"""
Django settings for django_api project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import environ
import datetime
import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(f"BASE_DIR: {BASE_DIR}")
print(f"Path(__file__).resolve(): {Path(__file__).resolve()}")

# ================= #
#  environ setting  #
# ================= #
# ROOT_DIR = (
#         environ.Path(__file__) - 2
# )
# print(f"Root dir: {ROOT_DIR}")

# reading .env file
# env = environ.Env()
# env.read_env(str(ROOT_DIR.path(".env")))
def env(key):
    try:
        return os.environ[key]
    except KeyError:
        raise ImproperlyConfigured(
            'Environment variable {key} required.'.format(key=key)
        )

# False if not in os.environ
# DEBUG = env('DEBUG')
# print(f"DEBUG: {DEBUG}")

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
# SECRET_KEY = env('SECRET_KEY')
# SECRET_KEY = "django-insecure-ul&i%n^6hr+0e7%jlab%ao#pbcousb9t@il*8a&koc+r&6^!"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-u)l&i%n^6hr+0e7%j)lab%ao#pbcousb9t@il*8a&koc+r&6^!'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ALLOWED_HOSTS = []

# Rest framework settings
REST_FRAMEWORK = {
    # Django REST Framework 預設就是使用 JSON，所以不用設定。
    # 使用 session 登入。
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    # 必須登入才能使用。
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': "rest_framework.schemas.coreapi.AutoSchema",

}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Application definition

INSTALLED_APPS = [
    'user.apps.UserConfig',
    'stores.apps.StoresConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    # 'django_celery_results',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_api.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

# ============== #
# social account #
# ============== #
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
}

SITE_ID = 1

# SOCIAL_GOOGLE_CLIENT_ID = env("SOCIAL_GOOGLE_CLIENT_ID")
SOCIAL_GOOGLE_CLIENT_ID = "122455133186-drprmpo7inpbpdp8j9fdnodn46hqslct.apps.googleusercontent.com"
# SOCIAL_FACEBOOK_CLIENT_ID = env("SOCIAL_GOOGLE_CLIENT_ID")

# CORS header
CORS_ORIGIN_WHITELIST = (
    'http://localhost:63342',  # localhost:63342 != 127.0.0.1:63342
)

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.mysql',
#     #     'NAME': 'django',
#     #     'USER': 'eddy',
#     #     'PASSWORD': 'eddy',
#     #     'HOST': 'localhost',
#     #     # POST官方推薦的是字串。
#     #     'POST': '3306',
#     # }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ================================= #
# =====    celery setting    ====== #
# https://tw511.com/a/01/33541.html #
# ================================= #
# 為django_celery_results儲存Celery任務執行結果設定後臺
# 格式為：db+scheme://user:password@host:port/dbname
# 支援資料庫django-db和快取django-cache儲存任務狀態及結果
# CELERY_RESULT_BACKEND = "django-db"

# celery內容等訊息的格式設定，預設json
# CELERY_ACCEPT_CONTENT = ['application/json', ]
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'

# celery時區設定，建議與Django settings中TIME_ZONE同樣時區，防止時差
# Django設定時區需同時設定USE_TZ=True和TIME_ZONE = 'Asia/Shanghai'
# CELERY_TIMEZONE = TIME_ZONE

# 為任務設定超時時間，單位秒。超時即中止，執行下個任務。
# CELERY_TASK_TIME_LIMIT = 5

# ======= #
#  Email  #
# ======= #
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'eddy15201@gmail.com'
# EMAIL_HOST_PASSWORD = 'lyvaknpnrtpuhphg'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# ============ #
# django-redis #
# ============ #
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": env("REDIS_URL"),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"
REDIS_TIMEOUT = 60 * 5  # five minutes
