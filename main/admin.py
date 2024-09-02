from django.contrib import admin
from .models import TotalValue, Income, Expenses

# Register your models here.
admin.site.register(TotalValue)
admin.site.register(Income)
admin.site.register(Expenses)