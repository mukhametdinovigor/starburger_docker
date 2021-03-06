# Generated by Django 3.2 on 2021-08-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0048_customerorderdetails_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorderdetails',
            name='comments',
            field=models.CharField(blank=True, max_length=200, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='customerorderdetails',
            name='status',
            field=models.CharField(choices=[('Обработанный', 'Обработанный'), ('Необработанный', 'Необработанный')], default='Необработанный', max_length=50, verbose_name='Статус заказа'),
        ),
    ]
