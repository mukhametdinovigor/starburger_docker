# Generated by Django 3.2 on 2021-08-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0061_auto_20210821_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorderdetails',
            name='status',
            field=models.CharField(blank=True, choices=[('Обработанный', 'Обработанный'), ('Необработанный', 'Необработанный')], default='Необработанный', max_length=50, verbose_name='Статус заказа'),
        ),
    ]
