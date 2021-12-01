# Generated by Django 3.2 on 2021-08-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0052_auto_20210813_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorderdetails',
            name='called_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время звонка'),
        ),
        migrations.AlterField(
            model_name='customerorderdetails',
            name='delivered_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время доставки'),
        ),
    ]