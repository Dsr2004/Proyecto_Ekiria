# pip install djangorestframework
# pip install markdown 
# pip install django-filter
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from ModuloUsuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id_usuario',
            'nombres',
            'apellidos',
            'apodo',
            'email',
            'rol',
            'estado',
        )  
        