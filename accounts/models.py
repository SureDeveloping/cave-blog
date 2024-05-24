from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    userbio = models.TextField()
    website_url = models.CharField(max_length=200, blank=True, null=True)
    facebook_url = models.CharField(max_length=200, blank=True, null=True)
    instagram_url = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(storage=RawMediaCloudinaryStorage(), blank=True, null=True)

    def __str__(self):
        return self.user.username + ' Profile'

    def get_absolute_url(self):
        return reverse('home')
