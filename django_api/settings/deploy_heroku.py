from .base import *
import dj_database_url

# 把 debug 模式關掉。
DEBUG = False

# 設定 secret key。
SECRET_KEY = env('DJANGO_SECRET_KEY')

# 尊重 HTTPS 連線中的 "X-Forwarded-Proto" header。
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# 設定靜態檔位置。
# STATIC_ROOT = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = 'static'

# 設定資料庫。
DATABASES = {
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ['*']
