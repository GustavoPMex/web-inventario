from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ServicioModel
from django.urls import reverse_lazy
from .forms import ServiciosCreateForm

class ServiciosList(ListView):
    model = ServicioModel
    template_name = 'servicios/servicios.html'

    def get_queryset(self):
        return ServicioModel.objects.filter(estado='pendiente')

class ServiciosListTerminados(ListView):
    model = ServicioModel
    template_name = 'servicios/servicios_completados.html'

    def get_queryset(self):
        return ServicioModel.objects.filter(estado='terminado')

class ServiciosCreate(CreateView):
    model = ServicioModel
    form_class = ServiciosCreateForm
    template_name = 'servicios/servicios_create.html'
    success_url = reverse_lazy('servicios:index')

