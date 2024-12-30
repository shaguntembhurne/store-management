from django.contrib import admin

# Register your models here.
from .models import Employees, Customers, Orders, Products
admin.site.register(Employees)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(Products)