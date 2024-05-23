from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'textcontent')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'author': forms.HiddenInput(), 
            'textcontent': forms.Textarea(attrs={'class': 'form-control textcontent'}),  
        }
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['author'].required = False

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'textcontent')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'textcontent': forms.Textarea(attrs={'class': 'form-control textcontent'}),  
        }