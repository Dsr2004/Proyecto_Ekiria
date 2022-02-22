from django.shortcuts import redirect, render
import json

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


from django.http import HttpResponse,JsonResponse
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

from .models import Rol
from .forms import RolForm


def Configuracion(request):
    return render(request, "Configuracion.html")

def Roles(request):
    return render(request, "Roles.html")

def Cambios(request):
    return render(request,"Cambios.html")

def Permisos(request):
    return render(request, "Permisos.html")
    
def Admin(request):
    return render(request, "Administrador.html")

def Empleado(request):
    return render(request, "Empleado.html")

def Cliente(request):
    return render(request, "Cliente.html")


def ListarRol(request):
    formulario=RolForm
    ListRoles = Rol.objects.all()
    contexto= {'roles':ListRoles, 'crear':formulario}
    return render(request, "Roles.html", contexto)

class CreateRolView(CreateView):
    model = Rol
    form_class = RolForm
    # template_name = 'Roles.html'
    template_name = 'CrearRol.html'
    if RolForm==success_url=reverse_lazy('Roles')
        pass

    else:
         return JsonResponse({'result': a})

# # prueba

    # def post(self,request,*args, **kwargs):
    #     if request.is_ajax():
    #         form=self.form_class(request.POST)
    #         if form.is_valid():
    #             nuevo_usuario=
    #             pass
    #     else:
    # #         pass
    # template_name = 'CrearRol.html'
    # success_url=reverse_lazy('Roles')

# class pruebas(CreateView):
#     model = Rol
#     form_class = RolForm
#     template_name = "pruebas.html"
#     success_url = reverse_lazy("pruebas")
    
class EditRolView(UpdateView):
    model = Rol
    form_class = RolForm
    template_name = 'Rol/EdirRol.html'
    success_url=reverse_lazy('Roles')
    