from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    textcontent = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # Formating for admin section
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    # Redirect after post to detail view page
    def get_absolute_url(self):
        return reverse('blog-post-detail', args=(self.id,))

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} - {self.commentator.username}"

    class Meta:
        ordering = ["-created_on"]
