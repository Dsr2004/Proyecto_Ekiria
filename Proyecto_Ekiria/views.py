#-----------------------------------------Importaciones---------------------------------------------------
from contextlib import redirect_stderr
from django.http import HttpResponse
from django.template import Template, Context, loader 
from django.shortcuts import render
from Usuarios.models import *
from Usuarios.authentication_mixins import Authentication
from django.views.generic import View
from rest_framework.views import APIView


#--------------------------------------Cargadores de templates------------------------------------

class Inicio(Authentication,View):
    def get(self, request, *args, **kwargs):
        mensaje = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        }
        return render(request, 'index.html', mensaje)

