from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import EquipoModel
from .forms import TallerFormCreate, TallerFormUpdate

class TallerList(ListView):
    model = EquipoModel
    template_name = 'taller/taller.html'

    def get_queryset(self):
        return EquipoModel.objects.filter(estado='pendiente')

class TallerListTerminados(ListView):
    model = EquipoModel
    template_name = 'taller/taller_terminados.html'

    def get_queryset(self):
        return EquipoModel.objects.filter(estado='terminado')

class TallerCreate(CreateView):
    model = EquipoModel
    form_class = TallerFormCreate
    template_name = 'taller/taller_create.html'
    success_url = reverse_lazy('servicios:index')

class TallerUpdate(UpdateView):
    model = EquipoModel
    context_object_name = 'obj'
    form_class = TallerFormUpdate
    template_name = 'taller/taller_update.html'
    success_url = reverse_lazy('taller:index')

class TallerDelete(DeleteView):
    model = EquipoModel
    template_name = 'taller/taller_delete.html'
    success_url = reverse_lazy('taller:index')

class SearchViewPendiente(ListView):
    model = EquipoModel
    template_name = 'taller/taller_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchViewPendiente, self).get_queryset()
        query = self.request.GET.get('search')

        query = query.title()

        if query:
            postresult = EquipoModel.objects.filter(cliente__nombre__contains=query, estado='pendiente')

            if postresult:
                result = postresult
            else:
                result = 'no results'
        else:
            result = 'no results'
        
        return result
    

class SearchViewTerminado(ListView):
    model = EquipoModel
    template_name = 'taller/taller_terminados_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchViewTerminado, self).get_queryset()
        query = self.request.GET.get('search')

        query = query.title()

        if query:
            postresult = EquipoModel.objects.filter(cliente__nombre__contains=query, estado='terminado')

            if postresult:
                result = postresult
            else:
                result = 'no results'
        else:
            result = 'no results'
        
        return result
    