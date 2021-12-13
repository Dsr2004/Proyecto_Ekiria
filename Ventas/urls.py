from django.urls import path
from Ventas.views import Catalogo, TerminarPedido, Calendario, ServiciosPersonalizados

urlpatterns = [
    path('Catalogo/', Catalogo, name="catalogo"),
    path('TerminarPedido/', TerminarPedido, name="TerminarPedido"),
    path('Calendario/', Calendario, name="calendario"),
    path('PersonalizarSer/', ServiciosPersonalizados, name="personalizar"),

]
