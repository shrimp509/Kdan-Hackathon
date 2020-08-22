from django.db import models
from book_store.models import Book
from book_store.models import BookStore


# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    name = models.TextField()
    cash_balance = models.FloatField()

    def __str__(self):
        return str(self.user_id) + ': ' + str(self.name) + '\t' + str(self.cash_balance)


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    transaction_amount = models.FloatField()
    transaction_date = models.DateTimeField()

    def __str__(self):
        return str(self.book) + '\t' + str(self.book_store)\
               + '\t' + str(self.user) + '\t' + str(self.transaction_amount)\
               + '\t' + str(self.transaction_date)
