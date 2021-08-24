from django.urls import path, include
from rest_framework import routers

from stores import views

# rest api
router = routers.DefaultRouter()
router.register("store", views.StoreViewSet, basename="store_api")

urlpatterns = [
    path('api/', include(router.urls)),
]

