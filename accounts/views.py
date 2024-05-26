from django.shortcuts import render, get_object_or_404 
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from . forms import RegisterForm, UserProfileForm, UserProfileUpdateForm
from . models import Profile
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class UserCreationView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "User Created Successfully"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response
            
class UserProfileCreationView(CreateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'registration/user_profile_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('user-profil-detail', kwargs={'pk': self.object.pk})

class ProfilePageDetailView(DetailView):
    model = Profile
    template_name = 'registration/user_profile_detail.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super().get_context_data(*args, **kwargs)
        profile_page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["profile_page_user"] = profile_page_user
        return context

class UserProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = Profile
    form_class = UserProfileUpdateForm
    template_name = 'registration/user_profile_update.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, pk=self.kwargs['pk'])

def get_form(self, form_class=None):
        form = super().get_form(form_class)
        profile = self.get_object()
        form.initial = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
        return form
