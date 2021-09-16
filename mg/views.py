from django.contrib.auth.decorators import login_required
from rest_framework import status

from stores.models import Store, Menu, Comment
from utils.response import jsonify
from utils.status_message import StatusMessage


# Create your views here.
@login_required
def add_stores_test_data(request):
    data_config = [
        dict(
            name="黑裝牛肉麵",
            type=Store.StoreType.Taiwan.value,
            phone_number="0929-111-222",
            description="test_store",
            local="新北市新店區中正路242巷1號1樓",
            create_by=request.user,
            menus=[
                dict(
                    name="大碗",
                    type=Menu.MenuType.PopularSelect.value,
                    price=140,
                    description="大碗test_menu",
                ),
                dict(
                    name="中碗",
                    type=Menu.MenuType.PopularSelect.value,
                    price=130,
                    description="中碗test_menu",
                ),
                dict(
                    name="小碗",
                    type=Menu.MenuType.Noodles.value,
                    price=120,
                    description="小碗test_menu",
                )
            ],
            comments=[
                dict(
                    score=Comment.CommentScore.Five.value,
                    description="Five test_comment",
                    create_by=request.user
                ),
                dict(
                    score=Comment.CommentScore.Three.value,
                    description="Three test_comment",
                    create_by=request.user
                )
            ]
        ),
        dict(
            name="麥當勞",
            type=Store.StoreType.America.value,
            phone_number="0977-888-666",
            description="test_store",
            local="新北市新店區中正路242巷2號2樓",
            create_by=request.user,
            menus=[
                dict(
                    name="大麥克",
                    type=Menu.MenuType.Meal.value,
                    price=160,
                    description="大麥克 test_menu",
                ),
                dict(
                    name="勁辣雞腿堡",
                    type=Menu.MenuType.Meal.value,
                    price=160,
                    description="勁辣雞腿堡 test_menu",
                ),
                dict(
                    name="松露蕈菇安格斯黑牛堡",
                    type=Menu.MenuType.PopularSelect.value,
                    price=170,
                    description="松露蕈菇安格斯黑牛堡 test_menu",
                ),
                dict(
                    name="麥克鷄塊(6塊)",
                    type=Menu.MenuType.Dessert.value,
                    price=59,
                    description="麥克鷄塊 test_menu",
                ),
                dict(
                    name="薯條",
                    type=Menu.MenuType.Dessert.value,
                    price=49,
                    description="薯條 test_menu",
                )
            ],
            comments=[
                dict(
                    score=2,
                    description="test_comment",
                    create_by=request.user
                ),
                dict(
                    score=1,
                    description="test_comment",
                    create_by=request.user
                )
            ]
        )
    ]

    for data in data_config:
        menus = data.pop("menus")
        comments = data.pop("comments")
        store = Store.objects.create(**data)

        for menu in menus:
            Menu.objects.create(store=store, **menu)

        for comment in comments:
            Comment.objects.create(store=store, **comment)

    return jsonify(
        data_status=status.HTTP_200_OK,
        data_msg=StatusMessage.HTTP_200_OK.value,
        http_status=status.HTTP_200_OK
    )


@login_required
def add_order_test_data(request):
    store_name = "黑裝牛肉麵"
    data_config = [
        dict(

        )
    ]

    return jsonify(
        data_status=status.HTTP_200_OK,
        data_msg=StatusMessage.HTTP_200_OK.value,
        http_status=status.HTTP_200_OK
    )
