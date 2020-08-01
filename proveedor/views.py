from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ProveedorForm
from .models import ProveedorModel

class ProveedorList(ListView):
    model = ProveedorModel
    template_name = 'proveedor/proveedor.html'

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
    
class ProveedorCreate(CreateView):
    model = ProveedorModel
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_create.html'
    
    success_url = reverse_lazy('proveedor:index')