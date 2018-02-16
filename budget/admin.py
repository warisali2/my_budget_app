from django.contrib import admin

from .models import Category, Expenditure, IncomeSource

admin.site.site_header = "myBudget App"

admin.site.site_title  = "myBudget App"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ['date', 'description', 'get_category_name', 'amount']

    def get_category_name(self, obj):
        return obj.category.name

    get_category_name.admin_order_field = 'category'
    get_category_name.short_description = 'Name'

@admin.register(IncomeSource)
class IncomeSourceAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'description', 'amount']

    empty_value_display = '<center>-</center>'