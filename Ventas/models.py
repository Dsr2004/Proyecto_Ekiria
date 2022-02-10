from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse 



# modelo para administrar los tipos de servicios
class Tipo_servicio(models.Model):
    id_tipo_servicio=models.AutoField("Id del Tipo de Servicio", primary_key=True, unique=True)
    nombre=models.CharField("Nombre", max_length=50, null=False,blank=False, unique=True)
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'tipo_servicios'
        verbose_name = 'tipo_servicio'
        verbose_name_plural = 'tipo_servicios'

    def __str__(self):
        return self.nombre

# modelo para administrar los servicios
class Servicio(models.Model):
    id_servicio=models.AutoField("Id del Servicio", primary_key=True, unique=True)
    slug=models.SlugField("Slug", unique=True)
    nombre=models.CharField("Nombre", max_length=40, null=False, blank=False, unique=True)
    descripcion=models.TextField("Descripcion",null=False,blank=False)
    img_servicio=models.ImageField("Imagen del Servicio", upload_to='Ventas/servicios',null=False, blank=False)
    precio=models.IntegerField("Precio",null=False, blank=False)
    tipo_servicio_id=models.ForeignKey(Tipo_servicio, verbose_name="Tipo de Servicio", on_delete=models.CASCADE,null=True, blank=True, db_column="tipo_servicio_id")
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'servicios'
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        c_servicio="{} cuesta ${}".format(self.nombre, self.precio)
        return c_servicio

    def get_absolute_url(self):
        return reverse("Ventas:detalleSer", kwargs={"slug": self.slug})
    
    # def ComentarioMin(self):
    #     query=Servicio.objects.all()
    #     return 
    

# modelo para administrar el catalogo
class Catalogo(models.Model):
    id_catalogo=models.AutoField("Id del Catalogo", primary_key=True, unique=True)
    servicio_id=models.OneToOneField(Servicio, verbose_name="Servicio", on_delete=models.CASCADE,null=True, blank=True,db_column="servicio_id")
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'catalogo'
        verbose_name = 'catalogo'
        ordering = ['id_catalogo','servicio_id','fecha_creacion','fecha_actualizacion','estado']

    def __str__(self):
        c_catalogo=Servicio.objects.filter(id_servicio=self.servicio_id)
        c_catalogo=str(c_catalogo)
        return f'El servicio es{c_catalogo}'

# modelo para administrar los servicios personalizados     
class Servicio_Personalizado(models.Model):
    id_servicio_personalizado=models.AutoField("Id del Servicio Personalizado", primary_key=True, unique=True)
    descripcion=models.TextField("Descripcion",null=True,blank=True)
    img_servicio=models.ImageField("Imagen del Servicio", upload_to="Ventas/servicios",null=False, blank=False)
    precio=models.IntegerField("Precio",null=True, blank=True)
    tipo_servicio_id=models.ForeignKey(Tipo_servicio, verbose_name="Tipo de Servicio", on_delete=models.CASCADE,null=True, blank=True, db_column="tipo_servicio_id")
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'servicios_personalizados'
        verbose_name = 'servicio_personalizado'
        verbose_name_plural = 'servicios_personalizados'

    def __str__(self):
        c_servicio="El servicio personalizado es: {}".format(self.descripcion)
        return c_servicio

# modelos para administrar los pedidos
class Pedido(models.Model):
    id_pedido=models.AutoField("Id del Pedido", primary_key=True, unique=True)
    total_pagar=models.IntegerField("Total a pagar",null=False,blank=False)
    fecha_cita=models.DateTimeField("Fecha de la Cita",null=False,blank=False)
    descripcion=models.TextField("Descripcion",null=True ,blank=True)
    servicio_id=models.ManyToManyField(Servicio, verbose_name="Servicios", null=True ,blank=True,db_column="servicio_id")
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return f"el id del pedido es: {self.id_pedido}"

# modelos para administrar los pedidos personalizados osea que tenga por lo menos un servicio personalizado
class Pedido_Personalizado(models.Model):
    id_pedido_personalizado=models.AutoField("Id del Pedido Personalizado", primary_key=True, unique=True)
    total_pagar=models.IntegerField("Total a pagar",null=False,blank=False)
    fecha_cita=models.DateTimeField("Fecha de la Cita",null=False,blank=False)
    descripcion=models.TextField("Descripcion",null=True ,blank=True)
    servicio_id=models.ManyToManyField(Servicio, verbose_name="Servicios", null=True ,blank=True,db_column="servicio_id")
    servicio_personalizado_id=models.ManyToManyField(Servicio_Personalizado, verbose_name="Servicios Personalizados", null=False ,blank=False,db_column="servicio_id")
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'pedidos_personalizados'
        verbose_name = 'pedido_personalizado'
        verbose_name_plural = 'pedidos_personalizados'

    def __str__(self):
        return f"el id del pedido personalizado es: {self.id_pedido_personalizado}"

class Cita(models.Model):
    id_cita=models.AutoField("Id de la Cita", primary_key=True, unique=True)
    cliente_id=models.IntegerField("Cliente de la Cita", default=1, null=True, blank=True)
    pedido_personalizado_id=models.OneToOneField(Pedido_Personalizado, verbose_name="Pedido Personalizado", on_delete=models.CASCADE,null=True, blank=True,db_column="pedido_personalizado_id")
    pedido_id=models.OneToOneField(Pedido, verbose_name="Pedido", on_delete=models.CASCADE,null=True, blank=True,db_column="pedido_id")
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'citas'
        verbose_name = 'cita'
        verbose_name_plural = 'citas'

    def __str__(self):
        return f"el cliente de esta cita es: {self.cliente_id}"

def pre_save_servicio_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)

pre_save.connect(pre_save_servicio_receiver,sender=Servicio)