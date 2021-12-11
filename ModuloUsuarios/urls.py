from django.urls import path
from ModuloUsuarios.views import login
urlpatterns = [
    path("InicioSesion/", login, name="iniciosesion")
]