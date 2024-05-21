from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post


# Create your views here.
# Overview with all blog posts
class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'

    