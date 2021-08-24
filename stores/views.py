from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.views import APIView

from stores.models import Store
from stores.serializers import StoreSerializer


# Create your views here.
class StoreViewSet(viewsets.ModelViewSet):
    """
    list:
    返回Store列表訊息
    retrieve:
    返回一家Store的詳細訊息
    create:
    新增一家Store
    update:
    更新一家Store
    partial_update:
    更新一家1231
    delete:
    刪除一家Store
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated]



