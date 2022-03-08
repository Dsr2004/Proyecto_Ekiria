from unicodedata import name
from django.urls import path
from Modulo_compras.views import Productos,Listarprov, Crearprov, Eliminarprov, modificarprov, Actprov, cambiarestado

urlpatterns = [
    path ("listarprov/", listarcompra, name="listarcompra"),
    path ("productos/", Productos, name="productos"),
    path ("listarprov/", Listarprov, name="listarprov"),
    path ("crearprov/", Crearprov.as_view(), name="crearprov"),
    path ("eliminarprov/<int:id_proveedor>", Eliminarprov, name="eliminarprov"),
    path ("modificarprov/<int:pk>", modificarprov.as_view(), name="modificarprov"),
    path ("actprov/", Actprov, name="actprov"),
    path ("cambiarestado/", cambiarestado, name="camestado"),






]
 