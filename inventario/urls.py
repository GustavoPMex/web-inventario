from django.urls import path
from .views import InventarioList, InventarioCreate, CategoriaCreate, InventarioUpdate, InventarioDelete, InventarioModificaciones, ventas_create

inventario_urls = ([
    path('list/', InventarioList.as_view(), name='index'),
    path('create/', InventarioCreate.as_view(), name='create'),
    path('update/<int:pk>/', InventarioUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', InventarioDelete.as_view(), name='delete'),
    path('create_categoria/', CategoriaCreate.as_view(), name='create_cat'),
    path('modificaciones/', InventarioModificaciones.as_view(), name='modifications'),
    path('create_ventas/', ventas_create, name='create-ventas')
 
], 'inventario')