from django.contrib import admin
from django.urls import path
from ModuloUsuarios.views import PassR, Perfil, Admin, UsuarioList
urlpatterns = [
    path('RecuperarContraseña/', PassR, name="RecuperarContraseña"),
    path('Perfil/', Perfil, name="Perfil"),
    path('Administracion/', Admin, name="Administracion"),
    path('Usuario/', UsuarioList.as_view(), name = 'usuario_list'),
]