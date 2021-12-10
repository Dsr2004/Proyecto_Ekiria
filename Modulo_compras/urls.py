from django.urls import path
from Modulo_compras.views import Proveedor, Productos

urlpatterns = [
    path ("proveedores/", Proveedor),
    path ("productos/", Productos)

]
