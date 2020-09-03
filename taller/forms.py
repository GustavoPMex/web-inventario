from django import forms
from .models import EquipoModel

class TallerFormCreate(forms.ModelForm):
    class Meta:
        model = EquipoModel
        fields = ['equipo', 'descripcion', 'cliente', 'personal', 'estado']
        widgets = {
            'equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa equipo'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Ingresa descrición'}),
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'personal': forms.Select(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
        }

class TallerFormUpdate(forms.ModelForm):
    class Meta:
        model = EquipoModel
        fields = ['equipo', 'descripcion', 'cliente', 'personal', 'estado']
        widgets = {
            'equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa equipo'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Ingresa descrición'}),
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'personal': forms.Select(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
        }