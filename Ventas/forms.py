# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column,ButtonHolder, Div, Fieldset, HTML, Field
# from crispy_forms.bootstrap import FormActions

# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper

from django import forms
from .models import Servicio, Tipo_servicio


class ServicioForm(forms.ModelForm):
    class Meta:
        model=Servicio
        fields=("nombre","precio","tipo_servicio_id","img_servicio","slug","descripcion", "estado")

        # labels={
        #     "nombre":"Nombre ",
        #     "precio":"Precio ",
        #     "tipo_servicio_id":"Tipo de Servicio ",
        #     "img_servicio":"Imagen del Servicio ",
        #     "slug":"Slug: ",
        #     "descripcion":"Descripcion ",
        #     "estado":"Estado ",

        # }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_servicio_id':forms.Select(attrs={"class":"form-select"}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'img_servicio':forms.FileInput(attrs={"class":"fileSerPersonalizado", "style":"margin-left:40px; top:-15px"}),
            'precio':forms.NumberInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.CheckboxInput(attrs={'class':'form-check-input estadoServicioRegistro',  "style":"margin-left: -5px; height: 30px; width: 60px; margin-top: -5px"})
        }
    def __init__(self, *args, **kwargs):
            super(ServicioForm, self).__init__(*args, **kwargs) 
            self.fields['tipo_servicio_id'].queryset = Tipo_servicio.objects.filter(estado=True)
            self.fields['nombre'].label = False
            self.fields['precio'].label = False
            self.fields['tipo_servicio_id'].label = False
            self.fields['img_servicio'].label = False
            self.fields['slug'].label = False
            self.fields['descripcion'].label = False
            self.fields['estado'].label = False

class EditarTipoServicioForm(forms.ModelForm):
    class Meta:
        model=Servicio
        fields=("estado",)

        widgets={
            'estado':forms.CheckboxInput(attrs={'class':'form-check-input estadoServicioRegistro',  'style':"top: 5px; font-size: -15px; left: 0px;transform: scale(0.5);", 'onclick':'editarTipoSerivico()', 'name':'estado'})
        }
    def __init__(self, *args, **kwargs):
            super(EditarTipoServicioForm, self).__init__(*args, **kwargs)
            self.fields['nombre'].label = False
            self.fields['estado'].label = False
            self.helper=FormHelper()
            self.helper.form_show_errors=False
            self.helper.error_text_inline = False

        
class Tipo_servicioForm(forms.ModelForm):
    class Meta:
        model=Tipo_servicio
        fields="__all__"
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.CheckboxInput(attrs={'class':'form-check-input estadoServicioRegistro',  "style":"margin-left: -5px; height: 30px; width: 60px; margin-top: -5px"})
        }
    def __init__(self, *args, **kwargs):
            super(Tipo_servicioForm, self).__init__(*args, **kwargs) 
            self.fields['nombre'].label = False
            self.fields['estado'].label = False
            self.helper=FormHelper()
            self.helper.form_show_errors=False
            self.helper.error_text_inline = False
            