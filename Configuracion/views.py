from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "Configuracion.html")

def Roles(request):
    return render(request, "Roles.html")

def Cambios(request):
    return render(request,"Cambios.html")

def Permisos(request):
    return render(request, "Permisos.html")
