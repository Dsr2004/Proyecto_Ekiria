from django.urls import path
from Ventas.views import Catalogo

urlpatterns = [
    path('Catalogo/', Catalogo)
]