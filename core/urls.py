"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countries', CountriesListView.as_view(), name='countries_list_url'),
    path('customers', CustomersListView.as_view(), name='customers_list_url'),
    path('products', ProductsListView.as_view(), name='products_list_url'),
    path('country_detail/<int:pk>', CountriesDetailView.as_view(), name='countries_detail_url'),
    # <int:pk> -> Будет стоять переменная типа int под именем pk
    # pk - Primary Key -> Тоже самое что и id
    # pk требуют DetailView, UpdateView, DeleteView
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='products_detail_url'),
]
