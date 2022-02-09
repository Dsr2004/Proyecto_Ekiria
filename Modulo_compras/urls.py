from django.urls import path
from Modulo_compras.views import Productos, Conf_compra,Listarprov, Crearprov

urlpatterns = [
    path ("productos/", Productos, name="productos"),
    path ("confcompra/", Conf_compra, name="confcompra"),
    path ("crearprov/", Crearprov, name="crearprov"),
    path ("listarprov/", Listarprov, name="listarprov"),

    

    

]
