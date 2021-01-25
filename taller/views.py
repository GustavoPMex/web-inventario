from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import EquipoModel
from .forms import TallerFormCreate, TallerFormUpdate

class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

        return HttpResponseNotAllowed(['GET', 'POST'])

class TallerList(ListView):
    model = EquipoModel
    template_name = 'taller/taller.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return EquipoModel.objects.filter(estado='pendiente')
        else:
            return EquipoModel.objects.filter(estado='pendiente', personal__usuario=self.request.user)

class TallerListTerminados(ListView):
    model = EquipoModel
    template_name = 'taller/taller_terminados.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return EquipoModel.objects.filter(estado='terminado')
        else:
            return EquipoModel.objects.filter(estado='terminado', personal__usuario=self.request.user)


class TallerCreate(StaffRequiredMixin, CreateView):
    model = EquipoModel
    form_class = TallerFormCreate
    template_name = 'taller/taller_create.html'
    success_url = reverse_lazy('taller:index')

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
            if self.request.user.is_superuser:
                postresult = EquipoModel.objects.filter(cliente__nombre__contains=query, estado='pendiente')
            else:
                postresult = EquipoModel.objects.filter(cliente__nombre__contains=query, estado='pendiente', personal__usuario=self.request.user)

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
            if self.request.user.is_superuser:
                postresult = EquipoModel.objects.filter(cliente__nombre__contains=query, estado='terminado')
            else:
                postresult = EquipoModel.objects.filter(cliente__nombre__contains=query, estado='terminado', personal__usuario=self.request.user)

            if postresult:
                result = postresult
            else:
                result = 'no results'
        else:
            result = 'no results'
        
        return result
    