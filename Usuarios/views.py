#-----------------------------------------Imports---------------------------------------------------
from ast import Return
from asyncio import transports
from email import header, message
from html.entities import html5
from msilib.schema import SelfReg
from multiprocessing import context
from pyexpat import model
from pyexpat.errors import messages
from re import template
from tkinter.messagebox import NO
from urllib import response
#-----------------------------------------Django---------------------------------------------------
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
#-----------------------------------------Rest Framework---------------------------------------------------
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
#-----------------------------------------Serializers---------------------------------------------------
from Usuarios.Serializers.general_serializers import UsuarioTokenSerializer
from Usuarios.Serializers.general_serializers import UsuarioTokenSerializer
#-----------------------------------------Models---------------------------------------------------
from Usuarios.models import Usuario
<<<<<<< HEAD
from Ventas.models import Servicio
#-----------------------------------------More---------------------------------------------------
from Usuarios.authentication_mixins import Authentication
from datetime import datetime
=======
# from Ventas.models import Servicio  todavia no jhorman pendejo jajaja
>>>>>>> e6ce8d946767afccb464c7942dda680c0d954bca
from Usuarios.forms import Regitro, Editar

#--------------------------------------Templates Loaders------------------------------------

# class Login(ObtainAuthToken, TemplateView):
#     template_name = 'registration/login.html'
#     def post(self,request,*arg, **kwargs):
        # if request:
        #     login_serializer = self.serializer_class(data = request.POST , context={'request':request})
        #     print(request)
        #     if login_serializer.is_valid():
        #         user=login_serializer.validated_data['user']
        #         if user.is_active:
        #             token,created = Token.objects.get_or_create(user=user)
        #             user_serializer = UsuarioTokenSerializer(user)
        #             Client = "http://127.0.0.1:8000/"
        #             if created:
        #                 token = Token.objects.create(user = user)
        #                 # header = {'Authorization':'Token '+token.key}
        #                 # return Response(headers=header)
        #                 return HttpResponseRedirect("/")
        #             else:
        #                 all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
        #                 if all_sessions.exists():
        #                     for session in all_sessions:
        #                         session_data = session.get_decoded()
        #                         if user.id_usuario == int(session_data.get('_auth_user_id')):
        #                             session.delete()
        #                 token.delete()
        #                 token = Token.objects.create(user = user)
        #                 # credentials = 'http://127.0.0.1:8000'
        #                 # transport = HTTPTransport(credentials=credentials)
        #                 # client = Client(transports=transport)
        #                 # print(transport)
        #                 # return Response(client)
        #                 header = {'Authorization':'Token '+token.key}
        #                 return Response(headers=header)
        #                 # header = {'Authorization':'Token '+token.key}
        #                 # return Response(headers=header, template_name="index.html")
                    
                    
        #         else:
        #             return Response({'error':'Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
        #     else:
        #         return Response({'error':'Contraseña o Usuario incorrectos'},status=status.HTTP_400_BAD_REQUEST)


                
# class Loguot(Authentication, APIView):
#     def post(self,request,*args,**kwargs):
#         try:    
#             token = token
            
#             if token:
                
#                 user = token.user
                
#                 for i in range(2):
#                     all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
#                     if all_sessions.exists():
#                         for session in all_sessions:
#                             session_data = session.get_decoded()
#                             if user.id_usuario == int(session_data.get('_auth_user_id')):
#                                 session.delete()
                                        
#                 token.delete()
                    
#                 session_message = 'Sesiones de usuario eliminadas.'
#                 token_message = 'Token eliminado.'
#                 return Response({'token_message': token_message, 'session_message': session_message}, status = status.HTTP_200_OK)
#             return Response({'error':'No se ha encontrado un usuario con estas credenciales.'}, status = status.HTTP_400_BAD_REQUEST)
#         except :
#             return Response({'error': 'No se ha encontrado token en la petición.'}, status = status.HTTP_409_CONFLICT)
        

def Loguot(request):
    logout(request)
    return redirect('Inicio')

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                request.session['username'] = usuario.username
                request.session['rol']= usuario.rol.nombre
                request.session['pk'] = usuario.id_usuario
                request.session['Admin'] = usuario.administrador
                print(usuario.id_usuario)
                return redirect("Inicio")
            else:
                return HttpResponse("Apodo o Contraseñas incorrectos")
        return HttpResponse( "Credenciales incorrectas")
            
    form = AuthenticationForm()
    return render(request, "registration/login.html", {'form': form})
            
def PassR(request):
    return render(request, "UserInformation/PasswordRecovery.html")

