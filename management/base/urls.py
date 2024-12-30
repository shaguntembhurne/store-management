from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('log/', views.loginpage, name="log"),
    path('logout/', views.logoutuser, name="logout"),
    path('dash/', views.dash, name='dash'),
    path('customer/', views.customer, name='cust'),
    path('product/', views.product, name='product'),
    path('create-order/', views.create_order, name='order'),
]
