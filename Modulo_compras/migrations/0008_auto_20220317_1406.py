# Generated by Django 3.2.9 on 2022-03-17 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modulo_compras', '0007_auto_20220313_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='precio',
        ),
    ]