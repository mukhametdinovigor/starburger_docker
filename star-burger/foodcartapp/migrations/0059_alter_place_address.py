# Generated by Django 3.2 on 2021-08-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0058_auto_20210816_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='адрес'),
        ),
    ]
