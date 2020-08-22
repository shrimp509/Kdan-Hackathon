from django.contrib import admin

from .models import BookStore, Book, BookInBookStore

# Register your models here.
admin.site.register(BookStore)
admin.site.register(Book)
admin.site.register(BookInBookStore)
