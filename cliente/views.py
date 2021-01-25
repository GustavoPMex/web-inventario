from django.shortcuts import render
from .models import ClienteModel
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import ClienteForm, ClienteModalForm
from django.urls import reverse_lazy

class ClienteList(ListView):
    model = ClienteModel
    template_name = 'cliente/clientes.html'

class ClienteCreate(CreateView):
    model = ClienteModel
    template_name = 'cliente/clientes_create.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:index')


class SearchView(ListView):
    model = ClienteModel
    template_name = 'cliente/clientes_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')

        query = query.title() 

        if query:
            postresult = ClienteModel.objects.filter(nombre__contains=query)

            if postresult:
                result = postresult
            else:
                result = 'no results'

        else:
            result = 'no results'

        return result

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['clientes'] = ClienteModel.objects.all() 

        return context

class ClienteUpdate(UpdateView):
    model = ClienteModel
    form_class = ClienteModalForm
    template_name = 'cliente/clientes_update.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('cliente:index')

class ClienteDelete(DeleteView):
    model = ClienteModel
    template_name = 'cliente/includes/modal_delete.html'
    success_url = reverse_lazy('cliente:index')
    