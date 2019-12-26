# Generated by Django 2.2.7 on 2019-12-24 19:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0007_remove_masterinbarbershop_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterinbarbershop',
            name='price',
        ),
        migrations.AddField(
            model_name='masterinbarbershop',
            name='custumer_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время'),
        ),
    ]
