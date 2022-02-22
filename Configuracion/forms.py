from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    
    class Meta:
        model = Rol
        fields = ('nombre', 'descripcion')
        widgets={
            'nombre':forms.TextInput(attrs={'id':'nombreRol'}),
            'descripcion':forms.Textarea(attrs={'id':"descripRol", 'rows':"5", 'cols':"60"})
        }

