from django.contrib import admin
from django.urls import path
from ModuloUsuarios.views import PassR, Perfil, Admin
urlpatterns = [
    path('RecuperarContraseña/', PassR, name="RecuperarContraseña"),
    path('Perfil/', Perfil, name="Perfil"),
    path('Administracion/', Admin, name="Administracion")
]