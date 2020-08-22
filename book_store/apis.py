from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import datetime

from .models import Book, BookStore, BookInBookStore, OpeningHour


####################
# APIs
####################
@csrf_exempt
def add_book(request: WSGIRequest):
    if request.method == 'POST':
        body = _to_json(request.body)

        book = Book()
        book.book_name = body['book_name']
        book.save()
        return _json_response(200, id=book.id)
    else:
        return _json_response(400, err_msg="wrong http method")


@csrf_exempt
def update_book(request: WSGIRequest, id: int):
    if request.method == 'GET':
        return _get_book(id)
    elif request.method == 'PUT':
        body = _to_json(request.body)
        return _put_book(id, body)
    elif request.method == 'DELETE':
        return _delete_book(id)


@csrf_exempt
def add_bookstore(request: WSGIRequest):
    if request.method == 'POST':
        body = _to_json(request.body)

        bookstore = BookStore()
        bookstore.book_name = body['store_name']
        bookstore.save()
        return _json_response(200, id=bookstore.id)
    else:
        return _json_response(400, err_msg="wrong http method")


@csrf_exempt
def update_bookstore(request: WSGIRequest, id: int):
    if request.method == 'GET':
        return _get_bookstore(id)
    elif request.method == 'PUT':
        body = _to_json(request.body)
        return _put_bookstore(id, body)
    elif request.method == 'DELETE':
        return _delete_bookstore(id)


####################
# Sub API methods
####################


def _get_book(id: int):
    try:
        book = Book.objects.get(id=id)
        return _json_response(200, book={
            'book_name': book.book_name
        })
    except:
        return _json_response(400, err_msg="not found")


def _put_book(id: int, body):
    try:
        book = Book.objects.get(id=id)
        book.book_name = body['name']
        book.save()
        return _json_response(200, status='ok')
    except:
        return _json_response(400, err_msg='not found')


def _delete_book(id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return _json_response(200, status='ok')
    except:
        return _json_response(400, err_msg="not found")


def _get_bookstore(id: int):
    try:
        bookstore = BookStore.objects.get(id=id)
        return _json_response(200, bookstore={
            'store_name': bookstore.store_name,
            'cash_balance': bookstore.cash_balance
        })
    except:
        return _json_response(400, err_msg="not found")


def _put_bookstore(id: int, body):
    try:
        bookstore = BookStore.objects.get(id=id)
        bookstore.store_name = body['store_name']
        bookstore.save()
        return _json_response(200, status='ok')
    except:
        return _json_response(400, err_msg='not found')


def _delete_bookstore(id):
    try:
        bookstore = BookStore.objects.get(id=id)
        bookstore.delete()
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
