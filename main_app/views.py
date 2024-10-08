from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
# reverse_lazy -> Ждет пока окончится процесс, и только после перенаправляет


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


# CreateView -> Джанговская Вью, которая нужна для создания объекта в БД(Insert)
class CountriesCreateView(CreateView):
    model = Countries
    fields = ['name']  # fields -> list/tuple в котором указывается список полей для insert
    # fields = '__all__'  # Взять все поля
    template_name = 'countries_create_template.html'
    # success_url -> URL куда перекидывать после сохранения
    success_url = reverse_lazy('countries_list_url')
    # reverse_lazy ждет пока сохранение пройдет


class ProductsCreateView(CreateView):
    model = Products
    fields = '__all__'
    template_name = 'products_create_template.html'
    success_url = reverse_lazy('products_list_url')


class CountriesDeleteView(DeleteView):
    model = Countries
    context_object_name = 'Country'
    template_name = 'countries_delete_template.html'
    success_url = reverse_lazy('countries_list_url')


class CountriesUpdateView(UpdateView):
    model = Countries
    template_name = 'countries_update_template.html'
    fields = ['name']
    success_url = reverse_lazy('countries_list_url')

# 1) Создать UpdateView для товаров(Products)
# 2) В fields указать все поля (__all__)
# 3) Создать темплейт для UpdateView
# 4) Провести url к UpdateView


class MainTemplateView(TemplateView):
    template_name = 'main_template.html'
