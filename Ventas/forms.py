# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column,ButtonHolder, Div, Fieldset, HTML, Field
# from crispy_forms.bootstrap import FormActions

# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
# from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

from django import forms
from .models import Servicio, Tipo_servicio, Catalogo, Servicio_Personalizado,Cita


class ServicioForm(forms.ModelForm):
    class Meta:
        model=Servicio  
        fields=("nombre","precio","tipo_servicio_id","img_servicio","slug","descripcion", "estado","duracion")
        widgets={
            'duracion':forms.NumberInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_servicio_id':forms.Select(attrs={"class":"form-select"}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'img_servicio':forms.FileInput(attrs={"class":"fileSerPersonalizado", "style":"margin-left:40px; top:-15px"}),
            'precio':forms.NumberInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control', }),
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
            self.fields['duracion'].label = False
            self.fields['slug'].required = False

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
            'nombre':forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}),
            'estado':forms.CheckboxInput(attrs={'class':'form-check-input estadoServicioRegistro',  "style":"margin-left: -5px; height: 30px; width: 60px; margin-top: -5px"})
        }
    def __init__(self, *args, **kwargs):
            super(Tipo_servicioForm, self).__init__(*args, **kwargs) 
            self.fields['nombre'].label = False
            self.fields['estado'].label = False
            self.helper=FormHelper()
            self.helper.form_show_errors=False
            self.helper.error_text_inline = False

class CatalogoForm(forms.ModelForm):
    class Meta:
        model=Catalogo
        fields="__all__"
        widgets={
            'servicio_id':forms.Select(attrs={"class":"form-select"}),
            'estado':forms.CheckboxInput(attrs={'class':'form-check-input estadoServicioRegistro',  "style":"margin-left: -5px; height: 30px; width: 60px; margin-top: -5px"})
        }
    def __init__(self, *args, **kwargs):
        super(CatalogoForm, self).__init__(*args, **kwargs)
        consulta = Servicio.objects.filter(estado=True)
        self.fields['servicio_id'].queryset = consulta

class Servicio_PersonalizadoForm(forms.ModelForm):
    class Meta:
        model=Servicio_Personalizado
        fields=("tipo_servicio_id","descripcion","img_servicio","duracion")
        widgets={
            'duracion':forms.NumberInput(attrs={'class':'form-control'}),
            'tipo_servicio_id':forms.Select(attrs={"class":"form-select"}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'img_servicio':forms.FileInput(attrs={"class":"fileSerPersonalizado", "style":"margin-left:40px; top:-15px"})
        }
    def __init__(self, *args, **kwargs):
        super(Servicio_PersonalizadoForm, self).__init__(*args, **kwargs) 
        self.fields['tipo_servicio_id'].queryset = Tipo_servicio.objects.filter(nombre__in=["Manicure","Pedicure","manicure","pedicure","MANICURE","PEDICURE"]).filter(estado=True)
        self.fields['img_servicio'].label = False
        self.fields['duracion'].label = False


class CitaForm(forms.ModelForm):
    class Meta:
        model= Cita
        fields =["empleado_id","diaCita","horaInicioCita","descripcion"]
        widgets={
            "diaCita":forms.DateInput(attrs={"class":"form-control","id":"DiaCita","type":"text","autocomplete":"off"}),
            "horaInicioCita":forms.TimeInput(attrs={"class":"form-control","id":"horaInicio","type":"text","autocomplete":"off"}),
            "empleado_id":forms.Select(attrs={"class":"form-select","id":"empleado","type":"text"}),
            "descripcion":forms.Textarea(attrs={"class":"form-control","cols":"60","rows":"10"})
        }
    # date_field = forms.DateField(widget=DatePicker())
    # date_field_required_with_min_max_date = forms.DateField(
    #     required=True,
    #     widget=DatePicker(
    #         options={
    #             'minDate': '2009-01-20',
    #             'maxDate': '2017-01-20',
    #         },
    #          attrs={
    #             'append': 'fa fa-calendar',
    #             'icon_toggle': True,
    #         }
    #     ),
    #     initial='2013-01-01',
    # )
    # """
    # In this example, the date portion of `defaultDate` is irrelevant;
    # only the time portion is used. The reason for this is that it has
    # to be passed in a valid MomentJS format. This will default the time
    # to be 14:56:00 (or 2:56pm).
    # """
    # time_field = forms.TimeField(
    #    widget=TimePicker(
    #         options={
    #             'useCurrent': True,
    #             'collapse': False,
    #         },
    #         attrs={
    #             'append': 'fa fa-clock-o',
    #             'icon_toggle': True,
    #         }
    #     ),
    # )
    # datetime_field = forms.DateTimeField(
    #     widget=DateTimePicker(
    #         options={
    #             'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
    #             'defaultDate': '1970-01-01T14:56:00',
    #             'useCurrent': True,
    #             'collapse': False,
    #         },
    #         attrs={
    #             'append': 'fa fa-calendar',
    #             'icon_toggle': True,
    #         }
    #     ),
    # )
    




class pruebaxForm(forms.Form):
    todo = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    date = forms.DateField(
        widget=DatePickerInput(format='%m/%d/%Y')
    )


    # date_field = forms.DateField(widget=DatePicker())
    # date_field_required_with_min_max_date = forms.DateField(
    #     required=True,
    #     widget=DatePicker(
    #         options={
    #             'minDate': '2009-01-20',
    #             'maxDate': '2017-01-20',
    #         },
    #          attrs={
    #             'append': 'fa fa-calendar',
    #             'icon_toggle': True,
    #         }
    #     ),
    #     initial='2013-01-01',
    # )
    # """
    # In this example, the date portion of `defaultDate` is irrelevant;
    # only the time portion is used. The reason for this is that it has
    # to be passed in a valid MomentJS format. This will default the time
    # to be 14:56:00 (or 2:56pm).
    # """
    # time_field = forms.TimeField(
    #    widget=TimePicker(
    #         options={
    #             'useCurrent': True,
    #             'collapse': False,
    #         },
    #         attrs={
    #             'append': 'fa fa-clock-o',
    #             'icon_toggle': True,
    #             'class':"kisiandMelocoton"
    #         }
    #     ),
    # )
    # datetime_field = forms.DateTimeField(
    #     widget=DateTimePicker(
    #         options={
    #             'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
    #             'defaultDate': '1970-01-01T14:56:00',
    #             'useCurrent': True,
    #             'collapse': False,
    #         },
    #         attrs={
    #             'append': 'fa fa-calendar',
    #             'icon_toggle': True,
    #         }
    #     ),
    # )

    