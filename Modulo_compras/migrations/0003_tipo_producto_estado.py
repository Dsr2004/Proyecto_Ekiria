# Generated by Django 3.2.9 on 2022-03-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modulo_compras', '0002_auto_20220308_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_producto',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='estado'),
        ),
    ]
