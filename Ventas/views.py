from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from Ventas.models import Servicio

class Catalogo(ListView):
    queryset=Servicio.objects.filter(estado=True)
    context_object_name="servicios"
    template_name="Catalogo.html"
    

class Carrito(TemplateView):
    template_name="Carrito.html"

class TerminarPedido(TemplateView):
    template_name="TerminarPedido.html"

class Calendario(TemplateView):
    template_name="Calendario.html"

class ServiciosPersonalizados(TemplateView):
   template_name="AddservicioPer.html"

class DetalleCita(TemplateView):
   template_name="DetalleCita.html"

class AdminVentas(TemplateView):
    template_name="Ventas.html"

class AgregarServicio(TemplateView):
    template_name="AgregarServicio.html"

class ListarServicio(TemplateView):
    template_name="ListarServicios.html"
    
class EditarServicio(TemplateView):
    template_name="EditarServicio.html"

class AgregarCita(TemplateView):
    template_name="AgregarCita.html"

class ListarCita(TemplateView):
    template_name="ListarCitas.html"
    
class EditarCita(TemplateView):
    template_name="EditarCita.html"