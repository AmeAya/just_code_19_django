from django.contrib import admin
from .models import *

# from .models -> Джанго будет искать в этой же папке файлик models.py
# from models -> Джанго будет искать библиотеку models
# from .models import * -> Импортируем все из файла models.py


admin.site.register(Products)  # Регистрируем модель Products в админке
admin.site.register(Countries)  # Регистрируем модель Countries в админке
admin.site.register(Customers)
