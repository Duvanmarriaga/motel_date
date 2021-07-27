from MD_BD.models import Usuario,Reserva
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.forms import ModelForm

class Fcliente(ModelForm):
    
    password2=forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'ingrese nuevamente su contraseña..',
            'id':'ps2',
            'required':'required',
        }
    ))
    class Meta:
        model= Usuario
        fields=('nombre_usuario','email','nombres','documento','edad','apellidos','password')
        widgets={
            'edad':forms.NumberInput(attrs=({'type':'number','class':'form-control'})),
            'email':forms.EmailInput(attrs=({'type':'email','class':'form-control'})),
            'nombres':forms.TextInput(attrs=({'type':'text','class':'form-control'})),
            'apellidos':forms.TextInput(attrs=({'type':'text','class':'form-control'})),
            'documento':forms.NumberInput(attrs=({'type':'number','class':'form-control'})),
            'nombre_usuario':forms.TextInput(attrs=({'type':'text','class':'form-control'})),
            'password':forms.TextInput(attrs=({
                    'class':'form-control',
                    'placeholder':'ingrese su contraseña..',
                    'id':'ps1',
                    'required':'required',
                    'type':'password',
                })
            )
        }
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            return -1
        return password2

class FEdit(ModelForm):
    
    
    class Meta:
        model= Usuario
        fields=('email','nombres','edad','apellidos','password','documento')
        widgets={
            'edad':forms.NumberInput(attrs=({'type':'number','class':'form-control','id':'idedad'})),
            'email':forms.EmailInput(attrs=({'type':'email','class':'form-control'})),
            'nombres':forms.TextInput(attrs=({'type':'text','class':'form-control','id':'idnom'})),
            'apellidos':forms.TextInput(attrs=({'type':'text','class':'form-control'})),
            'documento':forms.NumberInput(attrs=({'type':'number','class':'form-control'})),
            'password':forms.TextInput(attrs=({
                    'class':'form-control',
                    'placeholder':'ingrese su contraseña..',
                    'id':'ps1',
                    'required':'required',
                    'type':'password',
                    
                })
            )
        }
class Form_reserva(ModelForm):
    class Meta:
        model= Reserva
        fields=('id_habitacion','id_usuario','fecha_inicio','fecha_fin')
        widgets={
            'id_habitacion':forms.DateInput(attrs=({'type':'hidden'})),
            'fecha_inicio':forms.DateInput(attrs=({'type':'date','class':'form-control'})),
            'fecha_fin':forms.DateInput(attrs=({'type':'date','class':'form-control'})),
            'fecha_reserva':forms.DateInput(attrs=({'type':'date','class':'form-control'})),
            'id_usuario':forms.DateInput(attrs=({'type':'hidden'})),
        }