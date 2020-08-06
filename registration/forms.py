from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Campo requerido, 254 caracteres como máximo')

    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya está registrado')
        
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'direccion', 'telefono', 'correo']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'direccion': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'placeholder':'Ingrese su dirección'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese Telefono'}),
            'correo': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingrese correo'}),
        }