from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from . forms import RegisterForm, UserProfileForm
from . models import Profile
from django.views.generic import CreateView

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
