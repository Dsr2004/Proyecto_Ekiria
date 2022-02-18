from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import CreateView
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
    query = Rol.objects.all()
    contexto= {'roles':query}
    return render(request, "Roles.html", contexto)

# def CrearRol(request):
#     if request =="POST":
    # FormRoles=RolForm
    # contexto= {'roles':query, 'createform':FormRoles, 'editarForm':FormRoles}
    # return render(request, "Roles.html", contexto)

class CreateRolView(CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'Roles.html'
    success_url=reverse_lazy('Roles')

# def EditarRoles(request):
#     pk = request.POST.post('pk')
#     object = post_object_or_404(Paper, pk = pk)
#     form = editarForm(instance=object)
#     return render(request, 'Roles.html', {
#         'object': object,
#         'pk': pk,
#         'form': form,
#         })
    
