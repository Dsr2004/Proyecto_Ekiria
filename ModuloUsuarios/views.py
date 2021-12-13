#-----------------------------------------Importaciones---------------------------------------------------
from django.http import HttpResponse
from django.template import Template, Context, loader 
from django.shortcuts import render

#--------------------------------------Cargadores de templates------------------------------------
def login(request):
    return render(request, "Information/login.html")
def PassR(request):
    return render(request, "UserInformation/PasswordRecovery.html")
def Register(request):
    return render(request, "Information/Registration.html")
def Perfil(request):
    return render(request, "UserInformation/Perfil.html")
def Admin(request):
    return render(request, "UsersConfiguration/UsersAdministration.html")