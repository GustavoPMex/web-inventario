from django.urls import path
from .views import ServiciosList, ServiciosListTerminados, ServiciosCreate

servicios_urls = ([
    path('pendientes/', ServiciosList.as_view(), name='index'),
    path('terminados/', ServiciosListTerminados.as_view(), name='terminados'),
    path('create/', ServiciosCreate.as_view(), name='create')
], 'servicios')