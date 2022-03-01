from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    
    class Meta:
        model = Rol
        fields = ('nombre', 'descripcion')
        widgets={
            'nombre':forms.TextInput(attrs={"class":"form-control"}),
            'descripcion':forms.TextInput(attrs={"class":"form-control", 'rows':"5", 'cols':"60"})
        }

