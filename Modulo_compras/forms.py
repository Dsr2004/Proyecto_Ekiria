from django import forms
from Modulo_compras.models import Proveedor, Producto , Compra

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','telefono','celular','descripcion']

        
class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio','proveedor','tipo_producto','cantidad']
        widgets ={
            'nombre':forms.TextInput({})
        }



class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['producto','descripcion','cantidad','precio']