from dataclasses import fields
from socket import fromshare
from django import forms
from ModuloUsuarios.models import Usuario

class InicioSesion(forms.ModelForm):
    class Meta:
        model = Usuario
        
        fields=[
            'tipo_documento',
        ]
        widgets = {
            
        }