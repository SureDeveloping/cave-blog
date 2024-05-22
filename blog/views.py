from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, UpdateForm
from .models import Post
from django.urls import reverse_lazy


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

class BlogPostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('home')