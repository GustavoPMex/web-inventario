from django.urls import path
from .views import SignUpView, UsuariosList, ProfileUpdate

urlpatterns = [
    path('profile/', UsuariosList.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile_update/', ProfileUpdate.as_view(), name='profile_update'),
]