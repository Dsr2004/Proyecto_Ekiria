from django.urls import path
from Modulo_compras.views import Proveedor

urlpatterns = [
    path ("listar/", Proveedor)
]
