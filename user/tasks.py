import time

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def task_mail(subject: str, message: str, user_email: list):
    mail_sent = send_mail(
        subject=subject,
        message=message,
        from_email="",
        recipient_list=[user_email]
    )
    return mail_sent

# Celery -A django_api worker -l info -P eventlet
# Celery -A django_api worker -l info -P solo
