from django.urls import path
from .views import InventarioList, InventarioCreate, CategoriaCreate, categoria_list

inventario_urls = ([
    path('list/', InventarioList.as_view(), name='index'),
    path('create/', InventarioCreate.as_view(), name='create'),
    path('create_categoria/', CategoriaCreate.as_view(), name='create_cat'),
    path('create_api_cat/', categoria_list, name='create_api_cat')
], 'inventario')