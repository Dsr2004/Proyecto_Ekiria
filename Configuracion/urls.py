from unicodedata import name
from django.urls import  path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("Roles/", views.Roles, name="Roles"),
    path("Cambios/", views.Cambios, name="Cambios"),
    path("Permisos/", views.Permisos, name="Permisos")
]
