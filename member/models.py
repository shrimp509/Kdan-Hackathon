from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100, default="")
    cash_balance = models.FloatField()

    def __str__(self):
        return str(self.user_id) + ': ' + str(self.name) + '\t' + str(self.cash_balance)


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('book_store.Book', on_delete=models.CASCADE)
    book_store = models.ForeignKey('book_store.BookStore', on_delete=models.CASCADE)
    transaction_amount = models.FloatField()
    transaction_date = models.DateTimeField()

    def __str__(self):
        return str(self.book) + '\t' + str(self.book_store)\
               + '\t' + str(self.user) + '\t' + str(self.transaction_amount)\
               + '\t' + str(self.transaction_date)
