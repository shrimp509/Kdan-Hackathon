from django.db import models
from member.models import User


# Create your models here.
class BookStore(models.Model):
    store_name = models.TextField()
    cash_balance = models.FloatField()

    def __str__(self):
        return str(self.store_name) + ': ' + str(self.cash_balance)


class Book(models.Model):
    book_name = models.TextField()

    def __str__(self):
        return str(self.book_name)


class BookInBookStore(models.Model):
    book_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book_store) + ': ' + str(self.book)


class OpeningHour(models.Model):
    book_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    open_time = models.IntegerField()
    close_time = models.IntegerField()

    def __str__(self):
        return str(self.book_store) + ': ' + str(self.open_time) + '\t' + str(self.close_time)
