from django.contrib import admin

from .models import User, PurchaseHistory

# Register your models here.
admin.site.register(User)
admin.site.register(PurchaseHistory)