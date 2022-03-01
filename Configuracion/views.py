from django.shortcuts import redirect, render
import json

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


from django.http import HttpResponse,JsonResponse
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

from .models import Rol,cambios
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
    contexto= {'roles':ListRoles, 'crear':formulario }
    return render(request, "Roles.html", contexto)

# def insertValues(request):
#     if request.method=="POST":
#         if request.POST.get("")
#             saverecord=cambios()
#             saverecord=ColorLetra=request.POST.get("")
#             saverecord=save()
#             return render(request, 'Cambios.html')
#         else:
#             return render(request, 'Cambios.html')

def EstadoRol(request):
    id_estado=request.POST.get("estado")
    Object=Rol.objects.get(id_rol=id_estado)
    estado = Object.estado
    if estado == True:
        Object.estado = False
        Object.save()
        return HttpResponse('cosa')
    elif estado == False:
        Object.estado = True
        Object.save()
        return HttpResponse('cosa2')


class CreateRolView(CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'CrearRol.html'

    def post(self,request, *args, **kwargs):
            if request.method == "POST":
                formulario=self.form_class(request.POST)
                if formulario.is_valid():
                    formulario.save()
                    return JsonResponse({"mensaje": f"{self.model.__name__} Se ha creado correctamente", "errores":"No hay errores"})
                else:
                    errores=formulario.errors
                    mensaje=f"{self.model.__name__} No se ha creado correctamente!"
                    respuesta=JsonResponse({"mensaje":mensaje, "errores":errores})
                    respuesta.status_code=400
                    return respuesta
            else:
                return HttpResponse("holis mango")
    

   

# def EstadoRol(self,request,*args, **kwargs):
#     roles = Rol.objects.get(id_rol=request.POST['id_rol'])
#     if request.POST['estado']:
#         id_rol=self.id_rol(request.POST)
#         if form.is_valid():
#             nuevo_usuario=
#             pass
#     else:
# #         pass
# template_name = 'CrearRol.html'
# success_url=reverse_lazy('Roles')

    
class EditRolView(UpdateView):
    model = Rol
    form_class = RolForm
    template_name = 'Rol/EdirRol.html'
    success_url=reverse_lazy('Roles')





    