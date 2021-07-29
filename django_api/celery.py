import os
from celery import Celery

# 設定環境變數
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_api.settings')

# 範例化
app = Celery('django_api')

# namespace='CELERY'作用是允許你在Django組態檔中對Celery進行設定
# 但所有Celery設定項必須以CELERY開頭，防止衝突
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自動從Django的已註冊app中發現任務
app.autodiscover_tasks()


# 一個測試任務
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
