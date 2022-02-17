"""Proyecto_Ekiria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from Proyecto_Ekiria.views import Inicio
from Usuarios.views import Login, Register, Loguot
from rest_framework.authtoken import views

urlpatterns = [
    path('', Inicio.as_view(), name="Inicio"),
    path('IniciarSesion/', Login.as_view(), name="IniciarSesion"),
    path('CerrarSesion/', Loguot.as_view(), name="CerrarSesion"),
    path('Registro/', Register.as_view(), name="Registro"),
    path('InformacionUsuario/', include('Usuarios.urls')),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('compras/', include('Modulo_compras.urls')),
=======
    path('Configuracion/', include ('Configuracion.urls')),
>>>>>>> 38f6f9dd4c0e12ab68efb131ca10207c9018fa2f
    path('api-auth/', include('rest_framework.urls')),
    path('api_generate_token/', views.obtain_auth_token, name="tokenGenerate"),
]

