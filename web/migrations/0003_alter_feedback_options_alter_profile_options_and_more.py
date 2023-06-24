# Generated by Django 4.2.2 on 2023-06-24 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_profession_orders_contract_orders_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='feedback',
            name='order',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='web.orders', verbose_name='Заказ'),
            preserve_default=False,
        ),
    ]
