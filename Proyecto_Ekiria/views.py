#-----------------------------------------Importaciones---------------------------------------------------
from django.http import HttpResponse
from django.template import Template, Context, loader 
from django.shortcuts import render
from Usuarios.models import *
from Usuarios.authentication_mixins import Authentication
from django.views.generic import View
from Configuracion.forms import CambiosForm, FooterForm
from Configuracion.models import cambios, cambiosFooter

#--------------------------------------Cargadores de templates------------------------------------


class Inicio(View):
    def get(self, request, *args, **kwargs):
        formulario = CambiosForm
        # formulario2 = FooterForm
        # Listarfooter =cambiosFooter.objects.all()
        ListarCambios = cambios.objects.all()
        mensaje = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,],'Cambios' :ListarCambios
        }
        return render(request, 'index.html', mensaje)

        # , 'footer' :Listarfooter