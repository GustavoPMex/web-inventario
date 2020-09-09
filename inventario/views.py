from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import ArticuloModel, CategoriaInvModel
from .forms import InventarioCreateForm, CategoriaCreateForm

class InventarioList(ListView):
    model = ArticuloModel
    template_name = 'inventario/inventario.html'

class InventarioCreate(CreateView):
    model = ArticuloModel
    form_class = InventarioCreateForm
    template_name = 'inventario/inventario_create.html'
    success_url = reverse_lazy('inventario:index')

class CategoriaCreate(CreateView):
    model = CategoriaInvModel
    form_class = CategoriaCreateForm
    template_name = 'inventario/categoria_create.html'
    success_url = reverse_lazy('inventario:create')
    