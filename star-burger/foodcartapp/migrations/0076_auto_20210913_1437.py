# Generated by Django 3.2 on 2021-09-13 03:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0075_alter_orderitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order_cost',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='position_cost',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='стоимость позиции'),
        ),
    ]