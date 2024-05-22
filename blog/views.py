from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm, UpdateForm
from .models import Post


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

class BlogPostUpdateView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'blog/blog_post_update.html'