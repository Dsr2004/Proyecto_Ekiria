from tabnanny import verbose
from django.db import models

  
# # declare a new model with a name "GeeksModel"
class Permisos(models.Model):

    id_permiso =  models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=250)
    estado= models.BooleanField()
 
class roles(models.Model):
    id_rol =  models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion= models.CharField(max_length=500)
    permisos_id = models.ForeignKey(Permisos, on_delete=models.CASCADE)
    estado = models.BooleanField()
 
#     # renames the instances of the model
#     # with their title name
    def __str__(self):
        return self.nombre # Create your models here.

