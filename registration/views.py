from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'registration/profile.html'

@method_decorator(login_required, name='dispatch')
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home:index')

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form() 
        #Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo electronico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Repite la contraseña'})
        return form 

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(usuario=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile_update')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        #Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
        return form

class ListUsers(ListView):
    model = Profile
    template_name = 'registration/list_users.html'