from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

class UsuariosList(ListView):
    pass

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('list_users')

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form() 
        #Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Repite la contraseña'})
        return form 