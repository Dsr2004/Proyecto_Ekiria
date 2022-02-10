# Generated by Django 3.2.9 on 2022-02-09 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_servicio',
            fields=[
                ('id_tipo_servicio', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Id del Tipo de Servicio')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'tipo_servicio',
                'verbose_name_plural': 'tipo_servicios',
                'db_table': 'tipo_servicios',
            },
        ),
        migrations.CreateModel(
            name='Servicio_Personalizado',
            fields=[
                ('id_servicio_personalizado', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Id del Servicio Personalizado')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('img_servicio', models.ImageField(upload_to='Ventas/servicios', verbose_name='Imagen del Servicio')),
                ('precio', models.IntegerField(blank=True, null=True, verbose_name='Precio')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('tipo_servicio_id', models.ForeignKey(blank=True, db_column='tipo_servicio_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='Ventas.tipo_servicio', verbose_name='Tipo de Servicio')),
            ],
            options={
                'verbose_name': 'servicio_personalizado',
                'verbose_name_plural': 'servicios_personalizados',
                'db_table': 'servicios_personalizados',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Id del Servicio')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('nombre', models.CharField(max_length=40, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('img_servicio', models.ImageField(upload_to='Ventas/servicios', verbose_name='Imagen del Servicio')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('tipo_servicio_id', models.ForeignKey(blank=True, db_column='tipo_servicio_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='Ventas.tipo_servicio', verbose_name='Tipo de Servicio')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'db_table': 'servicios',
            },
        ),
        migrations.CreateModel(
            name='Pedido_Personalizado',
            fields=[
                ('id_pedido_personalizado', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Id del Pedido Personalizado')),
                ('total_pagar', models.IntegerField(verbose_name='Total a pagar')),
                ('fecha_cita', models.DateTimeField(verbose_name='Fecha de la Cita')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('servicio_id', models.ManyToManyField(blank=True, db_column='servicio_id', null=True, to='Ventas.Servicio', verbose_name='Servicios')),
                ('servicio_personalizado_id', models.ManyToManyField(db_column='servicio_id', to='Ventas.Servicio_Personalizado', verbose_name='Servicios Personalizados')),
            ],
            options={
                'verbose_name': 'pedido_personalizado',
                'verbose_name_plural': 'pedidos_personalizados',
                'db_table': 'pedidos_personalizados',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Id del Pedido')),
                ('total_pagar', models.IntegerField(verbose_name='Total a pagar')),
                ('fecha_cita', models.DateTimeField(verbose_name='Fecha de la Cita')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('servicio_id', models.ManyToManyField(blank=True, db_column='servicio_id', null=True, to='Ventas.Servicio', verbose_name='Servicios')),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
                'db_table': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id_cita', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Id de la Cita')),
                ('cliente_id', models.IntegerField(blank=True, default=1, null=True, verbose_name='Cliente de la Cita')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('pedido_id', models.OneToOneField(blank=True, db_column='pedido_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='Ventas.pedido', verbose_name='Pedido')),
                ('pedido_personalizado_id', models.OneToOneField(blank=True, db_column='pedido_personalizado_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='Ventas.pedido_personalizado', verbose_name='Pedido Personalizado')),
            ],
            options={
                'verbose_name': 'cita',
                'verbose_name_plural': 'citas',
                'db_table': 'citas',
            },
        ),
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id_catalogo', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Id del Catalogo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('servicio_id', models.OneToOneField(blank=True, db_column='servicio_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='Ventas.servicio', verbose_name='Servicio')),
            ],
            options={
                'verbose_name': 'catalogo',
                'db_table': 'catalogo',
                'ordering': ['id_catalogo', 'servicio_id', 'fecha_creacion', 'fecha_actualizacion', 'estado'],
            },
        ),
    ]
