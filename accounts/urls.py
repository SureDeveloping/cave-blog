from django.urls import path
from .views import UserCreationView, UserProfileCreationView

urlpatterns = [
    path('register/', UserCreationView.as_view(), name='register'),
    path('create-user-profil', UserProfileCreationView.as_view(), name='user-profil-create'),
]