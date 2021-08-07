from django.contrib.auth.models import User

from rest_framework import serializers

from blog.models import BlogPost, BlogComment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'last_name']

class BlogCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = BlogComment
        fields = ['message', 'author', 'post', 'pub_date', 'upd_date']
