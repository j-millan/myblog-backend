from django.contrib.auth.models import User

from rest_framework import serializers

from blog.models import BlogPost, BlogComment, BlogCategory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class BlogCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = BlogComment
        fields = ['message', 'author', 'post', 'pub_date', 'upd_date']

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    thumbnail = serializers.SerializerMethodField('get_post_thumbnail')
    categories = BlogCategorySerializer(read_only=True, many=True)
    slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'introduction', 'body', 'thumbnail', 'pub_date', 'upd_date', 'categories', 'slug']
    
    def get_post_thumbnail(self, post):
        return post.thumbnail.url

