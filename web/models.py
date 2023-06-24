from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profession(models.Model):
    name = models.CharField(max_length=100, verbose_name="Специализация")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=11, verbose_name="Телефон", unique=True)
    avatar = models.ImageField(upload_to='profile_images/', verbose_name = "Фото ")
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, verbose_name="Специализация")
    bio = models.TextField(verbose_name="О себе")
    document = models.ImageField(upload_to='route_images/', verbose_name="Документ", blank=True)
    

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    order = models.CharField(max_length=255, verbose_name="Описание")
    price = models.PositiveBigIntegerField(verbose_name = "Цена заказа")
    description = models.TextField(verbose_name="Чек-лист")
    date = models.DateTimeField(verbose_name="Дата и время")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    route_link = models.URLField(verbose_name="Маршрут", blank=True)
    route = models.ImageField(upload_to='route_images/', verbose_name="Фото маршрута", blank=True)
    contract = models.ImageField(upload_to = 'contract_images/', verbose_name = "Договор", blank=True)

    def __str__(self):
        return self.order

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

class Feedback(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name="Заказ")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    personal = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Исполнитель")
    rate = models.PositiveIntegerField(verbose_name="Оценка")
    comment = models.TextField(verbose_name="Отзыв")

    def __str__(self):
        return self.order

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


#Исполнитель отправляет заказчику по окончанию работы
class CompletedOrders(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    photo_1 = models.ImageField(upload_to='completed_orders/', verbose_name="Фото №1")
    photo_2 = models.ImageField(upload_to='completed_orders/', verbose_name="Фото №2")
    photo_3 = models.ImageField(upload_to='completed_orders/', verbose_name="Фото №3")
    photo_4 = models.ImageField(upload_to='completed_orders/', verbose_name="Фото №4", blank = True)
    photo_5 = models.ImageField(upload_to='completed_orders/', verbose_name="Фото №5", blank = True)
    comment = models.TextField(verbose_name="Комментарий")
    rate = models.PositiveIntegerField(verbose_name="Оценка заказа")
    
    def __str__(self):
        return self.order

    class Meta:
        verbose_name = 'Выполненный заказ'
        verbose_name_plural = 'Выполненный заказ'
    

class Response(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='responses', verbose_name='Заказ')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Исполнитель')
    message = models.TextField(verbose_name='Сообщение')
    is_accepted = models.BooleanField(default=False, verbose_name='Принят')

    def __str__(self):
        return f"Response for order: {self.order.order} by user: {self.user.username}"
