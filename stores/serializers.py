from rest_framework import serializers

from stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        # fields = '__all__'
        fields = [
            "id", "name", "store_type",
            "phone_number", "notes", "local",
            "create_at", "create_by"
        ]


# class MenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         # fields = '__all__'
#         fields = ["id"]
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         # fields = '__all__'
#         fields = ["id"]

