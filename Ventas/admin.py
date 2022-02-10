from django.contrib import admin
from Ventas.models import Servicio, Tipo_servicio

class ServicioAdmin(admin.ModelAdmin):
    pass

class TipoServicioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Tipo_servicio,TipoServicioAdmin)

# Register your models here.
