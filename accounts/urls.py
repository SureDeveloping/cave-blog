from django.urls import path
from .views import UserCreationView, UserProfileCreationView, ProfilePageDetailView

urlpatterns = [
    path('register/', UserCreationView.as_view(), name='register'),
    path('create-user-profil', UserProfileCreationView.as_view(), name='user-profil-create'),
    path('user-profil/<int:pk>/', ProfilePageDetailView.as_view(), name='user-profil-detail'),
]