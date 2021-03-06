from django.db import models


# Create your models here.
class BookStore(models.Model):
    store_name = models.CharField(max_length=100, default="")
    cash_balance = models.FloatField()

    def __str__(self):
        return str(self.store_name) + ': ' + str(self.cash_balance)


class Book(models.Model):
    book_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.book_name)


class BookInBookStore(models.Model):
    book_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    def __str__(self):
        return str(self.book_store) + ': ' + str(self.book) + ': ' + str(self.price)


class OpeningHour(models.Model):
    book_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()

    def __str__(self):
        return str(self.book_store) + ': ' + str(self.open_time) + '\t' + str(self.close_time)
