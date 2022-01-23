#-----------------------------------------Importaciones---------------------------------------------------
from email import message
import email
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context, loader, RequestContext 
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from ModuloUsuarios.forms import InicioSesion
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.contrib import messages
from rest_framework import generics
from ModuloUsuarios.models import Usuario
from .serializers import UsuarioSerializer


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
#--------------------------------------Cargadores de templates------------------------------------
def login(request):
    return render(request, "registration/login.html")  
def PassR(request):
    return render(request, "UserInformation/PasswordRecovery.html")
def Register(request):
    return render(request, "registration/Registration.html")
def Perfil(request):
    return render(request, "UserInformation/Perfil.html")
def Admin(request):
    return render(request, "UsersConfiguration/UsersAdministration.html")