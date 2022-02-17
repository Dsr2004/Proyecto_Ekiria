from django.contrib import admin
from Usuarios.models import Usuario

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    pass
