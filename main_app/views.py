from .models import *
from django.views.generic import ListView
# Генерики - views, которые были заранее написаны Django разработчиками


# ListView -> Это вью, который берет ВСЕ данные из таблицы в виде списка
# Указываем:
# 1) model(Из какой модельки брать данные)
# 2) context_object_name(Как назвать полученный список)
# 3) template_name(Имя html файла, куда отправить данные)
class CountriesListView(ListView):
    model = Countries
    context_object_name = 'country_list'
    template_name = 'countries_list_template.html'


class CustomersListView(ListView):
    model = Customers
    context_object_name = 'customer_list'
    template_name = 'customers_list_template.html'

# 1) Для модельки Customers создать CustomersListView(views.py)
# 2) Создать темплейт для CustomersListView(templates/...)
# 3) В созданном теплейте с помощью цикла for в тэге ul
#    выгрузить всех кастомеров
# 4) Добавить маршрут к CustomersListView в core/urls.py
# 5) Открыть страницу в браузере и убедиться что все работает
