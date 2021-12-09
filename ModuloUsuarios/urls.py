from django.contrib import admin
from django.urls import path
from ModuloUsuarios.views import login
urlpatterns = [
    path('admin/', admin.site.urls),
]