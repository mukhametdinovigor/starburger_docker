# Generated by Django 3.2 on 2021-08-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0064_alter_customerorderdetails_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorderdetails',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('Наличностью', 'Наличностью'), ('Электронно', 'Электронно')], max_length=50, verbose_name='Платежный метод'),
        ),
    ]
