# Generated by Django 3.2.9 on 2022-02-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0006_alter_usuario_img_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='img_usuario',
            field=models.ImageField(default='profile.jpg', max_length=200, upload_to='perfil/', verbose_name='Imagen De Perfil'),
        ),
    ]
