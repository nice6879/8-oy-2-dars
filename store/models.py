from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.username
