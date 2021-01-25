from django.urls import path
from .views import GarantiasList, GarantiasCompletas, GarantiasCreate, GarantiasUpdate, GarantiasDelete, personal_filter, fecha_filter, personal_filter_terminados, fecha_filter_terminado

garantias_urls = ([
    path('pendientes/', GarantiasList.as_view(), name='index'),
    path('completas/', GarantiasCompletas.as_view(), name='completas'),
    path('create/', GarantiasCreate.as_view(), name='create'),
    path('update/<int:pk>/', GarantiasUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', GarantiasDelete.as_view(), name='delete'),
    path('pendientes/personal/', personal_filter, name='filter_personal'),
    path('pendientes/fecha/', fecha_filter, name='filter_fecha'),
    path('completas/personal/', personal_filter_terminados, name='filter_personal_completas'),
    path('completas/fecha/', fecha_filter_terminado, name='filter_fecha_completas')


], 'garantias')