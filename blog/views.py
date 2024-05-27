from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Overview with all blog posts
class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'

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
    form_class = PostForm
    template_name = 'blog/blog_post_update.html'

    def is_author(self, post):
        return self.request.user == post.author   

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

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_update.html'

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'), post=post)
        return comment
    
    def get_queryset(self):
        return Comment.objects.filter(commentator=self.request.user)

    def get_success_url(self):
        return reverse_lazy('blog-post-detail', args=(self.object.post.pk,))

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'), post=post)
        return comment
    
    def get_queryset(self):
        return Comment.objects.filter(commentator=self.request.user)

    def get_success_url(self):
        return reverse_lazy('blog-post-detail', args=(self.object.post.pk,))