class Register(CreateView):
    model = Usuario
    form_class = Regitro
    template_name = 'registration/Registration.html'
    success_url = reverse_lazy("Inicio")
    
def Perfil(request):
    try:
        if request.session:
            imagen = Usuario.objects.get(id_usuario=request.session['pk'])
            imagen = imagen.img_usuario
            UserSesion = {"username":request.session['username'], "rol":request.session['rol'], "imagen":imagen}
        usuario = Usuario.objects.get(id_usuario=request.session['pk'])
        print(usuario)
        return render(request, "UserInformation/Perfil.html", {"Usuario":usuario, "User":UserSesion})
    except:
        return redirect("UNR")

# def Admin(request):
#     context = {1,2,3,3,4,5,6,7,8,9,10}
#     return render(request, "UsersConfiguration/UsersAdministration.html",{'rep':context})

# class Perfil(DetailView):
#     model = Usuario
#     context_object_name="Usuario"
#     template_name="UserInformation/Perfil.html"
#     queryset=Usuario.objects.all()
    

# class EditarPerfil(UpdateView):
#     model = Usuario
#     form_class = Editar
#     template_name = "UserInformation/EditarPerfil.html"
#     def post(self, request, *args, **kwargs):
#         form=self.form_class(request.POST or None, request.FILES or None, instance=self.get_object())
#         if form.is_valid():
#             form.save()
#             print(request.FILES)
#             username = request.POST.get('username')
#             Object = Usuario.objects.get(username=username)
#             id = Object.id_usuario
#             return redirect("../Perfil/"+str(id))
#         else:
#             e=form.errors
#             print(e)
#             return JsonResponse({"x":e})
def EditarPerfil(request):
    template_name = "UserInformation/EditarPerfil.html"
    try:
        if request.session:
            get_object = Usuario.objects.get(id_usuario=request.session['pk'])
            form = Editar(instance=get_object)
            imagen = Usuario.objects.get(id_usuario=request.session['pk'])
            imagen = imagen.img_usuario
            UserSesion = {"username":request.session['username'], "rol":request.session['rol'], "imagen":imagen, "admin":request.session["Admin"]}
        if request.method=="POST":
            form = Editar(request.POST or None, request.FILES or None, instance=get_object)
            if form.is_valid():
                form.save()
                return redirect("Perfil")
            else:
                e=form.errors
                print(e)
                return JsonResponse({"x":e})
        return render(request, template_name, {"form":form,"User":UserSesion})
    except:
        return redirect("UNR")
    
def Change(request):
    return render(request,'UserInformation/ChangePassword.html')
def Admin(request):
    try:
        if request.session:
            imagen = Usuario.objects.get(id_usuario=request.session['pk'])
            imagen = imagen.img_usuario
            if request.session['Admin'] == True:
                UserSesion = {"username":request.session['username'], "rol":request.session['rol'], "imagen":imagen}
            else:
                return redirect("SinPermisos")
        model = Usuario
        filter = "yes"
        template_name = "UsersConfiguration/UsersAdministration.html"
        if request.method=="GET":
            queryset = model.objects.all()
            Servicios = Servicio.objects.all()
        return render(request, template_name, {"Usuario":queryset,"contexto":Servicios, "User":UserSesion})
    except:
        return redirect("UNR")
    
    
class CreateUser(CreateView):
    model = Usuario
    form_class = Regitro
    template_name = 'UsersConfiguration/CreateUsers.html'
    success_url = reverse_lazy("Administracion")

class UpdateUser(UpdateView):
    model = Usuario    
    template_name = 'UsersConfiguration/CreateUsers.html'
    form_class = Regitro
    success_url=reverse_lazy("Administracion")   
# class Notification(View):
#     template_name = 'UserInformation/Notification.html'
# class Notificacion(TemplateView):
#     template_name="UserInformation/Notification.html"

@csrf_exempt
def Notification(request):
    UserSesion = ""
    if request.session:
        imagen = Usuario.objects.get(id_usuario=request.session['pk'])
        imagen = imagen.img_usuario
        UserSesion = {"username":request.session['username'], "rol":request.session['rol'], "imagen":imagen}
    return render(request, "UserInformation/Notification.html", {"User":UserSesion})
    
def CambiarEstadoUsuario(request):
    print(request.POST)
    if request.method=="POST":
        id = request.POST["estado"]
        update=Usuario.objects.get(id_usuario=id)
        estado=update.estado
        if estado==True:
            update.estado=False
            update.save()
        elif estado==False:
            update.estado=True
            update.save()
        else:
            return redirect("Administracion")
        return HttpResponse(update)
    else:
        return JsonResponse({"x":"no"})