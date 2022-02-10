#-----------------------------------------Import's---------------------------------------------------
from asyncio import transports
from email import header
from html.entities import html5
from re import template
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from Usuarios.authentication_mixins import Authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from Usuarios.Serializers.general_serializers import UsuarioTokenSerializer
from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework.views import APIView
from Usuarios.models import Usuario
from Usuarios.forms import Regitro
from Usuarios.Serializers.general_serializers import UsuarioTokenSerializer
from rest_framework.renderers import TemplateHTMLRenderer

#--------------------------------------Templates Loaders------------------------------------
class Login(ObtainAuthToken, TemplateView):
    template_name = 'registration/login.html'
    def post(self,request,*arg, **kwargs):
        if request:
            login_serializer = self.serializer_class(data = request.data, context={'request':request})
            print(request)
            if login_serializer.is_valid():
                user=login_serializer.validated_data['user']
                if user.is_active:
                    token,created = Token.objects.get_or_create(user=user)
                    user_serializer = UsuarioTokenSerializer(user)
                    Client = "http://127.0.0.1:8000/"
                    if created:
                        token = Token.objects.create(user = user)
                        # header = {'Authorization':'Token '+token.key}
                        # return Response(headers=header)
                        return HttpResponseRedirect("/")
                    else:
                        all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                        if all_sessions.exists():
                            for session in all_sessions:
                                session_data = session.get_decoded()
                                if user.id_usuario == int(session_data.get('_auth_user_id')):
                                    session.delete()
                        token.delete()
                        token = Token.objects.create(user = user)
                        # credentials = 'http://127.0.0.1:8000'
                        # transport = HTTPTransport(credentials=credentials)
                        # client = Client(transports=transport)
                        # print(transport)
                        # return Response(client)
                        header = {'Authorization':'Token '+token.key}
                        return Response(headers=header)
                        # header = {'Authorization':'Token '+token.key}
                        # return Response(headers=header, template_name="index.html")
                    
                else:
                    return Response({'error':'Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error':'Nombre de usuario o contraseña incorrectos.'}, status=status.HTTP_400_BAD_REQUEST)


                
class Loguot(ObtainAuthToken, APIView):
    def post(self,request,*args,**kwargs):
        try:    
            token = Token.objects.filter(key = request.POST.get('token')).first()
            
            if token:
                
                user = token.user
                
                for i in range(2):
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id_usuario == int(session_data.get('_auth_user_id')):
                                session.delete()
                                        
                token.delete()
                    
                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado.'
                return Response({'token_message': token_message, 'session_message': session_message}, status = status.HTTP_200_OK)
            return Response({'error':'No se ha encontrado un usuario con estas credenciales.'}, status = status.HTTP_400_BAD_REQUEST)
        except :
            return Response({'error': 'No se ha encontrado token en la petición.'}, status = status.HTTP_409_CONFLICT)
        
        
            
def PassR(request):
    return render(request, "UserInformation/PasswordRecovery.html")

class Register(CreateView):
    model = Usuario
    form_class = Regitro
    template_name = 'registration/Registration.html'
    success_url = reverse_lazy("Inicio")
    
def Perfil(request):
    return render(request, "UserInformation/Perfil.html")
def Admin(request):
    return render(request, "UsersConfiguration/UsersAdministration.html")

# class Notification(TemplateView):
#     template_name = 'UserInformation/Notification.html'
def Notification(request):
    return render(request, "UserInformation/Notification.html")