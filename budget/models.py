from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Expenditure(models.Model):
    date = models.DateTimeField(primary_key=True)
    description = models.CharField(max_length=1000)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class IncomeSource(models.Model):
    date = models.DateTimeField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True, blank=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)