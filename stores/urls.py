from django.urls import path, include
from rest_framework import routers

from stores import views

app_name = "stores"

# rest api
router = routers.DefaultRouter()
router.register("store", views.StoreViewSet)
router.register("menu", views.MenuViewSet, basename="menu_api")
router.register("comment", views.CommentViewSet, basename="comment_api")

urlpatterns = [
    path('api/', include(router.urls)),
    path('query_store_score_rank/', views.QueryStoreScoreRank.as_view(), name="query_store_score_rank"),
    path('query_store_create_time_rank/', views.QueryStoreCreateTimeRank.as_view(), name="query_store_create_time_rank"),
]

