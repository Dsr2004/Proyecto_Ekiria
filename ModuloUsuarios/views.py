#-----------------------------------------Importaciones---------------------------------------------------
from django.http import HttpResponse
from django.template import Template, Context, loader 
from django.shortcuts import render

#--------------------------------------Cargadores de templates------------------------------------
def Nose(request):
    return render(request, "Nose.html")