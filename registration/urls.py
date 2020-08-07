from django.urls import path
from .views import SignUpView, UsuariosList, ProfileUpdate, EmailUpdate

urlpatterns = [
    path('profile/', UsuariosList.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile_update/', ProfileUpdate.as_view(), name='profile_update'),
    path('profile_update/email/', EmailUpdate.as_view(), name='profile_email'),
]