from django.urls import path, include
from rest_framework import routers

from stores import views

# rest api
router = routers.DefaultRouter()
router.register("store", views.StoreViewSet)
router.register("menu", views.MenuViewSet, basename="menu_api")
router.register("comment", views.CommentViewSet, basename="comment_api")

urlpatterns = [
    path('api/', include(router.urls)),
]

