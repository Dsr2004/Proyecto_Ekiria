# Generated by Django 3.2.9 on 2022-01-30 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modulo_compras', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='producto_id',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='proveedor_id',
            new_name='proveedor',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='proveedor_id',
            new_name='proveedor',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='tipo_producto_id',
            new_name='tipo_producto',
        ),
    ]
