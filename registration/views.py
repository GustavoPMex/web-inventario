from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from .models import Profile
from django.contrib.auth.models import User

class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

        return HttpResponseNotAllowed(['GET', 'POST'])

class ProfileView(TemplateView):
    template_name = 'registration/profile.html'

    
class SignUpView(StaffRequiredMixin, CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('list_users')

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form() 
        #Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo electronico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Repite la contraseña'})
        return form 


class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(usuario=self.request.user)
        return profile

class ProfileDelete(StaffRequiredMixin, DeleteView):
    model = Profile
    template_name = 'registration/profile_delete.html'
    success_url = reverse_lazy('list_users')
 
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

class ListUsers(StaffRequiredMixin, ListView):
    model = Profile
    template_name = 'registration/list_users.html'


class SearchView(StaffRequiredMixin, ListView):
    model = Profile
    template_name = 'registration/search_list.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')

        query = query.title() 

        if query:
            postresult = Profile.objects.filter(usuario__username__contains=query)

            if postresult:
                result = postresult
            else:
                result = 'no results'

        else:
            result = 'no results'

        return result

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()

        return context
