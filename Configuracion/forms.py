from dataclasses import fields
from django import forms
from .models import Rol
from .models import cambios
from crispy_forms.helper import FormHelper

class RolForm(forms.ModelForm):
    
    class Meta:
        model = Rol
        fields = ('nombre', 'descripcion')
        widgets={
            'nombre':forms.TextInput(attrs={"class":"form-control"}),
            'descripcion':forms.Textarea(attrs={"class":"form-control", 'rows':"5", 'cols':"60"})
        }

    def __init__(self, *args, **kwargs):
        super(RolForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"novalidate": "novalidate"}

class CambiosForm(forms.ModelForm):

    class Meta:
        model = cambios
        fields = '__all__'

class FooterForm(forms.ModelForm):

    class Meta:
        model = footer
        fields = '__all__'
