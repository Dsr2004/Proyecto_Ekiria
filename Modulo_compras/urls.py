from django.urls import path
from Modulo_compras.views import Proveedor, Productos

urlpatterns = [
    path ("listar/", Proveedor),
    path ("lis/", Productos)

]
