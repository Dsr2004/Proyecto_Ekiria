from unicodedata import name
from django.urls import path
from Usuarios.views import PassR, Perfil, Admin, Notification, CreateUser
urlpatterns = [
    path('RecuperarContraseña/', PassR, name="RecuperarContraseña"),
    path('Perfil/', Perfil, name="Perfil"),
    path('Administracion/', Admin.as_view(), name="Administracion"),
    path('Notificaciones/', Notification, name="Notify"),
    path('CrearUsuario/', CreateUser.as_view(), name="CreateUser"),
    # path('', Usertoken.as_view(), name = "refresh_token"),
]