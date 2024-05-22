from django.urls import path
from . views import HomeView, BlogPostDetailView, BlogPostCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog-post/<int:pk>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('create-blog-post/', BlogPostCreateView.as_view(), name='blog-post-create'),
]