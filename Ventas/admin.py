from django.contrib import admin
from Ventas.models import Servicio, Tipo_servicio

class ServicioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Servicio,ServicioAdmin)

# Register your models here.
