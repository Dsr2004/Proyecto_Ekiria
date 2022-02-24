
from email.policy import default
from turtle import width
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from Configuracion.models import Rol


class TipoDocumento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True)
    nom_tipo_documento = models.CharField(max_length=5)

    class Meta:
        db_table = 'tipo_documento'
        
    def __str__(self) :
        return self.nom_tipo_documento

class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nom_municipio = models.CharField(max_length=60)
    estado = models.BooleanField(default=True)  # This field type is a guess.

    class Meta:
        db_table = 'municipios'
        
    def __str__(self) :
        return self.nom_municipio
class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,celular,fec_nac,num_documento,direccion, cod_postal,password=None):
        if  not email:
            raise ValueError('El usuario debe tener un correo electronico!')
        usuario = self.model(
            username=username, 
            email = self.normalize_email(email), 
            nombres = nombres, 
            apellidos = apellidos,
            celular = celular, 
            fec_nac = fec_nac, 
            num_documento = num_documento,
            direccion = direccion,
            cod_postal = cod_postal,
            )
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self,email,username,nombres,apellidos,celular,fec_nac,num_documento, direccion, cod_postal, password):
        usuario = self.create_user(
            email,
            username=username, 
            nombres = nombres, 
            apellidos = apellidos,
            celular = celular, 
            fec_nac = fec_nac, 
            num_documento = num_documento,
            direccion = direccion,
            cod_postal = cod_postal,
            password=password,
        )
        usuario.administrador = True
        usuario.save()
        return usuario
class Usuario(AbstractBaseUser):
    id_usuario = models.AutoField(unique=True, primary_key=True)
    username = models.CharField('Nombre de usuario', unique = True, max_length=25)
    nombres = models.CharField('Nombres', max_length=60, blank=False, null = False)
    apellidos = models.CharField('Apellidos', max_length=60, blank=False, null= False)
    telefono = models.CharField('Número Télefonico',max_length=10, blank=True, null=True)
    celular = models.CharField('Número De Celular',max_length=10, blank=False, null=False)
    email = models.EmailField('Correo Electrónico', unique=True)
    fec_nac = models.DateField('Fecha De Nacimiento')
    tipo_documento = models.ForeignKey(TipoDocumento, null=True, blank=True, on_delete=models.CASCADE)
    num_documento = models.CharField('Número De Identificación',max_length=10)
    img_usuario = models.ImageField(
        'Imagen De Perfil', 
        upload_to='perfil/', 
        default="profile.jpg",
        max_length=200,
        )
    municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE)
    direccion = models.CharField(blank=True, null=True, max_length=250)
    cod_postal = models.CharField(max_length=20, null=True)
    rol = models.ForeignKey(Rol, default=1, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.BooleanField(default = True) 
    administrador = models.BooleanField(default=False)
    objects = UsuarioManager()
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email', 'nombres', 'apellidos', 'celular', 'fec_nac', 'num_documento', 'direccion', 'cod_postal']
    
    class Meta:
        db_table = 'usuarios'
    def __str__(self):
        return '{}'.format(self.nombres+' '+self.apellidos)
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.administrador
    
class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=1000)
    usuario_id = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

    
    class Meta:
        db_table = 'notificaciones'
        verbose_name ='notificacion'
        verbose_name_plural='notificiaciones'
