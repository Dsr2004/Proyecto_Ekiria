#-----------------------------------------Importaciones---------------------------------------------------
from urllib import response
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from ModuloUsuarios.serializers import UsuarioTokenSerializer
from django.contrib.sessions.models import Session
from datetime import datetime
#--------------------------------------Cargadores de templates------------------------------------

class Login(ObtainAuthToken, TemplateView):
    template_name = "registration/login.html"
    def post(self,request,*arg, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context={'request':request})
        if login_serializer.is_valid():
            user=login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                user_serializer = UsuarioTokenSerializer(user)
                if created:
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message':'Inicio de Sesión Exitoso.'
                    },status=status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id_usuario == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message':'Inicio de Sesión Exitoso.'
                    },status=status.HTTP_201_CREATED)
                    # return Response({
                    #     'error': 'Ya se ha iniciado sesión con este usuario, ¡intentalo de nuevo!'
                    # })
            else:
                return Response({'error':'Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Nombre de usuario o contraseña incorrectos.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje': 'hola desde response'}, status = status.HTTP_200_OK)
        
def PassR(request):
    return render(request, "UserInformation/PasswordRecovery.html")
def Register(request):
    return render(request, "registration/Registration.html")
def Perfil(request):
    return render(request, "UserInformation/Perfil.html")
def Admin(request):
    return render(request, "UsersConfiguration/UsersAdministration.html")