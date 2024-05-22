from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


# Create your views here.
# Overview with all blog posts
class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'

# Datail view for one blog posts
class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_post_detail.html'

class BlogPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_post_create.html'