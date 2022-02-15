from django import forms
from Modulo_compras.models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','telefono','celular','descripcion']