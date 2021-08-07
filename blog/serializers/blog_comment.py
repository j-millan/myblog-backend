from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import BlogPost, BlogComment
from blog.serializers.user import UserSerializer

class BlogCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = BlogComment
        fields = ['id', 'message', 'author', 'post_id', 'pub_date', 'upd_date']
        read_only_fields = ['__all__']

class BlogCommentCreateSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source='author.id')
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=BlogPost.objects.all(), 
        source='post'
    )
    
    class Meta:
        model = BlogComment
        fields = ['id', 'author_id', 'post_id', 'message']

class BlogCommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ['id', 'message']
        read_only_fields = ['id']
