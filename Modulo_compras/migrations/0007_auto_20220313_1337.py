# Generated by Django 3.2.9 on 2022-03-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modulo_compras', '0006_auto_20220310_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='descripcion',
            field=models.TextField(verbose_name='descripcion'),
        ),
        migrations.RemoveField(
            model_name='compra',
            name='producto',
        ),
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ManyToManyField(to='Modulo_compras.Producto'),
        ),
    ]
