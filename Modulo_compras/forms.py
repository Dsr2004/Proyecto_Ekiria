from django import forms
from Modulo_compras.models import Proveedor, Producto , Compra, Tipo_producto

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','telefono','celular','descripcion']



class Tipo_productoForm(forms.ModelForm):
    class Meta:
        model = Tipo_producto
        fields = ['nombre']

        
class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio','proveedor','tipo_producto','cantidad']
   


class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['producto','descripcion','total']
        widgets={
            "producto":forms.CheckboxSelectMultiple()
        }