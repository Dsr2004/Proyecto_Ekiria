from django.urls import path
from Modulo_compras.views import Proveedor, Productos, Conf_compra,Crearprov

urlpatterns = [
    path ("proveedor/", Proveedor, name="proveedor"),
    path ("productos/", Productos, name="productos"),
    path ("confcompra/", Conf_compra, name="confcompra"),
    path ("p/", Crearprov, name="crear"),

    

]
