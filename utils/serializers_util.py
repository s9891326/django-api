from typing import List, Dict

from django.contrib.auth.models import User


def add_after_delete(model, update_data: List[Dict[str, str]], create_by: User = None):
    """
    更新關聯式欄位資訊
    :param model: 需要更新的模型
    :param update_data: 更新資料
    :param create_by:
    :return:
    """
    if not update_data:
        return

    model.all().delete()
    for data in update_data:
        if create_by:
            model.create(**data, create_by=create_by)
        else:
            model.create(**data)
