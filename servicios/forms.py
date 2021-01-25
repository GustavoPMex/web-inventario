from django import forms
from .models import ServicioModel

class ServiciosCreateForm(forms.ModelForm):
    
    class Meta:
        model = ServicioModel
        fields = ['cliente', 'descripcion', 'tecnico', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese descripción', 'rows':3}),
            'tecnico': forms.Select(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
        }

class ServiciosUpdateForm(forms.ModelForm):
    
    class Meta:
        model = ServicioModel
        fields = ['cliente', 'descripcion', 'tecnico', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese descripción', 'rows':3}),
            'tecnico': forms.Select(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
        }