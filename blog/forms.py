from django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'textcontent')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'author': forms.HiddenInput(), 
            'textcontent': SummernoteWidget(attrs={'class': 'form-control textcontent'}),  
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
            'textcontent': SummernoteWidget(attrs={'class': 'form-control textcontent'}),  
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control textcontent'}), 
        } 