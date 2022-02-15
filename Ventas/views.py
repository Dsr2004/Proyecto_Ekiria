from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import ServicioForm

from Ventas.models import Servicio

def pruebas(request):
    query=Servicio.objects.values_list("descripcion")
    
    print(query)
    return render(request, "prueba.html", {"form":ServicioForm})


class Catalogo(ListView): 
    queryset=Servicio.objects.filter(estado=True)
    context_object_name="servicios"
    template_name="Catalogo.html"
    
# def ServicioDetalle(request, servicio):
#     servicio=Servicio.objects.filter(slug=servicio) 
#     return render(request, "Catalogo.html",{"servicio":servicio})

class ServicioDetalle(DetailView):
    queryset=Servicio.objects.all()
    context_object_name="DetailSs"
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

class AgregarServicio(CreateView):
    model=Servicio
    form_class=ServicioForm
    template_name="AgregarServicio.html"
    success_url=reverse_lazy('Ventas:listarServicios')

class ListarServicio(ListView):
    queryset=Servicio.objects.all()
    context_object_name="servicios"
    template_name="ListarServicios.html"
    
class EditarServicio(UpdateView):
    model=Servicio
    form_class=ServicioForm
    template_name="EditarServicio.html"
    print("kiwi")
    print(form_class.errors) 
    success_url=reverse_lazy('Ventas:listarServicios')


class AgregarCita(TemplateView):
    template_name="AgregarCita.html"

class ListarCita(TemplateView):
    template_name="ListarCitas.html"
    
class EditarCita(TemplateView):
    template_name="EditarCita.html"


