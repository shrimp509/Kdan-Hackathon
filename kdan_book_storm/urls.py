"""kdan_book_storm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from member.apis import *
from book_store.apis import *


API_PREFIX = 'api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),

    path(API_PREFIX + '/book', add_book),  # POST                                  #先測試這個
    path(API_PREFIX + '/book/<int:id>', update_book),  # GET,DELETE,PUT            #先測試這個

    path(API_PREFIX + '/bookstore', add_bookstore),  # POST
    path(API_PREFIX + '/bookstore/<int:id>', update_bookstore),  # GET,DELETE,PUT

    path(API_PREFIX + '/user', add_user),  # POST
    path(API_PREFIX + '/user/<int:id>', update_user),  # GET,DELETE,PUT

    #path(API_PREFIX + '/opening_hour', add_opening_hour),  # POST
    #path(API_PREFIX + '/opening_hour/<int:id>', update_opening_hour),  # GET,DELETE,PUT

    #path(API_PREFIX + '/books_in_bookstore', add_books_in_bookstore),  # POST
    #path(API_PREFIX + '/books_in_bookstore/<int:id>', update_books_in_bookstore),  # GET,DELETE,PUT

    path(API_PREFIX + '/purchase_history', add_purchase_history),  # POST
    path(API_PREFIX + '/purchase_history/<int:id>', update_purchase_history),  # GET,DELETE,PUT

    # parameters:
    # * at: timestamp
    # * hour_open_more_than / hour_open_less_than:
    # * book_more_than / book_less_than:
    # * price_min / price_max
    path(API_PREFIX + '/bookstore/list', list_bookstores),  # GET

    # # parameters:
    # # * store_name
    # path(API_PREFIX + '/bookstore/search'),  # GET
    #
    # # parameters
    # # by: transaction_volume, number_of_transactions, transaction_dollar_value
    # path(API_PREFIX + '/bookstore/popular'),  # GET
    #
    # # parameters:
    # # * price_min:
    # # * price_max:
    # path(API_PREFIX + '/book/list'),  # GET
    #
    # # parameters:
    # # * book_name
    # path(API_PREFIX + '/book/search'),  # GET
    #
    # # parameters:
    # # * transaction_dollar_value_more_than / transaction_dollar_value_less_than
    # # * date_min / date_max:
    # path(API_PREFIX + '/user/list'),  # GET
    #
    # # parameters:
    # # * top:
    # # * date_min / date_max:
    # path(API_PREFIX + '/user/search'),   # GET
    #
    # # parameters:
    # # * date_min / date_max:
    # path(API_PREFIX + '/purchase_history/search'),  # GET
    #
    # # body:
    # # * user_id
    # # * book_id
    # # * bookstore_id
    # path(API_PREFIX + '/purchase')  # POST
]
