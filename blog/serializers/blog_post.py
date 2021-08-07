from django.contrib.auth.models import User

from rest_framework import serializers

from blog.models import BlogPost, BlogCategory
from blog.serializers.user import UserSerializer
from blog.serializers.blog_category import BlogCategorySerializer


class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    thumbnail = serializers.SerializerMethodField('get_post_thumbnail')
    categories = BlogCategorySerializer(read_only=True, many=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'introduction', 'body',
                  'thumbnail', 'pub_date', 'upd_date', 'categories', 'slug']
        read_only_fields = ['__all__']

    def get_post_thumbnail(self, post):
        return post.thumbnail.url

class BlogPostCreateSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogCategory.objects.all())
    author_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = BlogPost
        fields = ['author_id', 'id', 'title', 'introduction', 'body', 'thumbnail', 'categories']
        read_only_fields = ['id']