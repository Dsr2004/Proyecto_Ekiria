from django.db import models

# Create your models here.



class Proveedor(models.Model):
    id_proveedor=models.AutoField("id_proveedor",primary_key=True, unique=True)
    nombre=models.CharField(max_length=20,blank=False, null=False)
    telefono=models.CharField(max_length=10,blank=True, null=True)
    celular=models.CharField(max_length=10,blank=False, null=False)
    encargado=models.CharField(max_length=15,blank=False, null=False)
    descripcion=models.TextField(max_length=200,blank=True, null=True)
    estado=models.BooleanField('estado', default=True)

    class Meta:
        verbose_name ='Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Tipo_producto(models.Model):
    id_tipo_producto=models.AutoField("id_tipo_producto",primary_key=True, unique=True)
    nombre=models.CharField(max_length=20,blank=False, null=False)

    class Meta:
        verbose_name ='Tipo_producto'
        verbose_name_plural = 'Tipo_productos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    id_producto=models.AutoField("id_producto",primary_key=True, unique=True)
    nombre=models.CharField('nombre',max_length=20,blank=False, null=False)
    descripcion=models.TextField('descripcion',max_length=200,blank=False, null=False)
    precio=models.IntegerField('precio',blank=False, null=False)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    tipo_producto=models.OneToOneField(Tipo_producto,on_delete=models.CASCADE)
    cantidad=models.IntegerField('cantidad',blank=False, null=False)
    estado=models.BooleanField('estado', default=True)

    class Meta:
        verbose_name ='Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    id_compras=models.AutoField("id_compra",primary_key=True, unique=True)
    descripcion=models.TextField('descripcion',max_length=200,blank=False, null=False)
    cantidad=models.IntegerField('cantidad',blank=False, null=False)
    producto=models.ManyToManyField(Producto)
    proveedor=models.ForeignKey(Proveedor,  on_delete=models.CASCADE)
    precio=models.IntegerField('precio',blank=False, null=False)
    estado=models.BooleanField('estado', default=True)

    class Meta:
        verbose_name ='Compra'
        verbose_name_plural = 'Compras'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion
