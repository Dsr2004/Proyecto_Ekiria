#-----------------------------------------Importaciones---------------------------------------------------
from django.http import HttpResponse
from django.template import Template, Context, loader 
from django.shortcuts import render
from ModuloUsuarios.models import *
from ModuloUsuarios.authentication_mixins import Authentication
from django.views.generic import View

#--------------------------------------Cargadores de templates------------------------------------


class Inicio(Authentication, View):
    def get(self, request, *args, **kwargs):
        mensaje = self.user
        return render(request, 'index.html', {'post':mensaje})