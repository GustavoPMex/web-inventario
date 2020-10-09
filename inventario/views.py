from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import ArticuloModel, CategoriaInvModel, VentasModel
from .forms import InventarioCreateForm, CategoriaCreateForm, InventarioUpdateForm, VentasCreateForm

class InventarioList(ListView):
    model = ArticuloModel
    template_name = 'inventario/inventario.html'

class InventarioCreate(CreateView):
    model = ArticuloModel
    form_class = InventarioCreateForm
    template_name = 'inventario/inventario_create.html'
    success_url = reverse_lazy('inventario:index')

class InventarioUpdate(UpdateView):
    model = ArticuloModel
    form_class = InventarioUpdateForm
    template_name = 'inventario/inventario_update.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inventario:index')

class InventarioDelete(DeleteView):
    model = ArticuloModel
    template_name = 'inventario/inventario_delete.html'
    success_url = reverse_lazy('inventario:index')

class CategoriaCreate(CreateView):
    model = CategoriaInvModel
    form_class = CategoriaCreateForm
    template_name = 'inventario/categoria_create.html'
    success_url = reverse_lazy('inventario:create')

class InventarioModificaciones(ListView):
    template_name = 'inventario/inventario_modificaciones.html'
    def get_queryset(self):
        history = ArticuloModel.history.all()
        return history
  
def ventas_create(request):
    form = VentasCreateForm()
    if request.method == 'POST':
        form = VentasCreateForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('inventario:index')
    else:
        form = VentasCreateForm()
    
    return render(request, 'inventario/ventas_create.html', {'form':form})


class ventas_list(ListView):
    model = VentasModel
    template_name = 'inventario/ventas.html'