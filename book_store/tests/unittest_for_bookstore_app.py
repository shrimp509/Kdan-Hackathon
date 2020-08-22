from django.test import TestCase
from django.db.models import DecimalField, CharField, ImageField, BooleanField, DateTimeField, FloatField, IntegerField

from book_store.models import BookStore
from book_store.models import Book
from book_store.models import BookInBookStore
from book_store.models import OpeningHour

class TestBookStoreFieldType(TestCase):

    # 針對 Table: BookStores
    def test_book_store_name_field_type(self):
        self.assertTrue(isinstance(
            self.get_BookStore_field("store_name"),
            CharField
        ))

    def test_cash_balance_field_type(self):
        self.assertTrue(isinstance(
            self.get_BookStore_field("cash_balance"),
            FloatField
        ))

    # 針對 Table: OpeningHours
    def test_open_time_field_type(self):
        self.assertTrue(isinstance(
            self.get_OpeningHour_field("open_time"),
            IntegerField
        ))

    def test_close_time_field_type(self):
        self.assertTrue(isinstance(
            self.get_OpeningHour_field("close_time"),
            IntegerField
        ))

    # 針對 Table: Books
    def test_book_name_field_type(self):
        self.assertTrue(isinstance(
            self.get_Book_field("book_name"),
            CharField
        ))


    # 針對 Table: BookInBookStore
    def test_price_field_type(self):
        #assert_same_type(self, "price", CharField)
        self.assertTrue(isinstance(
            self.get_BookInBookStore_field("price"),
            FloatField
        ))
# ===================================================== #
    def get_BookStore_field(self, field_name):
        return BookStore._meta.get_field(field_name)

    def get_OpeningHour_field(self, field_name):
        return OpeningHour._meta.get_field(field_name)
        
    def get_Book_field(self, field_name):
        return Book._meta.get_field(field_name)
                
    def get_BookInBookStore_field(self, field_name):
        return BookInBookStore._meta.get_field(field_name)