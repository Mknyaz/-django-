# Generated by Django 2.2.7 on 2019-12-24 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0006_masterinbarbershop_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterinbarbershop',
            name='total_price',
        ),
    ]
