from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm, CustomerForm, OrderForm, ProductForm
from .models import Customers, Products, Orders

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User is successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'You cannot log in')
    return render(request, 'log.html')


def logoutuser(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


def home(request):
    return render(request, 'nav.html')





def order(request):
    return render(request, 'base/order.html')


@login_required(login_url="log")
def product(request):
    prod = Products.objects.all()  # Corrected from 'products' to 'Products'
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    context = {"prod": prod, "form": form}
    return render(request, 'base/product.html', context)


@login_required(login_url='log')
def customer(request):
    cust = Customers.objects.all()  # Corrected from 'customers' to 'Customers'
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cust')
    context = {'cust': cust, 'form': form}
    return render(request, "base/customer.html", context)


def create_order(request):
    customers_list = Customers.objects.all()
    products_list = Products.objects.all()
    orders_list = Orders.objects.all()  # Fetch all orders to display in the table

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order successfully added!')
            return redirect('order')  # Ensure 'order' is a valid URL name
    else:
        form = OrderForm()

    context = {
        'form': form,  # Optional, not used in this template
        'customers': customers_list,
        'products': products_list,
        'orders': orders_list,  # Pass orders to the template
    }

    return render(request, 'base/order.html', context)

def dash(request):
    return render(request, 'base/dash.html')