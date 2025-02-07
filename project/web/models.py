from django.db import models

# Create your models here.

# Модель еды (порции) с ее атрибутами
class food_model(models.Model):
    # название блюда
    name = models.CharField(max_length=25, unique=True)
    # общее количество порций (в шт/в граммах)
    all_count = models.IntegerField()
    # количество блюда. заказано порций в штуках
    count = models.IntegerField()
    # время заказа
    time = models.DateTimeField()
    # цена порции (dp - разряд рублей, md - копейки )
    price = models.DecimalField(decimal_places=3, max_digits=5)
    # изображение блюда
    # image = models.ImageField()


