from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post


# Create your views here.
# Overview with all blog posts
class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'

# Datail view for one blog posts
class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_post_detail.html'
