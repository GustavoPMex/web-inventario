from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import ArticuloModel, CategoriaInvModel
from .forms import InventarioCreateForm, CategoriaCreateForm
from .serializers import CategoriaSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(['GET', 'POST'])
def categoria_list(request):

    if request.method == 'GET':
        categorias_list = CategoriaInvModel.objects.all()
        serializer_list = CategoriaSerializer(categorias_list, many=True)
        return Response(serializer_list.data)

    elif request.method == 'POST':
        serializer_list = CategoriaSerializer(data=request.data)
        if serializer_list.is_valid():
            serializer_list.save()
            return Response(serializer_list.data, status=status.HTTP_201_CREATED)
        return Response(serializer_list.errors, status=status.HTTP_400_BAD_REQUEST)
    