from django.contrib import admin
from .models import roles
from .models import Permisos

admin.site.register(roles)

admin.site.register(Permisos)
