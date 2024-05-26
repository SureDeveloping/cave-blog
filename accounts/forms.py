from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from . models import Profile
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password1')

    def __init__(self, *args, **kwargs):
        super(RegisterForm ,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'country', 'userbio', 'website_url', 'facebook_url', 'instagram_url', 'profile_picture')
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control textcontent'}), 
            'country': forms.TextInput(attrs={'class': 'form-control textcontent'}),
            'userbio': SummernoteWidget(attrs={'class': 'form-control textcontent'}),  
            'website_url': forms.TextInput(attrs={'class': 'form-control textcontent'}),  
            'facebook_url': forms.TextInput(attrs={'class': 'form-control textcontent'}),  
            'instagram_url': forms.TextInput(attrs={'class': 'form-control textcontent'}),  
            'profile_picture': forms.FileInput(attrs={'class': 'form-control textcontent'}),  
        }


class UserProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'city', 'country', 'userbio', 'website_url', 'facebook_url', 'instagram_url', 'profile_picture']
    
    widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}), 
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'userbio': SummernoteWidget(attrs={'class': 'form-control textcontent'}),  
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),  
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),  
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),  
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),  
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        instance = kwargs.get('instance')
        if instance:
            initial = kwargs.get('initial', {})
            initial.update({
                'first_name': instance.user.first_name,
                'last_name': instance.user.last_name,
                'email': instance.user.email,
            })
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        profile = super().save(commit=commit)
        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        return profile