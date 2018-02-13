from django.contrib import admin

from .models import Category, Expenditure, IncomeSource

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ['date', 'description', 'get_category_name', 'amount']

    def get_category_name(self, obj):
        return obj.category.name

    get_category_name.admin_order_field = 'category'
    get_category_name.short_description = 'Name'

class IncomeSourceAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'description', 'amount']

    empty_value_display = '<center>-</center>'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Expenditure, ExpenditureAdmin)
admin.site.register(IncomeSource, IncomeSourceAdmin)
