from django.contrib import admin

from blog.models import BlogPost, BlogComment, BlogCategory

admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(BlogCategory)