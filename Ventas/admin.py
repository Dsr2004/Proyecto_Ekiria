from django.contrib import admin
from Ventas.models import Servicio, Tipo_servicio,Catalogo,Pedido,PedidoItem,Cita


admin.site.register(Servicio)
admin.site.register(Tipo_servicio)
admin.site.register(Catalogo)
admin.site.register(Pedido)
admin.site.register(PedidoItem)
admin.site.register(Cita)

# Register your models here.
