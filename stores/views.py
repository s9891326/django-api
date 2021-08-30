from django.shortcuts import render
from requests import Response
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView

from stores.models import Store, Menu, Comment
from stores.serializers import StoreSerializer, MenuSerializer, CommentSerializer


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


class MenuViewSet(viewsets.ModelViewSet):
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
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
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
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
