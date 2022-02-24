from pyexpat import model
from turtle import update
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from .forms import ServicioForm, Tipo_servicioForm, EditarTipoServicioForm

from Ventas.models import Servicio, Tipo_servicio

def pruebas(request):
    query = Servicio.objects.values_list("descripcion")
    
    print(query)
    return render(request, "prueba.html", {"form":ServicioForm})


class Catalogo(ListView): 
    queryset = Servicio.objects.filter(estado=True)
    context_object_name = "servicios"
    template_name = "Catalogo.html"
    
# def ServicioDetalle(request, servicio):
#     servicio=Servicio.objects.filter(slug=servicio) 
#     return render(request, "Catalogo.html",{"servicio":servicio})

class ServicioDetalle(DetailView):
    queryset = Servicio.objects.all()
    context_object_name = "DetailSs"
    template_name = "Catalogo.html"

class Carrito(TemplateView):
    template_name = "Carrito.html"

class TerminarPedido(TemplateView):
    template_name = "TerminarPedido.html"

class Calendario(TemplateView):
    template_name = "Calendario.html"

class ServiciosPersonalizados(TemplateView):
   template_name = "AddservicioPer.html"

class DetalleCita(TemplateView):
   template_name = "DetalleCita.html"

class AdminVentas(TemplateView):
    template_name = "Ventas.html"
    def get_context_data(self,*args, **kwargs): 
        context = super().get_context_data(*args,**kwargs) 
        context['Tipo_Servicios'] = Tipo_servicio.objects.all()
        formTipo_Servicio = EditarTipoServicioForm
        context['form_Tipo_Servicio'] = formTipo_Servicio
        return context

class AgregarTipo_Servicio(CreateView):
    model = Tipo_servicio
    form_class = Tipo_servicioForm
    template_name = "Tipo_Servicio/Tipo_servicioAdd.html"

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_TipoServicio = Tipo_servicio(
                    nombre = form.cleaned_data.get('nombre'),
                    estado = form.cleaned_data.get('estado')
                )
                nuevo_TipoServicio.save()
                mensaje = f"{self.model.__name__} registrado correctamente"
                error = "No hay error!"
                response = JsonResponse({"mensaje":mensaje, "error":error})
                response.status_code = 201
                return response
            else:
                ctx = {}
                ctx.update(csrf(request))
                form_html = render_crispy_form(form, context=ctx)
                mensaje = f"{self.model.__name__} no se ha podido registrar!"
                error = form.errors
                response = JsonResponse({"mensaje":mensaje, "error":error,'form': form_html})
                response.status_code = 400
                return response
        else:
            return redirect("Ventas:adminVentas")
            

class EditarTipo_Servicio(UpdateView):
    model = Tipo_servicio
    form_class = Tipo_servicioForm
    template_name = "Tipo_Servicio/Tipo_servicio.html"

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f"{self.model.__name__} actualizado correctamente"
                error = "No hay error!"
                response = JsonResponse({"mensaje":mensaje, "error":error})
                response.status_code = 201
                return response
            else:
                mensaje = f"{self.model.__name__} no se ha podido actualizar!"
                error = form.errors
                response = JsonResponse({"mensaje":mensaje, "error":error})
                response.status_code = 400
                return response
        else:
            return redirect("Ventas:adminVentas")
# class CambiarEstadoTipoServicio(UpdateView):
#     def post(self, request, *args, **kwargs) :
#         if request.method == "POST":
#             form = self.form_class(request.POST)
#             if form.is_valid():
#                 form.save()
#                 mensaje = f"{self.model.__name__} actualizado correctamente"
#                 error = "No hay error!"
#                 response = JsonResponse({"mensaje":mensaje, "error":error})
#                 response.status_code = 201
#                 return response
#             else:
#                 mensaje = f"{self.model.__name__} no se ha podido actualizar!"
#                 error = form.errors
#                 response = JsonResponse({"mensaje":mensaje, "error":error})
#                 response.status_code = 400
#                 return response
#         else:
#             return redirect("Ventas:adminVentas")

def CambiarEstadoTipoServicio(request, id):
    if request.method == "POST":
        
        Tipo_servicio.objects.filter(id_tipo_servicio=id).update(estado=request.POST["estado"])
        return redirect("Ventas:adminVentas")
    else:
        return redirect("Ventas:adminVentas")

class AgregarServicio(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = "AgregarServicio.html"
    success_url = reverse_lazy('Ventas:listarServicios')

class ListarServicio(ListView):
    queryset = Servicio.objects.all()
    context_object_name = "servicios"
    template_name = "ListarServicios.html"
    
class EditarServicio(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = "EditarServicio.html" 
    success_url = reverse_lazy('Ventas:listarServicios')
    


class AgregarCita(TemplateView):
    template_name = "AgregarCita.html"

class ListarCita(TemplateView):
    template_name = "ListarCitas.html"
    
class EditarCita(TemplateView):
    template_name = "EditarCita.html"




def ejemplo(request, id):
    consuta=Servicio.objects.filter(id_servicio=id)
