from django.contrib import admin
from django.urls import path
from ModuloUsuarios.views import PassR
urlpatterns = [
    path('RecuperarContraseña/', PassR),
]