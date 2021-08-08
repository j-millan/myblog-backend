from django.db import models
from django.contrib.auth.models import User

DEFAULT_PROFILE_PICTURE = 'img/profile-pictures/default.jpg'

def profile_picture_upload_location(instance, filename):
	return f'img/profile-pictures/author{instance.user.pk}-picture'

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.CharField(max_length=350, null=True, blank=True, verbose_name='biography')
    profile_picture = models.ImageField(upload_to=profile_picture_upload_location, default=DEFAULT_PROFILE_PICTURE)
    youtube = models.URLField(max_length=150, null=True, blank=True, verbose_name='youtube channel') 
    instagram = models.URLField(max_length=150, null=True, blank=True, verbose_name='instagram page') 
    twitter = models.URLField(max_length=150, null=True, blank=True, verbose_name='twitter page') 

    def __str__(self):
        return f"{self.user.username}' profile"
    
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def get_ordered_posts(self):
        return self.user.posts.all().order_by('-pub_date')