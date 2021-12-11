#-----------------------------------------Importaciones---------------------------------------------------
from django.http import HttpResponse
from django.template import Template, Context, loader 
from django.shortcuts import render

#--------------------------------------Cargadores de templates------------------------------------
def login(request):
    return render(request, "Information/login.html");