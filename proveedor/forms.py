from django import forms
from .models import ProveedorModel

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = ProveedorModel
        fields = ['nombre', 'descripcion', 'telefono_uno', 'telefono_dos', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa nombre'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingresa descripción', 'rows':3}),
            'telefono_uno': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingresa telefono'}),
            'telefono_dos': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Telefono opcional'}),
            'correo' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingresa email'})
        }