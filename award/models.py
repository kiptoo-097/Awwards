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


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    sitename = models.CharField(max_length=50)
    desc = HTMLField()
    post_date = models.DateTimeField(default=timezone.now)
    image1 = CloudinaryField('projects/')
    link = models.CharField(max_length=70)


 






