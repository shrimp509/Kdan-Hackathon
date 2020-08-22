from django.test import TestCase
from django.db.models import DecimalField, CharField, ImageField, BooleanField, DateTimeField

from bookstore.models import bookstore

class TestBookStoreFieldType(TestCase):

    # 針對 Table: BookStores
    def test_book_store_name_field_type(self):
        assert_same_type(self, "book_store_name", CharField)

    def test_cash_balance_field_type(self):
        assert_same_type(self, "cash_balance", FloatField )

    # 針對 Table: OpeningHours
    def test_open_time_field_type(self):
        assert_same_type(self, "open_time", DateTimeField)

    def test_close_time_field_type(self):
        assert_same_type(self, "close_time", DateTimeField)

    # 針對 Table: Books
    def test_book_name_field_type(self):
        assert_same_type(self, "book_name", CharField)

    # 針對 Table: BooksInBookStore
    def test_price_field_type(self):
        assert_same_type(self, "price", CharField)


    def assert_same_type(self, field_name, field_type):
        self.assertTrue(
            isinstance(
                get_product_field(field_name),
                field_type
            )
        )