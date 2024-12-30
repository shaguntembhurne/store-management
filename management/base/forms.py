from django.forms import ModelForm
from django import forms
from .models import Employees, Customers, Products, Orders


class EmployeeForm(ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"


class CustomerForm(ModelForm):
    class Meta:
        model = Customers
        fields = "__all__"


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['customer', 'product', 'quantity']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # Dynamically populate queryset to ensure up-to-date data
        self.fields['customer'].queryset = Customers.objects.all()
        self.fields['product'].queryset = Products.objects.all()
