from django.urls import path
from .views import SignUpView, ListView

urlpatterns = [
    path('', ListView.as_view(), name='list_users'),
    path('signup/', SignUpView.as_view(), name='signup'),
]