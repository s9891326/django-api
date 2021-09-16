from django.urls import path

from mg import views

app_name = "mg"

urlpatterns = [
    path('query_store_score_rank/', views.add_stores_test_data, name="add_store_test_data"),
]
