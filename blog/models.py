from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    textcontent = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # Formating for admin section
    def __str__(self):
        return self.title + ' | ' + str(self.author) 

    # Redirect after post to detail view page
    def get_absolute_url(self):
        return reverse('blog-post-detail', args=(self.id,))    