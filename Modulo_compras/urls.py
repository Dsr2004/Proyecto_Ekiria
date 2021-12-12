from django.urls import path
from Modulo_compras.views import Proveedor, Productos, Conf_compra

urlpatterns = [
    path ("proveedores/", Proveedor),
    path ("productos/", Productos),
    path ("confcompra/", Conf_compra)

]
