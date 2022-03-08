from unicodedata import name
from django.urls import path
from Modulo_compras.views import Listproductos, Crearprod, Listarprov, Listcompra , Crearprov, Eliminarprov, modificarprov, Actprov, cambiarestado

urlpatterns = [
    path ("listarcompra/", Listcompra, name="listarcompra"),
    path ("listarproductos/", Listproductos, name="listarprod"),
    path ("crearprod/", Crearprod.as_view(), name="crearprod"),
    path ("listarprov/", Listarprov, name="listarprov"),
    path ("crearprov/", Crearprov.as_view(), name="crearprov"),
    path ("eliminarprov/<int:id_proveedor>", Eliminarprov, name="eliminarprov"),
    path ("modificarprov/<int:pk>", modificarprov.as_view(), name="modificarprov"),
    path ("actprov/", Actprov, name="actprov"),
    path ("cambiarestado/", cambiarestado, name="camestado"),






]
 