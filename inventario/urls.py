from django.urls import path
<<<<<<< HEAD
from .views import InventarioList, InventarioCreate, categoria_list
=======
from .views import InventarioList, InventarioCreate, CategoriaCreate, InventarioUpdate, InventarioDelete, InventarioModificaciones, ventas_create, ventas_list, categorias_list, CategoriaUpdate, CategoriaDelete
>>>>>>> 5439550

inventario_urls = ([
    path('list/', InventarioList.as_view(), name='index'),
    path('create/', InventarioCreate.as_view(), name='create'),
<<<<<<< HEAD
    path('create_api_cat/', categoria_list, name='create_api_cat')
=======
    path('update/<int:pk>/', InventarioUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', InventarioDelete.as_view(), name='delete'),
    path('modificaciones/', InventarioModificaciones.as_view(), name='modifications'),
    path('create_ventas/<int:id_ventas>', ventas_create, name='create-ventas'), 
    path('lista_ventas/', ventas_list.as_view(), name='list-ventas'),
    path('cat/lista_categorias/', categorias_list.as_view(), name='list_categorias'),
    path('cat/create_categoria/', CategoriaCreate.as_view(), name='create_cat'),
    path('cat/update_categoria/<int:pk>/', CategoriaUpdate.as_view(), name='update_cat'),
    path('cat/delete_categoria/<int:pk>/', CategoriaDelete.as_view(), name='delete_cat')
 
>>>>>>> 5439550
], 'inventario')