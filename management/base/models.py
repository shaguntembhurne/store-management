from django.db import models
from django.contrib.auth.models import User


class Employees(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customers(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False, unique=True)
    phone = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Better for currency
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order for {self.customer.name} - {self.product.name} x {self.quantity}"
