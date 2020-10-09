from django import forms
from .models import ArticuloModel, CategoriaInvModel, VentasModel

class InventarioCreateForm(forms.ModelForm):
    class Meta:
        model = ArticuloModel
        fields = ['nombre', 'categoria', 'proveedor', 'precio', 'cantidad']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa nombre'}),
            'categoria':forms.SelectMultiple(attrs={'class':'form-control'}),
            'proveedor':forms.Select(attrs={'class': 'form-control'}),
            'precio':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingresa Precio'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingresa cantidad'}),
        }

class InventarioUpdateForm(forms.ModelForm):
    class Meta:
        model = ArticuloModel
        fields = ['nombre', 'categoria', 'proveedor', 'precio', 'cantidad']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa nombre'}),
            'categoria':forms.SelectMultiple(attrs={'class':'form-control'}),
            'proveedor':forms.Select(attrs={'class': 'form-control'}),
            'precio':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingresa Precio'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingresa cantidad'}),
        }

class CategoriaCreateForm(forms.ModelForm):
    class Meta:
        model = CategoriaInvModel
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control mb-1'})
        }

class VentasCreateForm(forms.ModelForm):
    class Meta:
        model = VentasModel
        fields = ['articulo', 'vendido']
        widgets = {
            'articulo':forms.Select(attrs={'class':'form-control mb-1'}),
            'vendido':forms.NumberInput(attrs={'class':'form-control'})
        }

    
    

