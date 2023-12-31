# Generated by Django 4.2.2 on 2023-06-23 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=255, verbose_name='Описание')),
                ('price', models.PositiveBigIntegerField(verbose_name='Цена заказа')),
                ('description', models.TextField(verbose_name='Чек-лист')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('route', models.ImageField(upload_to='route_images/', verbose_name='Маршрут')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказы',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
