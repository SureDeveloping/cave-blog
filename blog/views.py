from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, UpdateForm, CommentForm
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Overview with all blog posts
class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-created_on']

# Datail view for one blog posts
class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_post_detail.html'

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_post_create.html'

    # Set the logged-in user asauthor
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

class BlogPostUpdateView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'blog/blog_post_update.html'

class BlogPostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('home')

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_create.html'
    
    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.commentator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-post-detail', args=(self.kwargs['pk'],))