from django.urls import path
from .views import TallerList, TallerListTerminados , TallerCreate, TallerUpdate, TallerDelete, SearchViewPendiente, SearchViewTerminado

taller_urls = ([
    path('pendientes/', TallerList.as_view(), name='index'),
    path('terminados/', TallerListTerminados.as_view(), name='terminados'),
    path('create/', TallerCreate.as_view(), name='create'),
    path('update/<int:pk>/', TallerUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TallerDelete.as_view(), name='delete'),
    path('pendientes/search/', SearchViewPendiente.as_view(), name='search_pen'),
    path('terminados/search/', SearchViewTerminado.as_view(), name='search_ter'),
], 'taller')