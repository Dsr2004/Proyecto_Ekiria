from django import forms

from Usuarios.models import Usuario
class Regitro(forms.ModelForm):
    
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput(
        attrs={
            'id':"password",
            'requerid':'requerid',
        }
    ))
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(
        attrs={
            'id':"confpassword",
            'requerid':'requerid',
        }
    ))
    
    class Meta:
        model = Usuario
        
        fields=[
            'username',
            'nombres',
            'apellidos',
            'telefono',
            'celular',
            'email',
            'fec_nac',
            'tipo_documento',
            'num_documento',
            'municipio',
            'direccion',
            'cod_postal',
        ]
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'id':'Idate',
                    'required':'requerid',
                    'autocomplete':'off',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'required':'requerid',
                    'autocomplete':'off',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'required':'requerid',
                    'autocomplete':'off',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'required':'requerid',
                    'autocomplete':'off',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'required':'requerid',
                    'autocomplete':'off',
                }
            ),
            'celular': forms.TextInput(
                attrs={
                    'required':'requerid',
                    'autocomplete':'off',
                }
            ),
            'fec_nac': forms.DateInput(
                attrs={
                    'type':'date',
                    'required':'requerid',
                    'autocomplete':'off',
                    'style':'color:#fff;'
                }
            ),
            'tipo_documento': forms.Select(
                attrs={
                    'required':'requerid',
                    'autocomplete':'off',
                }
            ),
            'num_documento': forms.TextInput(
                attrs={
                    'required':'requerid',
                    'autocomplete':'off',
                    'type':'number',
                }
            ),
            'municipio': forms.Select(
                attrs={
                    'required':'requerid',
                    'autocomplete':'off',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'required':'requerid',
                    'autocomplete':'off',
                }
            ),
            'cod_postal': forms.TextInput(
                attrs={
                    'required':'requerid',
                    'autocomplete':'off',
                }
            ),
        }
    def clean_password2(self):
        """Validación de contraseña
        
        
        Metodo que valida que ambas contraseñas ingresadas sean iguales, antes de ser encriptadas, Retorna la contraseña Validada.
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseña no coinciden')
        return password2
    
    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
