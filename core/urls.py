from django.urls import path
from .views import HomeView

home_urls = ([
    path('', HomeView.as_view(), name='index')
    
], 'home')