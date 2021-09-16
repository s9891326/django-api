import coreapi
from django.db.models import Avg
from rest_framework import permissions, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from stores.models import Store, Menu, Comment
from stores.schema import QueryStoreScoreRankSchema, QueryStoreCreateTimeRankSchema
from stores.serializers import StoreSerializer, MenuSerializer, CommentSerializer
from utils.help_utils import get_date_time_str
from utils.response import APIResponse, jsonify
from utils.status_message import StatusMessage


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
    返回Menu列表訊息
    retrieve:
    返回一項Menu的詳細訊息
    create:
    新增一項Menu
    update:
    更新一項Menu
    partial_update:
    更新一項Menu
    delete:
    刪除一項Menu
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """
    list:
    返回Comment列表訊息
    retrieve:
    返回一篇Comment的詳細訊息
    create:
    新增一篇Comment
    update:
    更新一篇Comment
    partial_update:
    更新一篇Comment
    delete:
    刪除一篇Comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class QueryStoreScoreRank(APIView):
    """
    Query the ranking of store comment average score.
    """
    schema = QueryStoreScoreRankSchema()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        rank = int(request.GET.get(QueryStoreScoreRankSchema.RANK, 5))

        ranks = Store.objects.all().annotate(
            score_rank=Avg("comment_items__score")
        ).order_by("-score_rank")[:rank]

        result = []
        for score in ranks:
            result.append(dict(
                name=score.name,
                type=score.type,
                avg_score=score.score_rank
            ))

        return jsonify(
            data_status=status.HTTP_200_OK,
            data_msg=StatusMessage.HTTP_200_OK.value,
            results=result,
            http_status=status.HTTP_200_OK
        )


class QueryStoreCreateTimeRank(APIView):
    """
    Query the ranking of store create time.
    """
    schema = QueryStoreCreateTimeRankSchema()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        rank = int(request.GET.get(QueryStoreCreateTimeRankSchema.RANK, 5))

        ranks = Store.objects.all().order_by("-create_at")[:rank]

        result = []
        for rank in ranks:
            result.append(dict(
                name=rank.name,
                type=rank.type,
                phone_number=rank.phone_number,
                local=rank.local,
                description=rank.description,
                create_at=get_date_time_str(rank.create_at),
            ))

        return jsonify(
            data_status=status.HTTP_200_OK,
            data_msg=StatusMessage.HTTP_200_OK.value,
            result=result,
            http_status=status.HTTP_200_OK
        )

