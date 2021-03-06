# Generated by Django 3.2 on 2021-08-11 11:47

from django.db import migrations


def get_order_item_price(apps, schema_editor):
    OrderItems = apps.get_model('foodcartapp', 'OrderItems')
    for order_item in OrderItems.objects.all():
        order_item.price = order_item.product.price
        order_item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0042_orderitems_price'),
    ]

    operations = [
        migrations.RunPython(get_order_item_price),
    ]
