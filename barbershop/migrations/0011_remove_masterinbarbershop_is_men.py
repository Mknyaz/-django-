# Generated by Django 2.2.7 on 2019-12-25 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0010_masterinbarbershop_is_men'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterinbarbershop',
            name='is_men',
        ),
    ]
