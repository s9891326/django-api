"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from django_api.settings import base

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('stores/', include('stores.urls')),
    path('mg/', include('mg.urls')),
    path('docs/', include_docs_urls(title="DRF API", description="基於API")),
    # path('api-token-auth/', obtain_jwt_token),
    # path('api-token-refresh/', refresh_jwt_token),  # 能重新獲取新的token
    # path('api-token-verify/', verify_jwt_token),  # 測試輸入token是否正確
    # djoser
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),
    # google login
    path('accounts/', include('allauth.urls')),  # http://127.0.0.1:8000/accounts/google/login/
    path('logout', LogoutView.as_view()),
]

urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

