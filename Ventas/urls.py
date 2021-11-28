from django.urls import path
from Ventas.views import Catalogo, Carrito, Calendario, ServiciosPersonalizados

urlpatterns = [
    path('Catalogo/', Catalogo, name="catalogo"),
    path('Carrito/', Carrito, name="carrito"),
    path('Calendario/', Calendario, name="calendario"),
    path('ServiciosPersona/', Calendario, name="calendario"),

]
