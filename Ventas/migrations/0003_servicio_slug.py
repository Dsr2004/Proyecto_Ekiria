# Generated by Django 3.2.9 on 2022-01-30 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0002_alter_catalogo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]