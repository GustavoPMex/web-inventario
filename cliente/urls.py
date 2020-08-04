from django.urls import path
from .views import ClienteList, ClienteCreate, SearchView, ClienteUpdate, ClienteDelete

cliente_urls = ([
    path('', ClienteList.as_view(), name='index' ),
    path('create/', ClienteCreate.as_view(), name='create'),
    path('search/', SearchView.as_view(), name='search'),
    path('update/<int:pk>/', ClienteUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ClienteDelete.as_view(), name='delete'),
], 'cliente')