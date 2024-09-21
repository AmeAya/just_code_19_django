from django.db import models

# Create your models here.
# class Catalog(models.Model):
#     # (models.Model) -> Наследование, показываем Джанго что это не просто класс, а именно модель
#     # id -> Никогда не создается, Джанго сам его создает как SERIAL PRIMARY KEY
#     name = models.CharField(max_length=255)  # CharField -> string, с ограничением по длине(max_length)
#     type = models.CharField(max_length=255)
#     description = models.TextField()  # TextField -> string, без ограничения по длине


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    measurement = models.CharField(max_length=255)
    price = models.PositiveIntegerField()  # PositiveIntegerField -> Целые числа, только положительные
    country = models.CharField(max_length=255)
    article = models.CharField(max_length=50)
    warranty = models.PositiveSmallIntegerField()  # PositiveSmallIntegerField -> Целые положительные числа до 32767
    condition = models.CharField(max_length=50, choices=[
        ('Новое', 'Новое'),
        ('БУ', 'Бывшее в Употреблении'),
        ('ТР', 'Требует Ремонт')
    ])  # choices -> Доп параметр у CharField, лист вариантов
    # (Первое - Как будет записано в базе, второе - как будет показываться нам)

# Создать таблицу для строй. материалов:
# 1) Имя товара
# 2) Описание товара
# 3) Единицы измерения
# 4) Цена товара
# 5) Страна производителя товара
# 6) Артикул товара
# 7) Гарантий срок(В месяцах)
# 8) Состояние товара
