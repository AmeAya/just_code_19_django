from .models import *
from django.views.generic import ListView, DetailView


class CountriesListView(ListView):
    model = Countries
    context_object_name = 'country_list'
    template_name = 'countries_list_template.html'


class CustomersListView(ListView):
    model = Customers
    context_object_name = 'customer_list'
    template_name = 'customers_list_template.html'


class ProductsListView(ListView):
    model = Products
    context_object_name = 'product_list'
    template_name = 'products_list_template.html'


class CountriesDetailView(DetailView):
    model = Countries
    context_object_name = 'country_object'
    template_name = 'countries_detail_template.html'


class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product_object'
    template_name = 'products_detail_template.html'


# 1) Создать DetailView для модельки Products
# 2) Создать template для вьюшки из 1 пункта
# 3) Создать новый path в urls.py
