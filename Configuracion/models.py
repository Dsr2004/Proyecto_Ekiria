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
    Color_Letra = models.CharField(max_length=20, null=False, blank=False)
    Color_Fondo = models.CharField(max_length=20, null=False, blank=False)
    tamano_Titulo = models.CharField(max_length=20, null=False, blank=False)
    tamano_Texto = models.CharField(max_length=20, null=False, blank=False)
    Tipo_Letra = models.CharField(max_length=20, null=False, blank=False)
    Texto_Mision= models.CharField(max_length=500, null=False, blank=False)
    Texto_Vision= models.CharField(max_length=500, null=False, blank=False)

    class Meta:
        db_table = "Cambios"

    def __str__(self):
        return self.nombre 
        
class cambiosFooter(models.Model):
    id_footer = models.AutoField(primary_key=True, unique=True)
    Direccion = models.CharField(max_length=500, null=False, blank=False)
    Telefono = models.CharField(max_length=20, null=False, blank=False)
    Derechos = models.CharField(max_length=20, null=False, blank=False)
    Footer_Color_Letra = models.CharField(max_length=20, null=False, blank=False)
    Footer_Color_Fondo = models.CharField(max_length=20, null=False, blank=False)
    Footer_tamano_Titulo = models.CharField(max_length=20, null=False, blank=False)
    Footer_tamano_Texto = models.CharField(max_length=20, null=False, blank=False)
    Footer_Tipo_Letra = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = "footer"

    def __str__(self):
        return self.nombre