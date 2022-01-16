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

class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nom_municipio = models.TextField()
    estado = models.IntegerField()   # This field type is a guess.

    class Meta:
        db_table = 'municipios'
        verbose_name ='municipio'
        verbose_name_plural='municipios'
class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)
    permiso_id = models.IntegerField()
    estado = models.IntegerField()   # This field type is a guess.
    class Meta:
        db_table = 'roles'
        verbose_name ='rol'
        verbose_name_plural='roles'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.TextField()
    apellidos = models.TextField()
    apodo = models.TextField()
    telefono = models.TextField(blank=True, null=True)
    celular = models.TextField()
    email = models.EmailField()
    fec_nac = models.DateField()
    tipo_documento_id = models.OneToOneField(TipoDocumento, null=True, blank=True, on_delete=models.CASCADE)
    num_documento = models.TextField()
    img_usuario = models.TextField(blank=True, null=True)
    contrasena = models.TextField()
    municipio_id = models.OneToOneField(Municipio, null=True, blank=True, on_delete=models.CASCADE)
    direccion = models.TextField(blank=True, null=True)
    cod_postal = models.IntegerField()
    rol_id = models.OneToOneField(Rol, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.IntegerField()  # This field type is a guess.

    class Meta:
        db_table = 'usuarios'
        verbose_name ='usuario'
        verbose_name_plural='usuarios'
    
class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    mensaje = models.TextField()
    usuario_id = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

    
    class Meta:
        db_table = 'notificaciones'
        verbose_name ='notificacion'
        verbose_name_plural='notificiaciones'

# class Cita(models.Model):
#     id_cita = models.AutoField(primary_key=True)
#     cliente_id = models.IntegerField()
#     servicio_id = models.IntegerField()
#     servicio_personalizado_id = models.IntegerField(blank=True, null=True)
#     fecha_registro = models.DateTimeField()

#     class Meta:
#         db_table = 'citas'
#         verbose_name ='cita'
#         verbose_name_plural='citas'


# class Compra(models.Model):
#     id_compras = models.AutoField(primary_key=True)
#     descripcion = models.TextField()
#     cantidad = models.IntegerField()
#     producto_id = models.IntegerField()
#     proveedor_id = models.IntegerField()
#     precio = models.FloatField()
#     estado = models.IntegerField()   # This field type is a guess.
#     id_proveedores = models.IntegerField(blank=True, null=True)

#     class Meta:
#         db_table = 'compras'
#         verbose_name ='compra'
#         verbose_name_plural='compras'


# class FrontEnd(models.Model):
#     id_frond_end = models.IntegerField(primary_key=True)
#     titulo = models.CharField(max_length=50)
#     camp1 = models.CharField(max_length=1000)
#     camp2 = models.CharField(max_length=1000, blank=True, null=True)
#     camp3 = models.CharField(max_length=1000, blank=True, null=True)
#     camp4 = models.CharField(max_length=1000, blank=True, null=True)
#     camp5 = models.CharField(max_length=1000, blank=True, null=True)
#     camp6 = models.CharField(max_length=1000, blank=True, null=True)
#     img1 = models.CharField(max_length=1000, blank=True, null=True)
#     img2 = models.CharField(max_length=1000, blank=True, null=True)
#     color_titulo = models.CharField(max_length=11, blank=True, null=True)
#     color_txt = models.CharField(max_length=11, blank=True, null=True)
#     negrita_titulo = models.TextField(blank=True, null=True)  # This field type is a guess.
#     boton_tex_compra = models.CharField(max_length=11, blank=True, null=True)
#     negrita_producto = models.TextField(blank=True, null=True)  # This field type is a guess.
#     tamano_texto = models.IntegerField(blank=True, null=True)
#     tamano_titulo = models.IntegerField(blank=True, null=True)

#     class Meta:
#         db_table = 'front_end'
#         verbose_name ='front_end'
#         verbose_name_plural='front_end'




# class Pedido(models.Model):
#     id_pedido = models.AutoField(primary_key=True)
#     cita_id = models.IntegerField()
#     total_pagar = models.FloatField()
#     fecha_cita = models.DateTimeField()
#     descricpion = models.TextField(blank=True, null=True)
#     estado = models.IntegerField()   # This field type is a guess.

#     class Meta:
#         db_table = 'pedidos'
#         verbose_name ='pedido'
#         verbose_name_plural='pedidos'


# # class PedidoPersonalizado(models.Model):
# #     id_pedido = models.AutoField(primary_key=True)
# #     cita_id = models.IntegerField()
# #     total_pagar = models.FloatField()
# #     fecha_cita = models.DateTimeField()
# #     descricpion = models.TextField(blank=True, null=True)
# #     estado = models.TextField()  # This field type is a guess.

# #     class Meta:
# #         managed = False
# #         db_table = 'pedidos_personalizados'


# class Permiso(models.Model):
#     id_permiso = models.IntegerField(primary_key=True)
#     nombre = models.CharField(max_length=60)
#     descripcion = models.CharField(max_length=250)
#     estado = models.IntegerField()   # This field type is a guess.

#     class Meta:
#         db_table = 'permisos'
#         verbose_name ='permiso'
#         verbose_name_plural='permisos'


# class Producto(models.Model):
#     id_productos = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=20)
#     descripcion = models.TextField()
#     precio = models.FloatField()
#     proveedor_id = models.IntegerField()
#     tipo_producto_id = models.IntegerField()
#     cantidad = models.IntegerField()
#     estado = models.IntegerField()   # This field type is a guess.

#     class Meta:
#         db_table = 'productos'
#         verbose_name ='producto'
#         verbose_name_plural='productos'


# class Proveedor(models.Model):
#     id_proveedores = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=20)
#     telefono = models.CharField(max_length=10, blank=True, null=True)
#     celular = models.CharField(max_length=10, blank=True, null=True)
#     encargado = models.CharField(max_length=20, blank=True, null=True)
#     descripcion = models.TextField(blank=True, null=True)
#     estado = models.IntegerField()   # This field type is a guess.

#     class Meta:
#         db_table = 'proveedores'
#         verbose_name ='proveedor'
#         verbose_name_plural='proveedores'



# class Servicio(models.Model):
#     id_servicio = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=40)
#     descripcion = models.TextField()
#     img_servicios = models.TextField()
#     precio = models.IntegerField()
#     tipo_servicio_id = models.IntegerField()
#     fecha_creacion = models.DateField()
#     estado = models.IntegerField()   # This field type is a guess.

#     class Meta:
#         db_table = 'servicios'
#         verbose_name ='servicio'
#         verbose_name_plural='servicios'


# class ServicioPersonalizado(models.Model):
#     id_servicio_personalizado = models.AutoField(primary_key=True)
#     descripcion = models.TextField()
#     img_servicios = models.TextField()
#     tipo_servicio_id = models.IntegerField()
#     cita_id = models.IntegerField()

#     class Meta:
#         db_table = 'servicios_personalizados'
#         verbose_name ='servicio_personalizado'
#         verbose_name_plural='servicios_personalizados'
# class TipoProducto(models.Model):
#     id_tipo_producto = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=40)

#     class Meta:
#         db_table = 'tipo_producto'
#         verbose_name ='tipo_producto'
#         verbose_name_plural='tipo_producto'


# class TipoServicio(models.Model):
#     id_tipo_servicio = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=40)

#     class Meta:
#         db_table = 'tipo_servicios'
#         verbose_name ='tipo_servicio'
#         verbose_name_plural='tipo_servicios'

