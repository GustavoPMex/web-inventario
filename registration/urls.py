from django.urls import path
from .views import SignUpView, ProfileView, ProfileUpdate, EmailUpdate, ListUsers, SearchView, ProfileDelete
from .models import Profile

urlpatterns = [
    path('list_users/', ListUsers.as_view(), name='list_users'),
    path('list_users/delete/<int:pk>/', ProfileDelete.as_view(), name='delete_users'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/profile_update/', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/profile_update/email/', EmailUpdate.as_view(), name='profile_email'),
    path('list_users/search/', SearchView.as_view(), name='search_p')
]