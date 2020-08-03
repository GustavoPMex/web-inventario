from django.urls import path
from .views import ClienteList, ClienteCreate, SearchView

cliente_urls = ([
    path('', ClienteList.as_view(), name='index' ),
    path('create/', ClienteCreate.as_view(), name='create'),
    path('search/', SearchView.as_view(), name='search'),
], 'cliente')