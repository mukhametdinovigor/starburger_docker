# Generated by Django 3.2 on 2021-09-09 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0073_auto_20210909_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='user_order_item',
            new_name='order',
        ),
    ]
