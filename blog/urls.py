from django.urls import path
from . views import HomeView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, CommentCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog-post/<int:pk>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('create-blog-post/', BlogPostCreateView.as_view(), name='blog-post-create'),
    path('update-blog-post/<int:pk>/', BlogPostUpdateView.as_view(), name='blog-post-update'),
    path('delete-blog-post/<int:pk>/', BlogPostDeleteView.as_view(), name='blog-post-delete'),
    path('blog-post/comment/<int:pk>/', CommentCreateView.as_view(), name='comment-create'),
 
]