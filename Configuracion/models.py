from django.db import models
# # declare a new model with a name "GeeksModel"
class Permiso(models.Model):
    id_permiso =  models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=40,null=False, blank=False)
    descripcion = models.TextField(max_length=250,null=False, blank=False)
    estado= models.BooleanField(default=True)
    
    class Meta:
        db_table = "permisos"

    def __str__(self):
        return self.nombre 
 
class Rol(models.Model):
    id_rol =  models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=40, unique=True, null=False, blank=False)
    descripcion= models.CharField(max_length=500, null=False, blank=False)
    permiso_id=models.ManyToManyField(Permiso, db_column="permiso_id")
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = "roles"

    def __str__(self):
        return self.nombre 

class cambios(models.Model):
    id_cambios =  models.AutoField(primary_key=True, unique=True)
    Color_Letra = models.CharField(max_length=20)
    Color_Fondo = models.CharField(max_length=20)
    Sangria_Letra = models.CharField(max_length=20)
    tamano_letra = models.CharField(max_length=20)
    Tipo_Letra = models.CharField(max_length=20)

    class Meta:
        db_table = "Cambios"

    def __str__(self):
        return self.nombre 