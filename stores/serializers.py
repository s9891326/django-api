from django.contrib.auth.models import User
from rest_framework import serializers

from stores.models import Store, Menu, Comment
from utils.serializers_util import add_after_delete


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        # fields = '__all__'
        fields = ["id", "name", "price"]

    def update(self, instance, validated_data):
        print("menu_items update")
        return super().update(instance, validated_data)


class CommentSerializer(serializers.ModelSerializer):
    create_by = serializers.StringRelatedField()

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ["id", "score", "notes", "create_by"]


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    menu_items = MenuSerializer(many=True)
    comment_items = CommentSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name="store-detail")
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    create_by = serializers.StringRelatedField()

    class Meta:
        model = Store
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')

        # 達到呼叫 [GET] /stores/api/store 不會取回menu_items、comment_items
        # 但 [GET] /stores/api/store/1 會取回menu_items、comment_items
        if request is not None and not request.parser_context.get('kwargs'):
            fields.pop('menu_items')
            fields.pop("comment_items")
        return fields

    def create(self, validated_data):
        validated_data["create_by"] = self.get_current_user()
        return super(StoreSerializer, self).create(validated_data=validated_data)

    def update(self, instance, validated_data):
        menu_items_data = validated_data.pop("menu_items")
        comment_items_data = validated_data.pop("comment_items")

        current_user = self.get_current_user()
        validated_data["create_by"] = current_user  # 更新創建者為當前用戶

        add_after_delete(model=instance.menu_items, update_data=menu_items_data)
        add_after_delete(model=instance.comment_items, update_data=comment_items_data, create_by=current_user)

        return super().update(instance, validated_data)

    def get_current_user(self):
        username = self.context["request"].user
        return User.objects.filter(username=username).first()

