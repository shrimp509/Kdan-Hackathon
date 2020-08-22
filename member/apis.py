from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import datetime

from .models import User, PurchaseHistory


####################
# APIs
####################
def add_user(request: WSGIRequest):
    if request.method == 'POST':
        body = _to_json(request.body)

        user = User()
        user.name = body['name']
        user.cash_balance = body['cash_balance']
        user.save()
        return _json_response(200, id=user.user_id)
    else:
        return _json_response(400, err_msg="wrong http method")


def update_user(request: WSGIRequest):
    return JsonResponse({'status': 'ok'})


####################
# Private methods
####################
def _to_json(data):
    return json.loads(data)


def _json_response(status: int, **kwargs):
    msg = {}
    for key, value in kwargs.items():
        msg[key] = value
    return JsonResponse(msg, status=status)
