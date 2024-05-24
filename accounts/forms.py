from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import Profile

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
            'userbio': forms.Textarea(attrs={'class': 'form-control textcontent'}),  
            'website_url': forms.TextInput(attrs={'class': 'form-control textcontent'}),  
            'facebook_url': forms.TextInput(attrs={'class': 'form-control textcontent'}),  
            'instagram_url': forms.TextInput(attrs={'class': 'form-control textcontent'}),  
            'profile_picture': forms.FileInput(attrs={'class': 'form-control textcontent'}),  
        }