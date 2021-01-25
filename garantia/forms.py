from django import forms
from .models import GarantiaModel


class GarantiasFormCreate(forms.ModelForm):
    class Meta:
        model = GarantiaModel
        fields = ['cliente', 'articulo', 'tecnico', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control', 'placeholder':'Seleccione cliente'}),
            'articulo': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese descripción', 'rows':3}),
            'tecnico': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'estado': forms.Select(attrs={'class':'form-control'})
        }


class GarantiasFormUpdate(forms.ModelForm):
    class Meta:
        model = GarantiaModel
        fields = ['cliente', 'articulo', 'tecnico', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control', 'size':"1"}),
            'articulo': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'tecnico': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'estado': forms.Select(attrs={'class':'form-control'})
        }