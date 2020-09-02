from django.urls import path
from .views import HomeView

home_urls = ([
    path('', HomeView, name='index')
    
], 'home')