from unicodedata import name
from django.urls import path
from Modulo_compras.views import Productos, Conf_compra,Listarprov, Crearprov, Eliminarprov, modificarprov, Actprov, cambiarestado

urlpatterns = [
    path ("confcompra/", Conf_compra, name="regcompra"),
    path ("productos/", Productos, name="productos"),
    path ("crearprov/", Crearprov.as_view(), name="crearprov"),
    path ("listarprov/", Listarprov, name="listarprov"),
    path ("eliminarprov/<int:id_proveedor>", Eliminarprov, name="eliminarprov"),
    path ("modificarprov/<int:pk>", modificarprov.as_view(), name="modificarprov"),
    path ("actprov/", Actprov, name="actprov"),
    path ("cambiarestado/", cambiarestado, name="camestado"),






]
 