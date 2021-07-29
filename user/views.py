from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from user.serializers import CurrentUserSerializer
from user.tasks import task_mail

# Create your views here.


class CurrentUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer


def test_celery(request):
    subject = "sub"
    message = "message"
    result = task_mail.delay(
        subject=subject,
        message=message,
        user_email="eddy15201@gmail.com"
    )

    # result = add.delay(3, 5)
    # result.status 需要在settings.py中設定CELERY_RESULT_BACKEND才可以查到狀態
    return HttpResponse(result.task_id + ":" + result.status)
