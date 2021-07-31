import random

from django.http import HttpResponse
from django.core.cache import cache
from rest_framework import permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from django_api.settings import REDIS_TIMEOUT, EMAIL_HOST_USER
from user.serializers import SocialLoginSerializer
from user.tasks import task_mail

from utils.response import APIResponse


# Create your views here.
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


class ForgetPassword(APIView):
    """
    Send email with verify code and save into the redis.

    * Requires token authentication.
    * Allow all users are able to access this view
    """
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    def __init__(self):
        super(ForgetPassword, self).__init__()
        self.subject = "Monkey．D．Luffy"
        self.message = "Please click this link to reset password in {time} minute. \nLink: {code}"

    def post(self, request):
        """
        Send email with verify code and save into the redis.
        :param request:
        :return:
        """
        # get parameter
        email = request.data.get("email")
        random_code = random.randint(100000, 999999)

        # celery send email
        result = task_mail.delay(
            subject=self.subject,
            message=self.message.format(time=REDIS_TIMEOUT / 60, code=random_code),
            user_email=EMAIL_HOST_USER
        )
        print(result.task_id + ":" + result.status)

        # set redis
        cache.set(email, random_code, timeout=REDIS_TIMEOUT)
        return Response({"code": 200, "msg": "email傳送成功"})


class VerifyCode(APIView):
    """
    Verify code with email in the redis. Return True or False represent verify whether success
    """

    def post(self, request):
        """
        Verify code
        :param request:
        :return:
        """
        # get parameter
        email = request.data.get("email")
        random_code = request.data.get("code")

        # get code from redis with email
        cache_code = cache.get(email)

        if not cache_code:
            return Response(data={"msg": "驗證時間過期"})
        elif random_code == cache_code:
            cache.delete(email)
            return Response(data={"msg": "驗證成功"})
        else:
            return Response(data={"msg": "驗證碼錯誤"})


# social Jwt token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class GoogleLogin(TokenObtainPairView):
    permission_classes = (AllowAny,)  # AllowAny for login
    serializer_class = SocialLoginSerializer

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # return Response(get_tokens_for_user(user))
            return APIResponse(data_status=status.HTTP_200_OK, data_msg="success", results=get_tokens_for_user(user),
                               http_status=200)
        else:
            raise ValueError('Not serializable')
