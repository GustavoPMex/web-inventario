from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProveedorForm,ProveedorModalForm
from .models import ProveedorModel
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class ProveedorList(ListView):
    model = ProveedorModel
    template_name = 'proveedor/proveedor.html'

@method_decorator(login_required, name='dispatch')
class ProveedorSearch(ListView):
    model = ProveedorModel
    template_name = 'proveedor/proveedor_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(ProveedorSearch, self).get_queryset()
        query = self.request.GET.get('search')

        query = query.title()

        if query:
            postresult = ProveedorModel.objects.filter(nombre__contains=query)

            if postresult:
                result = postresult
            else:
                result = 'no results'
        else:
            result = 'no results'

        return result

    def get_context_data(self, **kwargs):
        context = super(ProveedorSearch, self).get_context_data(**kwargs)
        context['proveedores'] = ProveedorModel.objects.all()

        return context

@method_decorator(login_required, name='dispatch')
class ProveedorCreate(CreateView):
    model = ProveedorModel
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_create.html'
    
    success_url = reverse_lazy('proveedor:index')

@method_decorator(login_required, name='dispatch')
class ProveedorUpdate(UpdateView):
    model = ProveedorModel
    form_class = ProveedorModalForm
    context_object_name = 'obj'
    template_name = 'proveedor/proveedor_update.html'
    success_url = reverse_lazy('proveedor:index')

@method_decorator(login_required, name='dispatch')
class ProveedorDelete(DeleteView):
    model = ProveedorModel
    template_name = 'proveedor/includes/modal_delete.html'
    success_url = reverse_lazy('proveedor:index')