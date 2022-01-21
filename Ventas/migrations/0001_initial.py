# Generated by Django 3.2.7 on 2022-01-15 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('cita_id', models.IntegerField()),
                ('total_pagar', models.FloatField()),
                ('fecha_cita', models.DateTimeField()),
                ('descricpion', models.TextField(blank=True, null=True)),
                ('estado', models.IntegerField()),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
                'db_table': 'pedidos',
            },
        ),
    ]