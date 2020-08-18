from django.urls import path
from .views import GarantiasList, GarantiasCompletas, GarantiasCreate, GarantiasUpdate, GarantiasDelete
garantias_urls = ([
    path('', GarantiasList.as_view(), name='index'),
    path('completas/', GarantiasCompletas.as_view(), name='completas'),
    path('create/', GarantiasCreate.as_view(), name='create'),
    path('update/<int:pk>/', GarantiasUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', GarantiasDelete.as_view(), name='delete'),
], 'garantias')