from django.urls import path
from Modulo_compras.views import Proveedor, Productos, Conf_compra

urlpatterns = [
    path ("proveedores/", Proveedor, name="proveedor"),
    path ("productos/", Productos, name="productos"),
    path ("confcompra/", Conf_compra, name="confcompra")

]
