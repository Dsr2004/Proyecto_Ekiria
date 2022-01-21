#-----------------------------------------Importaciones---------------------------------------------------
from email import message
import email
from django.http import HttpResponse
from django.template import Template, Context, loader, RequestContext 
from django.shortcuts import render, redirect
from ModuloUsuarios.forms import InicioSesion
from django.contrib.auth import authenticate, login
from django.contrib import messages

from ModuloUsuarios.models import Usuario

#--------------------------------------Cargadores de templates------------------------------------
def login(request):
    if request.method=='POST':
        try:
            try:
                detalleUsuario=Usuario.objects.get(email=request.POST['apodo'], contrasena=request.POST['password'])
            except:
                detalleUsuario=Usuario.objects.get(apodo=request.POST['apodo'], contrasena=request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['Email']=detalleUsuario.email
            return redirect('Inicio')
        except:
            messages.success(request, 'Nombre de usuario o Contraseña incorrectos..!')
    return render(request, "registration/login.html")
def PassR(request):
    return render(request, "UserInformation/PasswordRecovery.html")
def Register(request):
    return render(request, "Information/Registration.html")
def Perfil(request):
    return render(request, "UserInformation/Perfil.html")
def Admin(request):
    return render(request, "UsersConfiguration/UsersAdministration.html")