from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return f'img/blogpost_thumbnails/author-{instance.author.pk}/{instance.title}-thumbnail'

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.TextField(max_length=400)
    body = models.TextField(maxlength=25000)
    thumbnail = models.ImageField(upload_to=upload_location, null=False)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=False)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='date published')
    upd_date = models.DateTimeField(auto_now=True, verbose_name='date updated')
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title