from django.urls import path
from .views import ProveedorList, ProveedorSearch, ProveedorCreate, ProveedorUpdate, ProveedorDelete

proveedor_urls = ([
    path('', ProveedorList.as_view(), name='index'),
    path('search/', ProveedorSearch.as_view(), name='search'),
    path('create/', ProveedorCreate.as_view(), name='create'),
    path('update/<int:pk>/', ProveedorUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProveedorDelete.as_view(), name='delete'),
], 'proveedor')