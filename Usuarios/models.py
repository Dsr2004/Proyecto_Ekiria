
from email.policy import default
from turtle import width
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from Configuracion.models import Rol

class VistasDiarias(models.Model):
    id_dia = models.AutoField(primary_key=True)
    Contador = models.IntegerField()
    fecha = models.DateField()
    class Meta:
        db_table = "VisitasDiarias"
    def __str__(self):
        return self.Contador

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

class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=1000)
    usuario_id = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

    
    class Meta:
        db_table = 'notificaciones'
        verbose_name ='notificacion'
        verbose_name_plural='notificiaciones'
