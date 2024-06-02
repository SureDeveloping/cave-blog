from django.urls import path
from .views import (
    UserCreationView, UserProfileCreationView, ProfilePageDetailView,
    UserProfileUpdateView, UserProfileDeleteView
)

urlpatterns = [
    path('register/', UserCreationView.as_view(), name='register'),
    path(
        'create-user-profil', UserProfileCreationView.as_view(),
        name='user-profil-create'
    ),
    path(
        'user-profil/<int:pk>/', ProfilePageDetailView.as_view(),
        name='user-profil-detail'
    ),
    path(
        'update-user-profil/<int:pk>/', UserProfileUpdateView.as_view(),
        name='user-profil-update'
    ),
    path(
        'delete-user-profil/<int:pk>/', UserProfileDeleteView.as_view(),
        name='user-profil-delete'
    ),
]
