from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
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


class Customers(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    discount = models.IntegerField()

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname)
