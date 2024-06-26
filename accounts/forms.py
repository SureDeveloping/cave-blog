from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'country', 'userbio', 'website_url',
                  'facebook_url', 'instagram_url')
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'userbio': SummernoteWidget(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    userbio = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {
        'toolbar': [
            ['style', ['bold', 'underline', 'clear']],
            ['font', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', []],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    }}))


class UserProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    city = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    country = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    userbio = forms.CharField(
        widget=SummernoteWidget(attrs={'class': 'form-control'})
    )
    website_url = forms.URLField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    facebook_url = forms.URLField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    instagram_url = forms.URLField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'city',
            'country',
            'userbio',
            'website_url',
            'facebook_url',
            'instagram_url',
        ]

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

    userbio = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {
        'toolbar': [
            ['style', ['bold', 'underline', 'clear']],
            ['font', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', []],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    }}))
