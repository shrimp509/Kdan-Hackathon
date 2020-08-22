import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'kdan_book_storm.settings'

import django
django.setup()
from book_store.models import *
from member.models import *
import json
import re
from datetime import datetime
from datetime import timedelta
from django.utils.timezone import make_aware


def extract_opening_hours(text):
    opening_hours = {}
    tokens = text.split(' / ')
    week_day_items = ['Sun', 'Mon', 'Tues', 'Weds', 'Thurs', 'Fri', 'Sat']
    week_day_pattern = '|'.join(week_day_items)
    duration_pattern = '[0-9].*'

    for token in tokens:
        duration_text = re.findall(duration_pattern, token)[0]
        duration = extract_duration(duration_text)

        week_days_text = token.replace(duration_text, '')
        if '-' in week_days_text:
            week_day_tokens = week_days_text.split(' - ')
            start_week_day = week_day_items.index(week_day_tokens[0].strip())
            end_week_day = week_day_items.index(week_day_tokens[1].strip())
            if end_week_day < start_week_day:
                end_week_day += len(week_day_items)
            for week_day_index in range(start_week_day, end_week_day + 1):
                real_week_day_index = week_day_index % len(week_day_items)
                time_offset = real_week_day_index * 24 * 60
                modified_duration = [duration[0] + time_offset, duration[1] + time_offset]
                opening_hours[week_day_items[real_week_day_index]] = modified_duration
        else:
            week_days = re.findall(week_day_pattern, token)
            for week_day in week_days:
                time_offset = week_day_items.index(week_day) * 24 * 60
                modified_duration = [duration[0] + time_offset, duration[1] + time_offset]
                opening_hours[week_day] = modified_duration
    return opening_hours


def extract_duration(text):
    tokens = text.split(' - ')
    open_time = extract_time(tokens[0])
    close_time = extract_time(tokens[1])
    if open_time >= close_time:
        close_time += 24 * 60
    return [open_time, close_time]


def extract_time(text):
    time_text = text.split(' ')[0]
    if ':' not in time_text:
        time = int(time_text) * 60
    else:
        tokens = time_text.split(':')
        time = int(tokens[0]) * 60 + int(tokens[1])
    if 'pm' in text:
        time += 12 * 60
    if time == 12 * 60 or time == 24 * 60:
        time -= 12 * 60
    return time


def create_dataset():
    path = 'dataset/book_store_data.json'
    file = open(path, 'r')
    data = file.read()
    book_stores = json.loads(data)
    file.close()

    book_store_model_map = {}
    book_model_map = {}
    reference_datetime = make_aware(datetime.strptime('08/02/2020', '%m/%d/%Y'))

    for book_store in book_stores:
        store_name = book_store['storeName']
        cash_balance = book_store['cashBalance']
        print(str(cash_balance) + '\t' + str(store_name))
        books = book_store['books']
        book_store_model = BookStore()
        book_store_model.store_name = store_name
        book_store_model.cash_balance = cash_balance
        book_store_model.save()
        book_store_model_map[store_name] = book_store_model

        opening_hours = extract_opening_hours(book_store['openingHours'])
        print(opening_hours)
        for week_day in opening_hours:
            opening_hour_model = OpeningHour()
            opening_hour_model.book_store = book_store_model
            opening_hour_model.open_time = reference_datetime + timedelta(minutes=opening_hours[week_day][0])
            opening_hour_model.close_time = reference_datetime + timedelta(minutes=opening_hours[week_day][1])
            opening_hour_model.save()
        print('===')

        for book in books:
            book_name = book['bookName']
            price = book['price']
            if book_name not in book_model_map:
                book_model = Book()
                book_model.book_name = book_name
                book_model.save()
                book_model_map[book_name] = book_model
            book_in_book_store_model = BookInBookStore()
            book_in_book_store_model.book_store = book_store_model
            book_in_book_store_model.book = book_model_map[book_name]
            book_in_book_store_model.price = price
            book_in_book_store_model.save()

    path = 'dataset/user_data.json'
    file = open(path, 'r')
    data = file.read()
    users = json.loads(data)
    file.close()

    for user in users:
        user_id = user['id']
        name = user['name']
        cash_balance = user['cashBalance']

        user_model = User()
        user_model.user_id = user_id
        user_model.name = name
        user_model.cash_balance = cash_balance
        user_model.save()
        print('user = ' + str(name))

        purchase_history = user['purchaseHistory']
        for transaction in purchase_history:
            book_name = transaction['bookName']
            store_name = transaction['storeName']
            transaction_amount = transaction['transactionAmount']
            transaction_date = make_aware(datetime.strptime(transaction['transactionDate'], '%m/%d/%Y %I:%M %p'))
            transaction_model = PurchaseHistory()

            if store_name not in book_store_model_map:
                book_store_model = BookStore()
                book_store_model.store_name = store_name
                book_store_model.cash_balance = 0
                book_store_model.save()
                book_store_model_map[store_name] = book_store_model
            if book_name not in book_model_map:
                book_model = Book()
                book_model.book_name = book_name
                book_model.save()
                book_model_map[book_name] = book_model

            transaction_model.book_store = book_store_model_map[store_name]
            transaction_model.book = book_model_map[book_name]
            transaction_model.user = user_model
            transaction_model.transaction_amount = transaction_amount
            transaction_model.transaction_date = transaction_date
            transaction_model.save()


create_dataset()
