#-----------------------------------------Importaciones---------------------------------------------------
from contextlib import redirect_stderr
from django.http import HttpResponse
from django.template import Template, Context, loader 
from django.shortcuts import render


#--------------------------------------Cargadores de templates------------------------------------
def Menu(request):
    return render(request, "Menu_Usuario.html")
def Inicio(request):
    return render(request, "index.html")

