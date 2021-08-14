from django.urls import path
# from rest_framework import routers
from . import views


# REST API
# v1 = routers.DefaultRouter()
# v1.register("user", views.CurrentUserViewSet)

urlpatterns = [
    # path('', include(v1.urls)),
    path('test/', views.test_celery, name="test_celery"),
    path('forget_password/', views.ForgetPassword.as_view(), name="forget_password"),
    path('verify_code/', views.VerifyCode.as_view(), name="verify_code"),

    # 第三方登入
    path('token/obtain/', views.GoogleLogin.as_view(), name="obtain"),

    # Custom JWT token
    path('login/', views.CustomTokenObtainPairView.as_view(), name="token_login"),
    path('refresh/', views.CustomTokenRefreshView.as_view(), name="token_refresh"),
    path('register/', views.AuthRegisterView.as_view(), name="register"),

    # Signal test
    path('test_signals/', views.test_signals, name="test_signal")
]
