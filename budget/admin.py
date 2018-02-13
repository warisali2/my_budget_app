from django.contrib import admin

from .models import Category, Expenditure, IncomeSource

admin.site.register(Category)
admin.site.register(Expenditure)
admin.site.register(IncomeSource)
