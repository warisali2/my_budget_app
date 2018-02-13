from django.contrib import admin

from .models import Category, Expenditure, IncomeSource

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Expenditure)
admin.site.register(IncomeSource)
