from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ServicioModel
from django.urls import reverse_lazy
from .forms import ServiciosCreateForm, ServiciosUpdateForm
from registration.models import Profile

class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

        return HttpResponseNotAllowed(['GET', 'POST'])

class ServiciosList(ListView):
    model = ServicioModel
    template_name = 'servicios/servicios.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ServicioModel.objects.filter(estado='pendiente')
        else:
            return ServicioModel.objects.filter(estado='pendiente', tecnico__usuario=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(ServiciosList, self).get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        return context

class ServiciosListTerminados(ListView):
    model = ServicioModel
    template_name = 'servicios/servicios_completados.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ServicioModel.objects.filter(estado='terminado')
        else:
            return ServicioModel.objects.filter(estado='terminado', tecnico__usuario=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(ServiciosListTerminados, self).get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        
        return context

class ServiciosCreate(StaffRequiredMixin, CreateView):
    model = ServicioModel
    form_class = ServiciosCreateForm
    template_name = 'servicios/servicios_create.html'
    success_url = reverse_lazy('servicios:index')

class ServiciosUpdate(UpdateView):
    model = ServicioModel
    context_object_name = 'obj'
    form_class = ServiciosUpdateForm
    template_name = 'servicios/servicios_update.html'
    success_url = reverse_lazy('servicios:index')

class ServiciosDelete(DeleteView):
    model = ServicioModel 
    template_name = 'servicios/servicios_delete.html'
    success_url = reverse_lazy('servicios:terminados')

class SearchView(ListView):
    model = ServicioModel
    template_name = 'servicios/servicios_pen_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
    
        query = query.title()

        if query:
            if self.request.user.is_superuser:
                postresult = ServicioModel.objects.filter(cliente__nombre__contains=query, estado='pendiente')
            else:
                postresult = ServicioModel.objects.filter(cliente__nombre__contains=query, estado='pendiente',  tecnico__usuario=self.request.user)

            if postresult:
                result = postresult
            else:
                result = 'no results'
        else:
            result = 'no results'
        
        return result
    
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['clientes'] = ServicioModel.objects.all()
        context['profiles'] = Profile.objects.all()

        return context

class SearchView_terminado(ListView):
    model = ServicioModel
    template_name = 'servicios/servicios_ter_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView_terminado, self).get_queryset()
        query = self.request.GET.get('search')
    
        query = query.title()

        if query:
            if self.request.user.is_superuser:
                postresult = ServicioModel.objects.filter(cliente__nombre__contains=query, estado='terminado')
            else:
                postresult = ServicioModel.objects.filter(cliente__nombre__contains=query, estado='terminado', tecnico__usuario=self.request.user)

            if postresult:
                result = postresult
            else:
                result = 'no results'
        else:
            result = 'no results'
        
        return result
    
    def get_context_data(self, **kwargs):
        context = super(SearchView_terminado, self).get_context_data(**kwargs)
        context['clientes'] = ServicioModel.objects.all()
        context['profiles'] = Profile.objects.all()

        return context
