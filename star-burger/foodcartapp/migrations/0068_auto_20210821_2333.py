# Generated by Django 3.2 on 2021-08-21 12:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0067_rename_customerorderdetails_orderdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='cost',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='order_cost',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='стоимость заказа'),
        ),
    ]