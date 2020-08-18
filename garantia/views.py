from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import GarantiaModel
from .forms import GarantiasFormCreate, GarantiasFormUpdate
from django.http import HttpResponse, HttpResponseRedirect

class GarantiasList(ListView):
    model = GarantiaModel
    template_name = 'garantia/garantias.html'

    def get_queryset(self):
        return GarantiaModel.objects.filter(estado='pendiente')

    
class GarantiasCompletas(ListView):
    model = GarantiaModel
    template_name = 'garantia/garantias_completas.html'

    def get_queryset(self):
        return GarantiaModel.objects.filter(estado='terminado')

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
    # success_url = reverse_lazy('garantias:index')

    def post(self, request, pk):
        if request.method == 'POST':
            estado = request.POST.get('estado', )
            if estado == 'pendiente':
                new_form = form.save()
                return HttpResponseRedirect('/garantias/create')
            else:
                return HttpResponseRedirect('/garantias/completas')
        else:
            return HttpResponseRedirect('/garantias/')

    # def get_context_data(self, **kwargs):
    #     estado = request.POST.get('estado', )

    #     if estado == 'pendiente':
    #         return HttpResponseRedirect('/garantias/')
    #     else:
    #         return HttpResponseRedirect('/garantias/')

class GarantiasDelete(DeleteView):
    model = GarantiaModel
    template_name = 'garantia/garantias_delete.html'
    success_url = reverse_lazy('garantias:index')