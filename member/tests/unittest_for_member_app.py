from django.test import TestCase
from django.db.models import DecimalField, CharField, ImageField, BooleanField, DateTimeField, FloatField

from book_store.models import BookStore

class TestBookStoreFieldType(TestCase):

    # 針對 Table: User
    def test_user_name_field_type(self):
        assert_same_type(self, "user_name", CharField)

    def test_cash_balance_field_type(self):
        assert_same_type(self, "cash_balance", FloatField)

    # 針對 Table: PurchaseHistory
    def test_transaction_amount_field_type(self):
        assert_same_type(self, "transaction_amount", FloatField)

    def test_transaction_date_field_type(self):
        assert_same_type(self, "transaction_date", DateTimeField)
        
    def assert_same_type(self, field_name, field_type):
        self.assertTrue(
            isinstance(
                get_product_field(field_name),
                field_type
            )
        )