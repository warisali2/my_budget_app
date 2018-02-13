from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Expenditure(models.Model):
    date = models.DateTimeField(primary_key=True)
    description = models.CharField(max_length=1000)
    amount = models.DecimalField(decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
