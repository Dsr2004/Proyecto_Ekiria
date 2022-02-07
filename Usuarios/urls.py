from django.urls import path
from Usuarios.views import PassR, Perfil, Admin, Notification
urlpatterns = [
    path('RecuperarContraseña/', PassR, name="RecuperarContraseña"),
    path('Perfil/', Perfil, name="Perfil"),
    path('Administracion/', Admin, name="Administracion"),
    path('Notificaciones/', Notification, name="Notify"),
    # path('', Usertoken.as_view(), name = "refresh_token"),
]