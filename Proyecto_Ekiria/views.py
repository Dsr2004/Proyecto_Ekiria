#-----------------------------------------Importaciones---------------------------------------------------
from re import U
from django.http import HttpResponse
from django.template import Template, Context, loader 
from django.shortcuts import render
from ModuloUsuarios.models import *

#--------------------------------------Cargadores de templates------------------------------------
def Menu(request):
    return render(request, "Menu_Usuario.html")
def Inicio(request):
    usuarios = Usuario.objects.filter()
    return render(request, "index.html", {"usuarios":usuarios})