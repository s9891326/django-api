from django.urls import path, include
from rest_framework import routers
from . import views


# REST API
v1 = routers.DefaultRouter()
v1.register("user", views.CurrentUserViewSet)

urlpatterns = [
    path('', include(v1.urls)),
    path('test/', views.test_celery, name="test_celery")
]
