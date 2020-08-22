from django.contrib import admin

from .models import BookStore, Book, BookInBookStore, OpeningHour

# Register your models here.
from book_store.models import *

admin.site.register(BookStore)
admin.site.register(Book)
admin.site.register(BookInBookStore)
admin.site.register(OpeningHour)
