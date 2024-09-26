from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    # null = True -> Данное поле может быть null в sql таблице
    # blank = True -> Данное поле может быть пустым('') в sql таблице
    # Если null и blank не прописаны, то они по стандарту равны False
    measurement = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True)
    article = models.CharField(max_length=50)
    warranty = models.PositiveSmallIntegerField()
    condition = models.CharField(max_length=50, choices=[
        ('Новое', 'Новое'),
        ('БУ', 'Бывшее в Употреблении'),
        ('ТР', 'Требует Ремонт')
    ])

    def __str__(self):
        return str(self.name) + ' ' + str(self.article)


class Countries(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# 1) Создать новую модель customers(покупатели)
#    Фамилия
#    Имя
#    Email (EmailField)
#    discount(Скидка, сколько процентов)
# 2) Провести миграцию в ДБ(makemigrations, migrate)
# 3) Созданную модель зарегистрировать в админке
# 4) Прописать для модели def __str__(self), чтобы показывалось "<ИМЯ> <ФАМИЛИЯ>"
