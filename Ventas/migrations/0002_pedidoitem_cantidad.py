# Generated by Django 3.2.9 on 2022-03-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoitem',
            name='cantidad',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Cantidad'),
        ),
    ]
