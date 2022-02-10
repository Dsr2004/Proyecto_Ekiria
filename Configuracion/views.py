from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from .models import roles

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


def Roles(request):
    Roles = roles.objects.all()
    contexto= {'roles':roles}
    return render(request, "Roles.html", contexto)
