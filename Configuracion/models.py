from django.db import models
# # declare a new model with a name "GeeksModel"
class Permiso(models.Model):
    id_permiso =  models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=250)
    estado= models.BooleanField()
    
    class Meta:
        db_table = "permisos"
 
class Rol(models.Model):
    id_rol =  models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=40, unique=True)
    descripcion= models.CharField(max_length=500)
    permiso_id=models.ManyToManyField(Permiso, db_column="permiso_id")
    estado = models.BooleanField()

    class Meta:
        db_table = "roles"

#     # renames the instances of the model
#     # with their title name
    def __str__(self):
        return '{}'.format(self.nombre)

