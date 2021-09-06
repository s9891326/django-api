import json

from django.http import HttpResponse
from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, data_status=0, data_msg='ok',
                 results=None, http_status=None, headers=None,
                 exception=False, **kwargs):
        data = {
            'status': data_status,
            'msg': data_msg,
        }

        if results is not None:
            data['results'] = results

        data.update(kwargs)
        super().__init__(data=data, status=http_status, headers=headers,
                         exception=exception, content_type='application/json')


def jsonify(*args, **kwargs):
    encoded_data = json.dumps(
        dict(*args, **kwargs),
        ensure_ascii=False,
    )

    return HttpResponse(
        encoded_data,
        content_type="application/json"
    )
