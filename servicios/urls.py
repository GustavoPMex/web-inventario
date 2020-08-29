from django.urls import path
from .views import ServiciosList, ServiciosListTerminados, ServiciosCreate, ServiciosUpdate, SearchView, SearchView_terminado, ServiciosDelete

servicios_urls = ([
    path('pendientes/', ServiciosList.as_view(), name='index'),
    path('terminados/', ServiciosListTerminados.as_view(), name='terminados'),
    path('create/', ServiciosCreate.as_view(), name='create'),
    path('update/<int:pk>/', ServiciosUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ServiciosDelete.as_view(), name='delete'),
    path('search_pendientes/', SearchView.as_view(), name='search_p'),
    path('search_terminados/', SearchView_terminado.as_view(), name='search_t')
    
], 'servicios')