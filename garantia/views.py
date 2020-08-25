from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import GarantiaModel
from registration.models import Profile
from .forms import GarantiasFormCreate, GarantiasFormUpdate
from django.http import HttpResponse, HttpResponseRedirect
import datetime

class GarantiasList(ListView):
    model = GarantiaModel
    template_name = 'garantia/garantias.html'

    def get_queryset(self):
        return GarantiaModel.objects.filter(estado='pendiente')

    def get_context_data(self, **kwargs):
        context = super(GarantiasList, self).get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        return context
    
class GarantiasCompletas(ListView):
    model = GarantiaModel
    template_name = 'garantia/garantias_completas.html'

    def get_queryset(self):
        return GarantiaModel.objects.filter(estado='terminado')

    def get_context_data(self, **kwargs):
        context = super(GarantiasCompletas, self).get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        return context

class GarantiasCreate(CreateView):
    model = GarantiaModel
    template_name = 'garantia/garantias_create.html'
    form_class = GarantiasFormCreate

    def get_initial(self):
        return {'tecnico': self.request.user}

    success_url = reverse_lazy('garantias:index')

class GarantiasUpdate(UpdateView): 
    model = GarantiaModel
    form_class = GarantiasFormUpdate
    template_name = 'garantia/garantias_update.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('garantias:index')

class GarantiasDelete(DeleteView):
    model = GarantiaModel
    template_name = 'garantia/garantias_delete.html'
    success_url = reverse_lazy('garantias:index')

def personal_filter(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':
        select_value = request.POST.get('myselect', )
        estado = request.POST.get('estado', )

        if select_value == 'all':
            return redirect('garantias:index')

        else:
            list_item_post = GarantiaModel.objects.filter(tecnico=select_value, estado='pendiente')
            
    else:
        return redirect('garantias:index')

    context = {
        'profiles': profiles,
        'list_item_post':list_item_post
    }

    return render(request, 'garantia/garantias_personal.html', context)


def fecha_filter(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':

        select_value = request.POST.get('select_date', )

        if select_value == 'all':
            return redirect('garantias:index')

        elif select_value == '2019':
            print('2019')
            list_item_post_date = GarantiaModel.objects.filter(creacion__year = '2019', estado='pendiente')
         
        elif select_value == '2020':
            print('2020')
            list_item_post_date = GarantiaModel.objects.filter(creacion__year = '2020', estado='pendiente')
 
        else:
            return redirect('garantias:index') 

    else:
        return redirect('garantias:index') 

    context = {
        'profiles': profiles,
        'list_item_post_date':list_item_post_date
    }

    return render(request, 'garantia/garantias_fecha.html', context)


def personal_filter_terminados(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':
        select_value = request.POST.get('myselect', )
        estado = request.POST.get('estado', )

        if select_value == 'all':
            return redirect('garantias:completas')

        else:
            list_item_pendiente = GarantiaModel.objects.filter(tecnico=select_value, estado='terminado')
            
    else:
        return redirect('garantias:index')

    context = {
        'profiles': profiles,
        'list_item_pendiente':list_item_pendiente
    }

    return render(request, 'garantia/garantias_personal_terminado.html', context)


def fecha_filter_terminado(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':

        select_value = request.POST.get('select_date', )

        if select_value == 'all':
            return redirect('garantias:completas')

        elif select_value == '2019':
            print('2019')
            list_item_terminado = GarantiaModel.objects.filter(creacion__year = '2019', estado='terminado')
         
        elif select_value == '2020':
            print('2020')
            list_item_terminado = GarantiaModel.objects.filter(creacion__year = '2020', estado='terminado')
 
        else:
            return redirect('garantias:index') 

    else:
        return redirect('garantias:index') 

    context = {
        'profiles': profiles,
        'list_item_terminado':list_item_terminado
    }

    return render(request, 'garantia/garantias_fecha_terminado.html', context)