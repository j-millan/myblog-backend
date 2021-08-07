from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.text import Truncator, slugify

DEFAULT_THUMBNAIL = 'img/post-thumbnails/default.jpg'

def upload_location(instance, filename):
    FILENAME = str.lower(f'{instance.title}-{filename}')
    return f'img/post-thumbnails/author{instance.author.pk}/{FILENAME}'

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.TextField(max_length=400)
    body = models.TextField(max_length=25000)
    thumbnail = models.ImageField(upload_to=upload_location, default=DEFAULT_THUMBNAIL)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='date published')
    upd_date = models.DateTimeField(auto_now=True, verbose_name='date updated')
    categories = models.ManyToManyField('BlogCategory', related_name='posts')
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=BlogPost)
def post_delete_blog_post(sender, instance, *args, **kwargs):
    instance.thumbnail.delete(False)

def pre_save_blog_post(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(f'{instance.author.username}-{instance.title}')

pre_save.connect(pre_save_blog_post, sender=BlogPost)

class BlogComment(models.Model):
    message = models.TextField(max_length=600)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='date published')
    upd_date = models.DateTimeField(auto_now=True, verbose_name='date updated')

    def __str__(self):
        return f'"{Truncator(self.message).chars(50)}" by {self.author.username}'

class BlogCategory(models.Model):
	name = models.CharField(max_length=50, unique=True)
	color_choices = [
		('primary', 'primary'),
		('secondary', 'secondary'),
		('success', 'success'),
		('danger', 'danger'),
		('warning', 'warning'),
		('info', 'info'),
	]
	tag_color = models.CharField(max_length=10, choices=color_choices, default='light')

	def __str__(self):
		return self.name

class UserFollowing(models.Model):
    date_followed = models.DateTimeField(auto_now=True)
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower.username} follows {self.followed.username}'