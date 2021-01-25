from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import ArticuloModel, CategoriaInvModel, VentasModel
from .forms import InventarioCreateForm, CategoriaCreateForm, InventarioUpdateForm, VentasCreateForm
from django.core import serializers

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



class InventarioModificaciones(ListView):
    template_name = 'inventario/inventario_modificaciones.html'
    def get_queryset(self):
        history = ArticuloModel.history.all()
        return history
  
def ventas_create(request, id_ventas):
    
    elemento = get_object_or_404(ArticuloModel, id=id_ventas)

    json_data = serializers.serialize('json', ArticuloModel.objects.all())

    if request.method == 'POST':
        form = VentasCreateForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('inventario:index')
    else:
        form = VentasCreateForm()

    form = VentasCreateForm(initial={'articulo':elemento})

    context = {
        'form':form,
        'json_data': json_data,
        'elemento':elemento,
        
    }

    return render(request, 'inventario/ventas_create.html', context)


class ventas_list(ListView):
    model = VentasModel
    template_name = 'inventario/ventas.html'


class categorias_list(ListView):
    model = CategoriaInvModel
    template_name = 'inventario/categorias_list.html'

class CategoriaCreate(CreateView):
    model = CategoriaInvModel
    form_class = CategoriaCreateForm
    template_name = 'inventario/categorias_create.html'
    success_url = reverse_lazy('inventario:list_categorias')

class CategoriaUpdate(UpdateView):
    model = CategoriaInvModel
    form_class = CategoriaCreateForm
    template_name = 'inventario/categorias_update.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inventario:list_categorias')

class CategoriaDelete(DeleteView):
    model = CategoriaInvModel
    template_name = 'inventario/includes/categorias_delete.html'
    success_url = reverse_lazy('inventario:list_categorias')
