from django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'textcontent')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'textcontent': SummernoteWidget(attrs={'class': 'form-control textcontent'}),  
        }

    textcontent = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {
        'toolbar': [
            ['style', ['bold', 'underline', 'clear']],
            ['font', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['picture']], 
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    }}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control textcontent'}), 
        } 