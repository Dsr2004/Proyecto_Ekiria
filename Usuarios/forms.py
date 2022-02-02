from dataclasses import fields
from socket import fromshare
from django import forms
from Usuarios.models import Usuario

class InicioSesion(forms.ModelForm):
    class Meta:
        model = Usuario
        
        fields=[
            'tipo_documento',
        ]
        widgets = {
            
        }
        
class Regitro(forms.ModelForm):
    class Meta:
        model = Usuario