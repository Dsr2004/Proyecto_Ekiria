# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tabnanny import verbose
from django.db import models
from Ventas.models import Pedido


class TipoDocumento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True)
    nom_tipo_documento = models.TextField()

    class Meta:
        db_table = 'tipo_documento'
        verbose_name ='tipo_documento'
        verbose_name_plural='tipos_documentos'
        
    def __str__(self) :
        return self.nom_tipo_documento

class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nom_municipio = models.TextField()
    estado = models.IntegerField()   # This field type is a guess.

    class Meta:
        db_table = 'municipios'
        verbose_name ='municipio'
        verbose_name_plural='municipios'
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)
    permiso_id = models.IntegerField()
    estado = models.IntegerField()   # This field type is a guess.
    class Meta:
        db_table = 'roles'
        verbose_name ='rol'
        verbose_name_plural='roles'
    def __str__(self):
        return '{}'.format(self.nombre)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.TextField()
    apellidos = models.TextField()
    apodo = models.TextField()
    telefono = models.TextField(blank=True, null=True)
    celular = models.TextField()
    email = models.EmailField()
    fec_nac = models.DateField()
    tipo_documento = models.OneToOneField(TipoDocumento, null=True, blank=True, on_delete=models.CASCADE)
    num_documento = models.TextField()
    img_usuario = models.TextField(blank=True, null=True)
    contrasena = models.TextField()
    municipio = models.OneToOneField(Municipio, null=True, blank=True, on_delete=models.CASCADE)
    direccion = models.TextField(blank=True, null=True)
    cod_postal = models.IntegerField(null=True)
    rol = models.OneToOneField(Rol, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.IntegerField()  # This field type is a guess.
    
    class Meta:
        db_table = 'usuarios'
        verbose_name ='usuario'
        verbose_name_plural='usuarios'
    def __str__(self):
        return '{}'.format(self.apodo, self.apellidos, self.nombres, self.telefono, self.celular, self.email, self.fec_nac, self.tipo_documento, self.num_documento, self.img_usuario, self.municipio, self.direccion, self.cod_postal, self.estado)
    
class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    mensaje = models.TextField()
    usuario_id = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

    
    class Meta:
        db_table = 'notificaciones'
        verbose_name ='notificacion'
        verbose_name_plural='notificiaciones'
