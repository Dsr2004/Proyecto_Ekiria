
from turtle import width
from django.db import models

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

