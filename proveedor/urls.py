from django.urls import path
from .views import ProveedorList, ProveedorSearch, ProveedorCreate

proveedor_urls = ([
    path('', ProveedorList.as_view(), name='index'),
    path('search/', ProveedorSearch.as_view(), name='search'),
    path('create/', ProveedorCreate.as_view(), name='create'),
], 'proveedor')