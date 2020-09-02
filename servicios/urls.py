from django.urls import path
from .views import ServiciosList, ServiciosListTerminados, ServiciosCreate, ServiciosUpdate, SearchView, SearchView_terminado, ServiciosDelete, profile_view_filter, profile_view_filter_completados

servicios_urls = ([
    path('pendientes/', ServiciosList.as_view(), name='index'),
    path('terminados/', ServiciosListTerminados.as_view(), name='terminados'),
    path('create/', ServiciosCreate.as_view(), name='create'),
    path('update/<int:pk>/', ServiciosUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ServiciosDelete.as_view(), name='delete'),
    path('pendientes/search_pendientes/', SearchView.as_view(), name='search_p'),
    path('terminados/search_terminados/', SearchView_terminado.as_view(), name='search_t'),
    path('pendientes/profile_filter/', profile_view_filter, name='filter'),
    path('terminados/profile_filter_terminados/', profile_view_filter_completados, name='filter_completados')

    
], 'servicios')