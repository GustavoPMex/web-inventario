from django.urls import path
from .views import SignUpView, ProfileView, ProfileUpdate, EmailUpdate, ListUsers, SearchView
from .models import Profile

urlpatterns = [
    path('list_users/', ListUsers.as_view(), name='list_users'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile_update/', ProfileUpdate.as_view(), name='profile_update'),
    path('profile_update/email/', EmailUpdate.as_view(), name='profile_email'),
    path('search/', SearchView.as_view(), name='search_p')
]