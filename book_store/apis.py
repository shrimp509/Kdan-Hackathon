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


@csrf_exempt
def add_opening_hour(request: WSGIRequest):
    if request.method == 'POST':
        body = _to_json(request.body)

        opening_hour = OpeningHour()
        opening_hour.book_store = BookStore.objects.get(store_name=body['store_name'])
        opening_hour.open_time = body['open_time']
        opening_hour.close_time = body['close_time']
        opening_hour.save()
        return _json_response(200, id=opening_hour.id)
    else:
        return _json_response(400, err_msg="wrong http method")


@csrf_exempt
def update_opening_hour(request: WSGIRequest, id: int):
    if request.method == 'GET':
        return _get_opening_hour(id)
    elif request.method == 'PUT':
        body = _to_json(request.body)
        return _put_opening_hour(id, body)
    elif request.method == 'DELETE':
        return _delete_opening_hour(id)


@csrf_exempt
def add_books_in_bookstore(request: WSGIRequest):
    if request.method == 'POST':
        body = _to_json(request.body)

        books_in_bookstore = BookInBookStore()
        books_in_bookstore.book_store = BookStore.objects.get(store_name=body['store_name'])
        books_in_bookstore.book = Book.objects.get(book_name=body['book_name'])
        books_in_bookstore.price = float(body['price'])
        books_in_bookstore.save()
        return _json_response(200, id=books_in_bookstore.id)
    else:
        return _json_response(400, err_msg="wrong http method")


@csrf_exempt
def update_books_in_bookstore(request: WSGIRequest, id: int):
    if request.method == 'GET':
        return _get_books_in_bookstore(id)
    elif request.method == 'PUT':
        body = _to_json(request.body)
        return _put_books_in_bookstore(id, body)
    elif request.method == 'DELETE':
        return _delete_books_in_bookstore(id)


def list_bookstores(request: WSGIRequest):
    if request.method == 'GET':
        return _list_bookstores_with_timestamp(request.GET.get('at'))
    else:
        return _json_response(400, err_msg="not found")


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


def _get_opening_hour(id: int):
    try:
        opening_hour = OpeningHour.objects.get(id=id)
        return _json_response(200, opening_hour={
            'store_name': opening_hour.store_name,
            'open_time': opening_hour.open_time,
            'close_time': opening_hour.close_time
        })
    except:
        return _json_response(400, err_msg="not found")


def _put_opening_hour(id: int, body):
    try:
        opening_hour = OpeningHour.objects.get(id=id)
        opening_hour.book_store = BookStore.objects.get(store_name=body['store_name'])
        opening_hour.open_time = body['open_time']
        opening_hour.close_time = body['close_time']
        opening_hour.save()
        return _json_response(200, status='ok')
    except:
        return _json_response(400, err_msg='not found')


def _delete_opening_hour(id):
    try:
        opening_hour = OpeningHour.objects.get(id=id)
        opening_hour.delete()
        return _json_response(200, status='ok')
    except:
        return _json_response(400, err_msg="not found")


def _get_books_in_bookstore(id: int):
    try:
        books_in_bookstore = BookInBookStore.objects.get(id=id)
        return _json_response(200, books_in_bookstore={
            'book_store': books_in_bookstore.book_store,
            'book': books_in_bookstore.book,
            'price': books_in_bookstore.price
        })
    except:
        return _json_response(400, err_msg="not found")


def _put_books_in_bookstore(id: int, body):
    try:
        books_in_bookstore = BookInBookStore.objects.get(id=id)
        books_in_bookstore.book_store = BookStore.objects.get(store_name=body['store_name'])
        books_in_bookstore.book = Book.objects.get(book_name=body['book_name'])
        books_in_bookstore.price = float(body['price'])
        books_in_bookstore.save()
        return _json_response(200, status='ok')
    except:
        return _json_response(400, err_msg='not found')


def _delete_books_in_bookstore(id):
    try:
        books_in_bookstore = BookInBookStore.objects.get(id=id)
        books_in_bookstore.delete()
        return _json_response(200, status='ok')
    except:
        return _json_response(400, err_msg="not found")


def _list_bookstores_with_timestamp(at):
    OpeningHour.objects.filter(open_time=at)
    return _json_response(200)


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
