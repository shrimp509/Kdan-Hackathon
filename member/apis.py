from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import datetime

from .models import User, PurchaseHistory


####################
# APIs
####################
@csrf_exempt
def add_user(request: WSGIRequest):
    if request.method == 'POST':
        body = _to_json(request.body)

        user = User()
        user.user_id = User.objects.last().id + 1
        user.name = body['name']
        user.cash_balance = float(body['cash_balance'])
        user.save()
        return _json_response(200, id=user.user_id)
    else:
        return _json_response(400, err_msg="wrong http method")


@csrf_exempt
def update_user(request: WSGIRequest, id: int):
    if request.method == 'GET':
        return _get_user(id)
    elif request.method == 'PUT':
        body = _to_json(request.body)
        return _put_user(id, body)
    elif request.method == 'DELETE':
        return _delete_user(id)


####################
# Sub API methods
####################
def _get_user(id: int):
    try:
        user = User.objects.get(id=id)
        return _json_response(200, user={
            'name': user.name,
            'cash_balance': user.cash_balance
        })
    except:
        return _json_response(400, err_msg="not found")


def _put_user(id: int, body):
    try:
        user = User.objects.get(id=id)
        user.name = body['name']
        user.save()
        return _json_response(200, status='ok')
    except:
        return _json_response(400, err_msg='not found')


def _delete_user(id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return _json_response(200, status='ok')
    except:
        return _json_response(400, err_msg="not found")


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
