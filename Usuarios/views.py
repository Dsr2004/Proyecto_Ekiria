#-----------------------------------------Importaciones---------------------------------------------------
from re import template
from django.http import HttpResponseRedirect, request, HttpResponse
from django.views.generic import TemplateView, CreateView
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
from django.contrib.auth.forms import UserCreationForm
from Usuarios.Serializers.general_serializers import UsuarioTokenSerializer
from rest_framework.authentication import get_authorization_header
#--------------------------------------Cargadores de templates------------------------------------
# class Usertoken(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.POST.get('username')
#         print(username)
#         try:
#             user_token = Token.objects.get(
#                 user = UsuarioTokenSerializer().Meta.model.objects.filter(username = username).first()
#             )
#             return Response({
#                 'token': user_token.key
#             })
#         except:
#             return Response({'error': 'No se han enviado las credenciales.'}, status=status.HTTP_400_BAD_REQUEST)
class Login(ObtainAuthToken, TemplateView):
    template_name = 'registration/login.html'
    def post(self,request,*arg, **kwargs):
        if request:
            login_serializer = self.serializer_class(data = request.data, context={'request':request})
            if login_serializer.is_valid():
                user=login_serializer.validated_data['user']
                if user.is_active:
                    token,created = Token.objects.get_or_create(user=user)
                    user_serializer = UsuarioTokenSerializer(user)
                    
                    if created:
                        # return HttpResponseRedirect('/')
                        return Response({
                            'token': token.key,
                            'user': user_serializer.data,
                            'massage': 'Inicio de Sesión Exitoso.',
                        }, status = status.HTTP_201_CREATED)
                    else:
                        all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                        if all_sessions.exists():
                            for session in all_sessions:
                                session_data = session.get_decoded()
                                if user.id_usuario == int(session_data.get('_auth_user_id')):
                                    session.delete()
                        token.delete()
                        token = Token.objects.create(user = user)
                        response = HttpResponse(headers={'Authorization':'Token '+token.key})
                        # return response
                        # return Response(headers={'Authorization':'Token '+token.key})
                        return Response({
                            'token': token.key,
                            'user': user_serializer.data,
                            'massage': 'Inicio de Sesión Exitoso.',
                        }, status = status.HTTP_201_CREATED)
                        # return Response({
                        #     'error': 'Ya se ha iniciado sesión con este usuario, ¡intentalo de nuevo!'
                        # })
                else:
                    return Response({'error':'Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
                return redirect("/")
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

# def Register(request):
#     return render(request, "registration/Registration.html")

class Register(TemplateView):
    model = Usuario
    template_name = 'registration/Registration.html'
    form_class = UserCreationForm
    
def Perfil(request):
    return render(request, "UserInformation/Perfil.html")
def Admin(request):
    return render(request, "UsersConfiguration/UsersAdministration.html")

# class Notification(TemplateView):
#     template_name = 'UserInformation/Notification.html'
def Notification(request):
    return render(request, "UserInformation/Notification.html")