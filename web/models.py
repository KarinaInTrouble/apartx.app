from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    order = models.CharField(max_length=255, verbose_name="Описание")
    price = models.PositiveBigIntegerField(verbose_name = "Цена заказа")
    description = models.TextField(verbose_name="Чек-лист")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    route = models.ImageField(upload_to='route_images/', verbose_name="Маршрут")

    def __str__(self):
        return self.order

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'