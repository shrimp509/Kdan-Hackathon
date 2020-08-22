from django.test import TestCase
from django.db.models import DecimalField, CharField, ImageField, BooleanField, DateTimeField, FloatField

from member.models import PurchaseHistory, User

class TestBookStoreFieldType(TestCase):

    # 針對 Table: User
    def test_name_field_type(self):
        self.assertTrue(isinstance(
            self.get_User_field("name"),
            CharField
        ))

    def test_cash_balance_field_type(self):
        self.assertTrue(isinstance(
            self.get_User_field("cash_balance"),
            FloatField
        ))

    # 針對 Table: PurchaseHistory
    def test_transaction_amount_field_type(self):
        self.assertTrue(isinstance(
            self.get_PurchaseHistory_field("transaction_amount"),
            FloatField
        ))

    def test_transaction_date_field_type(self):
        self.assertTrue(isinstance(
            self.get_PurchaseHistory_field("transaction_date"),
            DateTimeField
        ))
# ============================================================= #
    def get_User_field(self, field_name):
        return User._meta.get_field(field_name)

    def get_PurchaseHistory_field(self, field_name):
        return PurchaseHistory._meta.get_field(field_name)