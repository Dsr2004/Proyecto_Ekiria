from django.urls import path
from Modulo_compras.views import Proveedor, Productos, Compras

urlpatterns = [
    path ("proveedores/", Proveedor),
    path ("productos/", Productos),
    path ("confcompra/", Compras)

]
