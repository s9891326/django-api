import coreapi
from rest_framework.schemas import AutoSchema


class QueryStoreScoreRankSchema(AutoSchema):
    RANK = "rank"

    def get_manual_fields(self, path, method):
        custom_fields = [coreapi.Field(
            name="rank",
            required=False,
            location="query",
            description="Query the top few",
            type=int,
        )]
        return self._manual_fields + custom_fields


class QueryStoreCreateTimeRankSchema(AutoSchema):
    RANK = "rank"

    def get_manual_fields(self, path, method):
        custom_fields = [coreapi.Field(
            name="rank",
            required=False,
            location="query",
            description="Query the top few",
            type=int,
        )]
        return self._manual_fields + custom_fields
