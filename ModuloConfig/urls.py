from django.urls import path
from ModuloConfig.views import Inicio, Roles

urlpatterns = [
    path ("rol/", Roles, name="roles"),
    path ("index/", Inicio, name="inicio"),

]
