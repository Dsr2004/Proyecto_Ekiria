from unicodedata import name
from django.urls import path
from Modulo_compras.views import Modificarprov, Productos, Conf_compra,Listarprov, Crearprov, Eliminarprov, Modificarprov, Actprov

urlpatterns = [
    path ("productos/", Productos, name="productos"),
    path ("confcompra/", Conf_compra, name="confcompra"),
    path ("crearprov/", Crearprov.as_view(), name="crearprov"),
    path ("listarprov/", Listarprov, name="listarprov"),
    path ("eliminarprov/<int:id_proveedor>", Eliminarprov, name="eliminarprov"),
    path ("modificarprov/", Modificarprov, name="modificarprov"),
    path ("actprov/", Actprov, name="actprov"),





]
 