from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = CloudinaryField('image')
    bio = models.TextField(default="No bio!")
    updated_at = models.DateTimeField(auto_now=True)



