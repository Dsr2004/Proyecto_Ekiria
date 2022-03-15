


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cambios',
            fields=[
                ('id_cambios', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Color_Letra', models.CharField(max_length=20)),
                ('Color_Fondo', models.CharField(max_length=20)),
                ('Sangria_Letra', models.CharField(max_length=20)),
                ('tamano_letra', models.CharField(max_length=20)),
                ('Tipo_Letra', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Cambios',
            },
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id_permiso', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(max_length=250)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'permisos',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=40, unique=True)),
                ('descripcion', models.CharField(max_length=500)),
                ('estado', models.BooleanField(default=True)),
                ('permiso_id', models.ManyToManyField(db_column='permiso_id', to='Configuracion.Permiso')),
            ],
            options={
                'db_table': 'roles',
            },
        ),
    ]
